# Agents Structure

This folder separates Annabel's AI operating system by agent role.

Start here:

- `agent.md` - how all agents work together

## Agent Homes

- `annie/` - life-wide assistant context, inbox, workspace, templates, SOPs, and access policy
- `garry/` - Claude-native startup advisor context, commands, and skills
- `business-partner/` - Codex-native critic, reviewer, implementation partner, and skills

## Shared Paper Trail

- `shared/` - templates, handoffs, durable context, and cross-agent records

## Runtime Model

Runtime folders outside AI-OS, such as `~/.claude/skills` and `~/.codex/skills`, should symlink directly to the relevant agent-owned skills.

AI-OS does not keep separate `agents/claude/` or `agents/codex/` folders unless a future runtime-specific need appears.

## Archive

- `archive/` - retired or historical agent assets
- `runtime-backups/` - backups of runtime command/skill folders
