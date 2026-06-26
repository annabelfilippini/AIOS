---
date: 2026-06-16
time: 11:20
project: tools / reddit-cli  +  websites / kite-wind-watch
status: SHIPPED — reddit-cli built+packaged; kite-wind-watch reads full Reddit comments and shows discovered spots. One optional follow-up open.
supersedes: 2026-06-16-1030-reddit-cli-authenticated-scraper-built.md
---

# Session: reddit-cli shipped + kite spot-discovery live

## What shipped
**reddit-cli** (`tools/reddit-cli/reddit-cli`, Python stdlib, read-only) — a
reusable authenticated Reddit scraper on the skool-pp-cli pattern. Reads Reddit
through Annabel's logged-in **browser-session cookie** (the only transport that
works: API app-creation is bugged; anon .json / Firecrawl scrape / headless
browser all blocked). Commands: `auth import/status`, `doctor`, `sync`, `find`
(FTS5), `export`, `stats`, `agent-context`. Secrets in `~/.config/reddit-cli/`,
SQLite mirror in `~/.local/share/reddit-cli/data.db` (both gitignored locations).
Hardened: transient 403/429 retry+backoff, one bad source can't abort a sync,
case-insensitive subreddit filters (Reddit normalizes `Wyoming`→`wyoming`).

**Packaging:** `cli-connections/reddit-cli/CONNECTION.md`,
`skills/reddit-intelligence-digest/SKILL.md`, `tools/reddit-cli/README.md`.

**kite-wind-watch:** `scraper/scrape_reddit.py` rewritten as a thin reddit-cli
orchestrator (sync kite/foil + geo subs → export → mine FULL comments with the
existing spot tagging + discovery extractor; `--no-sync` re-mines the mirror).
Dashboard `index.html` gained a "New spots people mention (not tracked yet)" row
rendering `discovered_spots`. Verified live (DOM + console clean).

## Result (147 threads / 3,671 comments mirrored)
- Known-spot ranking by real comment frequency: Lake Dillon 15×, McConaughy 10×,
  Aurora 5×, Boulder Reservoir 5×, Chatfield 3×, Rabbit Ears 3×.
- NEW spots discovered in comments: **Seminoe Reservoir (WY)**, Brainard Lake,
  Lost Lake, Swan Lake.
- Dad spots: Lake Hattie = chatter; Twin Buttes / Williams Fork = quiet.

## How to operate
- Refresh data: `cd projects/websites/kite-wind-watch && python3 scraper/scrape_reddit.py`
  (drops --no-sync to re-pull from Reddit). Cache-bust the preview with `?v=`.
- Cookie expires every few weeks → `reddit-cli doctor` flags it; re-capture with
  `pbpaste | reddit-cli auth import -` after a browser "Copy as cURL".
- launchd `com.kitewindwatch.scrape` still runs scrape_reddit.py; now needs a
  valid reddit-cli session, fails safe (keeps data) if the cookie is stale.

## Open / next (optional, needs Annabel)
- Promote the strongest discovered spots (Seminoe Reservoir, Brainard Lake, …) to
  **selectable dashboard spots**: needs OSM coords + her OK, exactly like Dad's
  spots. Until then they're detection candidates shown in the discovered row.
- Possible: dual-transport upgrade to official OAuth token if the API app ever
  creates; broaden subs/queries; tune discovery thresholds.

## Gotchas captured
- Reddit search default `t=year` hides 2+yr-old (evergreen) spot threads → use
  `--time all`. Preview window here scrolls inside a container + screenshots from
  top + viewport stuck at 1px until explicit width/height resize (preset path
  buggy) — verify via DOM eval, not just screenshot.
- My environment IP is Reddit-blocked; all reddit-cli runs happen via Bash on
  Annabel's Mac (her session/IP).
