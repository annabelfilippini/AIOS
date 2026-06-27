#!/usr/bin/env python3
"""
Re-pull each influencer's ShopMy storefront into data/sources/<handle>.json so the
feed stops going stale. Standalone + cron-able: hits Firecrawl's HTTP API directly
(FIRECRAWL_API_KEY in .env), writes the exact shape build_feed.load_products() reads
({"json": {"products": [...]}}).

Run:  python3 refresh_sources.py            # all handles
      python3 refresh_sources.py paigelorenze graceatwood   # just some

ShopMy storefronts are a client-rendered SPA (server HTML is an empty shell), so a
plain fetch returns nothing — Firecrawl with waitFor renders the page first. A render
only exposes the first ~20-40 pins, so this MERGES fresh pins into the existing file
(dedup by product id) instead of replacing — the feed only grows. An empty or garbage
pull never overwrites a good file (a transient scrape failure shouldn't wipe the feed).
Schedule it (cron/launchd) to keep sources fresh without losing history.
"""
import os, sys, re, json, time, urllib.request, urllib.error
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


# a real ShopMy product link is /shop/product/<digits> — NOT "product1" (Firecrawl's
# placeholder rows look like shopmy.us/shop/product1, which a substring check accepts).
PID_RE = re.compile(r"shopmy\.us/shop/product/(\d+)")


def pid(p):
    m = PID_RE.search(p.get("productUrl") or "")
    return m.group(1) if m else None


def is_real(p):
    return pid(p) is not None and (p.get("imageUrl") or "").startswith("http")


def load_existing(path):
    """Read a source file in either shape build_feed accepts (raw Firecrawl list
    [{"text": "..."}] or {"json": {"products": [...]}}). Returns product list."""
    if not path.exists():
        return []
    raw = json.load(open(path))
    txt = raw[0]["text"] if isinstance(raw, list) else raw
    obj = json.loads(txt) if isinstance(txt, str) else txt
    return obj.get("json", {}).get("products") or []


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
    fresh = [p for p in prods if is_real(p)]
    # ponytail: never clobber a good snapshot with an empty/garbage pull
    if not fresh:
        return f"  {h:18} 0 real pins from scrape — kept old file"
    # MERGE, don't replace: storefronts only render their first ~20-40 pins, so a
    # plain overwrite would shrink the feed. Union fresh pins into the existing base,
    # dedup by product id. Feed only grows; nothing the creator rotated off vanishes.
    base = [p for p in load_existing(path) if is_real(p)]
    by_id = {pid(p): p for p in base}
    added = sum(by_id.setdefault(pid(p), p) is p for p in fresh)
    merged = list(by_id.values())
    path.write_text(json.dumps({"json": {"products": merged}}, indent=2))
    return f"  {h:18} {len(merged):4} total (+{added} new, {len(fresh)} scraped) -> {path.name}"


def main(handles):
    key = api_key()
    with ThreadPoolExecutor(max_workers=len(handles)) as ex:
        for line in ex.map(lambda h: refresh_one(h, key), handles):
            print(line, flush=True)


if __name__ == "__main__":
    main(sys.argv[1:] or HANDLES)
