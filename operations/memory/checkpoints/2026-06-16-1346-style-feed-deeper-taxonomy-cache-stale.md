---
date: 2026-06-16
time: 13:46
project: style-feed (personal shopping-advice feed, working name "The Edit")
status: Live silhouette/palette rerank SHIPPED & verified (heart → matching cuts/colours rise instantly, no rebuild; proven in headless browser: 5 fitted likes → held-out fitted +58 vs relaxed control +29). She is swiping heavily on the live :8801 feed — feedback.json now 62 liked / 87 disliked (was 50/58 at last rebuild). build_feed.py was then extended (by Annabel / another session) with a DEEPER per-item taxonomy borrowed from "The Yes": vision schema/prompt now also return neckline, sleeve, length, fabric, drape (+ "na" for axes that don't apply to shoes/bags); these are wired into card() dataset (data-neck/slv/len/fab/drp) and into affinity()/vision_adjust scoring. ONE BLOCKER: data/vision_cache.json still holds the OLD 7-key tags (garment,primary_color,neutral,silhouette,formality,oldmoney,pattern) — the 135 cached images have NO new-axis data, and vision_tag() returns the cache as-is, so the deeper taxonomy is currently INERT (all data-neck/slv/len/fab/drp render empty). The richer tags only populate on a re-tag.
next-session: IMMEDIATE = re-tag with the new schema so the deeper axes actually fill in. Either delete data/vision_cache.json or version the cache key, then `python3 build_feed.py` (re-tags all ~147 wearables, ~$2.41, ~3.5 min on claude-opus-4-8; cached after). That same rebuild also folds in the newest swipes (built at 50/58, now 62/87) into the baked centroid + "why" text. Then Cmd+R on :8801. After re-tag, sanity-check that affinity() actually reads the new axes (grep showed refs at lines ~387/457/594) and that "na" values don't distort scoring for bags/shoes. Loop unchanged: read feedback.json → build_feed.py → Cmd+R. Stack: ANTHROPIC_API_KEY in projects/style-feed/.env (gitignored repo .gitignore:25); anthropic 0.109.2; VISION_MODEL=claude-opus-4-8 (swap claude-haiku-4-5 to cut cost ~5x). Her taste @50/58 readout (will shift again at 62/87): selective WITHIN every category; now likes bags (MK/Fendi/Gucci) after passing all at 12 swipes; neutral lean softened (0.93→0.79), oldmoney 0.60→0.50; silhouettes spread fitted/a-line/structured/wide-leg. Later roadmap: source expansion (more creators / pull from retailers so pool isn't capped at 4 ppl's buys — she asked about this), C frictionless feedback, D design pass + real name, add Dairy Boy.
---

# Session: The Edit — live cut/colour rerank shipped; deeper "The Yes" taxonomy added (cache re-tag pending)

## What happened this session

1. **Rebuilt from her big swipe batch** (12/7 → 50/58 → now 62/87 and climbing).
2. **Shipped the live in-browser rerank** so a heart instantly pulls matching
   silhouette + palette up (mirrors server vision_adjust). Verified decisively in
   a headless browser on a throwaway :8899 (her :8801 untouched): clean slate →
   heart 5 fitted → held-out fitted +58 vs relaxed control +29 (= +29 silhouette
   bump). JS passed `node --check`. Console "errors" were only /feedback POST 404
   on the static test server.
3. **Deeper taxonomy added to build_feed.py** (intentional, by Annabel / another
   session): vision now returns neckline/sleeve/length/fabric/drape on top of
   silhouette/formality/neutral/oldmoney/pattern, "na" for non-applicable axes;
   wired into card dataset + affinity. The idea: one swipe teaches many garment
   dimensions, not just cut.

## The blocker to clear first next time

`data/vision_cache.json` is STALE vs the new schema — cached entries only have
the old 7 keys, so the 5 new axes are empty for every already-tagged image and
the richer matching does nothing yet. **Re-tag is required:** delete (or version)
the cache, then rebuild to repopulate all axes (~$2.41, ~3.5 min). Same rebuild
also catches the baked order up from 50/58 to the latest 62/87.

## Verify / gotchas (carried forward)

- localStorage persists per-origin: clear it AND reload so the in-memory `state`
  re-inits empty before any rerank test.
- toggle() reranks on a 300ms slide-out timer — wait before measuring.
- Baked data-score already encodes the centroid, so favored silhouettes start
  high; isolate live deltas with a clean slate + a control silhouette.
- Bags/shoes/accessories (~22 of her likes) give weak silhouette signal ("other");
  the new fabric/drape/length axes may help, but watch "na" not distorting them.

## Next steps

1. Re-tag (clear vision_cache) + rebuild → populate deeper axes + fold in 62/87.
2. Confirm affinity() uses the new axes sensibly; guard "na".
3. Source expansion (more creators / retailers) — she asked; natural next lever.
4. Then C (frictionless feedback), D (design + real name), add Dairy Boy.
