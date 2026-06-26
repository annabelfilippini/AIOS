# Kite Wind Watch Design Brief

## North Star

A personal, friendly wind dashboard Annabel can glance at to decide whether a
nearby Colorado (or driveable high-plains) kitesurf spot is worth watching over
the next few days. It should feel calm, light, and modern, like a good consumer
weather app, not a cinematic brand site and not a dense SaaS dashboard.

## Vibe Lane

Soft UI / tool dashboard (NOT the editorial/cinematic lanes). This is a personal
utility, so it intentionally departs from the global "sharp corners, full-bleed
photo hero" default. Reference feel: pale blue/lavender consumer weather apps
with one big number, rounded panels, soft shadows, compact metric cards, a left
rail, and a charming illustrated character.

## Brand

- Colors: pale cool-blue background (`#e9eef7`), white cards, **navy accent**
  (`#1c3d6e` → `#2f6bb0` gradient), sky blue secondary (`#5aa9f7`). (Accent was
  lavender/indigo `#7b6ef6` through 2026-06-14; Annabel asked for navy — reads
  more like water / kiting.)
- Wind condition scale (semantic): too light = blue-gray, marginal = blue,
  rideable = green (`#2fbf91`), strong = amber (`#f5a623`), nuking = coral
  (`#ef5a78`).
- Type: Inter / system sans. Big, friendly, sentence-case. No all-caps mono
  labels (that was the old editorial look).
- Shape: rounded corners (16–24px radius), soft shadows. Pills are fine here.
- Character: **REMOVED 2026-06-17 — Annabel disliked the kitesurfer icon. Deleted
  from `index.html` and the design-direction mockups. Do NOT re-add without her
  explicit go-ahead.** Former spec kept for history below:
  an original inline-SVG line-art kitesurfer, powered up and stoked,
  leaning back off the tail with the kite flying full overhead, one hand on the
  bar and the other thrown up in a shaka, board planing with spray. Single-weight
  strokes, charming, drawn from Annabel's reference photo of a grinning rider
  throwing a shaka. (Earlier version was a deadpan "waiting for wind" rider with a
  drooping kite and limp flag; Annabel asked to make him actually ride.) Inline
  SVG only, so the page stays self-contained.

## Asset Strategy

