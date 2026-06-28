---
date: 2026-06-28 11:50
project: style-feed
status: in-progress
type: checkpoint
slug: the-edit-recurate-by-hearts
---

# The Edit re-curated to rank by her hearts (un-reacted = down-ranked)

## The ask
"Re-curate my feed based on what I've hearted. Everything else in The Edit I
haven't reacted to, I don't like." She wants the feed to LOOK LIKE her 278
hearts, not the generic catalogue.

## Root cause
The feed already hydrates her 278♥/334✕ (feedback.json) and live-reranks via
`liveScore` (boot path: `hydrate → applyView → rerank → liveScore`, feed.html).
BUT `liveScore` started from each card's cold `data-base` (~80–100) and her
hearts only nudged it ±. So un-reacted items coasted near the top on base alone
— the opposite of what she wanted.

## Change (one function, source = build_feed.py ~line 1459, NOT the generated file)
Rewrote `liveScore`: compute `d` = fit-to-hearts (brand + category + cut/palette
vision axes + neutrality, same terms as before) and track `pos` = count of
positive matches. Then:
- cold start (`nLiked < 8`): return `base + d` (unchanged fallback so feed isn't empty)
- curated: return `d*3 + base*0.12` — fit dominates, base is a faint tiebreaker
- `pos===0` (un-reacted, zero overlap with her hearts): `d -= 12` → pushed down
Regenerated feed.html via `python3 build_feed.py` (clean, liked=278 disliked=334).

## Verified (node sim of liveScore over items.json + feedback.json, un-reacted only)
- TOP: loose wide-leg/relaxed bottoms in denim/linen/satin full-length, leather
  flats/sandals, structured bags; brands Margaux/AGOLDE/Sézane/La Ligne/Tory Burch.
- BOTTOM: a-line dresses (her #1 turn-off), eyelet/embroidered, Talbots/Lands'
  End/Tuckernuck/Anthropologie. 15 zero-positive items sink.
Matches taste-feedback.md one-line read exactly.

## Run / view
`cd projects/style-feed && python3 serve.py 8801` → http://localhost:8801/feed.html
(images only load through serve.py `/img` proxy). The re-rank is client-side, so
order reflects her saved hearts immediately on load.

## Round 2 — hard FILTER not just rank (she: "no point keeping things I don't like")
She asked to DROP non-matching items, not just rank them low, and (via question)
picked all three tightenings: cut loud prints, cap accessories, demote knee/a-line.
Implemented in build_feed.py emitted JS:
- `passesFit(card)` helper: once curated (>=8 likes), show only items with
  `__fit>0`; closet/inspiration always exempt. shouldShow + tab/chip counts both
  use it so numbers match what's shown. `showDismissed` toggle relabeled
  "show everything (N hidden)" and now reveals disliked + filtered + capped.
- Loud-color cut: `parseFloat(neut) < 0.3` → hidden. Started at 0.4 but that
  killed all bottoms/shoes (her denim/navy/olive sit ~0.3-0.5); 0.3 keeps muted
  tones, cuts true brights/red(0.0-0.2). DID NOT cut missing-neut (isNaN) — that
  wiped whole categories; un-tagged items pass.
- Accessory cap: `ACC_CAP=12` in rerank() marks `__capped` on the lowest-ranked
  un-reacted accessories (they're low-signal and flooded 70/122).
- knee/a-line: extra `d-=8 / d-=10` in liveScore so they fall under the fit>0 gate.
Result: All view ~33 shown / ~615 hidden, neutral, leads with Dairy Boy etc.

## Known gaps (told her, not yet fixed)
- RED still slips through: browser only has `c` (colorfulness), not hue, so a
  red-striped short at neut~0.3 passes. style_engine.py:29 already knows hated
  colors by NAME server-side — the real fix is a hard red/burgundy exclusion in
  build_feed.py (server), not the browser. Offered; awaiting her call. For now her
  ✕ trains it (disliked is hidden + feeds the profile).
- "All" skews to bags/accessories because her good clothing is ALREADY hearted
  (Loved=386); All is the un-reacted remainder + daily refresh. Working as intended.
- build_feed.py vision pass is NON-deterministic per run (re-tags some neut/sil),
  so exact counts wobble between rebuilds. Don't chase counts; tune the rules.

## Notes / watch
- No taste data changed — taste-feedback.md already has the 2026-06-27 derived
  section. This only changed how the feed USES it.
- A few satin/silk skirts at knee/mini ride brand+bottom+neutrality into the top
  despite knee-length being a mild loser. Minor; bottoms-lead / a-line-sink is correct.
- This is the in-browser order only; server `base`/`score` (and morning.html's
  outfit builder) unchanged — that builder is still the older keyword path
  (see [[2026-06-26-1505-morning-edit-shipped-style-next]] NEXT section).

Related: [[project_style_feed]], [[project_the_edit_taste_corrections]],
[[project_life_os]], [[2026-06-27-1745-life-os-the-edit-one-feed-live]].
