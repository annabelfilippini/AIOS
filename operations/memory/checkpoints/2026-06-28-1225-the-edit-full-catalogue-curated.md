---
date: 2026-06-28 12:25
project: style-feed
status: in-progress
type: checkpoint
slug: the-edit-full-catalogue-curated
---

# The Edit — full catalogue now hearted/✕'d (843 reactions), heart-fit feed live

## What happened this session
Two-part build on The Edit feed (projects/style-feed/feed.html, served by serve.py
on 8801), then Annabel swiped the rest of the feed.

1. **Re-curate by hearts** — `liveScore` in build_feed.py was riding each card's
   generous cold `data-base` (~80-100); hearts only nudged. Rewrote so fit-to-hearts
   dominates (`d*3 + base*0.12`) and un-reacted/no-overlap items sink.
2. **Hard filter, not just rank** (her: "no point keeping things I don't like") —
   added `passesFit()`: once curated, show only `__fit>0`; closet/inspiration exempt.
   Plus loud-color cut (`neut<0.3`), accessory cap (`ACC_CAP=12`), knee/a-line demote
   (`d-=8 / d-=10`). "Show everything (N hidden)" toggle reveals the cut pile.
   Details in [[2026-06-28-1150-the-edit-recurate-by-hearts]].
3. **She swiped the remaining feed.** Reactions went **612 → 843**
   (liked 278→399, disliked 334→444). The catalogue is now almost fully curated.

## Refreshed taste read (from 843 reactions — sharper than the 612 read)
- **Silhouette:** wide-leg 67% wins; **tailored 0% (0♥/19✕) = total reject**;
  oversized/cropped down. relaxed/straight neutral-to-positive.
- **Fabric:** denim 59 / linen 56 / leather 56 win; knit, wool, silk all lose.
- **Length:** full-length 62% clear winner; knee 30% and midi 36% lose.
- **Category:** loungewear up (85%), bags ~even; knit (27%), outerwear (17%),
  dress-tops lose. Inspiration + closet 100% (her own, as expected).
- Confirms + hardens the 2026-06-27 read in taste-feedback.md. No edit needed there
  yet, but "tailored = hard no" is new and worth folding in if curating again.

## State / how to run
- `cd projects/style-feed && python3 serve.py 8801` → /feed.html. Feed re-ranks
  client-side from her saved hearts (hydrated from data/feedback.json) on load.
- feedback.json: liked=399 disliked=444 (saved 12:24). NOT yet rebuilt into the
  server `base` — live feed already reflects it via liveScore; a `python3 build_feed.py`
  would refold it into base (optional; vision pass is non-deterministic so counts wobble).

## Open / next
- **RED still slips through** (e.g. a red striped short): browser only has
  colorfulness `c`, not hue. Real fix = hard red/burgundy ban in build_feed.py
  server side (style_engine.py:29 already knows hated colors by name). Offered;
  she hasn't said go yet.
- Optional: fold "tailored = hard no" + the 843-reaction read into taste-feedback.md.
- Optional: rebuild to refold reactions into base for the cold-start order.

Related: [[2026-06-28-1150-the-edit-recurate-by-hearts]], [[project_style_feed]],
[[project_the_edit_taste_corrections]], [[project_life_os]],
[[2026-06-27-1745-life-os-the-edit-one-feed-live]].
