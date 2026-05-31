---
name: site-scraper-cli-builder
description: Build or review a site-specific, read-only scraper CLI and matching AI-OS skill/CLI connection, modeled after skool-pp-cli, for sites Annabel can legitimately access. Use when creating reusable tools that mirror account/community/course/member/content data into a local searchable store with auth safety, doctor checks, agent-context, sync, search, digest, and citation workflows.
audience:
  - annie
  - business-partner
runtime:
  - codex
visibility: private
---

# Site Scraper CLI Builder

Use this skill when Annabel wants a reusable CLI-backed scraper for a specific
site, not a one-off script. The target shape is:

- a site-specific CLI binary under `tools/<site>-cli/`
- a canonical AI-OS CLI connection under `cli-connections/<site>-cli/`
- a task-facing skill under `skills/<site>-intelligence-*` or similar
- local-only storage for private scraped data, usually SQLite outside the repo

## First Pass

1. Confirm the site, account ownership/access rights, and the exact job:
   archive, search, digest, monitor, export, or lead/research workflow.
2. Inspect the site surfaces before coding: official API, web JSON routes,
   server-rendered HTML, browser-only routes, pagination, rate limits, media
   hosts, and bot-protection behavior.
3. Choose the least fragile transport that works:
   official API, authenticated HTTP, captured browser cURL/cookies, then
   Playwright only when the site requires browser rendering.
4. Start read-only. Do not add posting, liking, messaging, purchasing,
   account-setting, admin, or destructive commands unless Annabel explicitly
   approves that surface.
5. Use the Skool pattern reference for CLI architecture:
   `references/skool-pp-cli-pattern.md`.

## Minimum CLI Contract

Every durable scraper CLI should provide:

- `doctor --json --no-input --no-color` for auth, transport, freshness, and
  local-store health.
- `agent-context --pretty` with schema version, auth requirements, sensitive
  env vars, commands, flags, and read-only annotations.
- `auth status`, plus a safe auth setup path that stores secrets outside AI-OS.
- `sync` or `kb sync` with bounded options such as `--since`, `--max-pages`,
  `--limit`, and `--dry-run`.
- `find` or `search` over local data, with URLs/citations preserved.
- `stats` or `status` for local mirror freshness and row counts.
- `digest` or a site-specific synthesis command when recurring intelligence is
  the real use case.

Prefer `--agent` as a global shortcut for JSON, compact output, non-interactive
mode, no color, and yes-to-safe-defaults.

## AI-OS Wrapper Contract

For each finished scraper CLI, add:

- `cli-connections/<site>-cli/CONNECTION.md` with `safe_commands`,
  `approval_required`, auth/storage notes, and useful examples.
- `skills/<site>-.../SKILL.md` that explains when to use the CLI, bounded sync
  defaults, output principles, and private-data handling.

Keep private scraped content, cookies, JWTs, SQLite databases, exports, and
member/customer/person data out of git. Summaries and citations are fine; raw
private corpora live in the local store unless Annabel asks for a local export.

## Build Notes

- Use structured parsers for JSON, HTML, feeds, or media metadata.
- Persist raw source URLs and stable IDs before deriving summaries.
- Make syncs incremental and resumable where possible.
- Bound default scrapes. Make full archives opt-in.
- Add backoff/rate limiting and honor robots/terms constraints where relevant.
- Treat copied cURL files, browser cookies, and session headers as secrets.
- Validate with a narrow sync before broad archive commands.
