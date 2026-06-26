# Reddit spot-chatter scraper

Feeds the dashboard's **Colorado + Wyoming → "What people are saying"** panel.
Searches Reddit for people talking about CO/WY kite + snowkite spots and writes
`../data/discourse.json` and `../data/discourse.js`.

## Why Firecrawl (not Reddit directly)

As of 2026 Reddit returns **403 to all unauthenticated** requests to its `.json`
endpoints (both `www.reddit.com` and `old.reddit.com`). Firecrawl's *search*
endpoint reaches reddit.com fine, so we go through it. Note Firecrawl cannot
*scrape* individual Reddit threads ("site not supported"), so this is
**search-only** — but the search snippets already carry the spot names people
mention, which is the whole point.

## One-time setup

1. `cp .env.example .env` (in the project root, one level up from here).
2. Paste your Firecrawl key into `.env` as `FIRECRAWL_API_KEY=fc-...`.
   You already have one for the Firecrawl MCP — copy that value from
   `~/.claude.json` (or `~/.codex/config.toml`).

## Run it

```bash
cd ~/Documents/AI-OS/projects/websites/kite-wind-watch
python3 scraper/scrape_reddit.py
```

Standard library only, no `pip install`. Reload the dashboard to see the update.

## Make it daily — three options

- **AI-OS routine (recommended, no key handling):** schedule a daily Claude run
  that does the searches via the Firecrawl **MCP** and rewrites
  `data/discourse.js`. Ask Annie/Claude to "schedule the kite discourse scrape
  daily" — uses the already-authed MCP, nothing to copy.
- **launchd (macOS native, survives reboots):** a `~/Library/LaunchAgents`
  plist running this script every morning. Needs the `.env` key.
- **cron:** `0 7 * * * cd <project> && /usr/bin/python3 scraper/scrape_reddit.py`

## Tuning

- Spots tracked + their regex live in `SPOT_META` in `scrape_reddit.py`.
- Search phrasing lives in `QUERIES`. Keep queries simple — nested `OR`/quoted
  queries can return empty from the search API.
- Your dad's spots (Lake Hattie, Twin Buttes, Williams Fork) get an explicit
  "chatter vs quiet" status block so you can see if anyone's talking about them.
