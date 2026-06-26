---
date: 2026-06-17
time: 13:42
project: websites / kite-wind-watch
status: IN-PROGRESS — UX redesign at the "pick a direction" gate. Mascot removed, 3 directions mocked, references saved. Awaiting Annabel's A/B/C pick before editing index.html layout.
supersedes: 2026-06-16-1435-kite-wind-watch-session-state.md
---

# Session: kite-wind-watch — UX directions + mascot removed

Annabel resumed the kitesurfing app: wanted (1) an hourly wind-forecast loop,
(2) a better-looking UX. Then mid-session: save reference images, checkpoint,
and definitely remove the kitesurfer icon.

## Resolved this session

1. **Hourly wind loop = already shipped, left as-is (Annabel's call).** The push
   alerter (`scraper/wind_alert.py`) runs hourly via cron on the Hetzner VPS
   (`5 * * * *`, `root@5.78.218.220`). Verified live: it fired a real Telegram
   alert at 18:05 UTC today. Nothing rebuilt. She picked "leave it, it's working."

2. **Kitesurfer mascot REMOVED** from `index.html` (left-rail line-art SVG) and
   from the mockup, per her explicit request. App verified: console clean, rail
   now goes brand → Settings, looks cleaner. `design.md` Brand > Character marked
   REMOVED with a "do not re-add" note so a future session doesn't restore it.

3. **3 UX directions mocked for review** in `design-directions.html` (self-
   contained; copy on her Desktop as `kite-wind-watch-design-directions.html`,
   opened in her browser). All stay in the approved soft weather-app lane:
   - **A · Calm Rebalance** — current layout refined, map softened to the palette,
     answer card bigger under it, rail tightened. Lowest risk. **(my rec)**
   - **B · Answer First** — verdict + best-window become the top hero, map demoted
     to a strip.
   - **C · Ambient Map** — soft map as full-bleed pastel backdrop, answer floats on
     frosted glass.
   Shared core fix in all three: **restyle the loud default Google map to the
   pastel palette** (the single biggest eyesore today).

4. **Reference images saved** to `projects/websites/kite-wind-watch/references/`
   (Annabel pasted 3 weather apps she likes; recovered from the session transcript
   base64, converted to true PNG):
   - `01-globe-weather-layers-dark.png` — dark globe/map app, layer toggles
     (temp · wind · precipitation · air quality), bottom day strip, bottom tab bar.
   - `02-precip-temp-map-gauge.png` — orange precip/temp map, big circular gauge
     (hPa), "warmer than yesterday" plain-language summary, hourly precip bars.
   - `03-dark-dashboard-7day-globalmap.png` — dark 7-day forecast dashboard, global
     condition map, "chance of rain" chart, other-cities list, light/dark toggle.

5. **Declined CLAUDE.md self-improvement proposal** ("dont add").

## Open / Next

- **BLOCKER: Annabel to pick A / B / C** (or "A with C's map"). Only then edit the
  canonical `index.html` layout. Do NOT build a direction unprompted.
- The references are **inspiration only**. She said "dont add" — fold ideas in
  when building the chosen direction; do not add new features (dark-mode toggle,
  globe hero, layer menus, gauges, 7-day row) unless she asks.
- After she picks and the rebuild lands: **delete the Desktop mockup copy** so it
  can't be confused for the app (project canonical-file rule).

## Operate / gotchas

- Canonical file: ONE `index.html`, served at **localhost:8804**
  (`preview_start kite-wind-watch`). Never a file:// copy (Google Map needs the
  referrer-restricted origin).
- **Preview MCP only serves the app entry.** To preview a self-contained sibling
  page (like `design-directions.html`), render with headless Chrome to a PNG and
  read it: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  --headless=new --window-size=W,H --screenshot=/tmp/out.png file:///abs/path`.
  (Playwright MCP was locked by another session; preview navigation kept resetting
  to `/`.)
- Alerter unchanged and still on the VPS — see prior checkpoint
  `2026-06-16-1435-kite-wind-watch-session-state.md` for the full alerter/accuracy
  stack state (still accurate except the mascot + this UX work).
