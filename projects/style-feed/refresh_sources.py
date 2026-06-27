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


def scrape(handle, key):
    body = {"url": f"https://shopmy.us/shop/{handle}",
            "formats": [{"type": "json", "prompt": PROMPT, "schema": SCHEMA}],
            "waitFor": 8000, "timeout": 60000}
    req = urllib.request.Request("https://api.firecrawl.dev/v2/scrape",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"})
    r = json.loads(urllib.request.urlopen(req, timeout=90).read())
    return (r.get("data") or {}).get("json", {}).get("products") or []


def main(handles):
    key = api_key()
    for h in handles:
        path = SRC / f"{h}.json"
        try:
            prods = scrape(h, key)
        except urllib.error.HTTPError as e:
            print(f"  {h:18} HTTP {e.code} — kept old file")
            continue
        except Exception as e:
            print(f"  {h:18} {type(e).__name__}: {e} — kept old file")
            continue
        # ponytail: never clobber a good snapshot with an empty/failed pull
        if not prods:
            print(f"  {h:18} 0 products — kept old file")
            continue
        # keep only the well-formed pins (need an image + a shop link to be usable)
        prods = [p for p in prods if p.get("imageUrl") and p.get("productUrl")]
        path.write_text(json.dumps({"json": {"products": prods}}, indent=2))
        print(f"  {h:18} {len(prods):3} products -> {path.name}")
        time.sleep(1)  # be polite between scrapes


if __name__ == "__main__":
    main(sys.argv[1:] or HANDLES)
