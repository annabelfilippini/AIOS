---
date: 2026-06-18
time: 11:50
project: style-feed (personal shopping feed, "The Edit")
status: in-progress
next-session: FIX Lululemon image accuracy (known bug, root cause diagnosed). Scene7 images are keyed by COLOR CODE only, not product, so products sharing a colorway get the same/wrong image. Switch Lululemon to image_from="product_page" (resolve the real PDP image like Aritzia) instead of trusting the bare color-code URL. Then re-verify pics match titles.
---

# Session: The Edit — New tab + image auto-retry + Lululemon pic bug found

## What we worked on
Follow-on to Batch 3. Annabel reviewed the live feed, hit broken thumbnails,
and asked for a way to see just the new items. Added a "New" sidebar tab and an
image auto-retry handler. Diagnosed (not yet fixed) why Lululemon pics are wrong.

## Decisions made / shipped
- **"New" sidebar tab added** (build_feed.py). Works like the "Loved" view: a
  sentinel, not a category. TAB_DEFS gained ("new","New","new") right after All;
  cards carry data-new="1" when _is_new (first_seen within NEW_DAYS=7); inTab()
  early-returns on data-new; tab auto-hides when has_new is False; empty message
  "No new arrivals right now." Annabel reversed her earlier badge-only call —
  she wanted the dedicated view after seeing new items buried under creator picks.
- **Image auto-retry handler** (top of SCRIPT in build_feed.py). Broken thumbnails
  were Chrome ERR_NETWORK_CHANGED (client-side network blip on a burst of ~800
  static.shopmy.us images), NOT dead URLs — I tested 60 ShopMy URLs @40 concurrent,
  all 200. A failed <img> never refetches on its own. New handler: capture-phase
  'error' listener refetches the SAME url (no query mutation, keeps signed CDN urls
  valid) up to 3x with backoff. Tell Annabel to hard-reload (Cmd+Shift+R) to pick
  up any rebuild.

## KNOWN BUG (next session priority): Lululemon pics inaccurate
- **Root cause diagnosed:** Lululemon Scene7 image URL is
  `images.lululemon.com/is/image/lululemon/<colorCode>` — keyed by COLOR code only,
  NOT by product. Proof from the 8-item pull: Define Jacket + Define Cropped Jacket
  both map to color 77143 (same image); Flow Y Tank + Flow Y Bra both map to 75700.
  The bare color-code image is not product-specific, so the wrong photo shows.
- **Fix next time:** stop trusting the listing/color-code image. Switch Lululemon to
  image_from="product_page" (resolve the real PDP gallery image like Aritzia) and
  find Lululemon's correct PDP Scene7 pattern (style id + color + view, e.g.
  `<STYLE>_<color>_on_a` style paths), validating via curl_cffi. Keep the empty-retry
  on scrape_listing. Then re-verify each pic matches its title.
- Current Lululemon items in the feed are therefore unreliable photos — fine to
  leave for now, Annabel is aware.

## Files touched this session
- build_feed.py: data-new on card(); new_flag computed once; TAB_DEFS + has_new
  gating + _present("new"); inTab 'new' branch; empty-state 'new' message;
  image error-retry listener at top of SCRIPT.
- (Batch 3 earlier same day: scrape_stores.py lululemon + listing fixes,
  build_feed.py NEW badge — see 2026-06-18-1025 checkpoint.)

## Verification
- tabs now: All · New · Tops · … · Loved. 6 cards data-new="1" this build.
- Could not drive Annabel's browser (she had the page open — profile lock); verified
  structurally (tab button present, data-new count, deterministic inTab JS).
- ShopMy URL health: 60/60 returned 200 image/jpeg.

## Context to preserve
- serve.py left running on 8801 for review.
- Playwright MCP screenshots save to a sandboxed dir the shell can't read — verify
  renders programmatically (now also noted in ~/.claude/CLAUDE.md).
- "Run now" on the the-edit-daily-scrape task (Scheduled sidebar) pre-approves tools
  so 6am runs don't stall — Annabel to do once.
- Brand catalogs get trimmed to keep feed creator-led, and Aritzia/Lululemon skew
  athletic so the old-money filter drops many — New count stays modest. Levers if
  too sparse: raise NEW_DAYS, or exempt new arrivals from the brand-cap trim.
