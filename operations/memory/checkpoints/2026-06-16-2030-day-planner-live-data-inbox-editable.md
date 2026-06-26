---
date: 2026-06-16
time: 20:30
project: day-planner ("The Day" — personal calendar + to-do tab, pairs with "The Edit")
status: v0.3 shipped & verified — TRUE-LIVE Google Calendar. serve.py GET /api/calendar pulls this week live (read-only) and normalizes to Denver; page falls back to the data/calendar.json snapshot if offline. Inbox emptied + add/delete (write-locked /api/inbox). no-store headers killed the ?v= dance. Verified end-to-end in the preview: page shows live events incl. ones she added minutes earlier ("Uncle dave", "Take lanie to Kent!"); caption reads "Live · today 12:10 PM"; now-line correct.
next-session: Live calendar DONE. Open roadmap: AI "structure my day" auto-placement; confirm→create_event write-back (needs a write scope re-auth — currently calendar.readonly only); design/copy polish ("free time?" nudges REMOVED at her request — she dislikes them, do not re-add; "Uncle dave" got the generic note icon — name-matching is shallow); maybe read secondary calendars (Reach Consulting/Family). WATCH: OAuth token may expire ~7 days if consent screen is in "testing" — re-run auth_google.py or publish the app.
build: projects/day-planner/{planner.html, serve.py, data/calendar.json, data/inbox.json}. Launcher ~/Desktop/Open The Day.command → serve.py 8802. Preview config .claude/launch.json name "the-day".
---

# Session: The Day v0.2 — live data file + editable inbox

## What Annabel asked
1. "It doesn't seem to be actively pulling from my calendar."
2. "Delete my inbox and allow me to delete and add to that as well."
3. "What is the overall plan with this planner site?"

## Diagnosis
The calendar was a static JS array hard-coded into planner.html last session — it
never talked to the calendar, and had already drifted (her real calendar gained
upper body lift / core power / barry's / legs / yoga? that the bake never had).
Today (Tue 6/16) genuinely is empty on her real calendar, which made it look dead.

## Done this session (verified)
1. **Externalized calendar** → `data/calendar.json` (16 real events for the week,
   pulled fresh via MCP). planner.html fetches it on load; `let EVENTS=[]` +
   async `loadCalendar()`. today/week computed from the real clock (localISO +
   mondayOf), so the "today" highlight and now-line are always correct.
2. **serve.py** (mirrors The Edit): `no-store` headers kill the stale-cache trap
   (no more ?v=); `GET/POST /api/inbox` persists the inbox to `data/inbox.json`.
   Added `.claude/launch.json` config `the-day` (port 8802) + Desktop launcher.
3. **Inbox** seed removed (empty by default; KEY bumped v0→v1). Add via FAB and a
   new `+` in the inbox header; delete via a per-task `×`. Inbox writes to disk
   via /api/inbox (localStorage fallback if served without serve.py).
4. **Refresh button** (circular-arrows icon) re-reads calendar.json without losing
   inbox/done state; **"Synced today 8:25 PM"** caption from generatedAt.
5. Broadened the icon matcher for workouts (barry/barre/core/pilates/legs/full
   body/upper body…) and handled the midnight + all-day events from real data.

## Verify / gotchas
- Preview verified: Mon = all 7 real events incl. "Call about Derm" 12:00 AM;
  Wed = upper body lift 6:30 + Coffee w adi; Thu = all-day webflow + core power.
  No console errors. Screenshot good once the viewport was sized to 1280 (a
  zero-width viewport renders a 1px sliver — set size before screenshotting).
- **Bug found + fixed:** firing add+delete in the same instant raced serve.py's
  fixed `inbox.tmp` filename and corrupted inbox.json (broke GET). Added a
  threading.Lock around the write + made GET resilient to a bad file. Stress-
  tested with 10 parallel POSTs → stays valid JSON.
- The overnight "360min of free time?" nudge (gap between the midnight Derm call
  and 7am Work) is silly — free-time nudges should be suppressed outside waking
  hours. Minor polish, deferred.

## The honest constraint on "live"
A Python-served static file can't reach her Google Calendar by itself — the
calendar is reachable only through the Claude MCP. So true hands-off sync needs
either a scheduled Claude task that re-pulls (A+) or serve.py holding its own
Google API credentials (B). v0.2 lays the foundation (data lives in a file the
page reads + a Refresh button); the A+/B/C choice is the pending decision.

## Update (2026-06-17 12:10) — she chose B (true live), and it shipped

Turned out to need ZERO Google Cloud Console work: she already had gcloud, an
"installed"/Desktop OAuth client at `~/.config/gws/client_secret.json` (project
`aj-bot-489823`), and the Calendar API already enabled on it.

- `auth_google.py` reuses that client to mint a `calendar.readonly` `token.json`
  (gitignored) — she authorized in one browser click.
- `serve.py` now has `GET /api/calendar`: pulls this week live (singleEvents,
  Denver-normalized via zoneinfo + datetime.fromisoformat), 60s cache, writes the
  snapshot as a durable fallback. On token/network failure it serves the last
  snapshot with `live:false`, so the page never breaks.
- `planner.html` `loadCalendar()` fetches `/api/calendar` then falls back to the
  static file; caption shows "Live · …" when truly live.
- Verified: 18 live events; "Uncle dave" (Wed 7:15pm) + "Take lanie to Kent!"
  (Thu) appeared though they post-dated the original snapshot. Screenshot good.

Gotchas: installed google-api-python-client/auth/oauthlib into anaconda python.
The preview-managed server died once on restart (session-bound); run serve.py via
the Desktop launcher for a stable daily process. token.json + data/*.json are
gitignored (personal). Write scope NOT granted yet — write-back will need re-auth.
