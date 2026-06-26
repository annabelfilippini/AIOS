---
date: 2026-06-16
time: 13:38
project: style-feed (personal shopping-advice feed, working name "The Edit")
status: Live in-browser rerank is now silhouette/palette-aware (companion to the baked AI-vision scoring shipped earlier today). She swiped a lot this session → feedback.json now 50 liked / 58 disliked (was 12/7). build_feed.py changes: (1) card() emits data-sil/data-form/data-neut/data-om from the vision tags; (2) SCRIPT learn() rebuilt to read the taste centroid off the live DOM cards she's swiped (works for items swiped before tags existed), aggregating silhouette/formality/neutral/oldmoney for both liked & disliked; (3) affinity() extended with the same shape as server vision_adjust (silhouette ±, formality ±, oldmoney ±5, palette-proximity ±5). So a heart now pulls matching CUTS up instantly, no rebuild. VERIFIED in a headless browser on a throwaway :8899 (her :8801 untouched): from a clean slate, hearting 5 fitted pieces raised a held-out fitted item +58 vs a relaxed control +29 → +29 silhouette bump. JS passed node --check.
next-session: Loop unchanged (read feedback.json → python3 build_feed.py → Cmd+R on :8801). Her refreshed taste (50/58): selective WITHIN every category not for/against whole ones (liked 13 tops but passed 12; liked 5 dresses but rejected 13); NEW: she now likes bags (Michael Kors/Fendi/Gucci) after passing all bags at 12 swipes; neutral lean softened (vision neutral 0.93→0.79, oldmoney 0.60→0.50); silhouettes spread fitted/a-line/structured/wide-leg. Caveats to tune: (a) ~22 of 50 likes are bags/shoes/accessories where "silhouette" is weak signal (vision tags them "other"); color+brand carry matching there. (b) brand affinity in affinity() is still uncapped (10*count) — fine for now but can dominate vs the capped vision terms. (c) 12/147 wearables still untaggable (retailer-hosted imgs Anthropic URL-fetch can't load). Remaining roadmap: source expansion (more creators / pull from retailers so pool isn't capped at 4 ppl's buys — she asked about this), C frictionless feedback, D design pass + real name, add Dairy Boy. Stack: ANTHROPIC_API_KEY in projects/style-feed/.env (gitignored repo .gitignore:25); anthropic 0.109.2; VISION_MODEL=claude-opus-4-8 (swap to claude-haiku-4-5 to cut cost ~5x); vision cached in data/vision_cache.json.
---

# Session: The Edit — live silhouette/palette rerank + re-learn from 50/58 swipes

## Ask

Annabel swiped a big batch (12/7 → 50/58) and asked to update her preferences;
then approved wiring the **live in-browser rerank** to be cut/color-aware (the
piece that makes a heart move silhouette-siblings instantly, before a rebuild).
She also clarified the rerank reorders the SAME influencer pool (4 ShopMy
storefronts), not a new source — source expansion is a separate, later lever.

## Done this session (the proof)

1. **Re-learned from 50/58.** Rebuilt; vision centroid recomputed. Top of the
   undecided pile now leads with bags/structured boots/Gucci/Heaven Mayhem and
   pushes down "not your usual" brands + printed/cutout swim.
2. **Live rerank now silhouette/palette-aware:**
   - card() → data-sil/data-form/data-neut/data-om (empty when untagged / garment=false).
   - learn() reads the centroid off the live DOM (not stored info), so pre-tag
     swipes still count; aggregates liked & disliked silhouette/formality/neutral/oldmoney.
   - affinity() mirrors server vision_adjust (silhouette ±14/±12, formality ±8,
     oldmoney ±5, neutral-proximity ±5).
3. **Verified** in a headless browser (temp :8899, her :8801 untouched): clean
   slate → heart 5 fitted → held-out fitted +58 vs relaxed control +29 (= +29
   silhouette bump). node --check passed. Console "errors" were only the /feedback
   POST 404 on the static test server (her real serve.py handles it).

## Gotchas hit (test-harness, not product)

- localStorage persists per-origin: earlier test likes polluted the in-memory
  `state` on reload. Fix = localStorage.clear() THEN reload so state re-inits empty.
- toggle() reranks on a 300ms slide-out timer — must wait before measuring.
- Baked data-score already encodes the 50-like vision centroid, so favored
  silhouettes start high; isolate the live delta with a clean slate + control.

## Next steps

- Source expansion (she asked): more creators, or pull from retailers/brands so
  the pool isn't capped at 4 people's buys — the natural move now the model is good.
- Tune: down-weight "other"-silhouette items (bags) where cut is weak signal;
  consider capping brand affinity; recover 12 untaggable images.
- Then C (frictionless feedback), D (design + real name), add Dairy Boy.
