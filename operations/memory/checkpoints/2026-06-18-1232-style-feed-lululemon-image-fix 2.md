---
date: 2026-06-18
time: 12:32
project: style-feed (personal shopping feed, "The Edit")
status: in-progress
next-session: Verify the re-scrape wrote 8 Lululemon items with 8 DISTINCT correct images (run was still in flight at checkpoint). Then `python3 build_feed.py` (or `scrape_stores.py --rebuild`) and confirm in browser that Define Jacket vs Define Cropped Jacket (and Flow Y Tank vs Bra) now show different, correct product shots. If any item is missing, it's an unresolved og:image — re-run; img_cache makes re-runs cheap.
---

# Session: The Edit — Lululemon wrong-image bug fixed (og:image resolver)

## The bug we fixed
Lululemon product images were wrong/duplicated. Root cause: the listing grid and
the PDP image gallery only expose color SWATCH codes (e.g. `77143`), which are
SHARED by every product in that colorway. So Define Jacket + Define Cropped Jacket
(both 77143) and Flow Y Tank + Flow Y Bra (both 75700) got identical images. The
old config used `image_from="listing"` with `images.lululemon.com/is/image/lululemon/<swatchcode>`
— inherently collision-prone.

## The fix (root cause, not a patch)
The unique per-product image is the PDP `og:image` meta tag:
`images.lululemon.com/is/image/lululemon/<styleId>_<color>_1`
e.g. Define Jacket = `LW4CAFS_077143_1`, Define Cropped = `LW3HJFS_077143_1`
(verified distinct; both render 200 as ~45KB webp with `?wid=1080&fmt=jpg`).

Changes in `scrape_stores.py`:
- Lululemon store config: `image_from` changed `"listing"` -> `"og_image"`
  (kept `img_suffix="?wid=1080&fmt=jpg"`, `sku_re`, `proxy="stealth"`).
- New `_meta_of(doc)` helper — returns page meta as a plain dict. CRITICAL: firecrawl-py
  wraps metadata in a `DocumentMetadata` pydantic object (no `.get`); must call
  `.model_dump()`. First run failed on every item with
  `'DocumentMetadata' object has no attribute 'get'` until this was added.
- New `resolve_og_image(product_url, store, tries=4)` — cheap markdown scrape, reads
  `og_image` (fallback `og:image`) off metadata, appends img_suffix, validates via
  `_img_ok` (curl_cffi chrome120). Retries because the PDP intermittently serves a
  400 block page (no metadata); identical retry succeeds.
- `run_store` image branch: `product_page` and `og_image` now share the capped+cached
  PDP-resolve path (`resolver = resolve_og_image if ... == "og_image" else resolve_pdp_image`).

## State at checkpoint
- Wiped stale `data/brands/lululemon.json` + `lululemon.img_cache.json` (all 8 items had
  `first_seen=2026-06-18` = today, so nothing lost). img_cache was already empty.
- First re-scrape FAILED (the DocumentMetadata `.get` bug) -> 0 items written.
- Both `_meta_of` and the og_image key lookup were then fixed.
- Second re-scrape (`/tmp/lulu_scrape2.log`, bg task `bxixf1dzo`) was STILL RUNNING at
  checkpoint — Firecrawl stealth + per-PDP retries is slow (~5+ min for 8 tiles).
  NOT yet verified.

## build_feed.py — no change needed
`images.lululemon.com` is NOT in PROXY_HOSTS, so Lululemon loads direct (no /img proxy)
and skips the Aritzia AVIF->jpg path (that path is gated on `needs_proxy(url)`). webp is
fine for both PIL color-read and Anthropic vision. Just rebuild after the scrape lands.

## Context to preserve
- Run one store: `python3 scrape_stores.py lululemon` ; rebuild feed: add `--rebuild`.
- serve.py launch config "the-edit" on 8801. Verify renders by fetching image URLs
  through curl_cffi / the live server, not the preview MCP (it pins a generic server).
- og:image extraction works via firecrawl-py `fc.scrape(url, formats=['markdown'], proxy='auto')`
  then `doc.metadata.model_dump()['og_image']`. The AI JSON-extraction engine returns
  SWATCH garbage — do NOT use it for Lululemon images.
- Progress log: `projects/style-feed/checkpoints/in-progress.md`.

## Open / next
1. Confirm 8 items, 8 distinct images; rebuild; eyeball Define vs Cropped in browser.
2. The daily `/schedule` routine "the-edit-daily-scrape" already wraps
   `scrape_stores.py --rebuild` — the og_image fix flows into it automatically.
3. Optional: full Aritzia pull (no --limit); more stores.
