---
date: 2026-06-18
time: 20:40
project: style-feed (personal shopping feed, "The Edit")
status: in-progress
next-session: The Edit engine is solid (Aritzia, Lululemon, Reformation all clean + daily auto-scrape). Next natural moves, in order of value: (1) add another old-money store using the Reformation pattern — Sézane, Tuckernuck, Nordstrom, or J.Crew (all already in LIKED_BRANDS); (2) full Aritzia pull (drop --limit) for more pieces; (3) recover the 1 dropped Lululemon tile (7 of 8 landed — one PDP failed its og:image; re-run scrape_stores.py lululemon). Read the "add a store" recipe below before wiring a new one.
---

# Session: The Edit — Lululemon fix verified + Reformation store added

## 1. Lululemon og:image fix — VERIFIED (was unverified at 12:32 checkpoint)
The 12:32 fix (switch Lululemon image_from "listing"->"og_image" to kill the
swatch-code image collision) is confirmed working:
- Re-scrape landed 7 items, 7 DISTINCT imageUrls (each keyed by unique styleId).
- Collision pairs now differ: Define Jacket LW4CAFS_077143 vs Define Cropped
  LW3HJFS_077143; Flow Y Tank LW1GDDS_075700 vs Flow Y Bra LW2DH5S_075700.
- Both pair images return 200 via curl_cffi chrome120; all 4 render 1080px.
- Proof page (base64-embedded, opens in real Chrome despite Cloudflare gate on
  images.lululemon.com): ~/Desktop/the-edit-lululemon-fix.html.
- NOTE: 7 of 8 tiles landed; one PDP failed its og:image and was dropped
  (cosmetic). Re-running `python3 scrape_stores.py lululemon` would likely
  recover it (img_cache makes re-runs cheap).
- Headless Playwright CANNOT render images.lululemon.com (Cloudflare TLS
  fingerprint gate) — verify Lululemon via curl_cffi or Annabel's real Chrome,
  NOT the preview/Playwright browser. (Cloudinary/Reformation has no such gate.)

## 2. Added REFORMATION store (Annabel chose it from a menu)
Decision: when asked "what's next", offered add-a-store / full-Aritzia /
recover-Lulu-tile; Annabel picked add-a-store -> Reformation.

The add-a-store recipe (followed here, reusable):
1. Inspect the real new-arrivals page with firecrawl json extraction FIRST —
   get the listing URL, productUrl->sku pattern, and image host before coding.
2. Reformation specifics:
   - Listing URL: https://www.thereformation.com/new  (NOT /new-clothes -> 404).
   - Platform: Salesforce Commerce Cloud; images on Cloudinary
     media.thereformation.com/image/upload/.../w_600/PRD-SFCC/<style>/<COLOR>/<style>.1.<COLOR>
   - NO Cloudflare gate -> proxy="auto", NOT in PROXY_HOSTS, no /img proxy.
   - Grid imageUrl is per-product+color and reliable -> image_from="listing"
     (no PDP fetch needed; fast, 0 PDP image fetches).
   - sku_re = r"/products/[^/]+/([^/?.]+)\.html"  (sku like 1316984HWR).
3. New GENERIC scraper feature: store option `img_rewrite: [from, to]` does a
   str.replace on the listing image URL. Used here to swap Cloudinary
   /w_600/ -> /w_1080/ for a crisp card. Applied in run_store listing branch.
   Reusable for any future Cloudinary store.
4. Register in build_feed.py BRANDS list (explicit, not auto-discovered).
   Reformation was already in LIKED_BRANDS (+16 boost).
5. Result: 7 tiles -> 7 stored, 5 kept after taste filter, all w_1080 200,
   renders in feed (5 cards, host loads fine in headless too).

## State of The Edit
- Real store feeds wired: Aritzia (Cloudflare-proxied PDP images),
  Lululemon (og:image), Reformation (listing + Cloudinary w_1080). Plus the
  ShopMy-creator brands (Dairyboy, Zara, Revolve, Anthro, A&F).
- Daily routine "the-edit-daily-scrape" (cron 0 6 * * *) runs
  `scrape_stores.py --rebuild` = ALL stores, so Reformation flows in automatically.
- serve.py "the-edit" on 8801; feed at /feed.html. Left running this session.
- build_feed brands=8, brand_kept Reformation:5.

## Files touched
- scrape_stores.py: + reformation STORES entry; + img_rewrite generic option in
  run_store listing branch.
- build_feed.py: + ("Reformation", reformation.json) in BRANDS.
- data/brands/reformation.json (new, 7 items).
- checkpoints/in-progress.md appended.
