---
date: 2026-06-18
time: 11:01
project: wayloft
status: in-progress
next-session: Build Batch 4 (Mobile) in projects/wayloft/design/screens.html — mobile views of the key screens (Today, Earn, Burn deals, Burn trip check) + final polish. Then re-center apps/web into Editorial Cream squared (full re-center steps + locked tokens are in the 2026-06-17-1300 checkpoint). Read ~/.claude/design.md before designing. LIVE PREVIEW: a persistent threaded no-cache server is running for Annabel at http://localhost:8809/screens.html (script: projects/wayloft/design/serve_nocache.py). Relaunch with `python3 serve_nocache.py 8809` (run_in_background) if her Mac slept/restarted.
supersedes: 2026-06-18-1057-wayloft-batch3-burn.md
---

# Session: Wayloft Batch 3 (Burn) shipped + Earn wallet-coach polish + live preview server

Continues from Batch 2 (2026-06-17-1515). Lane is Editorial Cream squared
(Direction A); locked tokens in the 2026-06-17-1300 checkpoint.

## What shipped this session

**Batch 3 · Burn** — three screens added to `projects/wayloft/design/screens.html`
(06 first-run empty, 07 deals feed, 08 trip check). Built + verified, Desktop
copy refreshed, Batch 3 ticked in `in-progress.md`. Full detail in the superseded
2026-06-18-1057 checkpoint. Key decision: trip check shows the REAL locked
situation (points can't transfer without the Sapphire), so Burn and Earn argue
the same point.

**Earn wallet-coach polish** (from Annabel's review of the live preview):
1. **Alignment fix.** The three coach rows were each their own CSS grid, so
   columns sized independently and didn't line up. Merged into ONE shared grid
   (`.coachgrid` + `.coachsep` full-width dividers). Now Groceries/Dining/Travel
   align perfectly. Old `.coach` rules replaced.
2. **Clearer copy.** "Activate 5x this quarter / +6,000 pts" was confusing
   (Chase jargon). Now "Turn on 5x groceries / +6,000 pts / quarter". Muted rows
   changed from "No bonus card yet" to "No card earns extra here yet".
3. **Chase handoff affordance.** Groceries gain is now a tappable `<a class=gain>`
   in brass accent with an "opens Chase ↗" cue BELOW the points line (Annabel
   asked for it below, not inline). Signals the row hands off to Chase's
   activation screen (5x categories are activated in the Chase app, not in
   Wayloft). Product note for the real build: deep-link to Chase activation,
   track the quarter, re-surface the nudge each new quarter.
4. **Removed** "Today they cannot move." from the get-next-card paragraph
   (Annabel flagged it as the explanatory-one-liner style she dislikes).

## Live preview server (NEW — Annabel uses this now)

`projects/wayloft/design/serve_nocache.py` — a **ThreadingHTTPServer** with
no-store cache headers so a plain ⌘R always shows the latest edit (no hard
refresh). Serving at **http://localhost:8809/screens.html**. Replaces the
manual http.server + Playwright-screenshot loop for her review.

**Gotcha fixed this session:** the first version used single-threaded
`HTTPServer`, which HUNG on the browser's keep-alive connection (curl timed out,
"not loading well"). ThreadingHTTPServer + `daemon_threads=True` fixed it.
Also had 3 stale listeners fighting over 8809 — always
`lsof -ti:8809 | xargs kill -9` before relaunch.

## Also: CLAUDE.md preference recorded

`~/.claude/CLAUDE.md` Working Style now says: when introducing an unfamiliar
concept/tool/tradeoff, explain it in plain language the first time, before
jargon, without being asked. (Annabel liked how the locked-points and Chase 5x
mechanics were explained plainly.)

## Next steps

1. Batch 4: Mobile views of Today, Earn, Burn deals, Burn trip check + polish.
   Verify in browser, refresh Desktop copy. Keep the 8809 server running.
2. Then re-center `apps/web` into Editorial Cream squared (steps + tokens in the
   2026-06-17-1300 checkpoint).

## Context to preserve

- Living spec: `projects/wayloft/design/screens.html`. Tracker:
  `projects/wayloft/design/in-progress.md`. Design standard: `~/.claude/design.md`.
- Real setup drives content: Freedom Flex held, 38,420 Chase UR locked (no
  transfer-partner card), Sapphire is the next-card unlock, watching United /
  Star Alliance / Hyatt / Marriott, routes NYC→Lisbon / NYC→London.
- Verify static screens via the 8809 server + Playwright; file:// is blocked.
