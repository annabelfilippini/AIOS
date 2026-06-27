---
date: 2026-06-27 17:45
project: life-os
status: in-progress
type: checkpoint
slug: life-os-the-edit-one-feed-live
---

# The Edit is now ONE feed (closet + Pinterest + influencers + brands), live for review; debrief consolidation next

## Where this sits
Mid-consolidation. Annabel asked to collapse 5 style surfaces into ONE feed ("The
Edit") + ONE morning debrief. Batch 1 (data plumbing) and Batch 2a (feed merge) are
DONE and verified. The feed is LIVE for her review; she's looking now. Batches 2b + 2c
NOT started — paused for her feedback first.

## Live right now (leave running)
`projects/style-feed/serve.py 8801` → http://localhost:8801/feed.html = The Edit.
Serves the `/img` proxy (feed.html images only load through this, NOT as a raw file)
and saves ♥/✕ to `data/feedback.json`. If restarted: `cd projects/style-feed && python3 serve.py 8801`.

## Batch 1 — DONE (consistent ShopMy + real Pinterest + daily cron)
- `refresh_sources.py` (NEW): pulls each influencer ShopMy storefront live via Firecrawl
  v2. Fixes 3 real failure modes — 408 retry/backoff; STRICT placeholder guard
  `re.compile(r"shopmy\.us/shop/product/\d+")` (substring check fails: Firecrawl emits
  fake `shopmy.us/shop/product1` rows); MERGE-by-product-id not replace (storefronts only
  render first ~20-40 pins, so replace would shrink the feed ~90%). Rich bases restored
  from git 7d217d1. 1,383 real pins total. brigette only ever returns placeholders (base
  168 kept); paige+carly intermittently 408 (bases safe).
- `refresh_pinterest.py` (NEW): `gallery-dl -j --cookies-from-browser chrome` on
  https://www.pinterest.com/annabelflip1/clothes/ → `data/pinterest/clothes.json`. Her
  "Clothes" board = exactly 28 pins (verified vs board.pin_count). Merge by pin id.
  NOTE: the old `pinterest-board/` was NEVER her account — it was a taste-GUESS from
  random Pinterest search images. Retire it in 2c.
- `refresh_all.sh` (NEW) runs both. Scheduled via **crontab** `30 6 * * *` (NOT launchd —
  launchd hit TCC exit-78 writing ~/Documents; crontab has FDA here, like the existing
  autosync/wayloft/apartment-hunt jobs). Unverified: gallery-dl cookie access under cron;
  if it fails Pinterest keeps old pins (ShopMy needs no cookies, always works).

## Batch 2a — DONE + VERIFIED (Pinterest + closet INTO the feed)
`build_feed.py` edits (3 spots):
1. After the SOURCES/_ingest loops: `_add_look()` + ingest for Pinterest (cats=["inspiration"],
   source "Pinterest") and closet (`data/closet.json` pieces → SLOT_CAT map + cats=[cat,"closet"],
   source "Closet"). Closet ships its own tags (`sil/len/fab/drp/form/neut/om`) → mapped to the
   vision schema via `_closet_vision()`, so NO vision API call for closet.
2. After the vision pass: reapply `it["_tags"]` (color pass nulls vision for everyone).
3. TAB_DEFS: added ("closet","My Closet",["closet"]) + ("inspiration","Inspiration",["inspiration"]).
Build clean (exit 0): `pinterest=28 closet=17` ingested, 1,129 items, `feedback applied:
liked=278 disliked=334` (her 612 ♥/✕ ARE scoring the feed now). DOM-verified: My Closet
tab 12 cards, Inspiration 26, both with ♥/✕ + correct tags. Some images dropped by the
broken-image filter (12/17 closet, 26/28 pinterest) — normal hotlink blocking.

## Already true (from a prior session, confirmed this session)
`style_engine.py` ALREADY reads feedback.json and uses it in `_score` (line ~224,
`FEEDBACK_SCORE`). The old "engine ignores her 612" headline bug
[[2026-06-26-1627-life-os-style-engine-ignores-feedback]] was fixed before this session.

## NEXT — Batch 2b + 2c (agreed, not started)
- **2b One Morning Debrief:** make `day-planner/morning.html` (live-calendar-driven) the
  single debrief; fold in `style-feed/the-edit.html` card styling. Link it from BOTH The
  Day's "Morning" pill (already `<a href="/morning.html">Morning</a>`, planner.html:326)
  AND from The Edit — SAME link from both. Outfits may use owned AND aspirational pieces
  (her call: no hard closet gate; aspirational = discovery).
- **2c Shell + retire:** `life-os/serve.py` currently composes The Day + `the-edit.html`
  as the "The Edit" tab (serve.py:30 EDIT_HTML, :209 tab) — REPOINT that tab to `feed.html`.
  Beware: serve.py's cross-module banner keys off the-edit.html occasion cards (:154-173) —
  will break / need rework when The Edit becomes the feed. Then retire `lookbook.html`,
  `quickchoose.html`, `the-edit.html` (salvage its card CSS first), `pinterest-board/`.

## Open / watch
- feed.html only renders images through serve.py `/img` proxy — 2c wiring makes the whole
  thing work as one app.
- Annabel reviewing the live feed now; hold 2b for her layout/curation feedback.

Related: [[project_life_os]], [[project_style_feed]], [[project_day_planner]],
[[project_the_edit_taste_corrections]], [[reference_shopmy_scraping]],
[[reference_instagram_scraping]], [[2026-06-27-1700-life-os-shopmy-cron-pinterest-scrape]].
