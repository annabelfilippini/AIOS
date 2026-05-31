# Shared Skills Legacy Folder

This folder is no longer the source of truth.

Global skills for both Claude and Codex live in top-level `skills/`.

## Rule

AI-OS owns the source of truth.

Runtime folders should point to top-level `skills/` instead of owning separate
copies:

- `~/.claude/skills/<skill-name>`
- `~/.codex/skills/<skill-name>`

Prefer symlinks when the runtime supports them. If a runtime requires a copy,
treat the top-level AI-OS version as canonical.

## Placement

- New skills: `skills/<skill-name>/`
- New CLI/tool connections: `cli-connections/<connection-name>/`
- Agent access: `agents/<agent>/profile.yaml`

Do not create new durable skills directly in `~/.claude/skills` or
`~/.codex/skills`.
