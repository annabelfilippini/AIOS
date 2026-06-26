#!/usr/bin/env python3
"""wp-push - push a self-contained HTML section into a WordPress site.

Built for the Freeride Tarifa case: take a hand-built HTML section (the venue
guide grid) plus its local images and publish it into the client's WordPress
site over the REST API, so nobody has to paste HTML or upload images by hand.

Design rules (read before extending):
  * Auth is a WordPress Application Password (NOT the login password). The
    client creates one under Users -> Profile -> Application Passwords and you
    drop it in wp-push.toml. It can be revoked any time without changing the
    login.
  * The CLI owns ONE page per --slug. It creates that page or updates the page
    it previously created. It will refuse to overwrite a page it does not
    recognise as its own unless you pass --force, so it can never silently
    clobber an existing WPBakery / page-builder layout.
  * Pages are created as DRAFT by default. Going live is an explicit --publish.
  * No third-party packages beyond `requests`. Config is plain TOML
    (tomllib, stdlib on 3.11+).

Usage:
  wp_push.py ping
  wp_push.py publish --html section.html --base-dir . --slug tarifa-eat-drink
  wp_push.py publish --html section.html --slug tarifa-eat-drink --publish
  wp_push.py page-get --slug tarifa-eat-drink --out backup.html

Run `wp_push.py --help` for all options.
"""
from __future__ import annotations

import argparse
import json
import mimetypes
import os
import re
import sys
from pathlib import Path

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover - py<3.11
    sys.exit("wp-push needs Python 3.11+ (for tomllib). You have " + sys.version.split()[0])

try:
    import requests
except ModuleNotFoundError:
    sys.exit("Missing dependency: requests. Run  pip install -r requirements.txt")


# --------------------------------------------------------------------------
# config
# --------------------------------------------------------------------------
DEFAULT_CONFIG = "wp-push.toml"
MANIFEST_NAME = "wp-push-manifest.json"

# A marker we stamp into pages we create, so we can recognise our own page on a
# later run and never overwrite a hand-built page by accident.
OWNER_MARK = "<!-- managed-by:wp-push -->"


class Config:
    def __init__(self, site_url: str, username: str, app_password: str):
        self.site_url = site_url.rstrip("/")
        self.username = username
        self.app_password = app_password
        self.api = f"{self.site_url}/wp-json/wp/v2"

    @property
    def auth(self):
        return (self.username, self.app_password)

    @property
    def host(self) -> str:
        return re.sub(r"^https?://", "", self.site_url).split("/")[0]


def load_config(path: str) -> Config:
    p = Path(path)
    if not p.exists():
        sys.exit(
            f"No config at {path}. Copy config.example.toml to {DEFAULT_CONFIG} and "
            "fill in site_url / username / app_password (see README)."
        )
    with p.open("rb") as fh:
        data = tomllib.load(fh)
    missing = [k for k in ("site_url", "username", "app_password") if not data.get(k)]
    if missing:
        sys.exit(f"{path} is missing required keys: {', '.join(missing)}")
    if "PASTE" in data["app_password"] or "xxxx" in data["app_password"].lower():
        sys.exit(f"{path}: app_password still looks like the placeholder. Paste the real one.")
    return Config(data["site_url"], data["username"], data["app_password"])


# --------------------------------------------------------------------------
# http helpers
# --------------------------------------------------------------------------
def _check(resp: requests.Response, what: str):
    if resp.status_code >= 400:
        body = resp.text[:500]
        sys.exit(f"{what} failed: HTTP {resp.status_code}\n{body}")
    return resp


# --------------------------------------------------------------------------
# manifest (per-site image upload cache)
# --------------------------------------------------------------------------
def manifest_path(cfg: Config) -> Path:
    return Path(MANIFEST_NAME)


def load_manifest(cfg: Config) -> dict:
    p = manifest_path(cfg)
    if not p.exists():
        return {}
    data = json.loads(p.read_text())
    return data.get(cfg.host, {})


def save_manifest(cfg: Config, site_entries: dict):
    p = manifest_path(cfg)
    data = json.loads(p.read_text()) if p.exists() else {}
    data[cfg.host] = site_entries
    p.write_text(json.dumps(data, indent=2))


# --------------------------------------------------------------------------
# image discovery + upload + rewrite
# --------------------------------------------------------------------------
IMG_REF_RE = re.compile(r"""(?:src|href)\s*=\s*["']([^"']+)["']|url\(\s*["']?([^"')]+)["']?\s*\)""")
LOCAL_EXT = {".jpg", ".jpeg", ".png", ".webp", ".gif", ".avif", ".svg"}


