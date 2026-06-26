---
date: 2026-06-16
time: 12:34
project: style-feed (personal shopping-advice feed, working name "The Edit")
status: Roadmap step B SHIPPED & verified. AI-vision silhouette/colour scoring replaces the saturation heuristic for wearables. build_feed.py now makes one Claude vision call per wearable image (claude-opus-4-8, output_config json_schema → {garment, primary_color, neutral 0-1, silhouette, formality, oldmoney 0-1, pattern}), cached to data/vision_cache.json (one-time ~$2.41 for 147 imgs, then instant). New vision_adjust() scores each item against the CENTROID of her liked tags (silhouette/formality/pattern match + oldmoney + palette proximity), penalises disliked. Beauty/home + 12 untagged wearables fall back to old color_adjust saturation. Keyless rebuild still works (vision OFF → saturation). VERIFIED: tagged 135/147; her liked centroid = silhouettes flowy/fitted/wide-leg, oldmoney≈0.60, neutral≈0.93; undecided pile now ranks by real visual reasons ("wide leg cut, like your saved pieces", "a line cut"), not just brand.
next-session: She is swiping live; loop unchanged (read data/feedback.json → python3 build_feed.py → Cmd+R on her :8801). Now that vision tags exist, the next lever is making the LIVE in-browser rerank silhouette-aware too — currently feed.html SCRIPT only re-ranks on brand/category/colour (data-c); the baked server score already uses vision but a fresh heart doesn't move silhouette-siblings until a rebuild. Add data-sil/data-form/data-neut/data-om to each card + extend learn()/affinity() in build_feed.py's SCRIPT. Other tuning: (a) "fitted" silhouette over-dominates the undecided ranking (common tag + 2 fitted likes) — consider down-weighting common silhouettes or normalising by base rate; (b) 12 wearables Anthropic's URL-fetcher couldn't tag (retailer-hosted imgs) — same hotlink class as the broken-image set; (c) a few non-garments still classify as wearable (Earth Therapeutics body tool) — garment=false guard catches scoring but not the tab. Then roadmap C (frictionless feedback), D (design pass + real name), add Dairy Boy. Stack: ANTHROPIC_API_KEY in projects/style-feed/.env (gitignored via repo .gitignore:25); anthropic 0.109.2 installed --user. Model swappable to claude-haiku-4-5 (VISION_MODEL const) to cut cost ~5x.
---

# Session: The Edit — AI-vision silhouette/colour scoring (roadmap B)

## Ask

Annabel: rebuild from current swipes, then do B (the AI-vision scoring — "the real
magic" flagged in the prior checkpoint). She chose the **Anthropic API** path (auto,
scales to new creators) over me tagging in-session, and supplied an API key.

## Done this session (the proof)

1. **Rebuilt** from current feedback (12 liked / 7 disliked) — no new swipes since the
   last checkpoint, but confirmed the loop bakes feedback in (her 12 likes pinned at 100).
2. **Wired AI-vision into build_feed.py** (loaded the claude-api skill for the exact
   vision + structured-output shape):
   - `.env` loader + `VISION_ON` gate (key present and not STYLE_FEED_NO_VISION=1).
   - `vision_tag(url)`: one `messages.create` per image, `output_config.format` json_schema,
     image via `{"type":"image","source":{"type":"url",...}}` so Anthropic fetches it.
     Cached to `data/vision_cache.json`. Threaded (4 workers). Returns None on failure.
   - Schema: garment(bool), primary_color, neutral(0-1), silhouette(enum of 12),
     formality(enum of 5), oldmoney(0-1), pattern(enum of 8).
   - `_vision_signals()` builds liked & disliked centroids; `vision_adjust()` scores
     silhouette/formality/pattern match (+oldmoney ±5, +palette-proximity ±5), with a
     human "why" ("wide leg cut, like your saved pieces").
   - Restructured the pipeline: colour pass (still the image-load/broken check) → drop
     broken → vision pass on wearables only → centroids → score (vision for tagged,
     saturation fallback otherwise) → feedback adjust → sort.
3. **Validated stack the careful way**: key prefix sk-ant-api03- + len 108 (not just a
   grep); `.env` confirmed gitignored; 1-image smoke test before the 147 run (cost
   $0.0164/img → ~$2.41 total, shown to her).

## Verify / gotchas

- `vision: ON  tagged=135/147`. Keyless run prints `vision: OFF (saturation fallback)`
  and produces identical output to before — no regression.
- Liked centroid surfaced: silhouettes flowy/fitted/wide-leg; oldmoney≈0.60; neutral≈0.93.
- Top of feed is still her 12 pinned likes (score 100). The vision reshuffle is visible
  in the **undecided pile** (the All feed) — verified via parsing feed.html for non-swiped
  wearables; top items now carry silhouette/palette reasons.
- Did NOT spin a server on her :8801 (she opens via ~/Desktop/Open The Edit.command).
  She just needs Cmd+R to see it live; offered a side-by-side screenshot on another port.

## Next steps

- Make the **live in-browser rerank** silhouette-aware (add vision fields to card dataset
  + extend learn()/affinity() in SCRIPT) so a fresh heart moves silhouette-siblings
  without a rebuild — the biggest remaining gap now that tags exist.
- Tune: down-weight over-common silhouettes ("fitted"); recover 12 URL-untaggable imgs;
  tighten the wearable/non-garment classifier.
- Then C (frictionless feedback), D (design + real name), add Dairy Boy.
