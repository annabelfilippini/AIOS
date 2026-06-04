"""Verified-facts scraper for Frita Batidos. Yelp + GBP + own site."""

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
FACTS_DIR = BASE / "facts"
SCRAPE_DIR = FACTS_DIR / "scrape"

PROSPECTS = {
    "frita-batidos": {
        "name": "Frita Batidos",
        "city": "Ann Arbor",
        "yelp_search": "Frita Batidos Ann Arbor",
        "yelp": "https://www.yelp.com/biz/frita-batidos-ann-arbor",
        "opentable": None,  # walk-in / counter service
        "gbp_query": "Frita Batidos Ann Arbor hours phone",
        "own_site": "https://fritabatidos.com/ann-arbor",
        "press_queries": [
            "Eve Aronoff Frita Batidos James Beard 2025",
            "Frita Batidos Ann Arbor best burger 2025",
        ],
    },
}


def _to_dict(obj):
    if obj is None:
        return None
    if hasattr(obj, "model_dump"):
        return obj.model_dump()
    if isinstance(obj, dict):
        return obj
    try:
        return {k: v for k, v in vars(obj).items() if not k.startswith("_")}
    except TypeError:
        return obj


def save_screenshot(url, path):
    if not url:
        return False
    try:
        resp = requests.get(url, timeout=60)
        resp.raise_for_status()
        path.write_bytes(resp.content)
        return True
    except Exception as e:
        print(f"    screenshot download failed: {e}")
        return False


def scrape_source(slug, source, url, out_dir, want_screenshot=True):
    out_dir.mkdir(parents=True, exist_ok=True)
    print(f"  [{source}] {url}")
    try:
        formats = ["markdown"]
        if want_screenshot:
            formats.append(ScreenshotFormat(full_page=True))
        r = app.scrape(url, formats=formats, wait_for=4000)
        md = r.markdown or ""
        if not md.strip():
            return False, "empty markdown (likely bot-walled)"
        (out_dir / f"{slug}-{source}.md").write_text(f"# {slug} -- {source}\n**URL:** {url}\n\n{md}")
        print(f"    markdown: {len(md)} chars")
        if want_screenshot and getattr(r, "screenshot", None):
            save_screenshot(r.screenshot, out_dir / f"{slug}-{source}-full.png")
        low = md.lower()
        if ("captcha" in low or "are you a robot" in low or "access denied" in low
                or "unusual traffic" in low or len(md) < 200):
            return False, f"bot-wall suspected (len={len(md)})"
        return True, "ok"
    except Exception as e:
        return False, f"{type(e).__name__}: {e}"


def firecrawl_search(query, limit=5):
    try:
        r = app.search(query, limit=limit)
        d = _to_dict(r)
        if isinstance(d, dict):
            if "data" in d:
                d = d["data"]
            if isinstance(d, dict):
                return d.get("web", []) or []
            return d if isinstance(d, list) else []
        return d or []
    except Exception as e:
        print(f"    search errored: {e}")
        return []


def scrape_prospect(slug, cfg):
    print(f"\n{'='*60}\n{slug} -- {cfg['name']}\n{'='*60}")
    out = SCRAPE_DIR / slug
    out.mkdir(parents=True, exist_ok=True)
    results = {}

    # 1) Yelp
    if cfg.get("yelp"):
        ok, note = scrape_source(slug, "yelp", cfg["yelp"], out)
        results["yelp"] = {"url": cfg["yelp"], "ok": ok, "note": note}
        if not ok and cfg.get("yelp_search"):
            print(f"    searching Yelp for '{cfg['yelp_search']}'...")
            hits = firecrawl_search(f"site:yelp.com {cfg['yelp_search']}", limit=3)
            for h in hits:
                url = h.get("url") if isinstance(h, dict) else None
                if url and "/biz/" in url:
                    ok2, note2 = scrape_source(slug, "yelp-searched", url, out)
                    results["yelp_searched"] = {"url": url, "ok": ok2, "note": note2}
                    break

    # 2) Google Business Profile -- via search
    if cfg.get("gbp_query"):
        print(f"  [gbp] search: {cfg['gbp_query']}")
        hits = firecrawl_search(cfg["gbp_query"], limit=5)
        (out / f"{slug}-gbp-search.json").write_text(json.dumps(hits, indent=2, default=str))
        results["gbp_search"] = {
            "query": cfg["gbp_query"],
            "ok": bool(hits),
            "hits": len(hits) if isinstance(hits, list) else 0,
        }
        g_url = f"https://www.google.com/search?q={cfg['gbp_query'].replace(' ', '+')}"
        ok, note = scrape_source(slug, "google-search", g_url, out, want_screenshot=True)
        results["google_search"] = {"url": g_url, "ok": ok, "note": note}

    # 3) Press queries
    if cfg.get("press_queries"):
        press_out = []
        for q in cfg["press_queries"]:
            print(f"  [press] {q}")
            hits = firecrawl_search(q, limit=5)
            press_out.append({"query": q, "hits": hits})
        (out / f"{slug}-press.json").write_text(json.dumps(press_out, indent=2, default=str))
        results["press"] = {"queries": len(cfg["press_queries"])}

    (out / f"{slug}-index.json").write_text(json.dumps(results, indent=2, default=str))
    return results


def main():
    FACTS_DIR.mkdir(parents=True, exist_ok=True)
    SCRAPE_DIR.mkdir(parents=True, exist_ok=True)

    all_results = {}
    for slug, cfg in PROSPECTS.items():
        all_results[slug] = scrape_prospect(slug, cfg)
        time.sleep(1.0)

    (FACTS_DIR / "scrape-summary.json").write_text(json.dumps(all_results, indent=2, default=str))
    print(f"\n\n=== Done ===")
    print(f"Raw scrapes: {SCRAPE_DIR}")
    print(f"Summary:     {FACTS_DIR / 'scrape-summary.json'}")
    print("\nNext: synthesize facts/verified-facts.md from the raw scrapes.")


if __name__ == "__main__":
    main()
