"""Firecrawl scrape of Miss Kim Ann Arbor + 4 reference sites + verified-facts sources."""

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

MISS_KIM_PAGES = [
    ("homepage", "https://misskimannarbor.com/"),
    ("menu", "https://misskimannarbor.com/menu"),
    ("about", "https://misskimannarbor.com/about"),
    ("reservations", "https://misskimannarbor.com/reservations"),
    ("private-events", "https://misskimannarbor.com/private-events"),
    ("contact", "https://misskimannarbor.com/contact"),
]

REFERENCES = [
    ("rare-bird", "homepage", "https://www.rarebirdrooftop.com/"),
    ("bull-and-last", "homepage", "https://thebullandlast.co.uk/"),
    ("bull-and-last", "menus", "https://thebullandlast.co.uk/pages/menus"),
    ("king", "homepage", "https://kingrestaurant.nyc/"),
    ("la-semilla", "homepage", "https://www.lasemilla.kitchen/"),
]

# Verified-facts sources for Miss Kim
FACTS_SOURCES = [
    ("yelp", "https://www.yelp.com/biz/miss-kim-ann-arbor"),
    ("opentable", "https://www.opentable.com/miss-kim"),
    ("google-search", "https://www.google.com/search?q=Miss+Kim+Ann+Arbor+hours+phone+address"),
    ("zingermans-profile", "https://www.zingermanscommunity.com/miss-kim/"),
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


def scrape_three_pass(name, url, out_dir, screenshots_dir):
    out_dir.mkdir(parents=True, exist_ok=True)
    screenshots_dir.mkdir(parents=True, exist_ok=True)
    print(f"\n{'='*60}\n{name} ({url})\n{'='*60}")

    try:
        r = app.scrape(url, formats=["markdown", ScreenshotFormat(full_page=True)], wait_for=4000)
        md = r.markdown or ""
        (out_dir / f"{name}.md").write_text(f"# {name}\n**URL:** {url}\n\n{md}")
        print(f"  markdown: {len(md)} chars")
        save_screenshot(r.screenshot, screenshots_dir / f"{name}-desktop-full.png")
        meta = metadata_to_dict(r.metadata)
        (out_dir / f"{name}-metadata.json").write_text(json.dumps(meta, indent=2, default=str))
    except Exception as e:
        print(f"  ERROR (desktop-full): {type(e).__name__}: {e}")

    try:
        r = app.scrape(url, formats=["screenshot"], mobile=True, wait_for=4000)
        save_screenshot(r.screenshot, screenshots_dir / f"{name}-mobile.png")
    except Exception as e:
        print(f"  ERROR (mobile): {type(e).__name__}: {e}")


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


def scrape_facts_source(name, url):
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


# === Miss Kim core pages ===
mk_out = BASE / "scrape"
mk_shots = mk_out / "screenshots"
for name, url in MISS_KIM_PAGES:
    scrape_three_pass(name, url, mk_out, mk_shots)
    time.sleep(0.5)

# === References ===
for brand, name, url in REFERENCES:
    scrape_reference(brand, name, url)
    time.sleep(0.5)

# === Verified facts ===
facts_results = {}
for name, url in FACTS_SOURCES:
    ok, note = scrape_facts_source(name, url)
    facts_results[name] = {"url": url, "ok": ok, "note": note}
    time.sleep(0.5)

(BASE / "facts" / "scrape-summary.json").write_text(json.dumps(facts_results, indent=2, default=str))

print("\n\n=== Done ===")
print(f"Miss Kim:  {mk_out}")
print(f"Refs:      {BASE / 'reference'}")
print(f"Facts:     {BASE / 'facts'}")
