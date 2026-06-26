---
date: 2026-06-14
time: 14:40
project: websites / kite-wind-watch
status: shipped
next-session: Optional polish on the kite-wind-watch illustration/feel, and decide whether to keep the newly-added "soft UI / tool dashboard" lane in the global design.md.
---

# Session: Kite Wind Watch soft redesign + global design.md decontamination

## What we worked on

- **Completely redesigned `kite-wind-watch/index.html`** from the rejected
  cinematic/editorial draft into the soft, light, modern weather-app look Annabel
  prefers: pale lavender background, rounded white cards, left rail with nav +
  settings, a big consensus-wind hero number, model-agreement bars, soft highlight
  tiles, an SVG hourly-wind area chart, and rounded 5-day outlook cards with the
  best day highlighted.
- **Added an original inline-SVG line-art kitesurfer** (geared up, kite drooping,
  flag limp = "still waiting on wind"), in the spirit of Annabel's funny
  umbrella/floaty reference image. Self-contained, no external assets.
- **Preserved the live forecast engine byte-for-byte** (Windguru + Open-Meteo
  Best/ECMWF/GFS/ICON + NWS hourly, consensus ranking, hourly timeline). Only the
  HTML structure, CSS, and render functions changed.
- **Killed the freeride leak:** the old draft hardlinked
  `../freeride-tarifa/assets/web/hero-web.mp4` + poster as its hero. Removed.
- **Cleaned the GLOBAL `projects/websites/design.md`** of all project-specific
  content (Annabel's explicit ask: global = cross-project taste only).
- Updated `kite-wind-watch/design.md` to the soft-UI direction and added a
  no-external-assets rule + iteration log.
- Added a `websites` server (port 8796, root `projects/websites`) to
  `.claude/launch.json`.

## Decisions made

- This dashboard uses the **soft UI / tool dashboard lane**, intentionally
  departing from the global "sharp corners / full-bleed photo hero" default. The
  project brief documents the local exception; I also added a blessed "soft UI /
  tool dashboard" lane to the global design.md (additive; revertable if Annabel
  dislikes globally softening the sharp-corner rule).
- Global design.md cleanup was **de-naming + deletion, not relocation** — the
  detailed Crepel/Radian/Santic translations and the Tarifa map saga already live
  in `freeride-tarifa/design.md`. Removed/generalized in global: the freeride
  brief pointer, the "Mathieu Crepel reference" + "Radian (rideradian.com)" +
  "Santic-style" headings, the "Freeride homepage scroll" example, and the dated
  Freeride Tarifa map confirmed-examples (kept the reusable OSM-vs-Google keyless
  embed lesson, dropped the project/beach names).

## Root cause of "Codex took freeride videos"

Three layers, now all fixed: (1) `index.html` hardcoded the freeride video path;
(2) the project `design.md` literally said "use the Freeride media direction /
full-bleed kitesurfing media"; (3) the global `design.md` defaulted everything to
cinematic kitesurf/editorial with named freeride/Crepel/Radian references and no
soft-UI lane.

## Open questions

- Keep the new global "soft UI / tool dashboard" lane, or revert and keep that
  exception project-local only?
- Does the kitesurfer illustration land as "funny" enough, or refine the figure?

## Next steps

1. Get Annabel's reaction to the redesign (verified desktop + mobile, console
   clean, 6 sources live, 0 blocked).
2. If she likes it, optionally refine the illustration and consider rolling the
   soft-UI lane pattern to any future personal tools/dashboards.

## Context to preserve

- Preview: server `websites` on port 8796 (root `projects/websites`); page at
  `http://localhost:8796/kite-wind-watch/index.html`. Cache-bust with `?v=` (the
  recurring python http.server stale-cache trap).
- Windguru can block direct browser fetches; the UI keeps failed sources visible.
  In this session's verification all 6 were live.
