---
date: 2026-06-17
time: 12:45
project: day-planner ("The Day" — personal calendar + to-do tab, pairs with "The Edit")
status: v0.4 BUILT + verified (plumbing) — calendar is now EDITABLE. Added Google write-back so events can be deleted and Inbox to-dos dragged onto the day to create real events. Frontend + serve.py endpoints done and verified end-to-end in the preview (live read still works, delete buttons render, tasks draggable, /api/event returns the needAuth gate). ONE manual step left for Annabel: re-auth with the write scope (`python3 auth_google.py`) — until then editing returns a friendly "turn on editing" toast and nothing writes.
next-session: Re-auth is the unblock. After she runs auth_google.py (ticking "make changes to events"), delete + drag write to Google immediately — NO server restart needed (serve.py reads token.json fresh per call). Then re-verify a real delete + a real drag-create land in Google. Open polish: (1) all-day events have no delete button yet (they render in the .allday strip, not as .row) — add if she wants; (2) drag places at the dropped-near gap via next-free-slot — could add exact drop-time placement / drag-to-reschedule existing events; (3) AI "structure my day" still a stub. WATCH: OAuth token still may expire ~7 days if consent screen is in "testing".
build: projects/day-planner/{planner.html, serve.py, auth_google.py}. auth_google.py + serve.py scope readonly→calendar.events. serve.py: _service()/_has_write_scope()/create_event()/delete_event() + POST /api/event {action:create|delete}; fetch_live_calendar now includes event id. planner.html: row delete button (.del2, hover), draggable Inbox tasks + #timeline drop zone, placeTask()/deleteEvent()/findSlot()/anchorFromDrop()/reloadCalendar(). Supersedes 2026-06-17-1223.
---

# Session: The Day v0.4 — editable calendar (delete + drag-from-inbox)

## What Annabel asked
"I can't edit anything on the calendar. I want to be able to delete things or
drag them over from the inbox."

## Diagnosis
The timeline showed her REAL Google Calendar but the app had read-only scope
(`calendar.readonly`) and no create/delete wiring. The Inbox "+" only penciled a
local "tentative" block that vanished on refresh. So nothing could actually be
edited — exactly her complaint. The fix is real write-back, which is the next
roadmap item anyway.

## Done & verified (plumbing)
1. **Scope readonly → calendar.events** in auth_google.py + serve.py (read +
   create + delete; no settings/ACL access). serve.py now loads creds WITHOUT
   forcing a scope list, so a still-readonly token keeps reading live during the
   gap before she re-auths (verified: 18 live events, LIVE caption).
2. **serve.py write API**: `_service()`, `_has_write_scope()` (reads token.json
   scopes), `create_event()`, `delete_event()`, and `POST /api/event`
   ({action:'create',day,s,e,t} | {action:'delete',id}). On missing write scope
   it returns 403 `{needAuth:true}` with a run-auth message. `fetch_live_calendar`
   now attaches each event's Google `id` so the page can delete it. Cache
   invalidated after a write so the next pull is fresh.
3. **planner.html — delete**: each timeline `.row` got a hover × (`.del2`,
   stacked above the done check). `deleteEvent()` → confirm() → POST delete →
   reloadCalendar(). Events without an id (local pencils) just remove locally.
4. **planner.html — drag**: Inbox `.task`s are `draggable`; `#timeline` is a drop
   zone (dashed highlight on dragover). `placeTask()` finds a non-clashing slot
   near the drop Y (`anchorFromDrop` + `findSlot`) and POSTs a real create; on
   success removes the to-do from the Inbox + reloads. If no server (static file)
   it falls back to the old local-pencil behavior. The "+" button now routes
   through the same real-create path.

## Verify (preview, port 8802, new serve.py)
- No console errors. EVENTS=18, each has id. selDay today shows 3 rows, 3 delete
  buttons. 1 draggable Inbox task. API_INBOX true, LIVE true.
- `POST /api/event` (delete + via placeTask create) → 403 needAuth + the exact
  "run python3 auth_google.py" toast; Inbox NOT emptied (to-do preserved when
  blocked). This is the full path — it will succeed once the token has the scope.
- Screenshot good at 1280x860 (size viewport before screenshotting — the old
  1px-sliver trap).

## The one manual step (Annabel)
In Terminal, from projects/day-planner:  `python3 auth_google.py`
Pick account → Advanced → Continue (unverified own app) → **tick "make changes to
events"** → Allow. token.json is rewritten with the write scope; editing works
immediately (serve.py re-reads the token per request — no restart). Reload The Day.
