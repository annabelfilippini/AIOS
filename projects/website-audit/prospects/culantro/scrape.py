"""Firecrawl scrape of Culantro Peru + references (Cutler & Co, Mission Ceviche, Gjelina) + facts.

Pass 1: homepage with branding + markdown + screenshot (saves branding.json)
Pass 2: sibling pages (if any) — markdown + screenshot
Pass 3: references — 1-2 pages each, markdown + screenshot
Pass 4: facts sources — Yelp + GBP for both Ferndale and Ann Arbor
"""

import os
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

CULANTRO_PAGES = [
    ("homepage", "https://www.culantroperu.com/"),
]

REFERENCES = [
    ("cutler-and-co", "homepage", "https://cutlerandco.com.au/"),
    ("cutler-and-co", "menu", "https://cutlerandco.com.au/menu"),
    ("mission-ceviche", "homepage", "https://www.missionceviche.com/"),
    ("mission-ceviche", "locations", "https://www.missionceviche.com/locations"),
    ("gjelina", "homepage", "https://www.gjelina.com/"),
    ("gjelina", "locations", "https://www.gjelina.com/locations"),
]

FACTS_SOURCES = [
    ("yelp-ferndale", "https://www.yelp.com/biz/culantro-ferndale"),
    ("yelp-ann-arbor", "https://www.yelp.com/biz/culantro-ann-arbor"),
    ("google-ferndale", "https://www.google.com/search?q=Culantro+Peruvian+Eatery+Ferndale+MI"),
    ("google-ann-arbor", "https://www.google.com/search?q=Culantro+Peruvian+Eatery+Ann+Arbor+MI"),
    ("opentable-ferndale", "https://www.opentable.com/r/culantro-ferndale"),
]


def save_screenshot(url, path):
    if not url:
        print(f"  [no screenshot url]")
        return False
    resp = requests.get(url, timeout=60)
    resp.raise_for_status()
    path.write_bytes(resp.content)
    print(f"  screenshot: {len(resp.content)//1024}KB -> {path.name}")
    return True


def metadata_to_dict(metadata):
    if metadata is None:
        return {}
    if hasattr(metadata, "model_dump"):
        return metadata.model_dump()
    return {k: v for k, v in vars(metadata).items() if not k.startswith("_")}


def scrape_homepage_with_branding(name, url, out_dir, screenshots_dir):
    """Homepage — branding + markdown + screenshot in one call."""
    out_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n{'='*60}\n{name} ({url}) [branding+md+shot]\n{'='*60}")
    try:
        r = app.scrape(
            url,
            formats=["markdown", ScreenshotFormat(full_page=True), "branding"],
            wait_for=4000,
        )
        md = r.markdown or ""
        (out_dir / f"{name}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, screenshots_dir / f"{name}-desktop-full.png")
        meta = metadata_to_dict(r.metadata)
        (out_dir / f"{name}-metadata.json").write_text(json.dumps(meta, indent=2, default=str))
        # Save branding.json at prospect root (hard dep for /audit-redesign)
        branding = getattr(r, "branding", None)
        if branding is None:
            data = getattr(r, "data", None)
            if data is not None:
                branding = getattr(data, "branding", None)
        if hasattr(branding, "model_dump"):
            branding = branding.model_dump()
        if branding:
            (BASE / "branding.json").write_text(json.dumps(branding, indent=2, default=str))
            print(f"  branding.json saved")
        else:
            print(f"  [no branding payload]")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")

    # mobile screenshot of homepage (for design reference)
    try:
        r = app.scrape(url, formats=["screenshot"], mobile=True, wait_for=3000)
        save_screenshot(r.screenshot, screenshots_dir / f"{name}-mobile.png")
    except Exception as e:
        print(f"  ERROR (mobile): {type(e).__name__}: {e}")


def scrape_sibling(name, url, out_dir, screenshots_dir):
    """Sibling page — markdown + screenshot only."""
    out_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[sibling] {name} ({url})")
    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=3000)
        md = r.markdown or ""
        (out_dir / f"{name}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, screenshots_dir / f"{name}-desktop-full.png")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")


def scrape_reference(brand, name, url):
    out_dir = BASE / "reference" / brand
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[ref:{brand}] {name} ({url})")
    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=4000)
        md = r.markdown or ""
        (out_dir / f"{name}.md").write_text(f"# {brand} - {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, out_dir / f"{name}-desktop-full.png")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")


def scrape_facts(name, url):
    out_dir = BASE / "facts"
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[facts] {name} ({url})")
    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=5000)
        md = r.markdown or ""
        (out_dir / f"{name}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        shots = out_dir / "screenshots"
        shots.mkdir(parents=True, exist_ok=True)
        save_screenshot(r.screenshot, shots / f"{name}.png")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")


# === Culantro homepage (branding + md + desktop + mobile) ===
culantro_out = BASE / "scrape"
culantro_shots = culantro_out / "screenshots"
for name, url in CULANTRO_PAGES:
    scrape_homepage_with_branding(name, url, culantro_out, culantro_shots)
    time.sleep(0.5)

# === References ===
for brand, name, url in REFERENCES:
    scrape_reference(brand, name, url)
    time.sleep(0.5)

# === Facts sources ===
for name, url in FACTS_SOURCES:
    scrape_facts(name, url)
    time.sleep(0.5)

print("\n\n=== Done ===")
print(f"Culantro:    {culantro_out}")
print(f"Refs:        {BASE / 'reference'}")
print(f"Facts:       {BASE / 'facts'}")
