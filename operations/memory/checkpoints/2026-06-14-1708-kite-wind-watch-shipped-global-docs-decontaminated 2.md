---
date: 2026-06-14
time: 17:08
project: websites / kite-wind-watch
status: shipped
next-session: Get Annabel's verdict on the live redesign. Optional follow-ups she was offered (not yet approved): audit other shared files for project-specific leaks, and build a permanent one-click launcher for the full Windguru-included version.
supersedes: 2026-06-14-1440-kite-wind-watch-soft-redesign-and-global-designmd-cleanup.md
---

# Session: Kite Wind Watch shipped + global website docs decontaminated

## What we worked on

1. **Completely redesigned `kite-wind-watch/index.html`** from the rejected
   cinematic/editorial draft into the soft, light, modern weather-app look
   Annabel prefers: pale lavender bg, rounded white cards, left rail (nav +
   settings), a big consensus-wind hero number, model-agreement bars, soft
   highlight tiles, an inline-SVG hourly-wind area chart, and rounded 5-day
   outlook cards with the best day highlighted.
2. **Added an original inline-SVG line-art kitesurfer** (geared up, kite
   drooping, flag limp = "still waiting on wind"), in the spirit of Annabel's
   funny umbrella/floaty reference image. Self-contained.
3. **Preserved the live forecast engine byte-for-byte** (Windguru + Open-Meteo
   Best/ECMWF/GFS/ICON + NWS hourly, consensus ranking, hourly timeline). Only
   HTML structure, CSS, and render functions changed. Fixed one redesign bug
   (chart line `<path>` needed `fill:none`).
4. **Killed the freeride leak**: removed the hardlinked
   `../freeride-tarifa/assets/web/hero-web.mp4` + poster. Page now self-contained.
5. **Cleaned the GLOBAL `projects/websites/design.md`** of all project-specific
   content (10 edits; grep now returns zero project names). Added a blessed
   "soft UI / tool dashboard" lane and scoped the sharp-corner rule to the
   editorial lanes.
6. **Updated `kite-wind-watch/design.md`** to the soft-UI direction + a
   no-external-assets rule + iteration log.
7. **Added the project-agnostic-shared-files rule to `~/.claude/CLAUDE.md`**
   (Context Budget), with Annabel's approval, so this contamination is prevented
   globally, not just for websites.
8. **Delivered the file for review**: copied to `~/Desktop/kite-wind-watch.html`
   and opened it in her browser. Added a `websites` server (port 8796, root
   `projects/websites`) to `.claude/launch.json`.

## Decisions made

- **Soft UI / tool dashboard lane KEPT in the global design.md** (Annabel's
  "make my preferences more apparent" endorsed it). Revertable to project-local
  if she changes her mind.
- Global design.md cleanup was **de-naming + deletion, not relocation** — the
  detailed Crepel/Radian/Santic translations and the Tarifa map saga already
  live in `freeride-tarifa/design.md`.
- The "specifics belong in the project, not global files" preference is now
  documented at three layers: `~/.claude/CLAUDE.md` (general), the websites
  `CLAUDE.md` (split test), and the top of the websites `design.md`. Deliberately
  NOT scattered further (that would be the same bloat the rule warns against).

## Root cause of "Codex took freeride videos" (resolved)

Three layers, all fixed: (1) `index.html` hardcoded the freeride video path;
(2) the project `design.md` said "use the Freeride media direction / full-bleed
kitesurfing media"; (3) the global `design.md` defaulted everything to cinematic
kitesurf/editorial with named freeride/Crepel/Radian references and no soft-UI
lane.

## Open questions / offered but not yet approved

- Audit other shared files (`skills/`, standards, memory index) for the same kind
  of project-specific leak.
- Build a permanent one-click launcher for the full version (Windguru included)
  so Annabel does not need a manually-started server.
- Does the kitesurfer illustration land as "funny" enough, or refine it?

## Context to preserve

- Preview: server `websites` on port 8796 (root `projects/websites`); page at
  `http://localhost:8796/kite-wind-watch/index.html`. Cache-bust with `?v=`
  (recurring python http.server stale-cache trap).
- `~/Desktop/kite-wind-watch.html` is a self-contained copy for double-click
  opening. From `file://`, Open-Meteo + NWS load live but **Windguru is blocked**
  (browser rejects its cross-origin request); the UI shows blocked sources
  honestly. Use the localhost URL for all 6 live.
- Verified in browser desktop + mobile this session: console clean, 6 sources
  live / 0 blocked, no freeride references remain.
