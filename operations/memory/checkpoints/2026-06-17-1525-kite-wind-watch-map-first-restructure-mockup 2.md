---
date: 2026-06-17
time: 15:25
project: websites / kite-wind-watch
status: IN-PROGRESS — Map-first restructure mockup built and open in Annabel's browser for review. Awaiting her read on map-first-as-pins, fixed-vs-slide-in spot panel, and serif-vs-grotesque before re-centering index.html. Reddit scraping deferred to next session (her call).
supersedes: 2026-06-17-1342-kite-wind-watch-ux-directions-mascot-removed.md
---

# Session: kite-wind-watch — map-first UX restructure (new mockup)

Annabel scrapped the A/B/C directions. She pasted the same 3 weather-app
references again (already saved in `references/`) and asked for a **total UX
restructure**: better usability, **remove ALL rounded corners**, a **clear
Google map showing where everything is**, **all spots on ONE map** (no more
Colorado/Wyoming spots on a separate tab), and (deferred) better Reddit scraping.

## Decisions locked this session

1. **Direction forks (via AskUserQuestion):**
   - Palette: **light / editorial** (keep navy/water accent, squared). Not dark.
   - Map base: **satellite / terrain** imagery as the canvas.
   - Reddit: **"let me explain"** — deferred to next session, her call ("focus on this").
2. **A/B/C scrapped.** `design-directions.html` + its Desktop copy **deleted** (no
   proliferation). New artifact is `design-mockup.html`.
3. **The restructure moves the app TOWARD the global design standard, not away.**
   `~/.claude/design.md` already wants squared corners, serif display, grotesque
   body, **mono for all figures**, one accent. The old "soft rounded weather-app"
   lane in this project's `design.md` was the exception. So design.md's Vibe Lane
   + Shape sections will need rewriting on approval (NOT done yet — pending).

## Built this session

- **`projects/websites/kite-wind-watch/design-mockup.html`** — self-contained,
  interactive, full-screen map-first mockup. Verified via headless-Chrome PNG at
  2x (`/tmp/kww-v2.png`). Structure:
  - **Full-bleed map canvas** = the whole app. Faked terrain (green Rockies west,
    gold plains east, water bodies under each pin, WY/CO/NE labels + state lines).
    All 11 real spots pinned with real coords, **colored by verdict** (the wind
    scale is now the map legend). McConaughy far-right NE, Pueblo bottom, Dad's
    spots + Dillon/Williams Fork in the mountains, Front Range on the seam.
  - **Bottom day strip scrubs time** → recolors every pin + updates the panel live
    (Wed 17 … Tue 23). This is the strongest borrowed idea from the references.
  - **Left layer rail** (Wind/Gust/Temp/Find), **bottom-left legend**, top-left
    serif wordmark, **right-side spot detail panel** (verdict in serif, big mono
    kt, best-window line, hourly consensus chart w/ green peak + threshold line,
    4-source row, **Reddit chatter folded in** as "What people say").
  - **Zero rounded corners.** Serif (Cormorant) display, Inter body, JetBrains
    Mono figures. Frosted squared panels over the map.

## Open / Next (BLOCKER: Annabel's review)

- Awaiting her read on three things: (a) map-first, everything-as-pins right? or
  still want a spot list? (b) spot panel fixed vs slide-in-on-tap (more map by
  default)? (c) serif for big type yes/no?
- **On approval:** rewrite this project's `design.md` Vibe Lane + Shape (squared,
  map-first, satellite, serif+mono) + add a dated iteration-log entry, THEN
  re-center the canonical `index.html` into this structure with the **real Google
  satellite map** (localhost:8804, referrer-restricted key).
- **Reddit scraping = next session** (deferred). She'll explain what's wrong
  (stale / thin / wrong-spot / noisy) then; design the spot-panel chatter around
  the real fix.
- Minor copy nit to resolve on the rebuild: numeric ranges in the panel use
  en-dashes ("1–5pm", "19–26"); global standard says no dashes in visible copy.
  Decide range-dash vs "1 to 5pm" when wiring real copy.

## Operate / gotchas (unchanged from prior checkpoint)

- Canonical app file: ONE `index.html`, served at **localhost:8804**
  (`preview_start kite-wind-watch`). Never a `file://` copy for the REAL app
  (Google Map needs the referrer-restricted origin). The **mockup** is fine on
  `file://` because its map is faked/self-contained.
- Preview MCP only serves the app entry. Preview a sibling page (the mockup) via
  headless Chrome → PNG: `"…/Google Chrome" --headless=new
  --force-device-scale-factor=2 --window-size=1440,900 --screenshot=/tmp/x.png
  --virtual-time-budget=3500 file://…/design-mockup.html`.
- Alerter unchanged: hourly cron on Hetzner VPS (`root@5.78.218.220`), still live.
  Full alerter/accuracy-stack state in `2026-06-16-1435-kite-wind-watch-session-state.md`.
