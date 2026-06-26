---
date: 2026-06-20
time: 14:10
project: day-planner ("The Day" — personal calendar + to-do tab)
status: shipped + verified (visual + DOM + live-restart). The center calendar gained GCal-style navigation: a WEEK | MONTH toggle plus ‹ Today › prev/next arrows in the header. WEEK = the existing focused day-timeline + week strip, but arrows now move week-to-week (was locked to the current week). MONTH = a 6-week grid with event chips (colored dot + time + title, "+N more" overflow, faded spill-over days, today marked in --love); click any day cell to drop back into WEEK view focused on that day. Verified at 1320x880 on the preview (8803) and the live agent (8802) restarted onto the new serve.py: week nav fetches the right range, month renders 42 cells / 24 days-with-events live, day-click drilldown lands on the correct selected day, only a harmless favicon 404 in console.
next-session: Feature is complete. Possible polish if she asks: (a) keyboard arrows for prev/next week/month; (b) a Day-only view (currently WEEK already shows a single focused day, so Day may be redundant); (c) month-cell event click could open the editor instead of only drilling to the day; (d) all-day events render as a chip in month cells but aren't visually distinct from timed ones — could add an all-day pill. Gmail live email STILL pending her one-time re-auth: `cd ~/Documents/AI-OS/projects/day-planner && python3 auth_google.py` (tick BOTH "make changes to events" AND "read your email"), then reload — she earlier ran it from ~ and hit "No such file" because the script lives in the project folder, not $HOME.
build: projects/day-planner/{planner.html, serve.py}.
  - serve.py: /api/calendar now accepts ?start=YYYY-MM-DD&end=YYYY-MM-DD (end exclusive); absent => current week (back-compat). Added _parse_day(). fetch_live_calendar(start=None,end=None). _cal_cache changed from a single slot to a dict keyed by range ("start|end" or "default"), cached 60s per range; durable data/calendar.json snapshot is written ONLY for the default current-week range. All three event-write cache invalidations changed from `_cal_cache["at"]=0.0` to `_cal_cache.clear()` (clear every range). do_GET passes self.path into _calendar(path).
  - planner.html: header markup gained .head-nav (prev/today/next) in grid col 1 and a .viewtog (Week|Month) in head-tools; added a <section class="month"> (month-dow + #monthGrid). CSS: .head-nav/.navbtn/.today-btn/.viewtog/.month/.mcell/.mev etc. JS: dynamic weekAnchor + monthAnchor (replacing the const WEEK fixed to today's Monday); weekDays(); currentRange(); loadCalendar() now requests the visible range with a client-side _calCache keyed by range (60s); renderMonth(); setView()/refreshView()/navGo()/navToday(); renderAll() branches on viewMode; reloadCalendar() -> renderAll(). Wired prevBtn/nextBtn/todayBtn + #viewTog buttons.
  - CRITICAL BUG found via screenshot (DOM property check missed it): setting .hidden on .week/.sheet/.month/.fab did NOT hide them — their explicit `display:grid/flex` author rules override the `hidden` attribute's UA `display:none`. In month view all three stacked together. Fix: global `[hidden]{display:none!important}` near the top of <style>. Lesson: verify hidden/shown via getComputedStyle(el).display, not el.hidden.
  - Live launchd agent com.annabel.theday restarted onto new serve.py: `launchctl bootout gui/$(id -u)/com.annabel.theday` then `launchctl bootstrap gui/$(id -u) ~/Library/LaunchAgents/com.annabel.theday.plist`. Probe /api/calendar?start=2026-06-01&end=2026-07-13 -> live:True, 56 events. Her real tab on 8802 serves the new UI (viewTog + hidden-fix confirmed in served HTML).
---

# Session: The Day — week navigation + month view (GCal-style)

## Ask
"I can't change to the next week. I'd like to see the next week and then the
month as well, exactly like GCal." (Also hit a `python3 auth_google.py` "No
such file" because she ran it from ~ instead of the project folder.)

## What shipped
- WEEK | MONTH toggle + ‹ Today › nav in the calendar header.
- Week nav moves week-to-week (keeps the same weekday selected) and refetches
  that week's range from Google.
- Month = 6-week grid, live events as colored chips with "+N more", faded
  spill-over days, today in love-red; click a day → WEEK view on that day.
- Backend range param on /api/calendar with per-range 60s cache.

## Verify
Preview 8803 (fresh server on new serve.py) + live 8802 (agent restarted):
week strip moves to 22–28 and fetches start=2026-06-22&end=2026-06-29; month
renders 42 cells, 24 with events, range start=2026-06-01&end=2026-07-13 live;
month prev/next swaps June↔July; day-cell click lands on selDay=18 with the
week strip back and Week toggle active. Caught + fixed the [hidden] override bug
via screenshot. Only console error = favicon 404.
