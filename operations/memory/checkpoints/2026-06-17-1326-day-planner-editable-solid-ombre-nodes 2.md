---
date: 2026-06-17
time: 13:26
project: day-planner ("The Day" — personal calendar + to-do tab, pairs with "The Edit")
status: v0.7 shipped + verified — END OF a productive session. The Day is now a FULLY EDITABLE live Google Calendar with the timeline look Annabel wanted. Editing (all write to her real Google primary cal): delete via hover ×, drag a to-do from the Inbox onto the day, double-click any event to change time/title. Visuals: routines row removed; event nodes are duration-scaled — ≤1hr = the original 44px SOLID circle, >1hr = a taller OMBRÉ pill (gradient stays in the color family, fades color→color-mix 68% white, NOT to cream which she disliked). Icon top-aligned. All verified in the preview against live data.
next-session: Feature-complete for editing + the look. Open polish only: (1) all-day events render in the .allday strip — no delete/edit/pill; (2) editor changes time + title but not the DAY (add a date field to move across days); (3) node-height cap 168px (~hits at ~2.5hr past the +60 offset, i.e. ~198min total) — raise if she wants very long blocks to keep scaling; (4) AI "structure my day" still a stub; (5) no drag-to-reschedule existing events (she chose double-click instead). WATCH: OAuth token may expire ~7d (consent screen "testing") — re-run `python3 auth_google.py` if live feed/edits go quiet. Preview server (preview_start "the-day") is FLAKY: dies on reload/across turns; FIRST screenshot after a navigation is a stale 1px sliver — resize (1300x880) then RE-SHOOT, or confirm window.innerWidth first. Stable manual test: `python3 serve.py 8802 --no-open` yourself (needs network egress for Google API).
build: projects/day-planner/{planner.html, serve.py, auth_google.py, data/, token.json}. NODE STYLING (planner.html): `.node{height:var(--nh) min 44px; border-radius:22px; icon top via align-items:start+padding-top:12px; background:var(--c)}` (solid); `.row.long .node{background:linear-gradient(180deg,var(--c),color-mix(in srgb,var(--c) 68%,#fff))}` (ombré). renderTimeline: `nodeH=min(168,44+round(max(0,durMin-60)*0.9))` set as --nh; row gets `long` class when durMin>60. serve.py: /api/event {action:create|update|delete} + update_event() (events().patch); fetch_live_calendar attaches Google id; scope calendar.events. Supersedes all earlier 2026-06-17 day-planner checkpoints (1223/1245/1305/1320).
---

# Session: The Day — editable calendar + Structured-style duration nodes

## Arc of this session (4 asks, all shipped + verified)
1. **"I can't edit anything."** → Added Google write-back. Re-scoped readonly→
   calendar.events (she re-authed once), added create/delete endpoints, hover ×
   delete on events, and drag-a-to-do-from-Inbox creates a real event.
2. **"Move it to 2pm by double-clicking."** → Double-click any timeline event →
   cream/serif Edit modal (title, start, end, Delete/Cancel/Save) → events().patch.
   Start change auto-shifts End to keep duration. Verified with a live round-trip
   (moved claire's video 1pm→3pm→back to 1pm).
3. **"I don't like these."** (routines chips) → removed the whole routines row.
4. **"Longer events = longer icons; 1hr solid, >1hr ombré, current ombré looks
   off."** → duration-scaled nodes; solid circle ≤1hr, in-color ombré pill >1hr.

## Verify
All via the preview against her live calendar. Node logic confirmed on Monday
(varied durations): 60min & 30min → 44px SOLID; 150min → 125px OMBRÉ; 165min →
139px OMBRÉ. No console errors. Her data left exactly as she had it.

## How she uses it
Open via the "Open The Day" desktop launcher (serve.py 8802). Hover an event for ×
to delete; drag an Inbox to-do onto the timeline to schedule it; double-click an
event to change its time/title. Everything writes to Google immediately.
