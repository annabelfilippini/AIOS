---
date: 2026-06-16
time: 11:55
project: day-planner (personal calendar + to-do tab, working name "The Day" — pairs with "The Edit")
status: v0 shipped & verified — standalone HTML planner wired to Annabel's REAL Google Calendar (annabelflip1@gmail.com, America/Denver), matching the Structured/Amie-style reference she shared. Two-pane Inbox + day timeline, real week data, local to-do Inbox, completion + tentative scheduling. Verified via Playwright DOM inspection (screenshot persistence broken this session).
next-session: Get Annabel's read on the layout vs her reference image. Open roadmap: (B) the AI "Structure my day" magic — auto-place the whole Inbox into the day's free gaps (currently a stub + a single-task next-free-slot pencil-in); (C) confirm-to-Google write-back via create_event (MCP available, schema loaded) so tentative blocks become real events; (D) wire a REAL to-do source (she never picked — Google Tasks pairs cleanest with existing Google access; else Apple Reminders/Todoist) to replace the local seed Inbox; (E) live calendar refresh (today is baked static — needs a build step or serve.py endpoint like The Edit); (F) design polish + clean app microcopy (remove em-dashes per her voice rule). Build: projects/day-planner/planner.html. Launcher: ~/Desktop/Open The Day.command → python http.server 8802 → /planner.html.
---

# Session: Calendar/To-do tab v0 — "The Day"

## Context

Annabel is building a personal multi-tab app (her "personal site"): the shopping
tab is **The Edit** (`projects/style-feed/`). She wanted a parallel track and
chose **calendar + to-do**, sharing a Structured/Amie-style reference image (iPad,
coral theme, left Inbox of unscheduled to-dos with time estimates + a `+` to drop
onto the day; right = day as a vertical timeline with colored icon bubbles,
completion checks, current-time marker, "X min of free time?" nudges; week strip
with density dots; AI button; routine chips; floating +).

## Stack reality confirmed

- Google Calendar IS connected via the calendar MCP (`b26628db…`). Primary =
  `annabelflip1@gmail.com`, tz **America/Denver**. Other calendars exist (Reach
  Consulting, Family, East Track/XC, Holidays) — v0 reads primary only.
- `create_event` schema is loaded and available for write-back (not yet used —
  no events created without explicit confirm).
- No to-do source connected yet (all "Shopify/Tasks" hits in memory were client
  work). v0 uses a local seed Inbox.

## Done this session (the proof)

1. Pulled Annabel's real week (Mon 6/15–Sun 6/21) and baked it into a standalone
   `planner.html` (self-contained HTML/CSS/JS, mirrors The Edit's local pattern).
2. Reproduced the reference layout: two-pane Inbox + day timeline, week strip with
   real per-day event-density dots, routine chips (Call Mum struck = done),
   AI/settings buttons, floating +, coral theme, white-line icons in colored
   circles (navy work / green fitness / blue swim / coral social / grey home).
3. Real-data behaviour verified via Playwright DOM eval:
   - Today (6/16) = empty-state ("Nothing scheduled today" + "Structure my day").
   - Monday (6/15) = all 6 real events with correct 12h times, durations, colors,
     plus a "30min of free time?" nudge in the 9:30–10:00 gap.
   - Click any week day → loads that day's real events.
4. Interactions (localStorage `theday:v0`): check off events (strikethrough +
   filled check), toggle routines, add Inbox to-dos (FAB prompt), and a `+` on an
   Inbox task pencils it into the day's next free slot as a **tentative** dashed
   block (local only) with a toast that confirm-to-Google is the next step.

## Verify / gotchas

- Playwright `file://` is blocked (same as The Edit) → served via
  `python3 -m http.server 8802`. Left running; harmless, dies on reboot.
- **Screenshot persistence is broken this session** — `browser_take_screenshot`
  reports success but writes no findable PNG. Fell back to DOM-eval verification
  + a Desktop launcher so Annabel sees the live app. Revisit if visual proof
  needed later.
- Calendar events carry odd tz labels (Europe/Madrid, America/Yellowknife) but
  all resolve to -06:00 in June, so rendered as Denver-local. "Call about Derm"
  on Mon sat at 00:00 (midnight) and was dropped from the demo as an edge case.
- Today is baked static; reopening days/weeks won't reflect new calendar changes
  until a refresh/build step exists.

## Next steps

- Annabel's read on layout vs her reference.
- Then B (AI structure-my-day) is the real magic; C (confirm→create_event
  write-back); D (real to-do source); E (live refresh); F (design + copy polish).
