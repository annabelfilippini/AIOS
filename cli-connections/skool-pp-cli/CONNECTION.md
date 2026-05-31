---
name: skool-pp-cli
display_name: Skool Personal Knowledge Base CLI
binary: tools/skool-pp-cli/bin/skool-pp-cli
audience:
  - annie
  - business-partner
runtime:
  - codex
visibility: private
related_skills:
  - skool-intelligence-digest
safe_commands:
  - tools/skool-pp-cli/bin/skool-pp-cli --version
  - tools/skool-pp-cli/bin/skool-pp-cli doctor --json --no-input --no-color
  - tools/skool-pp-cli/bin/skool-pp-cli agent-context --pretty
  - tools/skool-pp-cli/bin/skool-pp-cli communities list --agent
  - tools/skool-pp-cli/bin/skool-pp-cli kb stats --json
  - tools/skool-pp-cli/bin/skool-pp-cli find "<query>" --prefer-recent 0.5 --agent
  - tools/skool-pp-cli/bin/skool-pp-cli guide "<topic>" --markdown
approval_required:
  - tools/skool-pp-cli/bin/skool-pp-cli auth set-token
  - tools/skool-pp-cli/bin/skool-pp-cli kb sync-all
  - tools/skool-pp-cli/bin/skool-pp-cli kb sync
  - tools/skool-pp-cli/bin/skool-pp-cli transcribe-refs
---

# Skool Personal Knowledge Base CLI Connection

Use this connection when Annabel wants to mirror her own Skool communities into
a local SQLite knowledge base for search, citations, guides, digests, and agent
queries.

## Safety Model

- The CLI is read-only against Skool, but authenticated sync can access private
  paid-community content.
- Use only Skool accounts Annabel owns or is legitimately logged into.
- Do not commit cookies, JWTs, SQLite exports, lesson text, member data, or
  private community content to AI-OS.
- Store auth only through the CLI config at `~/.config/skool-pp-cli/config.toml`
  or via a per-call `SKOOL_AUTH_TOKEN`, `SKOOL_COOKIE`, or `SKOOL_CURL_FILE`
  environment variable.
- Annabel's current browser cURL export is outside the repo at
  `/Users/annabelfilippini/Documents/skool/skool-curl.txt`. Prefer passing it
  as `SKOOL_CURL_FILE` so the CLI can preserve Skool's full browser cookie
  bundle for `www.skool.com` routes.
- The local mirror lives at `~/.local/share/skool-pp-cli/data.db` by default.
- Auth setup and full sync require explicit Annabel approval.

## Useful Commands

```bash
SKOOL_CURL_FILE=/Users/annabelfilippini/Documents/skool/skool-curl.txt tools/skool-pp-cli/bin/skool-pp-cli doctor --json --no-input --no-color
tools/skool-pp-cli/bin/skool-pp-cli auth set-token <skool-auth-token>
SKOOL_CURL_FILE=/Users/annabelfilippini/Documents/skool/skool-curl.txt tools/skool-pp-cli/bin/skool-pp-cli communities list --agent
SKOOL_CURL_FILE=/Users/annabelfilippini/Documents/skool/skool-curl.txt tools/skool-pp-cli/bin/skool-pp-cli kb sync-all --since 30d --captions --agent
tools/skool-pp-cli/bin/skool-pp-cli find "agentic os setup" --prefer-recent 0.5 --agent
tools/skool-pp-cli/bin/skool-pp-cli guide "how should I run my AI-OS tech stack" --markdown
tools/skool-pp-cli/bin/skool-pp-cli digest --since 7d --resources --json
```

For the first sync, prefer a narrow pass before a full archive:

```bash
SKOOL_CURL_FILE=/Users/annabelfilippini/Documents/skool/skool-curl.txt tools/skool-pp-cli/bin/skool-pp-cli kb sync-all --since 30d --max-posts-pages 2 --agent
```

For Annabel's current paid Skool intelligence targets:

```bash
tools/skool-pp-cli/bin/skool-pp-cli kb sync earlyaidopters --since 30d --max-posts-pages 2 --agent
tools/skool-pp-cli/bin/skool-pp-cli kb sync ainative --since 30d --max-posts-pages 2 --agent
tools/skool-pp-cli/bin/skool-pp-cli find "Claude Code AIOS" --prefer-recent 0.5 --agent
```

If `communities list` reports `self.id empty`, or `posts list <slug>` returns
an empty `currentGroup`, the token is still accepted by `/health` but the
browser session is stale for Skool's private web routes. Refresh the browser
session with a new Chrome "Copy as cURL" export, or run:

```bash
tools/skool-pp-cli/bin/skool-pp-cli auth refresh
```

## Local Patch

The AI-OS binary includes a local patch that lets Skool web-route scraping use a
full browser Cookie header from `SKOOL_COOKIE`, `SKOOL_CURL_FILE`, or config
headers. This is needed because Skool accepted `auth_token` alone on
`api2.skool.com/health` but redirected token-only `www.skool.com` requests to
`/login`.
