---
date: 2026-06-27 17:00
project: life-os
status: in-progress
type: checkpoint
slug: life-os-shopmy-cron-pinterest-scrape
---

# The Edit: real Pinterest board scraped, ShopMy made consistent + daily cron, feed consolidation agreed

## What was wrong (Annabel's two questions)
1. **"Is influencer ShopMy being pulled consistently?"** No. Sources were static
   one-time snapshots from June 16-17 (`data/sources/*.json`), no scraper, no schedule.
2. **"The Pinterest board isn't my pins."** Correct — the `pinterest-board/` board was
   NEVER her account. A prior session built it from random Pinterest *search* images as
   a taste guess. She has a real board now: https://www.pinterest.com/annabelflip1/clothes/

## Batch 1 — BUILT this session
- **ShopMy refresh** `projects/style-feed/refresh_sources.py` (NEW). Standalone, hits
  Firecrawl v2 `/scrape` directly (FIRECRAWL_API_KEY in `.env`). Hit + fixed 3 real
  failure modes: (a) transient 408s → retry/backoff; (b) Firecrawl returns HALLUCINATED
  placeholder rows ("Brand A | Product 1", url `shopmy.us/shop/product1`) when a
  storefront doesn't render → strict guard `re.compile(r"shopmy\.us/shop/product/\d+")`
  (note: substring check is NOT enough — placeholders contain "shopmy.us/shop/product");
  (c) storefronts only render first ~20-40 pins → **MERGE not replace** (union by product
  id, never shrinks). Restored all 7 rich originals from git `7d217d1` as the merge base.
  Final real pins: brigette 168, paige 175, abby 44, carly 504, grace 198, merritt 252,
  mary 42 = **1,383 total**. brigette ONLY ever returns placeholders to Firecrawl (her
  storefront quirk) — base preserved, live adds nothing. paige+carly 408'd last run
  (bases safe). Self-check in script logic verified.
- **Pinterest scrape** `projects/style-feed/refresh_pinterest.py` (NEW). Uses
  `gallery-dl -j --cookies-from-browser chrome` (NOT Firecrawl — same pattern as IG, see
  [[reference_instagram_scraping]]). Her "Clothes" board = exactly 28 pins, all pulled to
  `data/pinterest/clothes.json` ({id,img,link,title,desc}). Most are pure image
  inspiration (i.pinimg.com/originals), a few Amazon shop links. Merge-mode by pin id.
- **Daily cron** `projects/style-feed/refresh_all.sh` (NEW) runs both. Scheduled via
  **crontab** at `30 6 * * *` (NOT launchd — launchd hit TCC exit-78 writing to
  ~/Documents; crontab already has FDA on this machine, proven by autosync + wayloft +
  apartment-hunt jobs). gallery-dl cookie access under cron is the one unverified bit;
  if it fails Pinterest just keeps old pins (ShopMy half needs no cookies, always works).

## Batch 2 — AGREED, NOT STARTED (the real Life OS work)
Annabel: "Why so many HTMLs?" (feed/lookbook/quickchoose/the-edit/pinterest-board = 5
surfaces). She wants **ONE feed/lookbook** where everything lives — her closet + Pinterest
+ influencer ShopMy + brands — that she ♥/✕ on, feeding **ONE morning debrief** that
builds outfits. Retire the other surfaces.
- **Key relaxation she gave:** outfits do NOT need to be only clothes she owns. Aspirational
  items are fine — she uses them as inspiration + to discover new clothes to buy. So NO
  hard closet gate on the outfit builder (simpler than the prior plan).
- This also fixes the headline bug from [[2026-06-26-1627-life-os-style-engine-ignores-feedback]]:
  `style_engine.py` never reads `feedback.json` (her 612 ♥/✕). Unify so the one feed's
  reactions are the only taste signal.
- Pinterest pins still need vision-tagging onto her taste vocab — reuse `build_feed.py`'s
  existing vision tagger (it already labeled 1,305 influencer imgs to `vision_cache.json`).
- Recon done: Pinterest is NOT yet a source in `build_feed.py` (SOURCES = influencers,
  BRANDS, Nuuly only). Closet feeds `style_engine.py`; feedback feeds only the feed rerank.

## Also done this session
- Pinterest BOARD layout fix (`pinterest-board/build_board.py`): forced
  `aspect-ratio:3/4`+`object-fit:cover` chopped heads/shoes → CSS-column masonry, natural
  heights. Verified via DOM (no cover crop, staggered cols). But note: that board is the
  taste-guess one, likely retired in Batch 2 anyway.

Related: [[project_life_os]], [[project_style_feed]], [[project_the_edit_taste_corrections]],
[[reference_shopmy_scraping]], [[reference_instagram_scraping]].