def find_local_images(html: str, base_dir: Path) -> list[Path]:
    """Return resolved local image files referenced by the HTML (deduped)."""
    found: dict[str, Path] = {}
    for m in IMG_REF_RE.finditer(html):
        ref = m.group(1) or m.group(2)
        if not ref or ref.startswith(("http://", "https://", "data:", "//", "#")):
            continue
        ext = os.path.splitext(ref.split("?")[0])[1].lower()
        if ext not in LOCAL_EXT:
            continue
        candidate = (base_dir / ref).resolve()
        if candidate.exists():
            found[str(candidate)] = candidate
        else:
            print(f"  ! referenced image not found on disk, skipping: {ref}")
    return list(found.values())


def upload_image(cfg: Config, path: Path) -> dict:
    ctype = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    with path.open("rb") as fh:
        resp = requests.post(
            f"{cfg.api}/media",
            auth=cfg.auth,
            headers={
                "Content-Disposition": f'attachment; filename="{path.name}"',
                "Content-Type": ctype,
            },
            data=fh.read(),
            timeout=120,
        )
    _check(resp, f"Upload {path.name}")
    j = resp.json()
    return {"id": j["id"], "source_url": j["source_url"]}


def rewrite_html(html: str, base_dir: Path, mapping: dict[str, str]) -> str:
    """Replace local image refs with their uploaded source_url.

    `mapping` is basename -> source_url.
    """
    def repl(m: re.Match) -> str:
        whole = m.group(0)
        ref = m.group(1) or m.group(2)
        if not ref or ref.startswith(("http://", "https://", "data:", "//", "#")):
            return whole
        base = os.path.basename(ref.split("?")[0])
        if base in mapping:
            return whole.replace(ref, mapping[base])
        return whole

    return IMG_REF_RE.sub(repl, html)


# --------------------------------------------------------------------------
# pages
# --------------------------------------------------------------------------
def find_page_by_slug(cfg: Config, slug: str) -> dict | None:
    resp = requests.get(
        f"{cfg.api}/pages",
        auth=cfg.auth,
        params={"slug": slug, "status": "publish,draft,pending,private,future"},
        timeout=60,
    )
    _check(resp, "Lookup page")
    arr = resp.json()
    return arr[0] if arr else None


def page_payload(title: str, slug: str, content: str, status: str) -> dict:
    return {
        "title": title,
        "slug": slug,
        "content": OWNER_MARK + "\n" + content,
        "status": status,
    }


# --------------------------------------------------------------------------
# commands
# --------------------------------------------------------------------------
def cmd_ping(cfg: Config, args):
    resp = requests.get(f"{cfg.api}/users/me", auth=cfg.auth, params={"context": "edit"}, timeout=60)
    if resp.status_code == 401:
        sys.exit(
            "Auth rejected (401). Check username + Application Password in wp-push.toml.\n"
            "The app password is the 24-char one with spaces, NOT the login password."
        )
    _check(resp, "Ping")
    me = resp.json()
    caps = me.get("capabilities", {}) or {}
    can_edit = caps.get("edit_pages") or caps.get("publish_pages") or me.get("roles")
    print(f"OK - connected to {cfg.site_url}")
    print(f"  user: {me.get('name')}  (slug: {me.get('slug')})")
    if me.get("roles"):
        print(f"  roles: {', '.join(me['roles'])}")
    if not can_edit:
        print("  ! this account may not be able to edit pages - confirm it is an admin/editor")


