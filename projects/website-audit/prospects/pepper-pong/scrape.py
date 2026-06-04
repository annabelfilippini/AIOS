"""Firecrawl scrape of pepperpong.com — screenshots + rendered content for audit."""

import os
import json
import requests
from pathlib import Path
from dotenv import load_dotenv
from firecrawl import FirecrawlApp
from firecrawl.v2.types import ScreenshotFormat

# Project root is three levels up: prospects/pepper-pong/scrape.py → website-audit/
PROJECT_ROOT = Path(__file__).resolve().parent.parent.parent
load_dotenv(PROJECT_ROOT / ".env")
API_KEY = os.environ["FIRECRAWL_API_KEY"]
app = FirecrawlApp(api_key=API_KEY)

OUTPUT_DIR = Path(__file__).resolve().parent / "scrape"
OUTPUT_DIR.mkdir(exist_ok=True)
SCREENSHOTS_DIR = OUTPUT_DIR / "screenshots"
SCREENSHOTS_DIR.mkdir(exist_ok=True)

PAGES = [
    ("homepage", "https://pepperpong.com"),
    ("product-full-set", "https://pepperpong.com/products/pepper-pong-full-set"),
    ("our-story", "https://pepperpong.com/pages/our-story"),
    ("how-to-play", "https://pepperpong.com/pages/how-to-play"),
    ("schools", "https://pepperpong.com/pages/schools"),
    ("press", "https://pepperpong.com/pages/press"),
    ("reviews", "https://pepperpong.com/pages/reviews"),
    ("faq", "https://pepperpong.com/pages/frequently-asked-questions"),
]


def save_screenshot(screenshot_url, path):
    """Download screenshot from URL and save locally."""
    if not screenshot_url:
        print(f"  No screenshot for {path.name}")
        return False
    resp = requests.get(screenshot_url, timeout=30)
    resp.raise_for_status()
    path.write_bytes(resp.content)
    print(f"  Screenshot: {len(resp.content)//1024}KB -> {path.name}")
    return True


for name, url in PAGES:
    print(f"\n{'='*60}")
    print(f"Scraping: {name} ({url})")
    print(f"{'='*60}")

    # 1. Desktop full-page screenshot + markdown
    try:
        result = app.scrape(
            url,
            formats=["markdown", ScreenshotFormat(full_page=True)],
            wait_for=3000,
        )

        md_content = result.markdown or ""
        md_path = OUTPUT_DIR / f"{name}.md"
        md_path.write_text(f"# {name}\n**URL:** {url}\n\n{md_content}")
        print(f"  Markdown: {len(md_content)} chars -> {md_path.name}")

        save_screenshot(result.screenshot, SCREENSHOTS_DIR / f"{name}-desktop-full.png")

        meta = result.metadata_dict
        meta_path = OUTPUT_DIR / f"{name}-metadata.json"
        meta_path.write_text(json.dumps(meta, indent=2, default=str))
        print(f"  Metadata: {meta_path.name}")

    except Exception as e:
        print(f"  ERROR (desktop full): {type(e).__name__}: {e}")

    # 2. Desktop viewport screenshot
    try:
        vp_result = app.scrape(url, formats=["screenshot"], wait_for=3000)
        save_screenshot(vp_result.screenshot, SCREENSHOTS_DIR / f"{name}-desktop-viewport.png")
    except Exception as e:
        print(f"  ERROR (viewport): {type(e).__name__}: {e}")

    # 3. Mobile screenshot
    try:
        mob_result = app.scrape(url, formats=["screenshot"], mobile=True, wait_for=3000)
        save_screenshot(mob_result.screenshot, SCREENSHOTS_DIR / f"{name}-mobile.png")
    except Exception as e:
        print(f"  ERROR (mobile): {type(e).__name__}: {e}")

print(f"\n\nDone! Files saved to {OUTPUT_DIR}")
print(f"Screenshots: {SCREENSHOTS_DIR}")
