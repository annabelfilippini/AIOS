---
date: 2026-06-26 16:10
project: life-os
status: in-progress
type: checkpoint
slug: the-edit-live-from-taste-engine
---

# The Edit is now live from the taste engine (both surfaces dynamic)

## Where we landed
Both style surfaces now render from one taste engine instead of hardcoded HTML /
regex. `morning.html` (Morning Edit, today) and `the-edit.html` (canonical
weekly Edit) both fetch `/api/looks` and render looks built from her real closet
+ calendar. The frozen Jun 25-28 hand-authored Edit is gone; the page now reads
the actual week. Verified end to end against the live calendar.

## The engine (built earlier this session)
- `projects/style-feed/data/closet.json` — her wardrobe as data (owned from
  purchases.json + Nuuly box + 2 `owned:false` guess staples), tagged
  slot/occ/tones.
- `projects/style-feed/style_engine.py` — `occasion_of` (None for non-dress
  events), `FORMULAS` (5 lanes from taste-feedback.md), `build_look`,
  `build_week`. Ranking: owned +2, occasion-fit +3, formula tone +4, loved-tone
  bonus, has-image bonus; hard-excludes red/burgundy/cardigan. `demo()`
  self-check passes (`python3 style_engine.py`).

## What changed THIS session (the-edit wiring) — NOT committed
- **`style_engine.py` `build_week`** now groups events by occasion lane and
  attaches `events` (deduped list of that lane's titles) to each look — one
  polished look per occasion type, not per event. Removed the short-lived
  `build_events`/`per=event` path (dead once we chose lane grouping).
- **`serve.py` `/api/looks`** simplified back to always `build_week` (no `per`
  param).
- **`the-edit.html` fully rewritten** — kept the Cormorant/cream `<style>` and
  chrome verbatim; replaced the 4 hardcoded cards with a `<script>` that fetches
  `/api/looks` for the current Mon–Sun week and renders cards. Cards head by
  LANE (Going out / Travel / Movement / Everyday / Work), list the week's events
  in `.when`, keep `data-occ` so The Day's hanger->look bridge still matches.
  Dynamic dateline. Refetch on `visibilitychange`. Script-in-body works in both
  the standalone page (day-planner serves it) and the life-os SPA (its
  `_extract` pulls body incl. script into one document).

## How it runs / verifies
- `cd projects/day-planner && python3 serve.py 8802` (currently running, pid ~9951).
- Engine: `cd projects/style-feed && python3 style_engine.py`.
- Morning Edit: `http://localhost:8802/morning.html?k=<key>` (today, per-lane).
- The Edit: `http://localhost:8802/the-edit.html?k=<key>` (this week, per-lane).
- Verified this week (Jun 22–28): 5 cards — Movement (Yoga/Bike/Strength/+1),
  Everyday (4 events), Travel (Airport/Vail), Going out (Alex bday/Shpiz lobster
  dinner), Work (AA meeting). Render-checked via node: 5 cards, no undefined,
  data-occ tokens present, mostly "Yours" tags.
- Server gotcha: multiple `serve.py 8802` instances accumulated mid-session;
  `pkill -9 -f "serve.py 8802"` then start ONE, wait ~5s before curling, or a
  stale instance returns the gate page (looks like empty JSON).

## NEXT
- **Annabel to visually confirm** both pages (hard-reload, Cmd+Shift+R; pages cache).
- **Two open issues she flagged**: (1) "AA meeting" -> Work is a mismatch (regex
  matched "meeting"); decide whether to add calendar words that should never be
  styled, or a skip list. (2) One look per lane means Airport and Vail share the
  Travel look; per-event distinct looks need the engine to VARY picks (rotate
  ranked alternates) — real upgrade.
- **life-os SPA** (`projects/life-os/serve.py`, port 8800) not re-tested this
  session; the-edit script-in-body should render there too — verify the hanger
  bridge + banner still work against the now-dynamic cards.
- **Commit** when approved (5 files: closet.json, style_engine.py,
  day-planner/serve.py, morning.html, the-edit.html).
- Refinement: active lane should prefer the matching Butter set (cami+short)
  over a generic white tee.

Related: [[project_day_planner]], [[project_life_os]],
[[project_the_edit_taste_corrections]]. Supersedes
2026-06-26-1530-per-event-taste-engine-morning-edit.
