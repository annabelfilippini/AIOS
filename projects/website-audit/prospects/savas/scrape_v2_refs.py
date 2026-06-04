"""V2 reference scrape for Sava's — adds Cutler & Co + Feather & Bone.

Annabel's directive: Sava's has strong photography; lean editorial/image-forward.
Cutler & Co (Melbourne fine-dining) and Feather & Bone (HK butcher/restaurant/grocer)
are the new primary references. Kept alongside v1 refs (wild-ginger, sarma, king,
la-semilla) — those remain as secondary context.

Writes:
  prospects/savas/reference/cutler-and-co/
  prospects/savas/reference/feather-and-bone/
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

REFERENCES = [
    ("cutler-and-co",   "homepage", "https://www.cutlerandco.com.au/"),
    ("cutler-and-co",   "menu",     "https://www.cutlerandco.com.au/menu"),
    ("cutler-and-co",   "about",    "https://www.cutlerandco.com.au/about"),
    ("feather-and-bone", "homepage", "https://featherandbone.com.hk/"),
    ("feather-and-bone", "restaurant", "https://featherandbone.com.hk/pages/restaurant"),
    ("feather-and-bone", "story",    "https://featherandbone.com.hk/pages/our-story"),
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


def metadata_to_dict(metadata):
    if metadata is None:
        return {}
    if hasattr(metadata, "model_dump"):
        return metadata.model_dump()
    return {k: v for k, v in vars(metadata).items() if not k.startswith("_")}


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


for brand, name, url in REFERENCES:
    scrape_reference(brand, name, url)
    time.sleep(0.5)

print("\n=== Done ===")
print(f"Refs: {BASE / 'reference'}")
