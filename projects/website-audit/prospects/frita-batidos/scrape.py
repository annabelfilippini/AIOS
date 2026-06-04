"""Firecrawl scrape of Frita Batidos (Ann Arbor primary) + reference sites (Au Cheval, Mighty Fine)."""

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

# Ann Arbor is the primary audit target (college town, walk-in crowd)
FRITA_PAGES = [
    ("homepage-main", "https://fritabatidos.com/"),
    ("ann-arbor-home", "https://fritabatidos.com/ann-arbor"),
    ("ann-arbor-food", "https://fritabatidos.com/ann-arbor/food"),
    ("ann-arbor-chef", "https://fritabatidos.com/ann-arbor/chef"),
    ("ann-arbor-philosophy", "https://fritabatidos.com/ann-arbor/philosophy"),
    ("ann-arbor-praise", "https://fritabatidos.com/ann-arbor/praise"),
    ("ann-arbor-contact", "https://fritabatidos.com/ann-arbor/contact"),
    ("ann-arbor-catering", "https://fritabatidos.com/ann-arbor/catering"),
]

# Detroit location — secondary, scrape homepage + food only
DETROIT_PAGES = [
    ("detroit-home", "https://fritabatidos.com/detroit"),
    ("detroit-food", "https://fritabatidos.com/detroit/food"),
]

REFERENCES = [
    ("au-cheval", "homepage", "https://auchevaldiner.com/"),
    ("mighty-fine", "homepage", "https://mightyfineburgers.com/"),
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


def scrape_three_pass(name, url, out_dir, screenshots_dir):
    """Full scrape: desktop full + markdown, desktop viewport, mobile."""
    out_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n{'='*60}\n{name} ({url})\n{'='*60}")

    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=3000)
        md = r.markdown or ""
        (out_dir / f"{name}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, screenshots_dir / f"{name}-desktop-full.png")
        meta = metadata_to_dict(r.metadata)
        (out_dir / f"{name}-metadata.json").write_text(json.dumps(meta, indent=2, default=str))
    except Exception as e:
        print(f"  ERROR (desktop-full): {type(e).__name__}: {e}")

    try:
        r = app.scrape(url, formats=["screenshot"], wait_for=3000)
        save_screenshot(r.screenshot, screenshots_dir / f"{name}-desktop-viewport.png")
    except Exception as e:
        print(f"  ERROR (viewport): {type(e).__name__}: {e}")

    try:
        r = app.scrape(url, formats=["screenshot"], mobile=True, wait_for=3000)
        save_screenshot(r.screenshot, screenshots_dir / f"{name}-mobile.png")
    except Exception as e:
        print(f"  ERROR (mobile): {type(e).__name__}: {e}")


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


# === Frita Batidos core pages (3-pass) ===
frita_out = BASE / "scrape"
frita_shots = frita_out / "screenshots"
for name, url in FRITA_PAGES:
    scrape_three_pass(name, url, frita_out, frita_shots)
    time.sleep(0.5)

# === Detroit secondary (3-pass) ===
for name, url in DETROIT_PAGES:
    scrape_three_pass(name, url, frita_out, frita_shots)
    time.sleep(0.5)

# === References (1-pass each) ===
for brand, name, url in REFERENCES:
    scrape_reference(brand, name, url)
    time.sleep(0.5)

print("\n\n=== Done ===")
print(f"Frita Batidos: {frita_out}")
print(f"Refs:          {BASE / 'reference'}")
