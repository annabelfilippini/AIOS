---
date: 2026-06-16
time: 12:30
project: aios-dashboard (shared design system) + day-planner + style-feed
status: Shipped & verified — established a shared AI-OS dashboard design system (anchor = The Edit) and re-skinned The Day to match it. Both tabs now read as one product.
next-session: Get Annabel's read on the match (esp. the one taste knob: muted earthy event colors vs fully monochrome like The Edit). Then resume The Day roadmap: AI "structure my day", confirm→Google write-back, real to-do source, live refresh. Future: build the actual dashboard shell at projects/aios-dashboard/ with the sidebar tab nav (The Edit's `.tab`/`.tab.on` is the pattern) to assemble The Day + The Edit + future tabs.
---

# Session: AI-OS dashboard design system + The Day re-skin

## Decision (architecture)

Annabel's "personal site" is a **personal AI-OS dashboard with tabs**: The Day
(calendar, tab 1), The Edit (shopping), more later. She wants them to match but is
designing each separately for now and assembling later. Resolution: a **shared
design system** (tokens + spec) that every tab mirrors, so assembly is trivial.
**The Edit is the anchor** (it is the most finished aesthetic).

## Done this session (the proof)

1. Extracted The Edit's exact design DNA from its source
   (`projects/style-feed/feed.html` line 8 `:root`): cream `--bg #f3efe9`, ink
   `#1b1916`, accent brown `#3a352d`, taupe `#7c756a`, hairline `#e0d9cd`, berry
   `--love #b54b5a`; **Cormorant Garamond + Jost (wt 300)**; uppercase
   letter-spaced labels; hairlines over shadows; `.tab`/`.tab.on` nav component.
2. Codified it as the shared system at **`projects/aios-dashboard/design-system/`**
   (`tokens.css` with `:root` + `.ds-*` component classes + functional `--fn-*`
   event accents; `DESIGN.md` one-page spec incl. "adding a new tab" + no-em-dash
   rule).
3. **Re-skinned The Day** (`projects/day-planner/planner.html`) into the cream/serif
   language — same calendar layout + logic, new skin: Cormorant titles/to-do
   titles, Jost uppercase labels, hairline cards/sheet, **earthy desaturated event
   colors** (`--fn-*`: brown focus / sage move / dusty-blue water / berry social /
   taupe home), berry now-marker, accent-filled selected day, italic-serif
   free-time nudges + empty state. Added a "Personal · The Day" kicker. Stripped
   em-dashes from UI copy.
4. The Edit unchanged (it IS the source). Coral v0 backed up to
   `day-planner/planner-v0-coral.html`.

## Verify / gotchas

- Playwright DOM-eval over `http://localhost:8802/planner.html?v=2` confirmed:
  Cormorant + Jost both loaded, body bg `#f3efe9`, title + task titles Cormorant,
  Work node `#3a352d`, selected-day fill `#3a352d`, italic free-time nudge, 6
  Monday rows intact. No console errors.
- Cache-bust with `?v=` (recurring python http.server stale-cache trap).
- Screenshot persistence still broken this session — verified via DOM-eval +
  opened live for review.

## Files touched (this batch)

- `projects/aios-dashboard/design-system/tokens.css` (new)
- `projects/aios-dashboard/design-system/DESIGN.md` (new)
- `projects/day-planner/planner.html` (re-skinned)
- `projects/day-planner/planner-v0-coral.html` (backup of coral v0)

## Next steps

- Annabel's read on the match + the muted-vs-monochrome event-color knob.
- Resume The Day roadmap; eventually build the dashboard shell to host the tabs.
