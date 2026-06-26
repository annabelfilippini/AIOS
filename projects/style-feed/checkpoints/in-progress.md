# In-progress: (none — Lululemon image fix DONE+verified, see 2026-06-18-1232 checkpoint)

## 2026-06-18 — Lululemon wrong-image bug fixed (og:image resolver)
- Root cause: listing/PDP-gallery only give color SWATCH codes (shared across a colorway),
  so Define Jacket+Cropped (77143) and Flow Y Tank+Bra (75700) got identical images.
- Fix: lululemon `image_from="listing"` -> `"og_image"`. New resolve_og_image() reads PDP
  og:image (`<styleId>_<color>_1`, unique per product) via firecrawl markdown scrape;
  new _meta_of() does `.model_dump()` on the DocumentMetadata pydantic object (no `.get`).
  run_store shares capped+cached PDP path for product_page|og_image.
- Wiped stale lululemon.json+img_cache (all first_seen=today). First re-scrape failed on the
  DocumentMetadata bug (fixed); second re-scrape (bg bxixf1dzo, /tmp/lulu_scrape2.log) STILL
  RUNNING at checkpoint — NOT yet verified.
- VERIFIED 2026-06-18: re-scrape wrote 7 items / 7 DISTINCT images (8 tiles in, 1 unresolved
  og:image skipped, non-fatal). All 7 return 200 image/webp via curl_cffi. build_feed.py clean
  (no change needed); 2 lululemon cards survived the taste filter, both with correct unique
  Scene7 URLs (LW7BY6S_075743_1, LW7DHYS_077843_1). Bug closed.


