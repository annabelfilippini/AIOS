---
date: 2026-06-20
time: 14:45
project: day-planner ("The Day" — personal calendar + to-do tab)
status: shipped + verified (DOM + payload-stub + screenshot, no console errors). Follow-up polish on the week/month calendar from the 14:10 checkpoint. THREE things this session: (1) header de-cluttered — removed the "LIVE · TODAY …" synced caption and the AI pill so the Week/Month toggle no longer crowds the date title; (2) month-grid spill-over days were rendering "off the calendar" (transparent/borderless .out cells made their July events float on the page background) — fixed by keeping the cell border on .out (muted number + .mev opacity .5) so all 42 cells stay contained and the grid fits the pane; (3) ADD-TO-CALENDAR: the bottom-right FAB now creates real Google Calendar events instead of adding to the Inbox. Earlier this session I had removed the Inbox entirely then restored it when she said she liked it — Inbox is BACK (3-col layout), top-right + still adds to Inbox, only the FAB changed.
next-session: Calendar add/edit is functional. Possible polish: (a) FAB is hidden in month view (setView sets fab.hidden = mode!=='week') — if she wants to add from month view, either show it there or make month-cell click offer "add on this day"; (b) the edit modal now has a Date field so editing an event can move it to another day (update action already supports day change) — verify the day-move live once; (c) all-day events still aren't visually distinct in month cells; (d) starred-but-automated senders (donotreply "Continue your rental application", Annie Morning Brief) show as pressing because starred=pressing — offered to filter, she hasn't decided. Live Gmail email IS working now (she ran auth_google.py from the project folder).
build: projects/day-planner/planner.html only (serve.py UNCHANGED — /api/event create/update/delete already existed). Live agent com.annabel.theday does NOT need a restart this round; she just reloads her tab (8802) to pick up the new planner.html.
  - planner.html add-event: modal got id="edHead" + a <input type="date" id="edDate">. newEvent() opens the modal in create mode (editing={isNew:true,id:null,day:selDay,'09:00'-'10:00'}, heading "New event", Delete hidden). openEditor() now sets heading "Edit event", shows Delete, fills edDate. saveEditor() branches isNew→POST action:create / id→update (now reads day from edDate so an edit can change the day) / else tentative. FAB onclick rewired addTodo→newEvent. Verified via fetch-stub: FAB→create payload {action:create,day:2026-06-20,s:14:00,e:15:00,t:Dentist}, modal closes. (Did NOT write a real test event.)
  - CACHE BUG fixed: the per-range client cache (_calCache, 60s) I added in the 14:10 session would hide a just-created/edited/deleted event for up to a minute even though the BACKEND clears its cache. Added bustCal() (deletes all _calCache keys) and called it at the top of reloadCalendar(), so every write/refresh re-pulls fresh. This also retroactively fixed drag-to-schedule + edit + delete staleness.
  - month .out cells: was `background:transparent;border-color:transparent` (events floated loose on the bg = "off the calendar"); now `background:transparent` keeps the .mcell border, `.mcell.out .mev{opacity:.5}`. Verified outCount=12 cells have border rgb(224,217,205); grid last-cell bottom 692 < 700 vh (fits).
  - header: removed `<span id="synced">` + `<button id="aiBtn">`; guarded aiBtn wiring with `(()=>{const a=...; if(a)...})()`. renderSynced already guards a missing #synced.
---

# Session: The Day — add calendar events + month spill-over + header declutter

## Asks (in order, same session)
1. "Remove the open section on the right" → removed Inbox. Then "wait I liked
   the inbox" → restored it; real issue was empty space + a crammed header.
2. "Week/Month tabs almost overlapping, remove LIVE then AI" → done.
3. Month screenshot: July days rendering "off the calendar" → contained them.
4. "I'd like to add to my calendar. The bottom-right + goes to inbox, I want it
   to add to my calendar" → FAB now creates Google Calendar events; top-right +
   stays Inbox.

## Verify
Preview 8803 (same token = real Google Calendar, so add was tested with a
stubbed fetch — no junk event written). FAB opens "New event" modal, Date
defaults to selDay, Save emits the correct create payload and closes. Month
out-cells bordered (12), grid fits 700px height, no console errors.
