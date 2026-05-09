# Shared

Shared contains the paper trail and reusable context between Claude and Codex.

- `context/` - durable preferences, project map, and working style.
- `skills/` - canonical skills shared by Claude and Codex runtimes.
- `templates/` - handoff, QA request, and review templates.
- `handoffs/` - active and archived Claude-to-Codex plans.
- `qa/` - active and archived Codex QA reviews of built work.

Do not put agent-specific workflows here. If a workflow belongs to Claude or Codex, keep it under that agent.
