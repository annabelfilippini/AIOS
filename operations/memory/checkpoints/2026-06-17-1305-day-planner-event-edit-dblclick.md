---
date: 2026-06-17
time: 13:05
project: day-planner ("The Day" — personal calendar + to-do tab, pairs with "The Edit")
status: v0.5 shipped + verified END-TO-END against the LIVE Google Calendar. Annabel re-authed (token now has calendar.events write scope), so delete + drag-create + edit all write to Google for real. This session added DOUBLE-CLICK TO EDIT: dbl-click any timeline event → a cream/serif modal (title, start, end, Delete/Cancel/Save) → patches the Google event. Verified: moved "watch claire's video" 1pm→3pm via the API and back to 1pm (real round-trip), and drove the UI (dbl-click opens, fields populate, changing Start auto-shifts End to keep duration, Save writes + closes + toasts). Her data left untouched at 1pm.
next-session: Calendar is now fully editable (delete + drag-in + edit time/title). Open polish: (1) all-day events still have no delete/edit (they render in the .allday strip, not as .row); (2) editor changes time + title only, not the DAY — add a date field if she wants to move an event to another day; (3) drag-to-reschedule existing events on the timeline (she chose dbl-click instead, which is done); (4) AI "structure my day" still a stub. WATCH: OAuth token may expire ~7d if the consent screen is "testing" — re-run auth_google.py if the live feed/edits go quiet. Preview server (preview_start "the-day") is FLAKY — dies on reload/across turns; for stable testing run `python3 serve.py 8802 --no-open` yourself (needs network egress) or use the Desktop launcher.
build: projects/day-planner/{planner.html, serve.py}. serve.py: added update_event() (events().patch) + action:'update' in /api/event. planner.html: edit modal markup + CSS (.modal/.field/.m-save…), rowRef()/deleteByRef() refactor, openEditor/closeEditor/saveEditor, dbl-click wiring on .row (excludes .rowacts), Start-change auto-shifts End, Esc/Enter/backdrop close. Supersedes 2026-06-17-1245.
---

# Session: The Day v0.5 — double-click an event to edit its time

## What Annabel asked
"I just put watch claire's video on my calendar [via drag]. I want to move it to
2pm — let me do that by double-clicking on it and having the option to change it."
(Implicitly confirms she completed the write-scope re-auth from v0.4.)

## Done & verified
1. **serve.py**: `update_event(eid,day,s,e,t)` → `events().patch` (start/end + summary);
   new `action:'update'` branch in `/api/event` (cache invalidated after). Same
   needAuth gate as create/delete.
2. **planner.html — edit modal**: double-click any timeline `.row` (anywhere but the
   delete/done buttons) opens a modal with Title + Start + End (native time inputs)
   and Delete / Cancel / Save. Save → POST update → reloadCalendar + toast
   ("Moved X to H:MM"). Changing **Start auto-shifts End** to preserve the original
   duration (so moving a 1h event to 2pm makes it 2–3pm in one edit). Esc/backdrop
   cancel, Enter saves. Delete in the modal reuses the shared `deleteByRef`.
   Events without a Google id (local pencils) update/delete locally.
3. Tooltip "Double-click to edit" + pointer cursor on the event body as the affordance.

## Verify (against her real calendar; safe round-trips, data restored)
- API: claire's video 13:00→15:00 (Google confirmed) → restored to 13:00-14:00.
- UI (preview): dbl-click opens modal; fields = "watch claire's video"/13:00/14:00;
  setting Start=14:00 auto-set End=15:00; Save (with original time) → modal closed,
  toast "Moved … to 1:00 PM", calendar still 13:00-14:00. Screenshot confirms the
  modal design. innerWidth confirmed 1280 (the 1px-sliver screenshot was a stale
  frame, not a layout bug — re-shoot after confirming innerWidth).

## For Annabel
Double-click "watch claire's video", change Start to 2:00 PM (End jumps to 3:00 PM
on its own), hit Save. It moves on your real Google Calendar. Same modal edits any
event's time or title; Delete is in there too.
