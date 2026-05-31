# Business Partner Skills Legacy Folder

This folder is no longer the source of truth. Global skills for both Claude and
Codex live in top-level `skills/`.

Former Business Partner-origin skills now live at:

- `skills/review-claude-plan/`
- `skills/implement-approved-plan/`
- `skills/plan-eng-review-lite/`
- `skills/adversarial-review-lite/`
- `skills/investigate-lite/`
- `skills/guardrails-lite/`
- `skills/markdown-lint-operating-docs/`

Do not add new durable skills here. Add them to top-level `skills/` and list
default agent routing in `agents/business-partner/profile.yaml`.
