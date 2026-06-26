---
date: 2026-06-21
time: 15:00
project: style-feed (personal shopping feed, "The Edit")
status: in-progress
next-session: Nuuly is now FULLY integrated (brand/category/colour + VISION) and Annabel reviewed it live — she likes it. ANNABEL WANTS MORE NUULY INFLUENCE (deferred, not done this session): she felt the Nuuly tilt could be stronger. Knobs to turn next time, cheapest first: (1) NUULY_VIS_SCALE/NUULY_VIS_CAP (currently 0.65/20) — raise toward ~0.8/24; (2) NUULY_RENTAL_WEIGHT (1.75) and/or closet weight (1.0) — bump rental toward 2.0+ and consider closet 1.25; (3) nuuly_adjust brand/cat caps (currently +11/+8). Re-run the base before/after archetype probe (relaxed+knit vs bodycon+satin) after any change to confirm it still DISCRIMINATES (watch for re-saturation at the cap). Other remaining direction items: (a) email purchase signal via Gmail MCP (Shopbop/Aritzia/Reformation order confirmations → strongest "owned" likes, reuse the synthetic-like + base-prior pattern from Nuuly); (b) activewear store so Workout grows past ~6; (c) undergarments source + classify() change; (d) decide whether to surface "You wear X on Nuuly" as the primary card reason (currently appended to why[], so vision/swipe reasons win why[0]). The Nuuly + base-prior architecture is the template for the email signal.
---

# Session: The Edit — Nuuly VISION folded into the taste engine

## What changed (build_feed.py only)
Extends the 14:00 Nuuly integration (brand/category/colour) to the VISION centroid
— the richest signal (silhouette, formality, fabric, neckline, sleeve, length,
drape, back, palette). All edits in `projects/style-feed/build_feed.py`.

1. **Vision-tagged the Nuuly pool.** Nuuly items aren't in the scraped feed, so
   they get their OWN `nuuly_pool` (id + img). After the main vision pass, the
   147 Nuuly images (70 rental + 77 closet) are run through the existing cached
   `vision_tag` (scene7 hotlinks + forced jpeg → fetch by URL). One-time ~2.5min
   API cost; now fully cached (147/147) so rebuilds are instant.
2. **Merged into the LIKED centroid for score + profile.** `Lcounts/Lneu/Lom` now
   come from ONE combined call: `_vision_signals({**liked, **nuuly_likes}, items +
   nuuly_pool)`, weighted by each record's weight (rental 1.75x / closet 1.0x /
   swipe 1.0x). So the server `score` (via vision_adjust) AND style-profile.md
   silhouettes/fabrics reflect her real Nuuly vision taste. Visible shift: relaxed
   silhouette 66.8→89.3, knit/cashmere fabrics up, oldmoney 0.76→0.70 (rentals
   are a touch more trend-forward than her curated swipes).
3. **THE KEY FIX again — Nuuly vision prior baked into `base`.** Both browsers
   re-rank live from `base`; the swipe-vision they recompute from localStorage
   can't see Nuuly. So a separate Nuuly-only centroid (`Ncounts/Nneu/Nom`) drives
   `nuuly_vision_adjust(it)`, folded into base alongside the brand/cat prior.
4. **Discrimination fix (important).** First cut used vision_adjust's capped reward
   `min(lc, lpc*nk)` — with a dense 147-item centroid it SATURATED: 83% of items
   hit the +18 cap → a near-flat boost that doesn't re-rank. Rewrote as
   PROPORTIONAL: `adj += lc * (Ncounts[f][val] / axis_total)` — rewards how
   TYPICAL an item is of her Nuuly taste, not "shares any common value". Tuned to
   SCALE=0.65, CAP=20 → only 10% at cap, mean ~11.5, real spread.

## Verified
- 147/147 Nuuly images tagged; build clean; liked stays PURE 292 / disliked 284.
- Prior DIRECTION correct: TOP = relaxed/knit, cotton tanks, cashmere (her taste);
  LOW = bodycon/satin/sequin dresses, silk earrings (off-taste).
- base before/after (full brand+cat+vision vs no nuuly): relaxed+knit (her Nuuly
  mode) 59.5→83.2 (+23.7); bodycon+satin (off-taste) 55.6→68.0 (+12.4). The
  on-taste vs off-taste GAP widened ~4pt → ~15pt = real re-ranking, not a flat
  lift. Restore-rebuild returns identical → committed artifacts reflect Nuuly.

## Key facts for next time
- Nuuly now feeds ALL three signal layers: brand/category/colour (taste_liked →
  feedback_adjust → score; nuuly_adjust → base) AND vision (merged Lcounts →
  score; nuuly_vision_adjust → base). base is the one that reaches what she sees.
- Saturation is the trap when folding a dense external signal into a capped
  scorer — use PROPORTION-of-centroid, not raw capped reward, so it discriminates.
- Refresh Nuuly: `tools/nuuly-cli/nuuly-cli pull --out
  projects/style-feed/data/nuuly.json`, then `python3 build_feed.py` (vision
  cached; new Nuuly items would re-tag, ~1 call each).
