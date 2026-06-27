# In progress — The Edit consolidation (Batch 2)

Session 2026-06-27 ~17:30. Building the one-feed + one-debrief consolidation.

## Done
- Batch 1: ShopMy refresh (refresh_sources.py, merge-safe, 1383 pins) + Pinterest
  scrape (refresh_pinterest.py, 28 pins) + daily cron (crontab 30 6 * * *, refresh_all.sh).
- Batch 2a (THIS): build_feed.py now ingests Pinterest ("Inspiration" tab) + closet
  ("My Closet" tab) into The Edit feed (feed.html). Closet reuses its own tags (no
  vision call); Pinterest vision-tagged in the normal pass. Both ♥/✕ -> feedback.json.

## Next (Batch 2b/2c — NOT started)
- 2b: one Morning Debrief = make day-planner/morning.html canonical (calendar-driven),
  fold in the-edit.html card styling. Link from BOTH The Day's "Morning" pill AND The Edit
  (same link). 
- 2c: life-os/serve.py — repoint "The Edit" tab to feed.html (currently the-edit.html).
  Retire lookbook.html, quickchoose.html, the-edit.html, pinterest-board/.

Full detail: 2026-06-27-1700-life-os-shopmy-cron-pinterest-scrape.md