- NO external media. Do not pull video, posters, or photos from other projects
  (an earlier draft wrongly hotlinked Freeride Tarifa's hero video). The page is
  fully self-contained: inline SVG illustration + icons, inline CSS/JS.
- The only network calls are the live forecast APIs below.

## Page Architecture

Single page, deliberately stripped to answer one question: *when do I go?*

- **Region tabs (top of main):** a segmented control switches the spot universe
  between **Front Range wind** (Denver-area reservoirs) and **Colorado +
  Wyoming** (mountain/plains spots plus Dad's tips: Lake Hattie, Twin Buttes,
  Williams Fork). The CO+WY tab also reveals the **"What people are saying"**
  panel (see Data Rules). Spots carry an `area` field that drives the filter.
- **Left rail:** brand, the line-art kitesurfer mascot, and a compact settings
  form (spot, rideable-from threshold, daylight, refresh). No in-page nav.
- **Topbar:** spot name + region, live-source status pills, updated time.
- **Top row (the answer):** a wide card with the best-window headline (eyebrow
  "Best window · <day>", one big consensus number = the wind *during* the
  highlighted window, condition pill, and a sub-line "Go <window> · <dir> ·
  holds X–Y · gusts Z · rideable <extent>") sitting directly above the hourly
  wind chart. The chart shades the **peak window** (strongest sustained block,
  capped ~4 hrs) so the highlight points to specific hours, not the whole day,
  with the rideable-threshold line drawn across it. Beside it, a narrower
  **"Other days"** rail: one row per forecast day showing that day's best hours
  + window mean (or "no window" + peak). Click any day to swap the chart.
- **Bottom:** the **Sources** card — each model's mean / peak / rideable-hours
  for the selected day, blocked sources still shown. The model disagreement
  lives here, underneath the single consensus answer up top.

Cut from the earlier version (intentional, "less info at once"): the separate
hero number that didn't match the chart, model-agreement bars, the 5 highlight
tiles, the big spot watch-list grid, and the how-to-read notes.

### Forecast-clarity rule (why the headline changed)

The old hero showed an all-models, all-day **average** (e.g. 16 kt) sitting next
to a single model's hourly chart reading 18–24 — two different calculations,
unlabeled, which read as a contradiction. The number on screen must mean the
thing the chart shows. So: the chart is an **hourly consensus** (every live
model averaged per hour), and the big number is the mean of the highlighted
window on that same curve. Top of page = one agreed answer; bottom = the votes.

## Data Rules (forecast engine — preserve this)

- Show Windguru first (Annabel already has the scraper/catalog), then compare at
  least three more established models plus official agency data.
- Current forecast models: Windguru GFS, Open-Meteo Best Match, ECMWF IFS, NOAA
  GFS, DWD ICON, **NOAA HRRR** (3 km rapid-refresh, ~48h — the model US kiters
  rate highest for short-term), and NWS official hourly. 7 sources blended into
  the hour-by-hour consensus.
- **Live "now" layer (observations, not models):** the green pill under the spot
  name shows REAL current wind from the nearest reporting station. NWS station
  obs are free/keyless (walk the nearest ~5 stations until one reports — the
  closest, e.g. Copper Mtn near Dillon, is often blank). **Synoptic/MesoWest**
  adds a denser second reading when `config.js` has a `synopticToken` (free tier
  is education/research; else trial→paid) — skipped gracefully without one.
  iKitesurf/WeatherFlow are the kiter live-data favorites but paid + owner-gated,
  so not integrated.
- Keep failed/blocked sources visible and honest, never hidden.
- Treat the dashboard as a first screen only. Colorado inland wind is gusty;
  local launch rules, water level, and storm timing still need checking.
- **Spot chatter (CO+WY tab):** `scraper/scrape_reddit.py` searches Reddit via
  Firecrawl (Reddit now 403s direct unauthenticated `.json` access; Firecrawl
  *search* reaches it, though Firecrawl can't *scrape* individual threads — fine,
  the search snippets carry the spot names) and writes `data/discourse.js`. The
  panel shows Dad's-spots chatter/quiet status, a "spots people mention" chip row
  (new finds badged, clickable to jump to that forecast), and recent threads.
  Daily run is opt-in (launchd / cron / AI-OS routine; see `scraper/README.md`).
- Dad's spots (Lake Hattie, Twin Buttes, Williams Fork) have no Windguru id yet,
  so they run on the 5 non-Windguru sources; Windguru shows gracefully
  unavailable for them rather than erroring.

## Iteration Notes (running log, newest first)

### 2026-06-18 — Pins coloured by wind + dedup + Reddit precision (Claude)

Four asks from Annabel, all shipped in `index.html` (+ `scraper/scrape_reddit.py`):

- **Pins now coloured by current wind**, not by role. One batched Open-Meteo
  call (`current=wind_speed_10m`, knots) on map load colours every tracked pin
  by tier relative to the rideable threshold: `--light` too light → `--marg`
  building → `--good` rideable → `--strong` strong → `--nuke` too much. Colours
  re-tier live when the threshold changes (no refetch). Legend rewritten to the
  wind scale. `windColor()` / `fetchSpotsWindNow()` / `applyWindColors()` /
  `colorPinsByWind()`. `highlightSelectedMarker()` now just enlarges the
  selected pin (selection no longer steals the green).
- **Reddit-tip pins are now a hollow ring** (white fill, coloured outline) so
  they read as secondary to your solid tracked pins, still wind-coloured, and
  limited to important tips (2+ mentions, max 8).
- **"Two green things" fixed (station-aware dedup).** NWS + Synoptic often
  resolve to the SAME station (KFNL at Loveland) → was two identical pills.
  `dedupeStations()` collapses same-station readings into one, keeps the
  freshest, and labels it "NWS · Synoptic" so you see they *agree*. Genuinely
  different nearby stations (e.g. Aurora's K8KF vs AURC2) still show both.
- **"What people are saying" trimmed.** Only high-relevance threads that name a
  real spot, newest first (new `created` field from the scraper), capped at 5,
  and the list renders empty (no filler) when nothing qualifies. Annabel's call:
  "only spot-relevant threads."
- **Scraper is kitesurfing-only now.** Dropped the snowkiting / wingfoil /
  foiling / eFoil subs and search terms; `KITE_RX` requires a real kitesurf/
  kiteboard compound (bare "kite" was pulling toy-kite threads, a Red Rocks
  lineup, and a UFO post); `SNOW_TITLE_RX` drops snow/wing threads outright;
  removed the snowkite-only spots (Lizard Head, Rabbit Ears, Bighorns). Re-mined
  the existing mirror (`--no-sync`): panel went from snowkite/wingfoil noise to
  5 clean r/Kiteboarding spot threads.
- **Cache-bust fix.** `data/discourse.js` is a static `<script>` tag the browser
  cached, so fresh scrapes weren't showing. Added `loadDiscourse()` — fetches
  `data/discourse.json` with `cache:"no-store"` on init, script tag kept as a
  fast fallback.

Verified live on `localhost:8804` (eval + headless Chrome): 11/11 pins
wind-coloured, Loveland live-now collapsed to one pill, panel shows 5 clean
kiteboarding threads. NOTE: data was re-mined from a mirror synced under the OLD
broad terms — a fresh `scrape_reddit.py` sync (needs the reddit-cli cookie) will
give cleaner recall under the narrowed kitesurf-only search.

### 2026-06-18 — Map-first re-center: real Google satellite + floating panels (Claude)

- **Annabel's verdict on the prior map: she didn't like how the app looked and
  wanted it to "look more like a map."** She also clarified the two non-negotiable
  behaviours: clicking a pin must show the forecast **without leaving the app**, and
  she wants to see **the good hours and the rest of the week**. Note: those two
  asks are only possible with the Google Maps **JS API** (which the app uses), NOT
  an embedded My Map iframe — an iframe is a sealed box the app can't read clicks
  from. Recorded this so we don't re-litigate it.
- **Re-centered `index.html` into the map-first layout** (the approved
  `design-mockup.html` direction, now wired to the REAL Google map):
  - `#map` is full-bleed (`position:absolute; inset:0`); the app IS the map.
  - Map default switched **`terrain` → `hybrid`** (satellite + labels). That alone
    fixed most of the "doesn't look like a map" complaint.
  - Forecast moved into a **floating right panel** (`.spot-panel`, frosted/squared)
    that reuses every existing forecast id (spotName, chart, otherDays, sources,
    chatter) — so **zero forecast-logic changes**, layout/CSS only.
  - Left stack: serif **"The map."** wordmark + Settings + a "What the pins mean"
    legend. Editorial type added (Cormorant display, JetBrains mono figures).
  - Squared corners on the structural surfaces (panels, cards, fields, primary
    button) per the global standard; micro-pills/badges left rounded for now.
  - Google controls repositioned out from under the panels: map-type toggle
    TOP_CENTER, zoom LEFT_BOTTOM, fullscreen off. `fitBounds` padded
    (left 280 / right 400) so pins don't hide behind panels.
- **Pins are still colored by ROLE, not wind** (navy = tracked, green = selected,
  orange = Reddit-discovered). The mockup's wind-tier pin coloring + bottom day
  strip were NOT built — they'd need fetching every spot's current wind on load.
  Possible next step if she wants the map itself to show conditions at a glance.
- **Launch config added:** `.claude/launch.json` now has a `kite-wind-watch` entry
  (python http.server on **8804**, the referrer-restricted origin the Maps key
  needs). `preview_start kite-wind-watch` was silently reusing the apartment-hunt
  config on 8753, where the map can't load.
- **Verify note (important):** the preview-MCP screenshotter renders full-viewport
  `position:fixed` layouts tiny in the top-left corner (looks broken, isn't).
  Confirm sizes with `preview_eval` and capture the real visual with headless
  Chrome against the live origin:
  `"…/Google Chrome" --headless=new --window-size=1440,900 --screenshot=/tmp/x.png --virtual-time-budget=6000 http://localhost:8804/index.html`.
- **Side artifact (not in the app):** built `~/Downloads/kite-spots.kml` (all 11
  spots, blue = tracked / green = Dad's tips, each with a Windguru/Windy forecast
  link) for Annabel to import into her personal Google **My Maps** and drag/add
  pins herself. Separate from the app map; if she corrects coords there she can
  export KML back and we sync `SPOTS`.

### 2026-06-17 — Kitesurfer mascot removed + 3 UX directions explored (Claude)

- **Mascot deleted** from `index.html` (the left-rail line-art kitesurfer SVG) at
  Annabel's request. Rail now goes brand → Settings directly; verified live
  (console clean, layout intact, looks cleaner). `.mascot` CSS left in place but
  unused. See Brand > Character note above: do not re-add without her go-ahead.
- **UX redesign not yet built** — Annabel wants to see options first. Built
  `design-directions.html` (self-contained mockup, also on her Desktop) showing 3
  takes, all inside the approved soft weather-app lane: **A · Calm Rebalance**
  (refine current, map softened to palette, lowest risk), **B · Answer First**
  (verdict/best-window hero, map demoted), **C · Ambient Map** (soft map as
  full-bleed backdrop, answer on frosted glass). The shared core fix across all
  three: **restyle the loud default Google map to the pastel palette.**
  Recommendation given: A, optionally borrowing C's soft-map backdrop. **Awaiting
  Annabel's pick (A / B / C) before touching `index.html` layout.**
- **Hourly wind loop confirmed already shipped** (VPS cron fired a real Telegram
  alert today). Annabel's call: leave as-is, nothing to add.
- **New references saved** to `references/` (3 weather apps Annabel likes): a dark
  globe/map app with temp·wind·precip·air-quality layer toggles + bottom day strip
  (`01`), an orange precip/temp map app with a big gauge + "warmer than yesterday"
  summary (`02`), and a dark 7-day dashboard with a global condition map (`03`).
  Inspiration only — fold in when building the chosen direction, do NOT add
  features unprompted.
- Build/verify note: the preview MCP only serves the app entry (`index.html`); to
  preview a self-contained sibling page, render it with headless Chrome to a PNG
  (`Google Chrome --headless=new --screenshot=... file://...`) and read that.

### 2026-06-16 — Hourly alerter upgraded to match the dashboard (Claude)

- `scraper/wind_alert.py` now (1) blends **Best Match + HRRR + GFS** for the 48h
  gust forecast (averaged per hour) instead of one model, and (2) pulls **live
  station readings** (Synoptic if `config.js` has a token, else NWS, walking the
  nearest ~5 stations). Synoptic token is read straight from `config.js` by regex
  — single source of truth, no duplication.
- New **"🟢 BLOWING NOW"** trigger: alerts when a spot is *currently* ≥18kn
  (daylight only), not just forecast. Every alert line now includes the real
  current reading. Dedup: forecast = once per spot per windy day (re-ping if peak
  climbs 3kn); live-now = once per spot per day.
- Verified live: Lake Hattie/Twin Buttes (27kn now), Lake Dillon (24kn now) all
  flagged BLOWING NOW; Telegram + macOS delivered. Closes the "alerter less
  accurate than dashboard" seam.
- STILL OPEN: kept map spots (browser localStorage) are not in the Python SPOTS
  list, so a newly kept spot doesn't auto-feed alerts — needs a shared spots
  source both sides read.

### 2026-06-16 — Accuracy stack: HRRR + live station observations (Claude)

- Researched what kiters trust (web indexes r/Kiteboarding better than the
  reddit-cli mirror, which is spot-discovery-focused). Verdict: **Windy** (for its
  HRRR+ECMWF+GFS compare), **Windguru**, and **iKitesurf** for live readings.
- Gap found + fixed: we lacked **HRRR**, the high-res US short-term model. Added
  via Open-Meteo (`models=ncep_hrrr_conus` on the gfs endpoint), free. Now 7
  models in the consensus.
- Added a **live observation layer** (the "is it windy RIGHT NOW" answer):
  green pill under the spot name from the nearest real station. NWS obs are
  free/keyless; iterate nearest ~5 stations (closest is often non-reporting).
  Synoptic/MesoWest wired as an optional 2nd pill behind `config.synopticToken`.
- Verified: Aurora→KBKF, Lake Dillon→KLXV (fell through blank KCCU). No errors.
- iKitesurf/WeatherFlow: documented as paid/owner-gated, not built.

### 2026-06-16 — Google Map became the hero; pins drive everything (Claude)

- Annabel's call: the map is now the **main component**. Navy pins = tracked
  spots (click → that spot's forecast loads in the panel below); a **green** pin
  marks the current selection; **yellow** pins = spots Reddit mentioned that
  aren't tracked yet. The Front Range / CO+WY **tabs were retired** — geography
  replaces them, and the spot menu now lists every spot.
- Yellow-pin flow: click → InfoWindow with the Reddit quote + **"Add to my
  spots"** (promote to permanent navy pin, persisted in `localStorage`) or "Just
  preview the forecast" (temporary). The map makes the geocode-trust problem
  visible — e.g. Brainard/Lost/Swan all came from *snowshoeing* chatter and
  obviously aren't kite spots, so you just don't add them.
- **Engine:** real Google Maps JS API (her choice over free Leaflet). Key lives
  in gitignored `config.js` (`window.KWW_CONFIG.googleMapsKey`); `config.example.js`
  is the committed template. Must keep the key HTTP-referrer-restricted to
  `localhost:8804/*` (+ any deploy domain) — it's visible in client HTML.
  Classic `google.maps.Marker` (no mapId needed) with SVG data-URI pins.
- Discovered spots are geocoded **client-side via keyless Nominatim/OSM** (cached
  in `localStorage`), biased with `region_guess`, so we don't force a second
  Google API (Geocoding) on her account.
- **Known seam:** "kept" spots persist to the browser only. The hourly
  `wind_alert.py` has its OWN hardcoded SPOTS list, so kept spots do NOT yet feed
  the Telegram/macOS alerts. Bridging needs a shared spots source both read.
- Map quirk: tiles grey out if the container resizes after load → added a window
  `resize` → `google.maps.event.trigger(map,'resize')` listener. Verify map via
  DOM eval, screenshot only after an explicit viewport resize (preview 1px bug).

### 2026-06-16 — Hourly wind alerter (push, not just pull) (Claude)

- Annabel wanted to "stay up to date on very windy places" via an hourly refresh.
  Clarified the data model: the dashboard already pulls **live** forecasts
  in-browser on every load, so nothing there is stale; the Reddit job is evergreen
  chatter (daily is correct, hourly risks the cookie). The real need was a **push
  alert**, not a faster refresh.
- Built `scraper/wind_alert.py` (stdlib, read-only): hourly Open-Meteo check of all
  11 spots; alerts when **gusts ≥ 18kn within 48h** during daylight (6–21 local).
  De-dupes per spot per windy-day (re-ping only if peak rises ≥3kn) via
  `~/.local/share/kite-wind-watch/alert_state.json`. Thresholds are constants at
  the top of the file. Scheduled: `com.kitewindwatch.windalert` launchd, hourly :05.
- Two channels: **macOS notification** (live, no creds; osascript needs ASCII —
  emoji broke it) and **Telegram** (chat 8519804405) which is blocked on a stale
  401 token in `~/.claude/channels/telegram/.env` — refresh via `/telegram:configure`.

### 2026-06-16 — Full comment reading via reddit-cli + discovered-spots row (Claude)

- The official Reddit API path (scraper v2) was dead on arrival: Reddit's
  app-creation form is bugged (silent CAPTCHA 403/429), and anonymous .json,
  Firecrawl scrape, and a headless browser are all blocked. Built a reusable
  **`reddit-cli`** (tools/reddit-cli, skool-pp-cli pattern) that reads Reddit
  through Annabel's **authenticated browser-session cookie** — the one transport
  that works. Read-only; cookie re-captured every few weeks.
- **scrape_reddit.py rewritten** as a thin orchestrator: `reddit-cli sync` across
  the kite/foil subs (searching the region) + regional subs (searching the sport),
  then `reddit-cli export` → mine the FULL comment text with the existing
  spot tagging + discovery extractor. `--no-sync` re-mines the mirror without
  hitting Reddit.
- **Result over 147 threads / 3,671 comments:** known-spot ranking now reflects
  real comment frequency (Lake Dillon 15×, McConaughy 10×, Aurora 5×, Boulder
  Reservoir 5×, Rabbit Ears 3×) and the discovery extractor surfaced new spots
  from comments: **Seminoe Reservoir (WY)**, Brainard Lake, Lost Lake, Swan Lake.
- **Dashboard:** added a "New spots people mention (not tracked yet)" row to the
  chatter panel rendering `discovered_spots` as dashed candidate chips with
  region + mention count + a quote tooltip. Verified live (DOM + console clean);
  the chatter-tag now reads "Reddit (full threads via reddit-cli)".
- **Daily job note:** launchd still runs `scrape_reddit.py`, which now drives
  reddit-cli. If the session cookie has expired it fails safe (keeps existing
  data) and Annabel re-runs `reddit-cli auth import`.
- **Open / next:** promote the strongest discovered spots (Seminoe, Brainard, …)
  to selectable dashboard spots — needs OSM coords + Annabel's OK, exactly like
  Dad's spots got. These are detection candidates until then.

### 2026-06-15 — Scraper v2: foiling + full-thread reading + spot discovery (Claude)

- Annabel asked to (1) add **foiling** (wing/kite/hydrofoil), (2) actually
  **thread-scrape full Reddit threads** (not just search snippets) — using a
  different tool if Firecrawl can't, and (3) **expand discovery** to find *every*
  good kite spot in the CO/WY region, not just her dad's spots or the ones she
  named.
- **Tool reality re-verified:** Firecrawl *scrape* still refuses Reddit threads
  ("we do not support this site"); Firecrawl *search* still works (snippets
  only). To read full threads + comments we use **Reddit's official OAuth API**
  (app-only `client_credentials` token, read-only, no Reddit password). Pending
  Annabel registering a "script" app and pasting `REDDIT_CLIENT_ID` /
  `REDDIT_CLIENT_SECRET` into the gitignored `.env`.
- **Scraper rebuilt as two layers, degrades gracefully:** (1) Firecrawl search =
  broadened, foiling-inclusive discovery (works now, improves the daily job
  immediately); (2) Reddit API = fetch each candidate thread's post **+ all
  comments** and mine them. If Reddit creds are absent it runs discovery-only and
  does **not** break the daily launchd job.
- **Foiling:** `KITE_RX` now matches wing/kite/hydro-foil + winging + efoil;
  added subreddits **r/wingfoil, r/foiling, r/eFoil**; foiling-specific queries.
  First broadened scan immediately surfaced the wingfoil crowd + spots the kite
  threads never mention.
- **Spot discovery extractor (new):** pulls *unknown* "X Lake / X Reservoir /
  X Pass" names out of the text, drops known spots + sentence-fragment artifacts
  + out-of-region (Colorado-*River* AZ/NV spots flagged "far"), ranks by distinct
  threads → `discovered_spots[]` in `discourse.json`. Real harvest comes once
  comments are readable; snippet-only mode is intentionally sparse.
- **New spots already added to tracking** from the broadened scans: Big Soda
  Lake (Lakewood), Boulder Reservoir, Horsetooth Reservoir, Carter Lake, Lizard
  Head Pass + Rabbit Ears Pass (snowkite), The Bighorns (WY snowkite). These are
  detection entries, not yet dashboard-selectable spots (need coords + Annabel's
  OK before they become live, like Dad's spots did).
- **Validated** in discovery-only mode end-to-end (24 posts, clean
  `discovered_spots`). Depth layer written but untested until creds land. Dashboard
  renderer for `discovered_spots` is the next batch, designed against real API
  output.

### 2026-06-14 — Navy recolor + region tabs + Reddit spot-chatter scraper (Claude)

- Annabel asked to (1) recolor the accent from purple/lavender to **navy**
  (water/kiting feel), (2) add a daily **Reddit scraper** for CO/WY kite-spot
  chatter, (3) split the dashboard into a **second tab** to rotate between
  Denver-area wind and Colorado/Wyoming spots/wind, and (4) add the spots her dad
  flagged (Lake Hattie, Twin Buttes, Williams Fork).
- **Recolor:** renamed `--lav*` CSS vars to `--navy*` (`#1c3d6e` / `#2f6bb0`),
  cooled the background + shadows, navy chart line/fill, navy favicon. No purple
  left (grep-verified).
- **Tabs:** a segmented control filters the spot dropdown by `area`
  (`front-range` vs `co-wy`); the CO+WY tab also shows the chatter panel. Gotcha
  fixed: `.chatter { display:grid }` overrode the `[hidden]` attribute, so the
  panel leaked onto the Front Range tab until I added
  `.chatter[hidden]{display:none}`.
- **Scraper:** Reddit 403s all unauthenticated `.json` now, so it goes through
  **Firecrawl search** (already configured, no new creds). Search-only. Seeded
  `data/discourse.js` from a live scan: confirmed Lake Hattie ("windy but
  gusty"), found Twin Buttes / Williams Fork quiet, surfaced two spots not on the
  list (Sloan Lake, Georgetown Lake).
- **Dad's spots:** added with OSM-verified coords, no Windguru id (5 sources
  carry the consensus). Verified live: both tabs, desktop + mobile, console
  clean, no horizontal overflow.

### 2026-06-14 — Mascot now rides + throws a shaka (Claude)

- Annabel shared a reference photo (grinning rider, leaning back, one hand on the
  bar, shaka with the other) and asked the mascot to actually be kiting, not
  waiting. Redrew the inline SVG: powered-up kite overhead, taut lines to the bar,
  rider leaning back off the tail, raised shaka hand, helmet + open grin, board
  planing with spray and a waterline. Dropped the limp "no wind" flag and
  stillness dots. Bumped sidebar render to 150px. Verified at sidebar size and
  enlarged; reads clearly, console clean.

### 2026-06-14 — Best-window focus + clarity fix (Claude)

- Annabel's feedback: the hero "16 kt" was confusing next to an hourly chart
  reading 18–24, and the page had too much at once. For kitesurfing she wants
  the *best hours to go* up top, the best hours for other days on the side, and
  sources at the bottom, nothing else.
- Rebuilt the layout around that: answer card (best-window headline + hourly
  chart with the peak window shaded) | "Other days" rail | Sources at bottom.
  Removed the standalone hero, model-agreement bars, highlight tiles, spot grid,
  and notes.
- Fixed the confusion at the source: the chart is now an hourly **consensus**
  (all live models averaged per hour) and the big number is the mean of the
  highlighted window on that curve, so they always agree. Per-model spread moved
  to the bottom Sources card.
- The highlight is the **peak sustained block** (capped ~4 hrs), not every hour
  over threshold, so on all-day-windy days it still points to specific hours
  ("Go 2–6pm") while the sub-line notes the full rideable extent.
- Verified live in browser (6 sources, console clean): desktop balanced two-up
  layout, day-switching swaps chart + headline + sources, mobile stacks with no
  overflow. Default forecast window widened to 7 days for a full week in the rail.

### 2026-06-14 — Soft weather-app redesign (Claude)

- Completely rebuilt the UI in the soft light weather-app direction Annabel
  liked better than the first cinematic draft. Pale lavender, rounded white
  cards, left rail, one big consensus wind number, model-agreement bars, soft
  highlight tiles, an SVG area chart for hourly wind, and rounded 5-day outlook
  cards with the best day highlighted.
- Added the funny line-art kitesurfer (geared up, kite drooping, flag limp).
- Removed the hotlinked Freeride Tarifa hero video + poster entirely. Page is now
  self-contained.
- Preserved the working forecast engine byte-for-byte (Windguru + Open-Meteo
  models + NWS, consensus ranking, hourly timeline). Verified in browser desktop
  + mobile: 6 sources live, 0 blocked, console clean.

### 2026-06-14 — First prototype (Codex, superseded)

- First static prototype used the global cinematic/editorial direction and
  borrowed Freeride media. Annabel rejected the look and shared soft weather-app
  references instead. Superseded by the redesign above.
