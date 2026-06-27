#!/usr/bin/env python3
"""
Re-pull each influencer's ShopMy storefront into data/sources/<handle>.json so the
feed stops going stale. Standalone + cron-able: hits Firecrawl's HTTP API directly
(FIRECRAWL_API_KEY in .env), writes the exact shape build_feed.load_products() reads
({"json": {"products": [...]}}).

Run:  python3 refresh_sources.py            # all handles
      python3 refresh_sources.py paigelorenze graceatwood   # just some

ShopMy storefronts are a client-rendered SPA (server HTML is an empty shell), so a
plain fetch returns nothing — Firecrawl with waitFor renders the page first. An empty
pull NEVER overwrites a good file (a transient scrape failure shouldn't wipe the feed).
"""
import os, sys, json, time, urllib.request, urllib.error
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "data" / "sources"

# handle == filename stem == the SOURCES entries build_feed.py reads.
HANDLES = [
    "brigettepheloung", "paigelorenze", "abbycatlin", "carlyriordan",
    "graceatwood", "merrittbeck", "marylawlesslee",
]

SCHEMA = {"type": "object", "properties": {"products": {"type": "array", "items": {"type": "object",
    "properties": {"title": {"type": "string"}, "brand": {"type": "string"}, "price": {"type": "string"},
                   "imageUrl": {"type": "string"}, "productUrl": {"type": "string"}}}}}}
PROMPT = ("Extract every product pin shown on this ShopMy storefront. For each: title, brand, "
          "price, imageUrl (the product image), and productUrl (the shopmy.us/shop/product link).")


def api_key():
    for line in (ROOT / ".env").read_text().splitlines():
        if line.startswith("FIRECRAWL_API_KEY="):
            return line.split("=", 1)[1].strip()
    raise SystemExit("FIRECRAWL_API_KEY not found in .env")


def scrape(handle, key, tries=3):
    body = {"url": f"https://shopmy.us/shop/{handle}",
            "formats": [{"type": "json", "prompt": PROMPT, "schema": SCHEMA}],
            "waitFor": 8000, "timeout": 60000}
    req = urllib.request.Request("https://api.firecrawl.dev/v2/scrape",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    last = None
    for attempt in range(tries):
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=120).read())
            return (r.get("data") or {}).get("json", {}).get("products") or []
        except urllib.error.HTTPError as e:
            # 408/429/5xx are transient — back off and retry; 4xx auth/bad-request aren't
            if e.code not in (408, 429, 500, 502, 503, 504):
                raise
            last = e
            time.sleep(5 * (attempt + 1))
    raise last


def refresh_one(h, key):
    path = SRC / f"{h}.json"
    try:
        prods = scrape(h, key)
    except urllib.error.HTTPError as e:
        return f"  {h:18} HTTP {e.code} — kept old file"
    except Exception as e:
        return f"  {h:18} {type(e).__name__}: {e} — kept old file"
    # ponytail: never clobber a good snapshot with an empty/failed pull
    if not prods:
        return f"  {h:18} 0 products — kept old file"
    # keep only the well-formed pins (need an image + a shop link to be usable)
    prods = [p for p in prods if p.get("imageUrl") and p.get("productUrl")]
    path.write_text(json.dumps({"json": {"products": prods}}, indent=2))
    return f"  {h:18} {len(prods):3} products -> {path.name}"


def main(handles):
    key = api_key()
    with ThreadPoolExecutor(max_workers=len(handles)) as ex:
        for line in ex.map(lambda h: refresh_one(h, key), handles):
            print(line, flush=True)


if __name__ == "__main__":
    main(sys.argv[1:] or HANDLES)
