# Shared

Shared contains the paper trail and reusable context between agents.

- `templates/` - handoff, QA request, and review templates.
- `handoffs/` - active and archived Claude-to-Codex plans.
- `qa/` - active and archived Codex QA reviews of built work.

Do not put skills here. Global skills for Claude and Codex live in top-level
`skills/`.

Do not put agent-specific workflows here. If a workflow belongs to Garry,
Business Partner, or Annie, keep it under that agent.
