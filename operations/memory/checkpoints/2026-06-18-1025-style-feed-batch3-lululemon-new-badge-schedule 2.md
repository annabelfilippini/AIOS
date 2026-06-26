---
date: 2026-06-18
time: 10:25
project: style-feed (personal shopping feed, "The Edit")
status: in-progress
next-session: Batch 3 is DONE+verified (Lululemon store, NEW badge, daily 6am scrape). Optional next: full Aritzia pull (no --limit) for more old-money pieces; add more stores to the STORES registry; revisit a dedicated "New" view only if the badge alone proves insufficient.
---

# Session: The Edit — Batch 3 (Lululemon + NEW badge + daily scrape)

## What we worked on
Finished the "unattended new-arrivals" loop: added Lululemon as a second
scraped store, shipped the NEW badge UI, and scheduled the daily 6am scrape.
All three verified.

## Decisions made
- **Lululemon is NOT Cloudflare-gated.** Plain `urllib` gets 200 image/jpeg from
  `images.lululemon.com` — so NO `/img` proxy and NO PROXY_HOSTS change (unlike
  Aritzia). Don't assume new stores mirror Aritzia; probe first.
- **Lululemon images are deterministic Scene7 URLs**
  (`images.lululemon.com/is/image/lululemon/<colorCode>`), and the grid extraction
  returns them reliably → `image_from="listing"` (not product_page). Bare URL is
  low-res, so `img_suffix="?wid=1080&fmt=jpg"`. `sku_re=r"/([^/?]+)\?color="`
  (handles both `/_/prod11020158?color=` and slug `/utlsgbq5yu?color=`).
  Listing URL: `shop.lululemon.com/c/women-whats-new/n1zg2xznskl`.
- **NEW badge = render-only.** `first_seen` was already stamped by the scraper and
  already flowed through `_ingest()` via `{**p}`, so no data plumbing. Added
  `NEW_DAYS=7`, `_is_new(it)`, a `.badge-new` span in `.imgwrap`, and CSS (accent
  pill, top-left). Legacy items (no `first_seen`) never badge. **Annabel chose
  badge-only, no separate "New" view.**
- **Daily routine scheduled** via the schedule MCP: task `the-edit-daily-scrape`,
  cron `0 6 * * *`, runs `cd projects/style-feed && python3 scrape_stores.py --rebuild`.

## Two scraper bugs found + fixed (both generic, help any store)
1. **scrape_listing now retries on EMPTY**, not just on exception. Lululemon
   intermittently serves a 400 block page with 0 tiles; an identical retry
   succeeds. Proven: same call returned 0 then 8 products.
2. **LISTING_SCHEMA/PROMPT were missing `imageUrl`** (Aritzia uses PDP images, so
   it was never added). Listing-mode stores got no image → every tile silently
   dropped (8 tiles, 0 stored) until added. The listing branch in `run_store` now
   applies `img_suffix` and validates the final URL via `_img_ok`.

## Verification
- `python3 scrape_stores.py lululemon --limit 8 --rebuild`: 8 tiles → 8 stored,
  5 kept after the old-money taste filter (athletic items dropped, like Aritzia).
- serve.py (port 8801): feed.html 200; Lululemon image direct 200 image/jpeg;
  Aritzia via `/img` 200 image/avif.
- Browser (Playwright): 11 NEW badges (5 Lululemon + 6 Aritzia), Lululemon card
  img naturalWidth=1080, badge text "New". Console errors are benign/unrelated
  (favicon 404, transient ERR_NETWORK_CHANGED on ShopMy).

## Files touched
- `projects/style-feed/scrape_stores.py`: lululemon in STORES; imageUrl in
  LISTING_SCHEMA + prompt; scrape_listing empty-retry; listing branch img_suffix +
  validation.
- `projects/style-feed/build_feed.py`: `import datetime`; `NEW_DAYS`; Lululemon in
  BRANDS; `_is_new()`; badge span in card(); `.badge-new` CSS.
- `projects/style-feed/data/brands/lululemon.json` (+ img_cache) NEW.
- Scheduled task: `~/.claude/scheduled-tasks/the-edit-daily-scrape/SKILL.md`.

## Context to preserve
- serve.py was left running on 8801 (`--no-open`) for review; `feed.html` rebuilt.
- Playwright MCP screenshots save to a sandboxed output dir not reachable from the
  shell — verify renders programmatically (naturalWidth, DOM) instead.
- Run scraper: `python3 scrape_stores.py [store] [--limit N] [--rebuild]`.
