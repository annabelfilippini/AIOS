---
date: 2026-06-16
time: 10:30
project: tools / reddit-cli  (+ websites / kite-wind-watch)
status: in-progress — reddit-cli core BUILT + validated live (auth + sync + find + stats). Batch 3 remaining: wire kite-wind-watch to it, then AI-OS packaging + docs.
supersedes: 2026-06-15-1600-kite-wind-watch-scraper-v2-foiling-thread-depth.md
---

# Session: reddit-cli — authenticated Reddit scraper CLI (skool-pp-cli pattern)

## Why this exists
Annabel wanted full Reddit **comment** reading for kite-wind-watch spot discovery,
and a durable reusable Reddit scraper for future projects. We exhausted every
other path:
- Reddit 403s anonymous `.json` (verified prior session).
- Firecrawl **scrape** refuses Reddit ("we do not support this site"). Firecrawl
  **search** works but snippets only.
- Headless browser (Playwright) → Reddit **"blocked by network security."**
- Official Reddit API needs an app, but the app-creation CAPTCHA is currently a
  **known Reddit bug** (silent reload / 429 loop). Annabel tried two accounts
  (incl. annabelflip1@gmail.com), no luck.

## Decision (locked)
Build `reddit-cli` per the **site-scraper-cli-builder** skill, transport =
**authenticated session cookie** (the skool-pp-cli pattern). Reddit only blocks
anonymous/datacenter/headless; her logged-in residential session reads full
threads fine. Annabel approved; she's OK with cookies expiring every few weeks.
**Dual-transport by design:** can upgrade to official OAuth token if she ever
gets app creds. Read-only.

## Built + VALIDATED LIVE (runs on her Mac, her IP, her session)
`tools/reddit-cli/reddit-cli` (Python 3, stdlib only, executable). Architecture
follows skool-pp-cli; language is Python (not Go) for fast iteration — flagged to
Annabel, Go parity optional later.

- **auth**: `auth import` parses a browser "Copy as cURL" (or raw cookie string),
  stores cookie + UA in `~/.config/reddit-cli/session.json` (chmod 600, never
  printed, gitignored location). Env overrides: REDDIT_CLI_COOKIE / REDDIT_CLI_UA.
  Annabel imported her cookie via `pbpaste | reddit-cli auth import -`.
- **doctor**: ALL GREEN — live_read "read 'Kiting near Boulder/Denver CO'
  (12 comments, 6 fetched)". Confirms authenticated transport works.
- **sync**: search (`-r sub -q query`) or listing (`--listing top`), fetches
  post + full comment tree, stores to SQLite. Bounded (`--limit`, `--max-comments`,
  `--since`, `--dry-run`). Politeness sleep 1.5s. **Default `--time all`** (spots
  are evergreen; `year` silently hid the old threads — gotcha found + fixed).
  Tested: 5 posts + 80 comments, 0 failed.
- **find**: FTS5 full-text over posts+comments, snippet() highlights, citation
  URLs (comment hits link to the exact comment permalink). Falls back to LIKE if
  no FTS5. Tested: "mcconaughy" → real post+comment hits.
- **stats**, **agent-context**, **version**. Global flags work before/after the
  subcommand (parent-parser + SUPPRESS fix).
- Store: `~/.local/share/reddit-cli/data.db` (SQLite WAL; items/comments/sources/
  sync_state + search_fts). Outside the repo.

## Batch 3 — REMAINING
1. **Wire kite-wind-watch to reddit-cli (the original payoff):** have
   `projects/websites/kite-wind-watch/scraper/scrape_reddit.py` drive
   `reddit-cli sync` across kite/foil/geo subs, then read the mirror (DB or a new
   `reddit-cli export --json`) and run the existing spot tagging + discovery
   extractor over the FULL comment text → real `discovered_spots` → dashboard.
   Decide sync breadth (which subs, --limit) — recommend: SPORT_SUBS + GEO_SUBS,
   ~30/sub, --time all, first run.
2. **AI-OS packaging:** `cli-connections/reddit-cli/CONNECTION.md` (safe_commands,
   approval_required=none since read-only, auth/storage notes, examples) and
   `skills/reddit-intelligence-digest/SKILL.md` (when to sync/find, bounded
   defaults, private-data handling). Plus a `tools/reddit-cli/README.md`.
3. Consider a generic `reddit-cli export` (JSON dump of posts+comments) so other
   projects consume it without touching the DB schema.

## Notes / gotchas
- Reddit search `t=year` excludes 2+yr-old threads — default to `all` for discovery.
- `--no-comments` stores search records only (fast); default fetches full trees.
- Cookie in chat: Annabel pasted her full cURL once; advised future use of the
  `pbpaste |` pipe so the secret stays local. Tokens expire on their own.
- My environment IP is Reddit-blocked; ALL reddit-cli testing must run via Bash on
  her Mac (which it does — that's her session/IP).
