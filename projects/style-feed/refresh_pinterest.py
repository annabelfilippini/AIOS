#!/usr/bin/env python3
"""
Pull Annabel's real Pinterest "Clothes" board into data/pinterest/clothes.json.
Uses gallery-dl with her Chrome cookies (same pattern as the IG scraper) — Pinterest
is a login-gated SPA, so an anonymous fetch returns nothing.

Run:  python3 refresh_pinterest.py

MERGES by pin id (never shrinks); an empty/failed pull keeps the old file. Cron-safe,
BUT cookie decryption needs the login keychain unlocked, so a headless launchd run can
fail to read cookies — that's fine, it just keeps the existing pins.
"""
import sys, json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "data" / "pinterest" / "clothes.json"
BOARD = "https://www.pinterest.com/annabelflip1/clothes/"


def extract(raw):
    pins = []
    for entry in raw:
        if not (isinstance(entry, list) and len(entry) >= 2 and isinstance(entry[1], dict)):
            continue
        p = entry[1]
        imgs = p.get("images") or {}
        url = None
        if isinstance(imgs, dict):
            for k in ("orig", "736x", "564x", "474x"):
                if imgs.get(k, {}).get("url"):
                    url = imgs[k]["url"]; break
            if not url:
                for v in imgs.values():
                    if isinstance(v, dict) and v.get("url"):
                        url = v["url"]; break
        if not url:
            continue
        pins.append({
            "id": str(p.get("id", "")),
            "img": url,
            "link": p.get("link") or (p.get("rich_metadata") or {}).get("url"),
            "title": (p.get("grid_title") or p.get("title") or "").strip(),
            "desc": (p.get("description") or "").strip(),
        })
    return pins


def load_existing():
    return json.load(open(OUT)) if OUT.exists() else []


def main():
    try:
        out = subprocess.run(
            ["gallery-dl", "-j", "--cookies-from-browser", "chrome", BOARD],
            capture_output=True, text=True, timeout=180)
        fresh = extract(json.loads(out.stdout)) if out.stdout.strip() else []
    except Exception as e:
        print(f"pinterest: {type(e).__name__}: {e} — kept old file")
        return
    fresh = [p for p in fresh if p["id"]]
    if not fresh:
        print("pinterest: 0 pins from scrape — kept old file")
        return
    by_id = {p["id"]: p for p in load_existing()}
    added = sum(by_id.setdefault(p["id"], p) is p for p in fresh)
    OUT.write_text(json.dumps(list(by_id.values()), indent=2))
    print(f"pinterest: {len(by_id)} total (+{added} new, {len(fresh)} scraped) -> {OUT.name}")


if __name__ == "__main__":
    sys.exit(main())
