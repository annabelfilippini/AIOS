#!/usr/bin/env python3
"""
scrape_stores.py — daily new-arrivals pull for The Edit.

For each registered store it:
  1. scrapes the store's "new arrivals" listing (Firecrawl, stealth proxy) and
     extracts {title, price, productUrl};
  2. dedupes against the existing data/brands/<store>.json by product id;
  3. for genuinely-new items, resolves the real product image — the grid images
     are JS-built and unreliable, so we read it off the product page (cached to
     data/brands/<store>.img_cache.json so a sku is only ever fetched once);
  4. merges, stamping each item with a first_seen date so build_feed.py can badge
     fresh drops, and writes the brand file in build_feed's expected shape.

Images on Cloudflare-fronted hosts (Aritzia) keep their real CDN URL here;
build_feed.py + serve.py route them through the /img proxy at render time.

Run:
  python3 scrape_stores.py                 # all stores, no rebuild
  python3 scrape_stores.py aritzia         # one store
  python3 scrape_stores.py --rebuild       # all stores, then rebuild feed
  python3 scrape_stores.py aritzia --limit 30 --rebuild

Designed to run unattended on a daily /schedule routine.
"""
import os, re, sys, json, time, pathlib, datetime, subprocess

ROOT = pathlib.Path(__file__).resolve().parent
BRANDS_DIR = ROOT / "data" / "brands"
TODAY = datetime.date.today().isoformat()

# ---- store registry ---------------------------------------------------------
# image_from: "product_page" => grid images unreliable, read the PDP (cached).
#             "listing"      => trust the imageUrl the grid extraction returns.
STORES = {
    "aritzia": {
        "name": "Aritzia",
        "file": "aritzia.json",
        "listings": ["https://www.aritzia.com/us/en/new"],
        "proxy": "stealth",
        "image_from": "product_page",
        "sku_re": r"/(\d{5,})\.html",          # .../product/<slug>/131517.html
    },
    "lululemon": {
        "name": "lululemon",
        "file": "lululemon.json",
        "listings": ["https://shop.lululemon.com/c/women-whats-new/n1zg2xznskl"],
        "proxy": "stealth",
        # The grid/PDP-gallery only exposes color SWATCH codes (e.g. 77143), which
        # COLLIDE across every product sharing a colorway. The unique per-product
        # image is the PDP og:image meta tag: <styleId>_<color>_1 (e.g. LW4CAFS_077143_1).
        "image_from": "og_image",
        "img_suffix": "?wid=1080&fmt=jpg",     # bare Scene7 URL is low-res; force sized image
        "sku_re": r"/([^/?]+)\?color=",        # .../prod11020158?color=77143 or .../slug?color=
    },
    "reformation": {
        "name": "Reformation",
        "file": "reformation.json",
        "listings": ["https://www.thereformation.com/new"],
        "proxy": "auto",
        # Salesforce Commerce Cloud + Cloudinary image host (no Cloudflare gate, so
        # no /img proxy needed). The grid imageUrl is per-product+color and reliable
        # (filename = <style>.1.<COLOR>), so trust the listing image. Cloudinary
        # serves it at w_600; rewrite to w_1080 for a crisp card image.
        "image_from": "listing",
        "img_rewrite": ["/w_600/", "/w_1080/"],
        "sku_re": r"/products/[^/]+/([^/?.]+)\.html",   # .../charlee.../1316984HWR.html
    },
}

DEFAULT_NEW_IMG_CAP = 40   # max per-product image resolutions per store per run

# ---- env / firecrawl --------------------------------------------------------
def _load_env():
    envf = ROOT / ".env"
    if not envf.exists():
        return
    for line in envf.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        k, v = line.split("=", 1)
        os.environ.setdefault(k.strip(), v.strip().strip('"').strip("'"))

_load_env()
_fc = None
def fc():
    global _fc
    if _fc is None:
        from firecrawl import Firecrawl
        key = os.environ.get("FIRECRAWL_API_KEY")
        if not key:
            sys.exit("FIRECRAWL_API_KEY missing from .env — cannot scrape.")
        _fc = Firecrawl(api_key=key)
    return _fc

