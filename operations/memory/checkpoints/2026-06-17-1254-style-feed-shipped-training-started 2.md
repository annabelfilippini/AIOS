---
date: 2026-06-17
time: 12:54
project: style-feed (personal shopping feed, "The Edit")
status: Roster + brand-catalog expansion SHIPPED and verified on screen; Annabel has started training it. Stopping here by her call; resume with items 2-4 below next time.
next-session: Do items 2-4 (her pick), and rebuild to bake her new feedback. (1) BETTER REVOLVE — current pull surfaced only 3 (catalog was party/going-out heavy); re-pull a quiet Revolve collection (linen / specific old-money labels) into data/brands/revolve.json. (2) ROUND-2 BRANDS — Aritzia (images 403, needs rehost/proxy), Lululemon (image from product detail page), Abercrombie (Firecrawl proxy:"stealth"), Anthropologie (needs one probe). (3) TUNE BRAND BAR — BRAND_MIN_SCORE (56) / BRAND_KEEP (24) in build_feed.py. Then rebuild with STYLE_FEED_VISION_MODEL=claude-haiku-4-5 (caches warm → fast; key valid).
---

# Session: The Edit — creators + brands shipped, Annabel started swiping

Full build details in the prior checkpoint
[[2026-06-17-1229-style-feed-creators-brands-shipped]]. Delta since then:

## Shipped & verified
- Feed rebuilt: **958 items**, 7 creators + 3 brands, vision-tagged on Haiku
  (1042/1043). Brand cut: **Dairy Boy 24 (capped), Zara 16, Revolve 3** (205
  dropped by the taste filter).
- Screenshotted the live feed (preview server `style-feed-shot` on :8813, added
  to `.claude/launch.json`). Top of feed reads correctly on-taste: wide-leg
  denim, neutral trousers, riding boots, beige knits; "why" lines + co-signs
  render (e.g. "Co-signed by Carly Riordan + Merritt Beck", "You like COACH").

## Training started (important for next rebuild)
- Annabel swiped in the live feed. `data/feedback.json` now **124 loved / 71
  passed** (was 59/40 at the 12:25 build). This richer feedback is SAVED but NOT
  yet baked — the displayed feed was built with the old 59/40. **Next rebuild
  will incorporate it**, so rebuild early next session.
- She views/trains at `localhost:8801/feed.html` (serve.py POSTs hearts to
  data/feedback.json); copy also at `~/Desktop/the-edit-feed.html`.

## Still parked
- agency-audit-network delete HELD (nests dad-pilot / Tom's pilot). freeyourmind
  already trashed. `rm` blocked this session → use `mv` to `~/.Trash`.
