---
date: 2026-06-17
time: 13:20
project: day-planner ("The Day" — personal calendar + to-do tab, pairs with "The Edit")
status: v0.6 shipped + verified. Fully editable LIVE Google Calendar (write scope active) + two visual refinements this session. EDIT: delete (hover ×) / drag-from-inbox / double-click-to-edit-time all write to Google. VISUAL: (1) removed the decorative routines row (Structure Tomorrow / Water Plants / Call Mum) at her request; (2) timeline nodes are now duration-proportional pills — ≤1hr stays the original 44px circle, events LONGER than an hour grow (Structured/Amie style), icon at top, color gradient fading to cream. Verified on Monday: 60min→44px circle, 150min→125px, 165min→139px.
next-session: Calendar editing + the pill look are done. Open polish: (1) all-day events still render in the .allday strip (no delete/edit, no pill); (2) editor changes time + title only, not the DAY (add a date field to move across days); (3) node-height cap is 168px (~3.3hr) — raise if she wants very long blocks to keep scaling; (4) AI "structure my day" still a stub; (5) drag-to-reschedule existing events not built (she chose double-click edit instead). WATCH: OAuth token may expire ~7d if consent screen is "testing" — re-run auth_google.py if live feed/edits go quiet. Preview server (preview_start "the-day") is FLAKY: dies on reload/across turns, and the FIRST screenshot after a navigation is a stale 1px-sliver frame — resize (e.g. 1300x880) then re-shoot, or confirm window.innerWidth before trusting a screenshot. For stable manual testing run `python3 serve.py 8802 --no-open` yourself (needs network egress for the Google API).
build: projects/day-planner/{planner.html, serve.py, auth_google.py}. This session's planner.html edits: removed .routines/.routine CSS + #routines div + renderRoutines() + its renderAll() call + S.routines from def; .node now uses height:var(--nh) min 44px, border-radius:22px, icon top-aligned, linear-gradient(var(--c)→color-mix cream); renderTimeline computes nodeH = min(168, 44 + max(0,durMin-60)*0.9) and sets --nh on the row. serve.py unchanged since v0.5 (update_event + /api/event create|update|delete). Supersedes 2026-06-17-1305.
---

# Session: The Day v0.6 — duration pills + routines removed

## What Annabel asked (two quick follow-ups after the edit feature)
1. "I don't like these" (pointed at the routines chips row) → remove them.
2. "I like how longer events have longer icons [in this reference] — can you do
   that." Then refined: "one-hour things should be like the icons before, and
   only when longer than an hour do they start being a bit longer."

## Done & verified
1. **Removed the routines row** entirely (markup, render fn + call, data, CSS).
   Old localStorage state with a stale `routines` key is harmless (unused).
2. **Duration-proportional nodes.** `.node` became a vertical capsule:
   height `var(--nh)` (min 44px), `border-radius:22px` (a 44px node is a perfect
   circle = the original look), icon top-aligned (`align-items:start;padding-top:12px`),
   and a `linear-gradient(var(--c) → color-mix cream)` so tall pills fade like the
   reference (flat `var(--c)` fallback for engines without color-mix).
   `renderTimeline`: `nodeH = min(168, 44 + round(max(0, durMin-60) * 0.9))` set as
   `--nh` on the row. So ≤60min = 44px circle; >60min grows ~0.9px/min, capped 168.
   Verified (Monday): Derm/Lift/Swim 60min→44, BE HOME 30min→44, Work/Pool
   150min→125, Work 165min→139. Screenshot matches the Amie/Structured reference.

## State of the planner
Live read ✓ · delete ✓ · drag-from-inbox-create ✓ · double-click edit time/title ✓
· routines removed ✓ · duration pills ✓. All writes hit her real Google Calendar.
