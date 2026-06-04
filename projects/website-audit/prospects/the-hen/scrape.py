"""Firecrawl scrape for The Hen (Ann Arbor) — redesign-only mode.

Homepage only + branding + verified-facts sources + 2 reference sites.
References: Sadelle's (NYC brunch), Cutler & Co (editorial photo-forward).
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

HEN_PAGES = [
    ("homepage", "https://www.theheneats.com/"),
]

REFERENCES = [
    ("sadelles", "homepage", "https://www.sadelles.com/"),
    ("sadelles", "menu", "https://www.sadelles.com/menus"),
    ("cutler-and-co", "homepage", "https://cutlerandco.com.au/"),
    ("cutler-and-co", "menu", "https://cutlerandco.com.au/menu/"),
]

FACTS_SOURCES = [
    ("yelp-washington", "https://www.yelp.com/biz/the-hen-ann-arbor"),
    ("yelp-packard", "https://www.yelp.com/biz/the-hen-ann-arbor-2"),
    ("google-hen-washington", "https://www.google.com/search?q=The+Hen+Ann+Arbor+403+East+Washington+hours+phone"),
    ("google-hen-packard", "https://www.google.com/search?q=The+Hen+Ann+Arbor+1906+Packard+hours+phone"),
    ("instagram", "https://www.instagram.com/theheneats/"),
]


def save_screenshot(url, path):
    if not url:
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


def metadata_to_dict(metadata):
    if metadata is None:
        return {}
    if hasattr(metadata, "model_dump"):
        return metadata.model_dump()
    return {k: v for k, v in vars(metadata).items() if not k.startswith("_")}


def scrape_hen_homepage():
    out_dir = BASE / "scrape"
    shots = out_dir / "screenshots"
    out_dir.mkdir(parents=True, exist_ok=True)
    shots.mkdir(parents=True, exist_ok=True)

    url = "https://www.theheneats.com/"
    print(f"\n{'='*60}\nhomepage ({url})\n{'='*60}")

    # Homepage: markdown + screenshot + branding in one call
    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=4000)
        md = r.markdown or ""
        (out_dir / "homepage.md").write_text(f"# homepage\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, shots / "homepage-desktop-full.png")
        meta = metadata_to_dict(r.metadata)
        (out_dir / "homepage-metadata.json").write_text(json.dumps(meta, indent=2, default=str))
    except Exception as e:
        print(f"  ERROR (homepage desktop): {type(e).__name__}: {e}")

    # Mobile screenshot
    try:
        r = app.scrape(url, formats=["screenshot"], mobile=True, wait_for=4000)
        save_screenshot(r.screenshot, shots / "homepage-mobile.png")
    except Exception as e:
        print(f"  ERROR (mobile): {type(e).__name__}: {e}")

    # Branding payload
    print("\n[branding]")
    try:
        r = app.scrape(url, formats=["branding"], wait_for=3000)
        branding = None
        for attr in ("branding", "brand"):
            if hasattr(r, attr):
                branding = getattr(r, attr)
                break
        if branding and hasattr(branding, "model_dump"):
            branding = branding.model_dump()
        elif branding:
            branding = {k: v for k, v in vars(branding).items() if not k.startswith("_")}
        if branding:
            (BASE / "branding.json").write_text(json.dumps({"source": "firecrawl:branding", "url": url, "branding": branding}, indent=2, default=str))
            print(f"  branding saved ({len(str(branding))} chars)")
            return
    except Exception as e:
        print(f"  native branding errored: {e}")

    # Fallback: rawHtml regex
    print("  falling back to rawHtml extraction")
    try:
        r = app.scrape(url, formats=["rawHtml", "links"], wait_for=3000)
        html = getattr(r, "raw_html", None) or getattr(r, "rawHtml", None) or ""
        hex_colors = sorted(set(re.findall(r"#[0-9A-Fa-f]{6}\b", html)))
        rgb_colors = sorted(set(re.findall(r"rgba?\([^)]+\)", html)))
        font_families = sorted({m.strip() for m in re.findall(r"font-family\s*:\s*([^;\"'}]+)", html, re.IGNORECASE)})
        google_fonts = sorted(set(re.findall(r"fonts\.googleapis\.com/css2?\?family=([^\"'&]+)", html)))
        logos = sorted(set(re.findall(r'<img[^>]+(?:src|data-src)=["\']([^"\']*logo[^"\']*)["\']', html, re.IGNORECASE)))
        payload = {
            "source": "fallback:rawHtml+regex",
            "url": url,
            "colors": {"hex": hex_colors, "rgb": rgb_colors},
            "fonts": {"font_families": font_families, "google_fonts": google_fonts},
            "logos": logos,
        }
        (BASE / "branding.json").write_text(json.dumps(payload, indent=2, default=str))
        print(f"  fallback branding saved (colors={len(hex_colors)}, fonts={len(font_families)})")
    except Exception as e:
        print(f"  fallback ERROR: {e}")


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


def scrape_facts(name, url):
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


# Execute
scrape_hen_homepage()

for brand, name, url in REFERENCES:
    scrape_reference(brand, name, url)
    time.sleep(0.5)

facts_results = {}
for name, url in FACTS_SOURCES:
    ok, note = scrape_facts(name, url)
    facts_results[name] = {"url": url, "ok": ok, "note": note}
    time.sleep(0.5)

(BASE / "facts" / "scrape-summary.json").write_text(json.dumps(facts_results, indent=2, default=str))

print("\n=== Done ===")
print(f"Scrape:    {BASE / 'scrape'}")
print(f"Refs:      {BASE / 'reference'}")
print(f"Facts:     {BASE / 'facts'}")
print(f"Branding:  {BASE / 'branding.json'}")
