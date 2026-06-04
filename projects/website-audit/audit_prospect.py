#!/usr/bin/env python3
"""audit_prospect.py — Run the full website-audit pipeline headlessly.

Shells out to `claude -p` once per step with AUDIT_AUTOMATED=1 so each step
runs in a fresh Claude Code subprocess (Filbert pattern: stateless supervisor,
per-task folder is the memory).

    python audit_prospect.py pepperpong.com --name pepper-pong
    python audit_prospect.py hopalley.com --ref https://uncleseafood.com
    python audit_prospect.py hopalley.com --skip-to redesign   # resume

Writes prospects/<slug>/result.json on completion.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import urlparse

PROJECT_ROOT = Path(__file__).resolve().parent
PROSPECTS_DIR = PROJECT_ROOT / "prospects"
PROSPECTS_MD = PROSPECTS_DIR / "prospects.md"
LOCKFILE = Path("/tmp/website-audit.lock")
DEFAULT_MAX_TOTAL_S = 4 * 60 * 60  # 4 hours


@dataclass
class Step:
    name: str                # skill name without the /audit- prefix
    command: str             # full prompt passed to `claude -p`
    expected: str            # relative path under prospects/<slug>/ that must exist after
    timeout_s: int           # per-step wall-clock cap


def slugify(domain: str) -> str:
    host = urlparse(domain if "://" in domain else f"https://{domain}").hostname or domain
    host = host.replace("www.", "")
    base = host.split(".")[0]
    return re.sub(r"[^a-z0-9]+", "-", base.lower()).strip("-")


def build_steps(slug: str, url: str, refs: list[str]) -> list[Step]:
    ref_args = " ".join(f"--ref {r}" for r in refs)
    return [
        Step("scrape",    f"/audit-scrape {slug} {url} {ref_args}".strip(), "scrape-data.md",                      1800),
        Step("seo",       f"/audit-seo {slug}",                             "seo-research.md",                     900),
        Step("ai-seo",    f"/audit-ai-seo {slug}",                          "ai-seo-research.md",                  900),
        Step("analyze",   f"/audit-analyze {slug}",                         "audit-client.md",                     900),
        Step("redesign",  f"/audit-redesign {slug}",                        "mockups/homepage-redesign.html",      3600),
        Step("dashboard", f"/audit-dashboard {slug}",                       "mockups/dashboard-preview.html",      3600),
        Step("package",   f"/audit-package {slug}",                         f"{slug}-audit/index.html",            900),
        Step("cleanup",   f"/audit-cleanup {slug}",                         f"{slug}-audit/index.html",            300),
    ]


def run_step(step: Step, prospect_dir: Path) -> tuple[bool, str]:
    logs_dir = prospect_dir / "logs"
    logs_dir.mkdir(parents=True, exist_ok=True)
    log_path = logs_dir / f"{step.name}.log"

    env = {**os.environ, "AUDIT_AUTOMATED": "1"}

    cmd = [
        "claude",
        "--dangerously-skip-permissions",
        "-p", step.command,
    ]

    print(f"\n━━ {step.name} ━━ {step.command}")
    print(f"   log: {log_path.relative_to(PROJECT_ROOT)}")
    t0 = time.time()

    with log_path.open("w") as log:
        log.write(f"$ {' '.join(cmd)}\n")
        log.write(f"cwd={PROJECT_ROOT} AUDIT_AUTOMATED=1\n\n")
        log.flush()
        try:
            proc = subprocess.run(
                cmd,
                cwd=PROJECT_ROOT,
                env=env,
                stdout=log,
                stderr=subprocess.STDOUT,
                timeout=step.timeout_s,
                check=False,
            )
        except subprocess.TimeoutExpired:
            return False, f"timeout after {step.timeout_s}s"

    elapsed = int(time.time() - t0)
    if proc.returncode != 0:
        return False, f"claude exited {proc.returncode} after {elapsed}s"

    expected_path = prospect_dir / step.expected
    if not expected_path.exists():
        return False, f"expected {step.expected} missing after {elapsed}s"

    print(f"   ✓ {elapsed}s · {step.expected}")
    return True, f"ok ({elapsed}s)"


def extract_deploy_url(prospect_dir: Path) -> str | None:
    log = prospect_dir / "logs" / "package.log"
    if not log.exists():
        return None
    m = re.search(r"https://[a-z0-9-]+\.vercel\.app", log.read_text())
    return m.group(0) if m else None


# ─── pre-flight ───────────────────────────────────────────────────────────────

def preflight() -> tuple[bool, list[str]]:
    """Verify everything the pipeline depends on. Cheap; runs in seconds."""
    failures: list[str] = []

    def check(label: str, cmd: list[str]) -> None:
        try:
            r = subprocess.run(cmd, capture_output=True, timeout=15, check=False)
            if r.returncode != 0:
                failures.append(f"{label}: exit {r.returncode} ({r.stderr.decode().strip()[:80]})")
        except (FileNotFoundError, subprocess.TimeoutExpired) as e:
            failures.append(f"{label}: {e}")

    check("claude --version", ["claude", "--version"])
    check("vercel whoami",   ["vercel", "whoami"])

    if not os.environ.get("FIRECRAWL_API_KEY"):
        failures.append("FIRECRAWL_API_KEY not set")

    design_lib = Path.home() / "Documents" / "AI-OS" / "wiki" / "wiki" / "design-library.md"
    if not design_lib.exists():
        failures.append(f"design-library.md missing at {design_lib}")

    return (not failures), failures


# ─── lockfile ─────────────────────────────────────────────────────────────────

def _pid_alive(pid: int) -> bool:
    try:
        os.kill(pid, 0)
        return True
    except (OSError, ProcessLookupError):
        return False


def acquire_lock() -> bool:
    """Atomic O_EXCL create. If a stale lock exists (PID dead), reclaim it."""
    if LOCKFILE.exists():
        try:
            old_pid = int(LOCKFILE.read_text().strip())
            if _pid_alive(old_pid):
                print(f"another run in progress (pid {old_pid}); bailing", file=sys.stderr)
                return False
            print(f"stale lock from pid {old_pid}; reclaiming", file=sys.stderr)
            LOCKFILE.unlink()
        except (ValueError, OSError):
            LOCKFILE.unlink(missing_ok=True)

    fd = os.open(str(LOCKFILE), os.O_CREAT | os.O_EXCL | os.O_WRONLY)
    os.write(fd, f"{os.getpid()}\n".encode())
    os.close(fd)
    return True


def release_lock() -> None:
    LOCKFILE.unlink(missing_ok=True)


# ─── queue read ───────────────────────────────────────────────────────────────

# Match a queued prospect block:
#   ### <Name>
#   - **Website:** <url>
#   - **Slug:** <slug>      ← optional; if missing, the entry is skipped
QUEUED_HEADERS = ("## 🟢 Queued", "## 🟡 Queued", "## 🔴 Queued")


def parse_queued_prospects() -> list[dict]:
    """Walk prospects.md, return queued entries with Slug + Website."""
    if not PROSPECTS_MD.exists():
        return []
    text = PROSPECTS_MD.read_text()
    entries: list[dict] = []
    in_queue = False
    current: dict | None = None

    for line in text.splitlines():
        if line.startswith("## "):
            in_queue = any(line.startswith(h) for h in QUEUED_HEADERS)
            if current and "url" in current:
                entries.append(current)
            current = None
            continue
        if not in_queue:
            continue
        if line.startswith("### "):
            if current and "url" in current:
                entries.append(current)
            name = line[4:].split("⭐")[0].split("*")[0].strip()
            current = {"name": name}
            continue
        if current is None:
            continue
        m = re.match(r"\s*-\s+\*\*Website:\*\*\s*(\S+)", line)
        if m:
            current["url"] = m.group(1).rstrip("/,)")
            continue
        m = re.match(r"\s*-\s+\*\*Slug:\*\*\s*`?([a-z0-9-]+)`?", line)
        if m:
            current["slug"] = m.group(1)

    if current and "url" in current:
        entries.append(current)
    return entries


def next_queued() -> dict | None:
    """First queued entry that has both a Slug and Website."""
    for entry in parse_queued_prospects():
        if "slug" in entry and "url" in entry:
            return entry
    return None


# ─── telegram notifier ────────────────────────────────────────────────────────

def notify(result: dict) -> None:
    """Best-effort Telegram message. No-op if env vars absent."""
    token = os.environ.get("TELEGRAM_BOT_TOKEN")
    chat  = os.environ.get("ANNABEL_CHAT_ID")
    if not (token and chat):
        print("notify: TELEGRAM_BOT_TOKEN / ANNABEL_CHAT_ID not set, skipping")
        return

    slug = result.get("slug", "?")
    if result.get("status") == "success":
        url = result.get("deploy_url") or "(no url captured)"
        text = f"🟢 {slug} shipped\n{url}\nready for video"
    else:
        step = result.get("failed_step", "?")
        log  = PROSPECTS_DIR / slug / "logs" / f"{step}.log"
        text = f"🔴 {slug} failed at {step}\n{result.get('detail','')}\nlog: {log}"

    body = urllib.parse.urlencode({"chat_id": chat, "text": text}).encode()
    req = urllib.request.Request(
        f"https://api.telegram.org/bot{token}/sendMessage",
        data=body,
        method="POST",
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            r.read()
    except urllib.error.URLError as e:
        print(f"notify: telegram send failed: {e}", file=sys.stderr)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("domain", nargs="?", help="e.g. pepperpong.com (omit when using --queue)")
    ap.add_argument("--name", help="explicit prospect slug (overrides auto-derived)")
    ap.add_argument("--ref", action="append", default=[], help="reference URL (repeatable)")
    ap.add_argument("--skip-to", help="resume at step (scrape/seo/ai-seo/analyze/redesign/dashboard/package/cleanup)")
    ap.add_argument("--queue", action="store_true", help="pick next queued prospect from prospects.md")
    ap.add_argument("--notify", action="store_true", help="send Telegram message on done/fail")
    ap.add_argument("--skip-preflight", action="store_true", help="skip claude/vercel/env checks")
    ap.add_argument("--max-total-seconds", type=int, default=DEFAULT_MAX_TOTAL_S, help=f"hard wall-clock cap (default {DEFAULT_MAX_TOTAL_S}s)")
    args = ap.parse_args()

    # ── queue mode picks domain + slug ────────────────────────────────────
    refs: list[str] = list(args.ref)
    if args.queue:
        if args.domain or args.name:
            print("--queue is mutually exclusive with domain/--name", file=sys.stderr)
            return 2
        entry = next_queued()
        if not entry:
            print("no queued prospect with a Slug field in prospects.md")
            return 0
        url  = entry["url"] if "://" in entry["url"] else f"https://{entry['url']}"
        slug = entry["slug"]
        print(f"queue → {entry['name']} (slug={slug})")
    else:
        if not args.domain:
            print("domain required (or pass --queue)", file=sys.stderr)
            return 2
        url  = args.domain if "://" in args.domain else f"https://{args.domain}"
        slug = args.name or slugify(args.domain)

    prospect_dir = PROSPECTS_DIR / slug
    prospect_dir.mkdir(parents=True, exist_ok=True)

    # ── pre-flight ────────────────────────────────────────────────────────
    if not args.skip_preflight:
        ok, failures = preflight()
        if not ok:
            print("✗ pre-flight failed:", file=sys.stderr)
            for f in failures:
                print(f"  - {f}", file=sys.stderr)
            return 2
        print("✓ pre-flight passed")

    # ── lockfile ──────────────────────────────────────────────────────────
    if not acquire_lock():
        return 2
    signal.signal(signal.SIGTERM, lambda *_: (release_lock(), sys.exit(143)))

    try:
        steps = build_steps(slug, url, refs)
        if args.skip_to:
            names = [s.name for s in steps]
            if args.skip_to not in names:
                print(f"unknown --skip-to {args.skip_to!r}; valid: {', '.join(names)}", file=sys.stderr)
                return 2
            steps = steps[names.index(args.skip_to):]

        print(f"audit_prospect: slug={slug} url={url} refs={refs or 'none'}")
        print(f"               dir={prospect_dir.relative_to(PROJECT_ROOT)}")
        print(f"               steps={[s.name for s in steps]}")
        print(f"               budget={args.max_total_seconds}s")

        started = time.time()
        for step in steps:
            if (time.time() - started) > args.max_total_seconds:
                detail = f"total budget {args.max_total_seconds}s exceeded before {step.name}"
                result = _result(slug, url, "failed", step.name, detail, started, prospect_dir)
                if args.notify:
                    notify(result)
                print(f"\n✗ {detail}")
                return 1

            ok, detail = run_step(step, prospect_dir)
            if not ok:
                result = _result(slug, url, "failed", step.name, detail, started, prospect_dir)
                if args.notify:
                    notify(result)
                print(f"\n✗ FAILED at {step.name}: {detail}")
                return 1

        result = _result(slug, url, "success", None, "all steps passed", started, prospect_dir)
        if args.notify:
            notify(result)
        print(f"\n✓ done in {result['elapsed_s']}s · {result['deploy_url'] or '(no deploy url captured)'}")
        return 0
    finally:
        release_lock()


def _result(slug: str, url: str, status: str, failed_step: str | None, detail: str, started: float, prospect_dir: Path) -> dict:
    result = {
        "slug": slug,
        "url": url,
        "status": status,
        "failed_step": failed_step,
        "detail": detail,
        "elapsed_s": int(time.time() - started),
        "deploy_url": extract_deploy_url(prospect_dir),
    }
    (prospect_dir / "result.json").write_text(json.dumps(result, indent=2))
    return result


if __name__ == "__main__":
    sys.exit(main())
