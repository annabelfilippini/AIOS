"""Firecrawl scrape for Amer's Deli — redesign-only mode.

Page set:
  - Homepage only (AUDIT_REDESIGN_ONLY=1 — Amer's sibling pages are usually CMS-walled)
  - 2 references: Landini Brothers (heritage) + High Street Deli (deli vertical)
  - Facts sources: Yelp + Google knowledge panel

Writes:
  prospects/amers/branding.json   (hard dep for /audit-redesign)
  prospects/amers/scrape/...      (homepage md + screenshot + metadata)
  prospects/amers/reference/<brand>/
  prospects/amers/facts/<source>.md
  prospects/amers/facts/scrape-summary.json
"""

import os
import re
import json
import time
import requests
from pathlib import Path
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from firecrawl.v2.types import ScreenshotFormat

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")
app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])

BASE = Path(__file__).resolve().parent

AMERS_PAGES = [
    ("homepage", "https://www.amersdeli.com/"),
]

REFERENCES = [
    ("landini-brothers", "homepage", "https://www.landinibrothers.com/"),
    ("landini-brothers", "menu", "https://www.landinibrothers.com/menus"),
    ("high-street-deli", "homepage", "https://www.highstdeli.com/"),
    ("high-street-deli", "menu", "https://www.highstdeli.com/menu"),
]

FACTS_SOURCES = [
    ("yelp-search", "https://www.yelp.com/search?find_desc=amers+deli&find_loc=Ann+Arbor%2C+MI"),
    ("google-search", "https://www.google.com/search?q=Amer%27s+Deli+Ann+Arbor+hours+phone+address"),
    ("google-locations", "https://www.google.com/search?q=Amers+Deli+State+Street+South+University+Ann+Arbor+locations"),
]


def save_screenshot(url, path):
    if not url:
        print("  [no screenshot url]")
        return False
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        path.write_bytes(resp.content)
        print(f"  screenshot: {len(resp.content)//1024}KB -> {path.name}")
        return True
    except Exception as e:
        print(f"  screenshot FAILED: {e}")
        return False


def to_dict(obj):
    if obj is None:
        return None
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if isinstance(obj, dict):
        return obj
    try:
        return {k: v for k, v in vars(obj).items() if not k.startswith("_")}
    except TypeError:
        return obj


def metadata_to_dict(metadata):
    if metadata is None:
        return {}
    if hasattr(metadata, "model_dump"):
        return metadata.model_dump()
    return {k: v for k, v in vars(metadata).items() if not k.startswith("_")}


