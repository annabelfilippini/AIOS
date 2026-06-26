---
date: 2026-06-21
time: 14:00
project: style-feed (personal shopping feed, "The Edit")
status: in-progress
next-session: Nuuly is now INTEGRATED into the taste engine and verified. Remaining open items from the direction: (a) email purchase signal via Gmail MCP (Shopbop/retailer order confirmations → strong "owned" likes, same synthetic-like pattern as Nuuly); (b) add an activewear store so Workout grows past ~6; (c) undergarments source + classify() change; (d) OPTIONAL deeper Nuuly: vision-tag the 70 rental + 123 closet images (scene7 hotlinks fine, forced f_jpg) and fold their silhouette/formality/oldmoney into the vision centroid (Lcounts/Lneu/Lom) — currently Nuuly only feeds BRAND/CATEGORY/COLOUR, not vision. That's the richest unused signal. Also consider surfacing the "You wear X on Nuuly" reason as why[0] (currently appended, so it never shows as the primary card reason).
---

# Session: The Edit — Nuuly folded into the taste engine

## DECISION captured from Annabel
Worn Nuuly rental counts **~1.75x a normal like**; closet save = **a normal like**.
(She'd parked this question last session; answered it this session.)

## What changed (build_feed.py only — quickchoose.html / feed.html untouched)
Nuuly history is now a taste signal, NOT new feed cards (rentals aren't shoppable
here) and NOT exported to feedback.json (derived, not swipes). All edits live in
`projects/style-feed/build_feed.py`.

1. **Synthetic likes from data/nuuly.json.** Build `nuuly_likes` dict keyed
   `nuuly:<id>`: 70 rentals (weight 1.75, ts = real rental `date` so recency
   applies) + closet saves (weight 1.0, ts = baseline 2026-06-17, no date in
   data). Closet items whose id already appears as a rental are deduped (keep the
   stronger rental vote) → **70 rental + 77 closet = 135 synthetic likes** (46
   closet overlapped rentals). cats derived via existing `classify(brand, name)`
   (Nuuly `class` is null on ~all items, so name-based).
2. **Weight multiplier** added to `_signals` and `_vision_signals`:
   `w = recency_w(rec) * float(rec.get("weight", 1.0) or 1.0)`. Backward-compatible
   (real swipes have no weight → 1.0).
3. **`liked` stays PURE** (real swipes, still **292**). A separate
   `taste_liked = {**nuuly_likes, **liked}` drives `_signals` →
   `feedback_adjust` (the server `score`). Pins ("You loved this") and the
   profile love-count still use pure `liked`. Nuuly ids never collide with
   scraped `brandtitle` ids, so no false pins.
4. **THE KEY FIX — Nuuly baked into `base`.** Both browser views (quick-choose +
   feed) re-rank LIVE from each item's `base` + a profile they recompute from
   localStorage swipes. Nuuly isn't a swipe, so it would NEVER reach the ranking
   Annabel sees unless it's in `base`. Added `nuuly_adjust(it)` (positive-only
   brand cap +11 / category cap +8 / colour +4, drawn from `nuuly_likes` ALONE so
   real-swipe feedback stays out of base) folded into the cold-score loop. Nuuly
   is a STATIC prior; her swipes still layer on top and can flip it.
5. **style-profile.md** gained a "## From Nuuly (worn rentals + closet)" section
   listing top rented/closet brands with weights.

## Verified
- Isolated weighting test on real data: liked stays 292; 135 synthetic likes;
  Anthropologie (11.0) + Free People (10.9) surface as top taste brands; 51
  brands new to the signal via Nuuly.
- **base before/after diff (vision cached, no API spend):**
  Free People 63.7→74.7 (+11 brand cap), Reformation 71.1→88.0 (+16.9),
  Madewell 70.4→86.1, Leset 73.1→81.1, J.Crew 71.3→76.2 (category prior).
  Restore-rebuild returns identical "with" values → committed artifacts reflect
  Nuuly.
- Full build clean: vision ON reading cache (1006/1007 tagged, no spend),
  feedback applied liked=292 disliked=284, items.json + style-profile.md
  regenerated.

## Notes for next time
- Run `python3 build_feed.py` from projects/style-feed (reads .env key; vision is
  cached so no real spend unless the daily scraper added new items). Use
  `STYLE_FEED_NO_VISION=1` ONLY for quick logic checks — it corrupts base/ranking
  (cached vision tags only apply when the vision path runs), do not ship that.
- nuuly.json is gitignored; refresh via `tools/nuuly-cli/nuuly-cli pull --out
  projects/style-feed/data/nuuly.json`.
- Three scorers stay in sync (quickchoose liveScore JS, build_feed feedback_adjust,
  build_feed SCRIPT liveScore JS) — but Nuuly only needed the `base` path since
  both browsers rank on base. The `taste_liked`→feedback_adjust change keeps the
  server `score` consistent but is secondary.