## 2026-06-17 — Aritzia unblock + daily scraper (in progress)
- Batch 1 DONE+verified: Aritzia images solved via curl_cffi proxy (NOT self-host).
  - serve.py: new GET /img?u= endpoint, allowlisted hosts only (SSRF guard), curl_cffi
    chrome120 fetch, in-memory FIFO cache. Verified 200 + valid AVIF through localhost.
  - build_feed.py: PROXY_HOSTS={assets.aritzia.com}, needs_proxy/fetch_bytes/proxied_src/
    as_jpg_url helpers. Color read + vision now use forced-JPEG bytes for Cloudflare hosts
    (PIL can't decode AVIF; Anthropic vision rejects AVIF). Card <img src> -> /img proxy.
    Root cause was Cloudflare bot mgmt (TLS fingerprint), NOT Cloudinary hotlink.
- Batch 2 NEXT: generalized scrape_stores.py (store registry, new-arrivals pull, merge to
  data/brands/<store>.json with first_seen date, trigger rebuild). Then wire Aritzia.
- Batch 3: Lululemon (PDP-image quirk) into the registry.

- Batch 2 DONE+verified: scrape_stores.py (unattended daily scraper).
  - Firecrawl key copied from ~/.claude.json into gitignored .env as FIRECRAWL_API_KEY.
  - Store registry (aritzia). Listing scrape -> dedupe by sku -> per-NEW-product PDP
    image resolve (grid images are JS/unreliable). first_seen date stamped per item.
  - Hardened: retry on Firecrawl proxy tunnel errors; image VALIDATION via curl_cffi
    (only stores images that actually 200 — PDP extraction yields dead URLs); per-item
    failure is non-fatal; new_img_cap caps PDP fetches/run.
  - Real run: 8 Aritzia tiles -> 8 valid images; rebuild kept 3 after taste filter;
    all 3 render through /img proxy (verified 200 image/avif via live serve.py).
  - build_feed.py BRANDS now includes Aritzia.
- Batch 3 DONE+verified (2026-06-18):
  - Lululemon added. NOT Cloudflare-gated (plain urllib 200 image/jpeg) -> no /img proxy,
    no PROXY_HOSTS change. Images are deterministic Scene7 URLs
    (images.lululemon.com/is/image/lululemon/<colorCode>); grid is reliable so
    image_from="listing" with img_suffix="?wid=1080&fmt=jpg" (bare URL is low-res).
    sku_re=r"/([^/?]+)\?color=". Listing URL: shop.lululemon.com/c/women-whats-new/n1zg2xznskl.
  - Two scraper fixes needed (both generic, help any store):
    1. scrape_listing now retries on EMPTY, not just on exception — Lululemon
       intermittently serves a 400 block page with 0 tiles; identical retry succeeds.
    2. LISTING_SCHEMA/PROMPT now include imageUrl — was missing (Aritzia uses PDP images),
       so every listing-mode tile was silently dropped (0 stored) until added.
    Listing branch in run_store applies img_suffix + validates via _img_ok.
  - Real run: 8 Lululemon tiles -> 8 stored, 5 kept after old-money taste filter.
  - NEW badge: build_feed.py NEW_DAYS=7 + _is_new(it) reading first_seen (ISO),
    renders <span class="badge-new">New</span> in .imgwrap, .badge-new CSS (accent pill,
    top-left). Legacy items (no first_seen) never badged. Annabel chose badge-only, no
    'New' view. Verified in browser: 11 badges (5 Lululemon + 6 Aritzia), Lululemon img
    naturalWidth=1080, badge text "New".
  - /schedule routine created: "the-edit-daily-scrape", cron 0 6 * * * (daily ~6am),
    runs `cd projects/style-feed && python3 scrape_stores.py --rebuild`.
- Post-Batch-3 (2026-06-18 same day):
  - "New" sidebar tab added (Annabel reversed badge-only call). Sentinel view like
    Loved: data-new on cards, inTab 'new' branch, has_new gating, auto-hide when none.
  - Image auto-retry handler in SCRIPT: broken thumbs were Chrome ERR_NETWORK_CHANGED
    (client blip on ~800 concurrent shopmy imgs), not dead URLs. Capture-phase 'error'
    listener refetches same url 3x w/ backoff. Hard-reload to pick up rebuilds.
- KNOWN BUG (next priority): Lululemon pics inaccurate. Scene7 url keyed by COLOR
  code only, not product, so products sharing a colorway get the same/wrong image
  (Define Jacket + Cropped both 77143; Flow Y Tank + Bra both 75700). FIX: switch
  Lululemon to image_from="product_page" (resolve real PDP image like Aritzia), find
  correct PDP Scene7 pattern (style id + color + view), validate via curl_cffi.
- NEXT (optional): full Aritzia pull (no --limit) for more old-money pieces; add more
  stores; levers for sparse New tab = raise NEW_DAYS or exempt new arrivals from brand-cap trim.

- 2026-06-18 (later): Lululemon og:image fix VERIFIED (7 items, 7 distinct
  imageUrls; Define vs Cropped + Flow Y Tank vs Bra all distinct, both
  collision-pair images 200 via curl_cffi). Desktop proof page:
  ~/Desktop/the-edit-lululemon-fix.html (base64-embedded, opens in real Chrome).
- Added REFORMATION store (Annabel's pick). https://www.thereformation.com/new,
  SFCC + Cloudinary host (media.thereformation.com, no Cloudflare → no proxy).
  image_from="listing" (grid img is per-product+color, reliable). New generic
  store option img_rewrite=[from,to] swaps Cloudinary /w_600/->/w_1080/ for
  full-res. sku_re=r"/products/[^/]+/([^/?.]+)\.html". Registered in build_feed
  BRANDS; already in LIKED_BRANDS (+16). Run: 7 tiles->7 stored, 5 kept after
  taste filter, all w_1080 200, renders in feed. Daily routine includes it
  automatically (runs all stores).

- 2026-06-19 09:26 MDT — shipped back-detail vision axis (open-back/halter/tie-back learning) + occasion filter; fixed dress/swim/active/work/accessory mis-tagging. Open: decide if Work needs sleeves; maybe restore ~2 tie-back likes lost in a live-server test. See 0926 checkpoint.