def scrape_homepage_with_branding(name, url, out_dir, screenshots_dir):
    """Homepage pass: markdown + full screenshot + branding payload."""
    out_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n{'='*60}\n{name} ({url}) — homepage + branding\n{'='*60}")

    # Pass 1: markdown + screenshot
    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=4000)
        md = r.markdown or ""
        (out_dir / f"{name}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, screenshots_dir / f"{name}-desktop-full.png")
        meta = metadata_to_dict(r.metadata)
        (out_dir / f"{name}-metadata.json").write_text(json.dumps(meta, indent=2, default=str))
    except Exception as e:
        print(f"  ERROR (markdown+screenshot): {type(e).__name__}: {e}")

    # Pass 2: mobile screenshot
    try:
        r = app.scrape(url, formats=["screenshot"], mobile=True, wait_for=4000)
        save_screenshot(r.screenshot, screenshots_dir / f"{name}-mobile.png")
    except Exception as e:
        print(f"  ERROR (mobile): {type(e).__name__}: {e}")

    # Pass 3: native branding
    native_branding = None
    try:
        r = app.scrape(url, formats=["branding"], wait_for=3000)
        for attr in ("branding", "brand"):
            if hasattr(r, attr):
                native_branding = to_dict(getattr(r, attr))
                break
        if native_branding:
            print(f"  native branding: OK ({len(str(native_branding))} chars)")
    except Exception as e:
        print(f"  native branding errored: {type(e).__name__}: {e}")

    # Pass 4: rawHtml fallback (always run — seeds fonts/colors if native misses)
    fallback = None
    try:
        r = app.scrape(url, formats=["rawHtml", "links"], wait_for=3000)
        html = getattr(r, "rawHtml", None) or getattr(r, "raw_html", None) or ""
        links = getattr(r, "links", []) or []
        hex_colors = sorted(set(re.findall(r"#[0-9A-Fa-f]{6}\b", html)))
        rgb_colors = sorted(set(re.findall(r"rgba?\([^)]+\)", html)))
        font_families = sorted(set(m.strip() for m in re.findall(r"font-family\s*:\s*([^;\"'}]+)", html, re.IGNORECASE)))
        google_fonts = sorted(set(re.findall(r"fonts\.googleapis\.com/css2?\?family=([^\"'&]+)", html)))
        logo_urls = set(re.findall(r'<img[^>]+(?:src|data-src)=["\']([^"\']*logo[^"\']*)["\']', html, re.IGNORECASE))
        for m in re.findall(r'<img[^>]+alt=["\'][^"\']*logo[^"\']*["\'][^>]*(?:src|data-src)=["\']([^"\']+)["\']', html, re.IGNORECASE):
            logo_urls.add(m)
        favicons = sorted(set(re.findall(r'<link[^>]+rel=["\'][^"\']*icon[^"\']*["\'][^>]*href=["\']([^"\']+)["\']', html, re.IGNORECASE)))
        fallback = {
            "source": "fallback:rawHtml+regex",
            "url": url,
            "colors": {"hex": hex_colors, "rgb": rgb_colors},
            "fonts": {"font_families": font_families, "google_fonts": google_fonts},
            "logos": sorted(logo_urls),
            "favicons": favicons,
            "links_sample": links[:30] if isinstance(links, list) else [],
        }
        print(f"  fallback: {len(hex_colors)} hex, {len(font_families)} font-families, {len(google_fonts)} google fonts, {len(logo_urls)} logos")
    except Exception as e:
        print(f"  fallback errored: {type(e).__name__}: {e}")

    # Write branding.json — prefer native, always attach fallback
    payload = {
        "url": url,
        "native": native_branding,
        "fallback": fallback,
    }
    # Surface flat colors/fonts at top level for /audit-redesign gate convenience
    if native_branding:
        payload["colors"] = native_branding.get("colors") if isinstance(native_branding, dict) else None
        payload["fonts"] = native_branding.get("fonts") if isinstance(native_branding, dict) else None
    if not payload.get("colors") and fallback:
        payload["colors"] = fallback["colors"]
    if not payload.get("fonts") and fallback:
        payload["fonts"] = fallback["fonts"]

    (BASE / "branding.json").write_text(json.dumps(payload, indent=2, default=str))
    print(f"  wrote branding.json")


def scrape_reference(brand, name, url):
    out_dir = BASE / "reference" / brand
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[ref:{brand}] {name} ({url})")
    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=5000)
        md = r.markdown or ""
        (out_dir / f"{name}.md").write_text(f"# {brand} - {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, out_dir / f"{name}-desktop-full.png")
        meta = metadata_to_dict(r.metadata)
        (out_dir / f"{name}-metadata.json").write_text(json.dumps(meta, indent=2, default=str))
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")


def scrape_facts_source(name, url):
    facts_dir = BASE / "facts"
    facts_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[facts:{name}] {url}")
    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=5000)
        md = r.markdown or ""
        if not md.strip() or len(md) < 200:
            print(f"  WEAK (len={len(md)}) — possibly bot-walled")
            (facts_dir / f"{name}-BLOCKED.md").write_text(f"# {name}\n**URL:** {url}\nWEAK/BOT-WALLED (len={len(md)})\n\n{md}")
            return False, f"weak (len={len(md)})"
        (facts_dir / f"{name}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, facts_dir / f"{name}-full.png")
        return True, "ok"
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")
        return False, str(e)


# === Amer's homepage + branding ===
shots = BASE / "scrape" / "screenshots"
out = BASE / "scrape"
for name, url in AMERS_PAGES:
    scrape_homepage_with_branding(name, url, out, shots)
    time.sleep(0.5)

# === References ===
for brand, name, url in REFERENCES:
    scrape_reference(brand, name, url)
    time.sleep(0.5)

# === Verified facts ===
facts_results = {}
for name, url in FACTS_SOURCES:
    ok, note = scrape_facts_source(name, url)
    facts_results[name] = {"url": url, "ok": ok, "note": note}
    time.sleep(0.5)

(BASE / "facts" / "scrape-summary.json").write_text(json.dumps(facts_results, indent=2, default=str))

print("\n\n=== Done ===")
print(f"Amer's:  {out}")
print(f"Refs:    {BASE / 'reference'}")
print(f"Facts:   {BASE / 'facts'}")