# ---- schemas ----------------------------------------------------------------
LISTING_SCHEMA = {
    "type": "object",
    "properties": {"products": {"type": "array", "items": {"type": "object", "properties": {
        "title": {"type": "string"},
        "brand": {"type": "string"},
        "price": {"type": "string"},
        "productUrl": {"type": "string"},
        "imageUrl": {"type": "string"},
    }}}},
}
LISTING_PROMPT = ("This is a women's clothing 'new arrivals' grid. Extract every product tile. "
                  "For each: title, brand (the label shown, else the store name), price, "
                  "productUrl (the full https link to that product's page), and imageUrl "
                  "(the full-resolution product image src URL including the CDN host). "
                  "Stores that read images from the product page may omit imageUrl.")

PDP_SCHEMA = {
    "type": "object",
    "properties": {"imageUrls": {"type": "array", "items": {"type": "string"}}},
}
PDP_PROMPT = ("Extract the product gallery image URLs in order — the full-resolution image src "
              "URLs including the CDN host. Return the main on-model front image first.")

# ---- helpers ----------------------------------------------------------------
def _json_of(doc):
    """firecrawl-py returns an object with .json (dict) for json format."""
    j = getattr(doc, "json", None)
    if j is None and isinstance(doc, dict):
        j = doc.get("json")
    return j or {}

def _meta_of(doc):
    """Page <meta> tags (incl. og:image). firecrawl-py wraps them in a
    DocumentMetadata pydantic object (no .get) — normalize to a plain dict."""
    m = getattr(doc, "metadata", None)
    if m is None and isinstance(doc, dict):
        m = doc.get("metadata")
    if m is not None and hasattr(m, "model_dump"):
        m = m.model_dump()
    return m or {}

def _scrape(url, fmt, store, tries=3):
    """fc().scrape with retry — Firecrawl proxy tunnels fail transiently."""
    last = None
    for i in range(tries):
        try:
            return fc().scrape(url, formats=[fmt],
                               proxy=store.get("proxy", "auto"), wait_for=6000)
        except Exception as e:
            last = e
            time.sleep(2 * (i + 1))
    raise last

def scrape_listing(url, store, tries=4):
    """Retry on EMPTY, not just on exception: some stores (lululemon) intermittently
    render a 400 block page with zero tiles, and an identical retry then succeeds."""
    last = []
    for i in range(tries):
        doc = _scrape(url, {"type": "json", "prompt": LISTING_PROMPT,
                            "schema": LISTING_SCHEMA}, store)
        last = _json_of(doc).get("products", []) or []
        if last:
            return last
        time.sleep(2 * (i + 1))
    return last

_curl = None
def _img_ok(url):
    """True if the image actually loads (Chrome fingerprint, as the proxy will)."""
    global _curl
    if _curl is None:
        from curl_cffi import requests as _r
        _curl = _r
    try:
        x = _curl.get(url, impersonate="chrome120", timeout=20)
        return x.status_code == 200 and (x.headers.get("content-type", "")).startswith("image")
    except Exception:
        return False

def resolve_pdp_image(product_url, store):
    """Return the first gallery image that actually loads — PDP extraction
    sometimes yields dead URLs, which must never reach the feed. On-model
    front frames (_on_a) are tried first."""
    doc = _scrape(product_url, {"type": "json", "prompt": PDP_PROMPT,
                                "schema": PDP_SCHEMA}, store)
    imgs = _json_of(doc).get("imageUrls", []) or []
    ordered = [u for u in imgs if "_on_a" in u] + [u for u in imgs if "_on_a" not in u]
    for u in ordered:
        if _img_ok(u):
            return u
    return None

def resolve_og_image(product_url, store, tries=4):
    """lululemon: the only per-product image is the PDP og:image meta tag
    (<styleId>_<color>_1). It lives in the static head, so a cheap markdown
    scrape carries it on .metadata. Retries because the PDP intermittently
    serves a 400 block page (no metadata); an identical retry then succeeds."""
    for i in range(tries):
        doc = _scrape(product_url, "markdown", store)
        meta = _meta_of(doc)
        og = (meta.get("og_image") or meta.get("og:image") or "").strip()
        if og:
            img = og + store.get("img_suffix", "")
            return img if _img_ok(img) else None
        time.sleep(2 * (i + 1))
    return None

def sku_of(url, store):
    m = re.search(store["sku_re"], url or "")
    return m.group(1) if m else None

