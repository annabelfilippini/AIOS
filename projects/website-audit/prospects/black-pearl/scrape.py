"""Firecrawl scrape of Black Pearl Ann Arbor + Gramercy Tavern reference."""

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

BLACK_PEARL_PAGES = [
    ("homepage", "https://www.blackpearlannarbor.com/"),
    ("menu", "https://www.blackpearlannarbor.com/menu"),
    ("weekly-specials", "https://www.blackpearlannarbor.com/weekly-specials"),
    ("reservations", "https://www.blackpearlannarbor.com/reservations"),
    ("private-events", "https://www.blackpearlannarbor.com/private-events"),
    ("about", "https://www.blackpearlannarbor.com/about"),
    ("contact-us", "https://www.blackpearlannarbor.com/contact-us"),
    ("faq", "https://www.blackpearlannarbor.com/frequently-asked-questions"),
]

GRAMERCY_PAGES = [
    ("homepage", "https://www.gramercytavern.com/"),
    ("menus", "https://www.gramercytavern.com/menus"),
    ("dining-room-menu", "https://www.gramercytavern.com/menus/tasting-menu"),
    ("tavern-menu", "https://www.gramercytavern.com/menus/tavern-menu"),
    ("about", "https://www.gramercytavern.com/about"),
    ("private-dining", "https://www.gramercytavern.com/private-dining"),
    ("reservations", "https://www.gramercytavern.com/reservations"),
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


bp_out = BASE / "scrape"
bp_shots = bp_out / "screenshots"
for name, url in BLACK_PEARL_PAGES:
    scrape_three_pass(name, url, bp_out, bp_shots)
    time.sleep(0.5)

for name, url in GRAMERCY_PAGES:
    scrape_reference("gramercy-tavern", name, url)
    time.sleep(0.5)

print("\n\n=== Done ===")
print(f"Black Pearl: {bp_out}")
print(f"Refs:        {BASE / 'reference'}")
