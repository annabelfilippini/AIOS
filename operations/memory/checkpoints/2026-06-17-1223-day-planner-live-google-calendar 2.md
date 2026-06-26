---
date: 2026-06-17
time: 12:23
project: day-planner ("The Day" — personal calendar + to-do tab, pairs with "The Edit")
status: v0.3 shipped & verified — TRUE-LIVE Google Calendar. The planner now pulls Annabel's real Google Calendar live (read-only) on every load, the Inbox is empty + fully editable (add/delete, persisted to disk), and the "free time?" nudges were removed at her request. Verified end-to-end in the preview against live data.
next-session: Live calendar + editable inbox are DONE. Open roadmap, in priority order: (1) AI "structure my day" — auto-place the whole Inbox into the day's free gaps (currently a stub + single-task next-free-slot pencil-in); (2) confirm→Google write-back via create_event (needs a write-scope re-auth — currently calendar.readonly only); (3) polish ("Uncle dave" etc. fall to the generic note icon — name matching is shallow; consider reading secondary calendars Reach Consulting / Family / East Track). WATCH: the OAuth refresh token may expire ~7 days if the consent screen on project aj-bot-489823 is in "testing" — if the live feed goes quiet, re-run `python3 auth_google.py`, or publish the app to make it durable.
build: projects/day-planner/{planner.html, serve.py, auth_google.py, data/calendar.json, data/inbox.json, token.json}. Launcher ~/Desktop/Open The Day.command → serve.py 8802. Preview config .claude/launch.json name "the-day". Supersedes checkpoint 2026-06-16-2030 (intermediate "decision pending" snapshot).
---

# Session: The Day v0.3 — live Google Calendar + editable inbox

## What Annabel asked
1. "It doesn't seem to be actively pulling from my calendar."
2. "Delete my inbox and allow me to delete and add to that as well."
3. "What is the overall plan with this planner site?"
4. (later) Chose **true-live (Google API)** for sync; then **remove the "free time?" nudges**.

## Diagnosis
The calendar was a static JS array hard-coded into planner.html — it never talked
to the calendar and had already drifted (her real week had gained workouts the
bake never had). Today looked empty because Tue 6/16 genuinely was.

## Done & verified
1. **Data out of the HTML** → `data/calendar.json`; page fetches it; today/week
   compute from the system clock so "today" + the now-line are always correct.
2. **serve.py** (mirrors The Edit): `no-store` headers end the `?v=` stale-cache
   dance; write-locked `GET/POST /api/inbox` persists the Inbox to disk.
3. **Inbox**: seed removed (empty by default, KEY v0→v1); add via FAB + header `+`;
   delete via per-task `×`. Bug found & fixed: concurrent writes raced a fixed
   tmp filename and corrupted inbox.json → added a threading lock + resilient GET
   (stress-tested 10 parallel POSTs → stays valid JSON).
4. **TRUE-LIVE Google Calendar** (she chose this): needed ZERO Cloud Console work
   — she already had gcloud, a Desktop OAuth client at `~/.config/gws/client_secret.json`
   (project `aj-bot-489823`), and the Calendar API already enabled.
   - `auth_google.py` reused that client → `calendar.readonly` `token.json`
     (gitignored). One browser click to authorize.
   - `serve.py GET /api/calendar` pulls this week live (singleEvents, Denver-
     normalized via zoneinfo), caches 60s, writes the snapshot as a durable
     fallback, and serves the snapshot with `live:false` if the token/network is
     missing — so the page never breaks. Caption shows "Live · …" vs "Synced …".
   - Verified: 18 live events incl. "Uncle dave" (Wed 7:15pm) + "Take lanie to
     Kent!" (Thu) that post-dated the snapshot → proof it's genuinely live.
5. **Removed the "free time?" nudges** (JS + dead CSS) per her preference.

## Verify / gotchas
- Verified via preview DOM-eval + screenshots. Lesson: size the preview viewport
  (1280x820) BEFORE screenshotting or it renders a 1px sliver.
- Installed google-api-python-client/auth/oauthlib into anaconda python3.
- token.json + data/*.json are gitignored (personal). Project `.gitignore` added.
- The preview-managed server is session-bound and died twice on restart; run
  serve.py via the Desktop launcher for a stable daily process.
- Write-back will need a re-auth with a write scope (calendar.events).

## Overall plan (the arc)
v0 look/feel ✅ → live data ✅ → editable to-dos ✅ → AI "structure my day"
(next) → confirm→Google write-back → polish. Pairs with "The Edit" (shopping).
