"""Scrape additional reference sites for Hop Alley redesign: fatcow.com.sg, cosmenyc.com.

Saves markdown + full-page desktop screenshot per page into
prospects/hop-alley/reference/<brand>/.
"""

import os
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

REFERENCES = [
    ("fatcow", "homepage", "https://fatcow.com.sg/"),
    ("fatcow", "about", "https://fatcow.com.sg/about"),
    ("fatcow", "menu", "https://fatcow.com.sg/menu"),
    ("cosme", "homepage", "https://cosmenyc.com/"),
    ("cosme", "about", "https://cosmenyc.com/about"),
    ("cosme", "reservations", "https://cosmenyc.com/reservations"),
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
        return True
    except Exception as e:
        print(f"  ERROR: {type(e).__name__}: {e}")
        return False


if __name__ == "__main__":
    for brand, name, url in REFERENCES:
        scrape_reference(brand, name, url)
        time.sleep(0.5)
    print("\n=== Done ===")
    print(f"Refs: {BASE / 'reference'}")
