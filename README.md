# AI-OS

Top-level mental model:

- `agents/` - source of truth for Claude, Codex, Annie, and shared agent behavior.
- `skills/` - canonical AI-OS skill library; current entries may symlink to legacy agent-owned folders during migration.
- `cli-connections/` - canonical AI-OS CLI/tool connection library.
- `knowledge/` - Obsidian/Git knowledge vault, especially raw notes and articles.
- `projects/` - actual products, client work, and buildable repos.
- `operations/` - automations, command center, memory, and legacy system wiring.
- `scratch/` - temporary artifacts, design experiments, and throwaway work.
- `_archive/` - historical or inactive material.

`wiki` is now a compatibility symlink to `knowledge/`. Prefer `knowledge/` for new references, but old `wiki/` paths should continue to work during the transition.

Legacy folders may remain while paths are migrated. Prefer the future-facing folders above for new work.

Annie's home is `agents/annie/`. She is the life-wide assistant agent for cross-project inbox, calendar, documents, briefs, drafts, follow-ups, and personal/business operations.
