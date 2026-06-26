---
name: reddit-cli
display_name: Reddit (authenticated read-only scraper + local mirror)
binary: tools/reddit-cli/reddit-cli
audience:
  - annie
  - business-partner
runtime:
  - claude
  - codex
visibility: private
related_skills:
  - reddit-intelligence-digest
safe_commands:
  - tools/reddit-cli/reddit-cli doctor --json
  - tools/reddit-cli/reddit-cli agent-context
  - tools/reddit-cli/reddit-cli auth status --json
  - tools/reddit-cli/reddit-cli sync -r "<sub,sub2>" -q "<query>" --limit 30 --time all --json
  - tools/reddit-cli/reddit-cli sync -r "<sub>" --listing top --time year --json
  - tools/reddit-cli/reddit-cli find "<query>" --json
  - tools/reddit-cli/reddit-cli find "<query>" -r "<sub>" --kind comment --json
  - tools/reddit-cli/reddit-cli export -r "<sub,sub2>" --json
  - tools/reddit-cli/reddit-cli stats --json
approval_required:
  - tools/reddit-cli/reddit-cli auth import   # writes the session cookie; the human captures + pipes it, not the agent
---

# Reddit CLI Connection

A reusable, **read-only** Reddit scraper in the `skool-pp-cli` mold. It mirrors
posts + full comment trees into a local SQLite store and searches them, so
agents can read Reddit discussions and cite them.

Use this connection when the task is: "what are people on Reddit actually saying
about X" — and you need the **comments**, not just titles.

## Why authenticated cookie (not the API)

Reddit blocks every cheaper path: anonymous `.json` → 403; Firecrawl refuses to
scrape threads; a headless browser → "blocked by network security"; and the
official API's app-creation form is currently bugged. The working transport is
**authenticated HTTP using Annabel's own logged-in browser session** (cookie),
which is the same pattern as `skool-pp-cli`. It is read-only and low-volume.

The session cookie lasts a few weeks. `doctor` flags staleness; re-capture with
`auth import` when it expires.

## What It Does

- `doctor` — validate session, cookie age, a live thread read, and the store.
- `agent-context` — machine-readable command/auth contract (read this first).
- `auth import` — store the session from a browser **Copy as cURL** (stdin or
  file). Human action: `pbpaste | reddit-cli auth import -`. Never printed/committed.
- `sync` — search (`-r sub -q query`) or pull a listing (`--listing top`) and
  store each thread's post + comment tree. Bounded: `--limit`, `--max-comments`,
  `--since`, `--time`, `--dry-run`. Default `--time all` (discussion is evergreen).
- `find` — FTS5 full-text search over posts + comments; returns citation URLs
  (comment hits link to the exact comment).
- `export` — dump posts + their comments as JSON (a stable contract for
  downstream processors, e.g. kite-wind-watch spot mining).
- `stats` — local mirror counts + per-sub freshness.

## Auth & Storage

- Session secret: `~/.config/reddit-cli/session.json` (chmod 600, **outside git**).
- Local mirror: `~/.local/share/reddit-cli/data.db` (SQLite WAL, **outside git**).
- Per-call env overrides for agents: `REDDIT_CLI_COOKIE`, `REDDIT_CLI_UA`.
- Treat the cookie/cURL as a secret: never echo it, never write it into the repo
  or a transcript. The `pbpaste | … auth import -` pipe keeps it local.

## Safety

Read-only by design — no posting, voting, messaging, or account changes. Respect
Reddit's load: the tool sleeps 1.5s between requests and retries transient
403/429 with backoff. Keep syncs bounded; full archives are opt-in via `--limit`.

## Examples

```
# one-time: capture the session (human runs this)
pbpaste | tools/reddit-cli/reddit-cli auth import -
tools/reddit-cli/reddit-cli doctor

# mirror Colorado/Wyoming kite chatter, then search the comments
tools/reddit-cli/reddit-cli sync -r Kiteboarding,wingfoil -q "Colorado OR Wyoming" --limit 30
tools/reddit-cli/reddit-cli find "reservoir" --kind comment --json
tools/reddit-cli/reddit-cli export -r Kiteboarding,wingfoil --json
```
