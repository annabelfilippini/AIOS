# reddit-cli

A small, **read-only** Reddit scraper that reads full threads (post + every
comment) into a local SQLite mirror you can search. Built in the `skool-pp-cli`
mold (see `skills/site-scraper-cli-builder`).

Python 3, standard library only. No `pip install`.

## Why it exists / how it reads Reddit

Reddit now blocks every cheap path: anonymous `.json` returns 403, Firecrawl
won't scrape threads, a headless browser gets "blocked by network security," and
the official API's app-creation form is currently bugged. So this tool uses the
one path that works: **your own logged-in browser session** (an authenticated
cookie), exactly like `skool-pp-cli`. Read-only, low-volume, polite.

The session cookie lasts a few weeks. When it expires, re-capture it (below).

## One-time setup: capture your session

1. Log into Reddit in your browser.
2. Open DevTools (right-click the page → **Inspect**) → **Network** tab → reload.
3. Click the top `www.reddit.com` row → right-click → **Copy → Copy as cURL**.
4. Pipe it straight in (keeps the cookie on your machine, never in a chat):

   ```bash
   pbpaste | python3 ~/Documents/AI-OS/tools/reddit-cli/reddit-cli auth import -
   ```

5. Validate:

   ```bash
   python3 ~/Documents/AI-OS/tools/reddit-cli/reddit-cli doctor
   ```

   `live_read: ok` means it can read full threads.

The cookie is stored in `~/.config/reddit-cli/session.json` (chmod 600, outside
git) and never printed.

## Commands

```bash
reddit-cli doctor              # validate session / cookie age / live read / store
reddit-cli agent-context       # machine-readable contract (commands, auth)
reddit-cli auth import [-|file] # store cookie from a Copy-as-cURL
reddit-cli auth status         # show session freshness

# mirror threads + comments into the local store
reddit-cli sync -r Kiteboarding,wingfoil -q "Colorado OR Wyoming" --limit 30
reddit-cli sync -r Colorado --listing top --time year      # listing instead of search

reddit-cli find "reservoir"                 # full-text search posts + comments
reddit-cli find "wingfoil" -r Kiteboarding --kind comment
reddit-cli export -r Kiteboarding --json    # dump posts+comments JSON for processing
reddit-cli stats                            # mirror counts + freshness
```

Global flags (work before or after the subcommand): `--agent` (JSON, compact,
non-interactive), `--json`, `--no-color`, `--no-input`.

### Useful `sync` flags

- `--limit N` — max threads per source (default 50).
- `--max-comments N` — cap comments fetched per thread (default 200).
- `--time all|year|month|week|day` — search/listing window (default **all**;
  discussion is evergreen, narrow it for monitoring).
- `--since 30d|6m|1y` — only store threads newer than this.
- `--no-comments` — store post records only (fast discovery).
- `--dry-run` — show what would be fetched, write nothing.

## Storage

- Session: `~/.config/reddit-cli/session.json` (secret, chmod 600)
- Mirror: `~/.local/share/reddit-cli/data.db` (SQLite WAL: items, comments,
  sources, sync_state, FTS5)

Both live outside the repo. Don't commit them.

## Notes

- Read-only: no posting, voting, messaging, or account changes.
- Sleeps 1.5s between requests; retries transient 403/429 with backoff.
- Dual-transport ready: if you ever get official API creds, the auth layer can
  be pointed at an OAuth token instead of the cookie.
- Reddit normalizes some sub names (e.g. `Wyoming` → `wyoming`); `find`/`export`
  match subreddits case-insensitively.
