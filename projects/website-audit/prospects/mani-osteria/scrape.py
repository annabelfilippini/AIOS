"""Unified scrape for Mani Osteria (redesign-only mode).

Scrapes:
  - Mani homepage (markdown + full screenshot + branding payload)
  - References: Via Carota (home + menus), Don Angie (home + menu)
  - Facts sources: Yelp, OpenTable, Google Business Profile search

Redesign-only mode — single pass per page, no mobile screenshots on prospect,
no sibling pages. Facts verified against third-party sources.
"""

import os
import json
import time
import re
import requests
from pathlib import Path
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from firecrawl.v2.types import ScreenshotFormat

PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")
app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])

BASE = Path(__file__).resolve().parent
SCRAPE_DIR = BASE / "scrape"
SHOTS_DIR = SCRAPE_DIR / "screenshots"
FACTS_DIR = BASE / "facts"
REF_DIR = BASE / "reference"

MANI_URL = "https://maniosteria.com/"

REFERENCES = [
    ("via-carota", "homepage", "https://www.viacarota.com/"),
    ("via-carota", "menus", "https://www.viacarota.com/menus"),
    ("don-angie", "homepage", "https://donangie.com/"),
    ("don-angie", "menu", "https://donangie.com/menu"),
]

FACTS_SOURCES = [
    ("yelp", "https://www.yelp.com/biz/mani-osteria-and-bar-ann-arbor"),
    ("opentable", "https://www.opentable.com/r/mani-osteria-and-bar-ann-arbor"),
]

GBP_QUERIES = [
    "Mani Osteria Ann Arbor hours phone address",
    "Mani Osteria Ann Arbor reviews",
]


def _to_dict(obj):
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


def save_screenshot(url, path):
    if not url:
        print("    [no screenshot url]")
        return False
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        path.write_bytes(resp.content)
        print(f"    screenshot: {len(resp.content)//1024}KB -> {path.name}")
        return True
    except Exception as e:
        print(f"    screenshot download failed: {e}")
        return False


def metadata_to_dict(metadata):
    if metadata is None:
        return {}
    if hasattr(metadata, "model_dump"):
        return metadata.model_dump()
    return {k: v for k, v in vars(metadata).items() if not k.startswith("_")}


# =============================================================
# 1) Mani homepage — markdown + full desktop screenshot + branding
# =============================================================

def scrape_mani_homepage():
    SCRAPE_DIR.mkdir(parents=True, exist_ok=True)
    SHOTS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n{'='*60}\nMani Osteria homepage\n{'='*60}")

    # Pass A: markdown + full screenshot
    try:
        r = app.scrape(MANI_URL, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=3500)
        md = r.markdown or ""
        (SCRAPE_DIR / "homepage.md").write_text(f"# mani-homepage\n**URL:** {MANI_URL}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, SHOTS_DIR / "homepage-desktop-full.png")
        meta = metadata_to_dict(r.metadata)
        (SCRAPE_DIR / "homepage-metadata.json").write_text(json.dumps(meta, indent=2, default=str))
    except Exception as e:
        print(f"  ERROR (desktop-full): {type(e).__name__}: {e}")

    # Pass B: mobile (one shot, useful for mockup responsive decisions)
    try:
        r = app.scrape(MANI_URL, formats=["screenshot"], mobile=True, wait_for=3500)
        save_screenshot(r.screenshot, SHOTS_DIR / "homepage-mobile.png")
    except Exception as e:
        print(f"  ERROR (mobile): {type(e).__name__}: {e}")

    # Pass C: branding payload
    try:
        r = app.scrape(MANI_URL, formats=["branding"], wait_for=3500)
        branding = None
        for attr in ("branding", "brand"):
            if hasattr(r, attr):
                branding = getattr(r, attr)
                break
        branding = _to_dict(branding)
        if branding:
            (BASE / "branding.json").write_text(json.dumps(
                {"source": "firecrawl:branding", "url": MANI_URL, "branding": branding},
                indent=2, default=str))
            print(f"  branding: {len(str(branding))} chars -> branding.json")
        else:
            print("  branding: native format returned nothing, falling back to CSS regex")
            fallback_branding_from_css()
    except Exception as e:
        print(f"  ERROR (branding): {type(e).__name__}: {e}")
        fallback_branding_from_css()


def fallback_branding_from_css():
    try:
        r = app.scrape(MANI_URL, formats=["rawHtml", "links"], wait_for=3500)
        html = getattr(r, "rawHtml", None) or getattr(r, "raw_html", None) or ""
        links = getattr(r, "links", []) or []

        hex_colors = sorted(set(re.findall(r"#[0-9A-Fa-f]{6}\b", html)))
        rgb_colors = sorted(set(re.findall(r"rgba?\([^)]+\)", html)))
        font_families = sorted({m.strip() for m in re.findall(r"font-family\s*:\s*([^;\"'}]+)", html, re.IGNORECASE)})
        google_fonts = sorted(set(re.findall(r"fonts\.googleapis\.com/css2?\?family=([^\"'&]+)", html)))

        logo_urls = sorted(set(
            re.findall(r'<img[^>]+(?:src|data-src)=["\']([^"\']*logo[^"\']*)["\']', html, re.IGNORECASE)
        ))
        favicons = sorted(set(re.findall(
            r'<link[^>]+rel=["\'][^"\']*icon[^"\']*["\'][^>]*href=["\']([^"\']+)["\']', html, re.IGNORECASE
        )))

        payload = {
            "source": "fallback:rawHtml+regex",
            "url": MANI_URL,
            "colors": {"hex": hex_colors, "rgb": rgb_colors},
            "fonts": {"font_families": font_families, "google_fonts": google_fonts},
            "logos": logo_urls,
            "favicons": favicons,
            "links_sample": links[:25] if isinstance(links, list) else [],
        }
        (BASE / "branding.json").write_text(json.dumps(payload, indent=2, default=str))
        print(f"  branding fallback -> branding.json (hex={len(hex_colors)}, fonts={len(font_families)})")
    except Exception as e:
        print(f"  fallback branding errored: {type(e).__name__}: {e}")


# =============================================================
# 2) References — 1 pass each
# =============================================================

def scrape_reference(brand, name, url):
    out = REF_DIR / brand
    out.mkdir(parents=True, exist_ok=True)
    print(f"\n[ref:{brand}] {name} ({url})")
    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=4000)
        md = r.markdown or ""
        (out / f"{name}.md").write_text(f"# {brand} - {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, out / f"{name}-desktop-full.png")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")


