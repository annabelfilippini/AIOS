"""Firecrawl scrape of Hop Alley + Uncle Ramen + reference sites (Mister Jiu's, Atomix)."""

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

HOP_ALLEY_PAGES = [
    ("homepage", "https://hopalleydenver.com/"),
    ("large-party-info", "https://hopalleydenver.com/large-party-info"),
]

EXTERNAL_TOUCHPOINTS = [
    ("tock-reservations", "https://www.exploretock.com/hop-alley-denver"),
    ("toast-online-order", "https://www.toasttab.com/hop-alley/v2/online-order"),
    ("toast-giftcards", "https://www.toasttab.com/hop-alley/giftcards"),
]

UNCLE_RAMEN_PAGES = [
    ("homepage", "http://www.uncleramen.com/"),
]

REFERENCES = [
    ("mister-jius", "homepage", "https://misterjius.com/"),
    ("mister-jius", "reservations", "https://misterjius.com/reservations"),
    ("atomix", "homepage", "https://www.atomixnyc.com/"),
    ("atomix", "about", "https://www.atomixnyc.com/about"),
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


def scrape_markdown_only(name, url, out_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[md-only] {name} ({url})")
    try:
        r = app.scrape(url, formats=["markdown"], wait_for=3000)
        md = r.markdown or ""
        (out_dir / f"{name}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")


def scrape_external_touchpoint(name, url, out_dir, screenshots_dir):
    """External booking/ordering page — capture screenshot + markdown to show UX break."""
    out_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n[external] {name} ({url})")
    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=4000)
        md = r.markdown or ""
        (out_dir / f"{name}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
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


# === Hop Alley core pages (3-pass) ===
hop_out = BASE / "scrape"
hop_shots = hop_out / "screenshots"
for name, url in HOP_ALLEY_PAGES:
    scrape_three_pass(name, url, hop_out, hop_shots)
    time.sleep(0.5)

# === External touchpoints (1-pass screenshot + md, shows UX break) ===
ext_out = BASE / "scrape" / "external"
ext_shots = hop_shots  # keep all HA screenshots together
for name, url in EXTERNAL_TOUCHPOINTS:
    scrape_external_touchpoint(name, url, ext_out, ext_shots)
    time.sleep(0.5)

# === Uncle Ramen companion (3-pass) ===
uncle_out = BASE / "companion" / "uncle-ramen" / "scrape"
uncle_shots = uncle_out / "screenshots"
for name, url in UNCLE_RAMEN_PAGES:
    scrape_three_pass(name, url, uncle_out, uncle_shots)
    time.sleep(0.5)

# === References (2 sites, 2 pages each, 1 pass) ===
for brand, name, url in REFERENCES:
    scrape_reference(brand, name, url)
    time.sleep(0.5)

print("\n\n=== Done ===")
print(f"Hop Alley:   {hop_out}")
print(f"Uncle Ramen: {uncle_out}")
print(f"Refs:        {BASE / 'reference'}")
