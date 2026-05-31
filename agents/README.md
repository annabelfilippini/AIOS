# Agents Structure

This folder separates Annabel's AI operating system by agent role.

Start here:

- `agent.md` - how all agents work together

## Agent Homes

- `annie/` - life-wide assistant context, inbox, workspace, templates, SOPs, and access policy
- `garry/` - Claude-native startup advisor context, commands, profile, and operating docs
- `business-partner/` - Codex-native critic, reviewer, implementation partner, profile, and operating docs

## Shared Paper Trail

- `shared/` - templates, handoffs, durable context, and cross-agent records

## Runtime Model

Runtime folders outside AI-OS, such as `~/.claude/skills` and `~/.codex/skills`, should symlink to canonical skills in top-level `skills/`.

Top-level `cli-connections/` holds canonical CLI/tool connection definitions.
Agent `profile.yaml` files declare which skills and CLI connections each agent
can use.

AI-OS does not keep separate `agents/claude/` or `agents/codex/` folders unless a future runtime-specific need appears.

## Archive

- `archive/` - retired or historical agent assets
- `runtime-backups/` - backups of runtime command/skill folders