# =============================================================
# 3) Facts sources
# =============================================================

def scrape_facts_source(source, url):
    FACTS_DIR.mkdir(parents=True, exist_ok=True)
    print(f"\n[facts:{source}] {url}")
    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=4000)
        md = r.markdown or ""
        if not md.strip() or len(md) < 250:
            note = f"bot-wall suspected (len={len(md)})"
            print(f"  {note}")
            (FACTS_DIR / f"{source}-BLOCKED.md").write_text(
                f"# {source} — BLOCKED\n**URL:** {url}\n**Note:** {note}\n\n{md}"
            )
            return {"source": source, "url": url, "ok": False, "note": note}
        (FACTS_DIR / f"{source}.md").write_text(f"# {source}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, FACTS_DIR / f"{source}.png")
        return {"source": source, "url": url, "ok": True, "chars": len(md)}
    except Exception as e:
        note = f"{type(e).__name__}: {e}"
        print(f"  ERROR: {note}")
        return {"source": source, "url": url, "ok": False, "note": note}


def firecrawl_search(query, limit=5):
    try:
        r = app.search(query, limit=limit)
        d = _to_dict(r)
        if isinstance(d, dict):
            if "data" in d:
                d = d["data"]
            if isinstance(d, dict):
                return d.get("web", []) or []
            return d if isinstance(d, list) else []
        return d or []
    except Exception as e:
        print(f"    search errored: {e}")
        return []


def scrape_gbp():
    FACTS_DIR.mkdir(parents=True, exist_ok=True)
    results = []
    for q in GBP_QUERIES:
        print(f"\n[gbp:search] {q}")
        hits = firecrawl_search(q, limit=5)
        results.append({"query": q, "hits": hits})
    (FACTS_DIR / "gbp-search.json").write_text(json.dumps(results, indent=2, default=str))
    print(f"  -> gbp-search.json ({sum(len(r['hits']) for r in results)} total hits)")
    return results


# =============================================================
# Main
# =============================================================

if __name__ == "__main__":
    scrape_mani_homepage()
    time.sleep(0.5)

    for brand, name, url in REFERENCES:
        scrape_reference(brand, name, url)
        time.sleep(0.5)

    facts_results = []
    for source, url in FACTS_SOURCES:
        facts_results.append(scrape_facts_source(source, url))
        time.sleep(0.5)

    scrape_gbp()

    (FACTS_DIR / "facts-summary.json").write_text(json.dumps(facts_results, indent=2, default=str))

    print("\n\n=== Done ===")
    print(f"Scrape:   {SCRAPE_DIR}")
    print(f"Branding: {BASE / 'branding.json'}")
    print(f"Refs:     {REF_DIR}")
    print(f"Facts:    {FACTS_DIR}")