def load_brand(path):
    """Return existing items keyed by id, preserving first_seen + resolved image."""
    if not path.exists():
        return {}
    raw = json.load(open(path))
    prods = (raw.get("json", {}) or {}).get("products", []) if isinstance(raw, dict) else []
    return {p["id"]: p for p in prods if p.get("id")}

def load_img_cache(path):
    return json.load(open(path)) if path.exists() else {}

# ---- per-store run ----------------------------------------------------------
def run_store(key, limit=None, new_img_cap=DEFAULT_NEW_IMG_CAP):
    store = STORES[key]
    bpath = BRANDS_DIR / store["file"]
    ipath = BRANDS_DIR / (pathlib.Path(store["file"]).stem + ".img_cache.json")
    existing = load_brand(bpath)
    img_cache = load_img_cache(ipath)

    seen, new_count, resolved = {}, 0, 0
    for url in store["listings"]:
        rows = scrape_listing(url, store)
        if limit:
            rows = rows[:limit]
        print(f"  [{key}] listing {url} -> {len(rows)} tiles")
        for r in rows:
            pu = (r.get("productUrl") or "").strip()
            sid = sku_of(pu, store)
            if not sid or sid in seen:
                continue
            title = (r.get("title") or "").strip()
            if not title:
                continue
            prior = existing.get(sid)
            # image: reuse prior/cached; only fetch PDP for genuinely-new skus
            img = (prior or {}).get("imageUrl") or img_cache.get(sid)
            if not img and store["image_from"] in ("product_page", "og_image") and resolved < new_img_cap:
                resolver = resolve_og_image if store["image_from"] == "og_image" else resolve_pdp_image
                try:
                    img = resolver(pu, store)
                    resolved += 1
                    if img:
                        img_cache[sid] = img
                except Exception as e:
                    print(f"    ! PDP image failed for {sid}: {str(e)[:80]} — skipping")
                    continue   # leave for a later run, don't crash the store
            elif not img and store["image_from"] == "listing":
                img = (r.get("imageUrl") or "").strip() or None
                if img and store.get("img_rewrite"):     # e.g. Cloudinary /w_600/ -> /w_1080/
                    a, b = store["img_rewrite"]
                    img = img.replace(a, b)
                if img and store.get("img_suffix") and "?" not in img:
                    img += store["img_suffix"]
                if img and not _img_ok(img):    # never let a dead grid URL reach the feed
                    img = None
            if not img:
                continue   # no usable image -> skip (don't poison the feed)
            seen[sid] = {
                "id": sid,
                "title": title,
                "brand": (r.get("brand") or store["name"]).strip() or store["name"],
                "price": (r.get("price") or "").strip(),
                "imageUrl": img,
                "productUrl": pu,
                "first_seen": (prior or {}).get("first_seen", TODAY),
            }
            if prior is None:
                new_count += 1

    # merge: keep everything we've ever seen for this store; refresh current tiles
    merged = dict(existing)
    merged.update(seen)
    products = list(merged.values())
    BRANDS_DIR.mkdir(parents=True, exist_ok=True)
    json.dump({"json": {"products": products}}, open(bpath, "w"), indent=1)
    json.dump(img_cache, open(ipath, "w"), indent=1)
    print(f"  [{key}] {len(products)} total | {new_count} new today | {resolved} PDP image fetches")
    return new_count

# ---- cli --------------------------------------------------------------------
def main(argv):
    rebuild = "--rebuild" in argv
    limit = next((int(argv[i+1]) for i, a in enumerate(argv) if a == "--limit"), None)
    skip = {i+1 for i, a in enumerate(argv) if a == "--limit"}   # the value after --limit
    args = [a for i, a in enumerate(argv) if not a.startswith("-") and i not in skip]
    keys = args or list(STORES)
    bad = [k for k in keys if k not in STORES]
    if bad:
        sys.exit(f"unknown store(s): {bad}. known: {list(STORES)}")
    total_new = 0
    for k in keys:
        print(f"== {k} ==")
        total_new += run_store(k, limit=limit)
    print(f"\nDONE. {total_new} new item(s) across {len(keys)} store(s).")
    if rebuild:
        print("rebuilding feed...")
        subprocess.run([sys.executable, str(ROOT / "build_feed.py")], check=True)

if __name__ == "__main__":
    main(sys.argv[1:])