def cmd_publish(cfg: Config, args):
    html_path = Path(args.html)
    if not html_path.exists():
        sys.exit(f"--html file not found: {args.html}")
    base_dir = Path(args.base_dir).resolve()
    html = html_path.read_text()

    # 1. images
    images = find_local_images(html, base_dir)
    print(f"Found {len(images)} local image(s) referenced by the section.")
    manifest = load_manifest(cfg)
    basename_to_url: dict[str, str] = {}
    for img in images:
        key = img.name
        cached = manifest.get(key)
        if cached and not args.reupload:
            print(f"  = {key} (already uploaded, id {cached['id']})")
            basename_to_url[key] = cached["source_url"]
            continue
        if args.dry_run:
            print(f"  + would upload {key}")
            basename_to_url[key] = f"<dry-run:{key}>"
            continue
        info = upload_image(cfg, img)
        manifest[key] = info
        basename_to_url[key] = info["source_url"]
        print(f"  + uploaded {key} -> id {info['id']}")
    if not args.dry_run:
        save_manifest(cfg, manifest)

    # 2. rewrite
    final_html = rewrite_html(html, base_dir, basename_to_url)
    if args.out:
        Path(args.out).write_text(final_html)
        print(f"Wrote rewritten HTML -> {args.out}")

    # 3. page
    status = "publish" if args.publish else "draft"
    existing = find_page_by_slug(cfg, args.slug)
    if args.dry_run:
        action = "update" if existing else "create"
        print(f"[dry-run] would {action} page '{args.slug}' as {status}. No changes sent.")
        return

    payload = page_payload(args.title, args.slug, final_html, status)
    if existing:
        is_ours = OWNER_MARK in (existing.get("content", {}).get("raw", "") or "")
        if not is_ours and not args.force:
            sys.exit(
                f"A page with slug '{args.slug}' already exists and was NOT created by wp-push "
                f"(id {existing['id']}).\nRefusing to overwrite it. Use a different --slug, or "
                "--force if you are certain. Back it up first with `page-get`."
            )
        resp = requests.post(f"{cfg.api}/pages/{existing['id']}", auth=cfg.auth, json=payload, timeout=120)
        _check(resp, "Update page")
        page = resp.json()
        print(f"Updated page id {page['id']} as {status}.")
    else:
        resp = requests.post(f"{cfg.api}/pages", auth=cfg.auth, json=payload, timeout=120)
        _check(resp, "Create page")
        page = resp.json()
        print(f"Created page id {page['id']} as {status}.")

    link = page.get("link")
    print(f"  view: {link}")
    print(f"  edit: {cfg.site_url}/wp-admin/post.php?post={page['id']}&action=edit")
    if status == "draft":
        print("  (draft - not public yet. Re-run with --publish, or hit Publish in wp-admin.)")
    if status == "publish":
        print("  NOTE: this site runs WP Rocket. Clear its cache in wp-admin so the change shows.")


def cmd_page_get(cfg: Config, args):
    existing = find_page_by_slug(cfg, args.slug)
    if not existing:
        sys.exit(f"No page with slug '{args.slug}'.")
    raw = existing.get("content", {}).get("raw")
    if raw is None:
        # need edit context
        resp = requests.get(f"{cfg.api}/pages/{existing['id']}", auth=cfg.auth, params={"context": "edit"}, timeout=60)
        _check(resp, "Fetch page")
        raw = resp.json().get("content", {}).get("raw", "")
    if args.out:
        Path(args.out).write_text(raw)
        print(f"Saved page '{args.slug}' (id {existing['id']}) -> {args.out}")
    else:
        print(raw)


# --------------------------------------------------------------------------
# arg parsing
# --------------------------------------------------------------------------
def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="wp-push", description="Push an HTML section into a WordPress site over the REST API.")
    p.add_argument("--config", default=DEFAULT_CONFIG, help=f"path to TOML config (default {DEFAULT_CONFIG})")
    sub = p.add_subparsers(dest="command", required=True)

    sp = sub.add_parser("ping", help="verify the connection + credentials")
    sp.set_defaults(func=cmd_ping)

    sp = sub.add_parser("publish", help="upload images + create/update a page from an HTML section")
    sp.add_argument("--html", required=True, help="path to the HTML section file")
    sp.add_argument("--base-dir", default=".", help="directory image paths in the HTML are relative to")
    sp.add_argument("--slug", required=True, help="page slug wp-push owns (e.g. tarifa-eat-drink)")
    sp.add_argument("--title", default=None, help="page title (defaults to a title from the slug)")
    sp.add_argument("--publish", action="store_true", help="publish live (default is draft)")
    sp.add_argument("--out", default=None, help="also write the rewritten HTML here")
    sp.add_argument("--reupload", action="store_true", help="re-upload images even if cached in the manifest")
    sp.add_argument("--force", action="store_true", help="allow overwriting a page wp-push did not create")
    sp.add_argument("--dry-run", action="store_true", help="show what would happen, send nothing")
    sp.set_defaults(func=cmd_publish)

    sp = sub.add_parser("page-get", help="download a page's raw content (back it up before overwriting)")
    sp.add_argument("--slug", required=True)
    sp.add_argument("--out", default=None, help="write to file instead of stdout")
    sp.set_defaults(func=cmd_page_get)

    return p


def main(argv=None):
    args = build_parser().parse_args(argv)
    if getattr(args, "title", None) is None and getattr(args, "slug", None):
        args.title = args.slug.replace("-", " ").title()
    cfg = load_config(args.config)
    args.func(cfg, args)


if __name__ == "__main__":
    main()
