"""Firecrawl scrape for Sava's Ann Arbor — redesign-only mode.

Page set:
  - Sava's homepage only (AUDIT_REDESIGN_ONLY=1; sibling pages are usually CMS-walled)
  - 4 references (homepage + menu each):
      wild-ginger     — wildginger.net        (upscale-casual, editorial headlines, photo-forward)
      sarma           — sarmarestaurant.com   (Mediterranean mezze, full-screen hero, globally inflected)
      king            — kingrestaurant.nyc    (urban-chic, editorial restraint, aspirational tier)
      la-semilla      — lasemilla.kitchen     (earthy palette, quirky typography, personality)
  - Facts sources: Yelp + OpenTable (Sava's) + Google knowledge panel

Writes:
  prospects/savas/branding.json   (hard dep for /audit-redesign)
  prospects/savas/scrape/...      (homepage md + screenshot + metadata)
  prospects/savas/reference/<brand>/
  prospects/savas/facts/<source>.md
  prospects/savas/facts/scrape-summary.json
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

SAVAS_PAGES = [
    ("homepage", "https://www.savasannarbor.com/"),
]

REFERENCES = [
    ("wild-ginger",  "homepage", "https://www.wildginger.net/"),
    ("wild-ginger",  "menu",     "https://www.wildginger.net/menu"),
    ("sarma",        "homepage", "https://www.sarmarestaurant.com/"),
    ("sarma",        "menu",     "https://www.sarmarestaurant.com/menu"),
    ("king",         "homepage", "https://kingrestaurant.nyc/"),
    ("king",         "menu",     "https://kingrestaurant.nyc/menus"),
    ("la-semilla",   "homepage", "https://www.lasemilla.kitchen/"),
    ("la-semilla",   "menu",     "https://www.lasemilla.kitchen/menu"),
]

FACTS_SOURCES = [
    ("yelp",         "https://www.yelp.com/biz/savas-ann-arbor"),
    ("opentable",    "https://www.opentable.com/savas"),
    ("google",       "https://www.google.com/search?q=Savas+Ann+Arbor+hours+phone+address+reviews"),
    ("tock",         "https://www.exploretock.com/savas"),
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
    """Homepage pass: markdown + full screenshot + mobile + branding payload."""
    out_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n{'='*60}\n{name} ({url}) — homepage + branding\n{'='*60}")

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

    try:
        r = app.scrape(url, formats=["screenshot"], mobile=True, wait_for=4000)
        save_screenshot(r.screenshot, screenshots_dir / f"{name}-mobile.png")
    except Exception as e:
        print(f"  ERROR (mobile): {type(e).__name__}: {e}")

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

    payload = {
        "url": url,
        "native": native_branding,
        "fallback": fallback,
    }
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


# === Sava's homepage + branding ===
shots = BASE / "scrape" / "screenshots"
out = BASE / "scrape"
for name, url in SAVAS_PAGES:
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
print(f"Sava's:  {out}")
print(f"Refs:    {BASE / 'reference'}")
print(f"Facts:   {BASE / 'facts'}")
