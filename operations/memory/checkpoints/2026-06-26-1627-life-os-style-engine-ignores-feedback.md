---
date: 2026-06-26 16:27
project: life-os
status: in-progress
type: checkpoint
slug: life-os-style-engine-ignores-feedback
---

# The Edit's outfit engine never reads her 612 ♥/✕ — root cause found, fix planned

## The headline finding
Annabel said the outfits feel off and she doesn't know how to teach her taste.
Diagnosis (confirmed in code): she HAS trained the system — `feedback.json` holds
**278 liked + 334 disliked = 612 reactions**, each richly tagged (silhouette,
drape, fabric, neckline, sleeve, length, `neut`, `om`/old-money). But the engine
that builds her outfits, `projects/style-feed/style_engine.py`, **never opens
feedback.json**. It ranks only from ~5 hand-written rules (`taste-feedback.md`) +
`closet.json`. She's been training the influencer FEED while a separate, dumber
path dresses her. `serve.py` saves reactions; `build_feed.py` uses them — only
for the feed, not the outfit engine.

## Three gaps (in priority order)
1. **Closet is starving the engine: only 18 pieces** in `closet.json` (`pieces`
   array). Smart engine on 18 items still can't dress her. Biggest lever.
2. **Vocabulary mismatch.** Closet pieces are tagged only `slot/occ/tones/color/
   owned/img`. Feedback speaks `sil/drp/fab/neck/slv/len/neut/om`. The signal
   can't map onto the closet until the closet is tagged in the same language.
3. **Engine ignores feedback entirely** (the headline).

## Key data insight
Per-attribute marginals OVERLAP heavily between liked and disliked (e.g.
`structured` drape is her most-liked AND most-disliked; `a-line` too). So taste
is **combinatorial** (proportion + pairings), NOT capturable as single-attribute
rules like "boost structured." Liked vs disliked separates only weakly on
averages: neut 0.84 vs 0.71, om 0.76 vs 0.69.

## Reusable asset
`build_feed.py` already runs a **vision tagger** that labeled 1,305 influencer
images (`data/vision_cache.json`) with exactly the rich vocabulary. Her closet
pieces have `img` URLs → point the SAME tagger at the closet to bridge gap #2.
No new tagging code needed.

## Her taste, read off inspiration images (2 batches, ~9 looks)
Owns most; treat as BOTH closet entries and taste target.
- **Everyday / clean-girl:** black+white+cream only, no pattern/color; ONE warm
  tonal accent (taupe knit over shoulders, brown bag, burgundy mary-janes, gold
  watch); long lean columns (black maxi column skirt, white a-line maxi, high-
  waist wide trousers); clean relaxed tops (boat-neck knit, fitted tee, v-neck
  over white tee); flats/loafers/white sneakers.
- **Going out / evening (sharpens current "going-out = sleek satin" one-liner):**
  satin + lace in neutrals (navy cowl-neck halter, white satin cami w/ black lace
  trim, black satin slip midi w/ lace hem); sleek body-skimming top + relaxed
  bottom (dark flared jeans / white wide jeans / baggy low-rise denim / satin
  midi); heels or mules; one structured accessory (woven Bottega clutch, silver
  pendant, chain bag). Black/white/navy.

## Plan (agreed; each step reuses existing code)
1. **(NEXT — in progress)** Wire `feedback.json` into `style_engine.py`: score
   each closet piece by similarity to her liked vs disliked attribute profiles.
   Quick win — improves looks today even on 18 pieces.
2. Tag the whole closet with `build_feed.py`'s vision tagger (bridges vocab gap).
3. Grow the closet (she'll keep dropping photos of what she owns).
4. Then bias toward liked *combinations*, not single tags (the combinatorial part;
   only escalate to a model if scoring isn't enough).

## Open / notes
- **Decision captured:** the pasted inspiration pics are directions she likes AND
  mostly owns → both closet entries and taste target.
- **Limitation surfaced:** Claude can't save chat-pasted images to disk (no file
  path). Engine doesn't need pixels — only the tags, which are captured here. If
  she wants a reference board kept, she drops files into
  `projects/style-feed/data/references/`.
- Nothing committed this session (pure diagnosis + plan). Prior uncommitted Edit
  work from earlier today may still be pending — see
  `2026-06-26-1610-the-edit-live-from-taste-engine.md`.

Related: [[project_life_os]], [[project_style_feed]],
[[project_the_edit_taste_corrections]], [[project_day_planner]].
