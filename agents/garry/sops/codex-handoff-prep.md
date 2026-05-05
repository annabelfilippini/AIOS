# SOP: Codex Handoff Prep

## Trigger

A business idea has been judged worth building or prototyping and needs to move from Claude strategy into Codex implementation.

Do not use this SOP for quick QA of code that already exists. For that, ask Codex/Business Partner for a QA review using the branch, diff, PR, or concise task summary.

## Inputs

- Business idea memo or conversation context
- Verdict from Garry
- Smallest useful version
- Known constraints, non-goals, risks, and assumptions

## Steps

1. Use `decision-pipeline`.
2. Keep the handoff directional, not over-specified.
3. Define the goal, desired behavior, user/buyer, pain or opportunity, and smallest useful scope.
4. Include non-goals and acceptance criteria.
5. Add risks and assumptions.
6. Add questions for Codex to verify against the repo.
7. Write the handoff to `agents/shared/handoffs/active/`.

## Output

A Claude-to-Codex handoff file that Codex can review through the Business Partner's `review-claude-plan` skill.

## Handoff Rules

Claude/Garry owns intent, scope, and product judgment.

Codex/Business Partner owns repository reality, implementation, verification, and code changes.

## Final Artifact Location

Write handoffs to:

`AI-OS/agents/shared/handoffs/active/`
