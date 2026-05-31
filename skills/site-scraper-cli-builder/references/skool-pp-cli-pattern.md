# skool-pp-cli Pattern

Use this reference when cloning the Skool CLI pattern for another site.

## What To Copy

The useful pattern is not "scrape Skool"; it is the agent-native local mirror:

- Cobra-style command tree with a consistent global flag layer.
- `--agent` mode that implies JSON, compact output, non-interactive behavior,
  no color, and confirmation-safe defaults.
- `doctor` as the first command an agent runs.
- `agent-context` as machine-readable runtime truth so agents do not rely on
  stale copied command lists.
- Local SQLite mirror with WAL, migrations, FTS search, sync cursors, and stats.
- Search/synthesis commands that preserve source URLs for citation.
- Clear separation between generic API commands and hand-written site-specific
  commands for pages, lessons, comments, media, members, or events.
- MCP/read-only annotations when commands may be exposed to agents.

## Source Map From Skool

In the Skool repo, these files show the pattern:

- `AGENTS.md`: tiny local operating contract for agents.
- `README.md`: human install/auth/sync guide.
- `SKILL.md`: agent skill wrapper with trigger cases and command recipes.
- `.printing-press.json`: generated CLI metadata and auth model.
- `spec.yaml`: base API/resource description.
- `internal/cli/root.go`: global flags, `--agent`, command registration.
- `internal/cli/agent_context.go`: structured command/auth discovery.
- `internal/cli/doctor.go`: config, auth, API, bot-wall, and cache checks.
- `internal/config/config.go`: auth/config/env-var loading.
- `internal/client/client.go`: HTTP, cache, retries, dry-run, rate limiting.
- `internal/store/store.go`: SQLite local store and migrations.
- `internal/cli/kb.go`: site-specific local knowledge-base commands.

## Command Shape Template

For most sites, start with:

```text
<site>-cli doctor --json --no-input --no-color
<site>-cli agent-context --pretty
<site>-cli auth status
<site>-cli sync <scope> --since 30d --max-pages 2 --agent
<site>-cli stats --json
<site>-cli find "<query>" --agent
<site>-cli digest --since 7d --json
```

Then add site-specific verbs only when they expose a real workflow:

- `classroom export`, `lesson transcript`, or `media captions` for learning
  platforms.
- `members list`, `profiles get`, or `directory search` for communities.
- `events sync/list` for calendars.
- `changes`, `watch`, or `tail` for monitoring.
- `resources extract` for links, templates, files, repositories, videos, or
  references embedded in posts/comments/pages.

## Auth And Safety

Prefer official auth if available. If a site only works through browser
sessions, keep that surface explicit:

- identify the sensitive env vars and config file path
- store secrets outside AI-OS, usually under `~/.config/<site>-cli/`
- support per-call env vars for agents
- never print raw cookies, JWTs, auth headers, or copied cURL content
- make `doctor` validate whether the session is usable for the actual private
  routes, not just a generic health endpoint

If bot protection or browser rendering is involved, document the transport:

- normal HTTP works
- authenticated HTTP with full cookie/header bundle works
- Playwright/system browser is required
- manual export is required

## Local Store

Use SQLite for durable, searchable private mirrors unless the site volume or
shape clearly demands something else.

Recommended tables:

- `sources` or site-native top-level entities
- `items` for posts/pages/lessons/resources
- `comments` or child records when conversation matters
- `refs` for extracted URLs and files
- `sync_state` for cursors and last sync timestamps
- FTS table over searchable text

Keep the database outside the repo, commonly:

```text
~/.local/share/<site>-cli/data.db
```

## AI-OS Packaging

After the CLI works, create the wrapper pair:

```text
cli-connections/<site>-cli/CONNECTION.md
skills/<site>-intelligence-digest/SKILL.md
```

The connection describes safe commands, approval-required commands, auth,
storage, and examples. The skill describes when to run sync/search/digest and
how to summarize results without leaking private corpora.
