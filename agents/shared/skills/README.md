# Shared Skills

Shared skills are canonical AI-OS skills that more than one runtime can use.

Use this folder when both Claude/Garry and Codex/Business Partner should share
the same workflow, examples, guardrails, or references.

## Rule

AI-OS owns the source of truth.

Runtime folders should point here instead of owning separate copies:

- `~/.claude/skills/<skill-name>`
- `~/.codex/skills/<skill-name>`

Prefer symlinks when the runtime supports them. If a runtime requires a copy,
treat the AI-OS version as canonical and refresh the runtime copy from here.

## Placement

- Shared by Claude and Codex: `agents/shared/skills/<skill-name>/`
- Claude/Garry only: `agents/garry/skills/<skill-name>/`
- Codex/Business Partner only: `agents/business-partner/skills/<skill-name>/`

Do not create new durable skills directly in `~/.claude/skills` or
`~/.codex/skills`.
