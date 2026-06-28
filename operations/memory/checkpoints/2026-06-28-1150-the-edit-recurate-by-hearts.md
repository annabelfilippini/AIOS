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
