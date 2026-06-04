"""Firecrawl scrape of Adelitas Cocina y Cantina + La Doña Mezcaleria + 3 reference sites."""

import os
import json
import time
import requests
from pathlib import Path
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from firecrawl.v2.types import ScreenshotFormat

# Project root is three levels up: prospects/adelitas/scrape.py → website-audit/
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")
app = FirecrawlApp(api_key=os.environ["FIRECRAWL_API_KEY"])

BASE = Path(__file__).resolve().parent

ADELITAS_PAGES = [
    ("homepage", "https://adelitasco.com/"),
    ("broadway", "https://adelitasco.com/broadway"),
    ("edgewater", "https://adelitasco.com/edgewater"),
    ("catering", "https://adelitasco.com/catering"),
    ("qr-code-menu", "https://adelitasco.com/qr-code-menu"),
    ("event", "https://adelitasco.com/event"),
    ("tequilas-family-mexican-restaurant", "https://adelitasco.com/tequilas-family-mexican-restaurant"),
]

ADELITAS_SEO_SAMPLE = [
    ("seo-sample-best-mexican-food", "https://adelitasco.com/best-mexican-food-in-denver-colorado"),
    ("seo-sample-mezcal-in-denver", "https://adelitasco.com/mezcal-in-denver"),
]

LA_DONA_PAGES = [
    ("homepage", "https://ladonamezcaleria.com/"),
]

REFERENCES = [
    ("atomix", "homepage", "https://www.atomixnyc.com/"),
    ("atomix", "about", "https://www.atomixnyc.com/about"),
    ("cosme", "homepage", "https://cosmenyc.com/"),
    ("cosme", "menu", "https://cosmenyc.com/menu/"),
    ("pujol", "homepage", "https://www.pujol.com.mx/en"),
    ("pujol", "experience", "https://www.pujol.com.mx/en/experience"),
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


def scrape_markdown_only(name, url, out_dir):
    """Lightweight: just markdown, for SEO doorway samples."""
    print(f"\n[md-only] {name} ({url})")
    try:
        r = app.scrape(url, formats=["markdown"], wait_for=3000)
        md = r.markdown or ""
        (out_dir / f"{name}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")


def scrape_reference(brand, name, url):
    """Reference site: homepage + 1 key page, full-page desktop + markdown only."""
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


# === Adelitas (7 core pages, 3 passes each) ===
adelitas_out = BASE / "scrape"
adelitas_shots = adelitas_out / "screenshots"
for name, url in ADELITAS_PAGES:
    scrape_three_pass(name, url, adelitas_out, adelitas_shots)
    time.sleep(0.5)

# === Adelitas SEO doorway samples (markdown only, 2 samples) ===
for name, url in ADELITAS_SEO_SAMPLE:
    scrape_markdown_only(name, url, adelitas_out)
    time.sleep(0.5)

# === La Doña (1 page, 3 passes) ===
ladona_out = BASE / "companion" / "la-dona" / "scrape"
ladona_shots = ladona_out / "screenshots"
for name, url in LA_DONA_PAGES:
    scrape_three_pass(name, url, ladona_out, ladona_shots)
    time.sleep(0.5)

# === References (3 sites, 2 pages each, 1 pass) ===
for brand, name, url in REFERENCES:
    scrape_reference(brand, name, url)
    time.sleep(0.5)

print("\n\n=== Done ===")
print(f"Adelitas: {adelitas_out}")
print(f"La Doña:  {ladona_out}")
print(f"Refs:     {BASE / 'reference'}")
