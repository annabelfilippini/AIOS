---
date: 2026-06-26 15:30
project: day-planner
status: in-progress
type: checkpoint
slug: per-event-taste-engine-morning-edit
---

# Per-event taste engine built; Morning Edit now renders from it

## Where we landed
The Morning Edit's outfits are no longer regex keyword-matching with canned
fallbacks. There is now a real taste engine: any calendar event -> occasion ->
her hand-given per-occasion formula -> best-ranked piece she actually owns per
slot. Verified end to end against her live calendar: 3 distinct, on-taste looks
(Alex bday -> going-out satin halter; Vail -> vacation; Yoga -> active),
non-dress events (money due, driving, errands) correctly produce no card.

## What changed this session (NOT yet committed)
- **NEW `projects/style-feed/data/closet.json`** — her wardrobe as data. Seeded
  from `purchases.json` (owned, with images) + current Nuuly box + 2 flagged
  `owned:false` guess staples (AGOLDE jean, Aritzia Effortless black trouser).
  Each piece tagged `slot` (top/bottom/shoe/layer/bag), `occ`, `tones`. This is
  the persistence the prior checkpoint flagged as missing.
- **NEW `projects/style-feed/style_engine.py`** — pure, no deps.
  `occasion_of(title)` (returns None for non-dress events), `FORMULAS` (the 5
  lanes from taste-feedback.md as slot templates + copy), `build_look(event)`,
  `build_week(events)` (one look per occasion lane/day). Ranking: owned +2,
  occasion-fit +3, formula-preferred tone +4, loved tones bonus, has-image
  bonus; hard-excludes red/burgundy/cardigan. `demo()`/`__main__` self-check.
  Run: `python3 style_engine.py`.
- **`projects/day-planner/serve.py`** — new `GET /api/looks` endpoint: reuses
  the live `_calendar` pull, lazy-imports style_engine from ../style-feed,
  returns `{looks:[...], live}`. Falls back to one everyday look if nothing
  outfit-driving today.
- **`projects/day-planner/morning.html`** — deleted the whole client-side
  builder (buildPieces/outfitCopy/chooseBy/banned/etc). Now fetches `/api/looks`
  and renders via thin `pieceHTML`/`cardHTML`/`renderLooks`. Dropped the
  `/api/style` fetch. Intro copy rewritten to count looks.

## How it runs / verifies
- `cd projects/day-planner && python3 serve.py 8802` (or any port).
- Engine self-check: `cd projects/style-feed && python3 style_engine.py`.
- Endpoint: `GET /api/looks?start=YYYY-MM-DD&end=YYYY-MM-DD` (gated; ?k= or cookie).
- Verified this session: self-check green; live endpoint over real Jun 26
  calendar returned 3 deduped on-taste looks, junk events excluded; render
  functions run against the real JSON produce 3 clean cards, no undefined,
  corrections on card 1 only.

## NEXT
- **Visual confirm**: open `morning.html?k=<key>` in the browser (only the final
  pixel check is unverified; data + render logic are verified). Annabel holds key.
- **the-edit.html still hardcoded** to the Jun 25-28 four. Point it at
  `/api/looks` too (she chose Morning Edit first this session). That unpins the
  canonical Edit. Engine + endpoint already support it.
- **Refinements**: (1) active lane should prefer the matching Butter set
  (cami + short) over a generic white tee — add a "matching set" bonus. (2)
  going-out/work trousers are `owned:false` guesses; confirm real trousers into
  closet.json to flip confidence to fully owned. (3) layer slot only appears in
  some lanes; fine.
- Commit when Annabel approves (4 files: closet.json, style_engine.py, serve.py,
  morning.html).

Related: [[project_day_planner]], [[project_life_os]],
[[project_the_edit_taste_corrections]]. Supersedes the "make outfits use real
taste" NEXT from 2026-06-26-1505-morning-edit-shipped-style-next.
