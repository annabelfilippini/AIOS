#!/usr/bin/env python3
"""
enforce_media_folder.py — called by the enforce-media-folder.sh PreToolUse hook.

Reads the hook payload (JSON) on stdin. Blocks (exit 2) any Write/Edit/Bash
that would write a .png / .html / .yaml / .jsonl outside of
    */media/YYYY-MM-DD-<slug>/...
Exempts the skill's own inspiration library and the _archive store, since
those legitimately carry protected-extension files.

Read-only Bash commands (`cat`, `ls`, `head`, etc.) are NEVER flagged —
only commands that actually write a protected file (redirection, cp, mv,
rsync, tee, dd) are checked.

Exit 0 → allow. Exit 2 with stderr → block (stderr surfaces to Claude).
"""

from __future__ import annotations

import json
import re
import sys

PROTECTED = re.compile(r"\.(png|html|yaml|jsonl)$", re.IGNORECASE)
ALLOWED = re.compile(r"(?:^|/)media/\d{4}-\d{2}-\d{2}[^/]*/")
EXEMPT = (
    "/skills/instagram-carousel/inspiration/",
    "/_archive/",
)


def candidates(tool: str, inp: dict):
    """Yield each path the tool is about to write to."""
    if tool in ("Write", "Edit", "NotebookEdit"):
        p = inp.get("file_path") or inp.get("notebook_path")
        if p:
            yield p
        return

    if tool == "Bash":
        cmd = inp.get("command", "") or ""
        if not cmd:
            return
        # Redirection targets: > foo  or  >> foo
        for m in re.finditer(r">>?\s*([~/]?[\w./\-]+)", cmd):
            yield m.group(1)
        # cp / mv / rsync / install — destination is the LAST path-like arg
        # in the segment. Source is read, not flagged.
        for m in re.finditer(
            r"\b(?:cp|mv|rsync|install)\b([^|;&\n]+)",
            cmd,
            re.IGNORECASE,
        ):
            segment = m.group(1)
            paths = re.findall(
                r"([~/]?[\w./\-]+\.(?:png|html|yaml|jsonl))",
                segment,
                re.IGNORECASE,
            )
            if paths:
                yield paths[-1]
        # tee / dd of=
        for m in re.finditer(r"\btee\s+(?:-a\s+)?([~/]?[\w./\-]+)", cmd):
            yield m.group(1)
        for m in re.finditer(r"\bdd\b[^|;&\n]*?of=([~/]?[\w./\-]+)", cmd):
            yield m.group(1)


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except json.JSONDecodeError:
        return 0  # malformed → don't block

    tool = payload.get("tool_name", "")
    inp = payload.get("tool_input", {}) or {}

    for path in candidates(tool, inp):
        if not PROTECTED.search(path):
            continue
        if any(ex in path for ex in EXEMPT):
            continue
        if ALLOWED.search(path):
            continue
        sys.stderr.write(
            "BLOCKED by enforce-media-folder.sh (instagram-carousel run active)\n"
            f"  Tool: {tool}\n"
            f"  Path: {path}\n"
            "  Expected: */media/YYYY-MM-DD-<slug>/...\n"
            "  Fix: pass --project-root to render_slides.py / generate_photos.py / "
            "build_review.py, or write the file under <project_root>/media/<date>-<slug>/.\n"
            "  Exempt locations: skills/instagram-carousel/inspiration/, _archive/.\n"
            "  Bypass: rm ~/.claude/state/active-skills/instagram-carousel.lock\n"
        )
        return 2

    return 0


if __name__ == "__main__":
    sys.exit(main())
