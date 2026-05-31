# 2026-05-21 17:01 - Global AI-OS Cleanup And Skill Unification

## Summary

Cleaned the global Claude/Codex/AI-OS system so it is a better starting point
for a new memory system.

## What Changed

- Removed literal Firecrawl/Stitch credential values from `~/.codex/config.toml`.
- Added `~/.codex/bin/firecrawl-mcp`, which expects `FIRECRAWL_API_KEY` from
  the shell or secret manager instead of storing the key in config.
- Updated stale `~/Documents/Claude` hooks in `~/.claude/hooks` and
  `~/.codex/hooks` to use AI-OS / `knowledge/` paths.
- Cleaned missing project pointers from `~/.claude.json`.
- Restored AI-OS markdown lint config at `.markdownlint-cli2.jsonc`.
- Added `operations/compound-engineering/lint-aios-system.sh`.
- Created Codex automation `weekly-ai-os-system-lint`, Mondays at 09:00.
- Restored compatibility symlink `wiki -> knowledge`.
- Removed stale Obsidian conflict note after verifying no Git unmerged files.
- Added `wiki-cache/` to `projects/annie-intake/.gitignore`.
- Made `CLAUDE.md` a concise Claude/Garry router, similar to `agents/agent.md`.
- Materialized top-level `skills/` as the global skill catalog instead of
  symlinks back into agent-owned skill folders.
- Pointed both runtimes at top-level global skills:
  - `~/.claude/skills/* -> ~/Documents/AI-OS/skills/*`
  - `~/.codex/skills/* -> ~/Documents/AI-OS/skills/*`
- Updated docs so `agents/shared/` is for handoffs, QA, templates, and
  cross-agent paper trails, not skills.
- Updated legacy `agents/*/skills/README.md` files to say those folders are no
  longer source of truth.

## Verification

Ran:

```bash
operations/compound-engineering/lint-aios-system.sh
```

Result: passed.

Checks included:

- Markdown lint
- Git whitespace check
- Runtime skill drift
- Stale Claude path check
- Runtime credential-shape check

Also verified Claude/Codex JSON and Codex TOML configs parse cleanly.

## Current System Model

- `~/AGENTS.md` - global Codex preferences.
- `~/.claude` - Claude runtime adapter only.
- `~/.codex` - Codex runtime adapter only.
- `~/Documents/AI-OS` - canonical source of truth.
- `AI-OS/skills` - global skill catalog usable by both Claude and Codex.
- `AI-OS/agents` - agent identities, profiles, commands, SOPs, templates.
- `AI-OS/agents/shared` - cross-agent handoffs, QA, and templates.
- `AI-OS/operations/memory` - durable checkpoints/refinement candidates.
- `AI-OS/knowledge` - Obsidian/wiki vault.

## Open Threads

- Rotate exposed Firecrawl/Stitch keys because they previously lived in
  plaintext runtime config.
- Decide whether to delete legacy tracked folders:
  - `agents/garry/skills`
  - `agents/business-partner/skills`
  - `agents/shared/skills`
- `knowledge/` still needs a deliberate reconciliation: it is behind
  `origin/main` by 28 commits and has many local deletes plus new raw imports.
- AI-OS repo remains dirty with many pre-existing modified/untracked files.

## Next Good Move

Make a dedicated cleanup commit for the router/skill/global-lint changes, then
handle the `knowledge/` repo separately so memory redesign starts from a stable
vault.
