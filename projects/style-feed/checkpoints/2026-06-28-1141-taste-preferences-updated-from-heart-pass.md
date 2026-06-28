---
date: 2026-06-28
time: 11:41
project: style-feed (personal shopping feed, "The Edit")
status: in-progress
next-session: Preferences updated from the full heart pass. Open follow-up Annabel can pick up: the heart handler does not stamp likes with a timestamp, so "what did I heart this session" can't be isolated (had to analyze the whole liked corpus). Offered to add a per-like timestamp to the heart handler in serve.py / feed.html so future passes can weight only the newest hearts. Other natural moves: (1) act on cooling brands via data/style-overrides.json "hide" if she wants them suppressed outright (not done — too aggressive, the learned model already down-weights); (2) re-run build after next batch of hearts to refresh style-profile.md numbers.
---

# Session: The Edit — taste preferences updated from the heart pass

## What Annabel asked
"I just hearted a lot of stuff. Everything else on the feed I don't like. Update
my preferences according to everything I liked."

## What I found (the system)
Two preference artifacts in style-feed:
- `style-profile.md` — AUTO-generated numbers, regenerated on every build. Header
  note: hand corrections go in `data/style-overrides.json` (boost/hide), do NOT
  hand-edit. It already reflected the current 278 loves / 334 passes, so no
  rebuild was needed.
- `taste-feedback.md` — the hand-curated "words" file that curation reads before
  building anything style-facing. It was stale (last dated 2026-06-22). This is
  the artifact that needed updating.
- `data/feedback.json` = {liked, disliked} dicts keyed by item id, each with
  attributes (brand, creators, cats, sil, form, fab, neck, slv, len, drp, neut,
  om). Most likes have NO ts, and the backup (feedback.bak.json) predates the
  session, so the freshly-hearted batch could not be cleanly isolated.

## What I did
Ran a discriminative analysis: per attribute, liked% minus disliked%, to surface
only where loves genuinely diverge from passes (signal not noise). Then wrote a
dated section to `taste-feedback.md` and refreshed the durable taste memory
(`~/.claude/.../memory/project_the_edit_taste_corrections.md`).

## The signal (loves vs passes, 278 vs 334)
- Fit (loudest): WINS wide-leg, relaxed, straight, fluid drape, full-length.
  LOSES hard a-line (biggest turn-off now), tailored, fitted, full oversized.
- Formality: moved MORE casual. Casual top winner, smart-casual top loser.
- Fabric (summer-weighted): linen, leather, denim up; cotton-basic, knit, wool down.
- Category: hearting bottoms / shoes / bags far more than tops.
- Neutrality 0.84 (loves) vs 0.71 (passes) — more neutral than ever.
- Brands UP: j.crew, dairy boy, leset, dolce vita, lunya, abercrombie, la ligne, agolde.
- Brands COOLING (now pass-leaning): zara (was a top buy), aritzia, reformation,
  anthropologie, madewell, boden.
- Creators UP: Merritt Beck, Revolve, Dairy Boy, Brigette Pheloung, Paige Lorenze, Alix Earle.
  DOWN: Carly Riordan, Grace Atwood, Mary Lawless Lee.

## Files touched
- projects/style-feed/taste-feedback.md — new 2026-06-27 dated section
- ~/.claude/projects/.../memory/project_the_edit_taste_corrections.md — refreshed

## Not done (deliberate)
- No rebuild (style-profile.md numbers already current).
- style-overrides.json left empty (hide/boost is binary suppression, too blunt for
  "cooling" brands; the learned model already down-weights them).
- Per-like timestamp not added (flagged as the open follow-up).
