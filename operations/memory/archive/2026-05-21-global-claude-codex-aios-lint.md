# 2026-05-21 Global Claude/Codex/AI-OS Lint

Scope: `~/.claude`, `~/.codex`, home `AGENTS.md`, and
`~/Documents/AI-OS`.

## Summary

The system is usable, but not clean enough to be the base for a new memory
system without a short consolidation pass.

Highest-value fixes:

1. Move live credentials out of runtime config files.
2. Retire stale `~/Documents/Claude` references now that AI-OS is canonical.
3. Restore a practical Markdown lint config with `MD013` disabled.
4. Align runtime skill names with the AI-OS skill catalog.
5. Decide what to do with old Claude/Codex session stores before designing new
   memory.

## Findings

### P0: Credentials In Runtime Config

`~/.codex/config.toml` contains live-looking API credentials for MCP servers.
The values were not copied into this report.

Also present: `~/.claude/channels/telegram/.env`.

Recommendation: rotate exposed keys, move secrets into an ignored env/secret
store, and keep runtime config to references only.

### P1: Stale `~/Documents/Claude` Routing

Several active runtime paths still point at `~/Documents/Claude`, which is now
missing:

- `~/.claude.json` project entries
- `~/.claude/projects/-Users-annabelfilippini-Documents-Claude*`
- `~/.claude/hooks/file-placement-guard.sh`
- `~/.claude/hooks/wiki-session-report.sh`
- `~/.codex/hooks/file-placement-guard.sh`
- `~/.codex/hooks/wiki-session-report.sh`

Recommendation: update hooks to AI-OS paths and archive/delete stale project
state only after confirming Claude does not still need it.

### P1: Codex Global Adapter Is Empty

`~/.codex/AGENTS.md` exists but is empty. The real Codex global instructions
are in home `AGENTS.md`.

Recommendation: either remove the empty runtime adapter if unused, or make it a
tiny pointer to home `AGENTS.md` and AI-OS.

### P1: Markdown Lint Config Missing

AI-OS git status shows `.markdownlint-cli2.jsonc` deleted. Running
`markdownlint-cli2` across operating docs produced 645 errors, mostly `MD013`
line length. After ignoring `MD013`, the real errors were concentrated in:

- `agents/garry/commands/begin.md`: first-line heading, compact table spacing,
  blank lines around headings/lists.
- `operations/annabel-press/README.md`: ordered-list prefix.

Recommendation: restore a repo lint config with `MD013: false`, exclude noisy
stores, then fix the small set of structural Markdown issues.

### P1: Dirty State Before Memory Redesign

AI-OS has many modified/untracked files, including startup docs, profiles,
skills, memory checkpoints, Annabel Press, and a swap file. `knowledge/` is also
behind origin by 28 commits with substantial deletes/untracked raw imports.

Recommendation: create one explicit consolidation branch/commit sequence before
changing memory architecture.

### P2: Runtime Skill Alignment Drift

The runtime skill drift script passed: no runtime-only durable skills were
detected. But the advertised Claude active skills in `Documents/AI-OS/CLAUDE.md`
do not match runtime symlink names:

- AI-OS lists `garry-office-hours-lite` and `garry-ceo-review-lite`.
- Runtime/top-level skills use `office-hours-lite` and `ceo-review-lite`.
- `~/.claude/skills` does not include office-hours or ceo-review symlinks.

Recommendation: standardize skill names before adding memory lookup skills.

### P2: Broken Symlinks / Compatibility Links

Broken links detected:

- `~/.claude/debug/latest`
- `Documents/AI-OS/operations/memory/_active`
- `Documents/AI-OS/operations/automation/_active`
- `Documents/AI-OS/operations/legacy-system/_system`

The AI-OS links point at missing legacy `_system` targets.

Recommendation: either recreate the intended compatibility targets or remove
these links if migration is complete.

### P2: Runtime Bulk

Approximate sizes:

- `~/.claude`: 136 MB
- `~/.codex`: 759 MB
- `~/Documents/AI-OS`: 3.9 GB

Large runtime bulk is mostly session JSONL, SQLite logs, generated images, and
Codex logs. The largest single runtime file found was
`~/.codex/logs_2.sqlite` at about 302 MB.

Recommendation: keep transcript/session stores out of the new durable memory
path. Treat them as raw audit archives only.

### P3: Low-Risk Hygiene

Found `.DS_Store`, a `.CLAUDE.md.swp`, `.codex/.tmp`, and
`.codex/.codex-global-state.json.bak`.

Recommendation: clean only after the git state is intentionally staged or
snapshotted.

## Verification Run

- JSON validation passed for selected Claude/Codex JSON config files.
- TOML validation passed for Codex config and automation TOML.
- Runtime skill drift check passed.
- Markdown lint ran on 116 operating-doc Markdown files and found 645 errors
  without config; almost all are line-length noise.

## Recommended Cleanup Order

1. Credential pass: rotate/move secrets out of config.
2. Routing pass: replace stale `~/Documents/Claude` hooks and project pointers.
3. Lint pass: restore `.markdownlint-cli2.jsonc`, fix structural Markdown.
4. Skill pass: normalize skill names and symlinks.
5. Memory pass: design new memory on top of `operations/memory/`, not runtime
   session stores.
