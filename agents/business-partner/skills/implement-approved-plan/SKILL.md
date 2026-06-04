---
name: implement-approved-plan
description: Implement a Garry handoff only after Business Partner has reviewed it against the repo. Use when given an approved or amended handoff and asked to make code changes, run verification, and write implementation notes.
---

# Implement Approved Plan

Use this skill after `review-claude-plan`.

## Core Rule

Do not implement an unreviewed plan.

The review controls the implementation scope.

## Inputs

Handoff path, usually:

`/Users/annabelfilippini/Documents/AI-OS/agents/shared/handoffs/active/<slug>.md`

Matching Business Partner review:

`<handoff-basename>.business-partner-review.md`

If the review file is missing, stop and run `review-claude-plan` first.

## Rules

- If the review verdict is `Blocked`, stop and explain the blocker.
- If the review verdict is `Needs Changes`, implement only the adjusted plan if it is explicit.
- Keep edits scoped to the approved or adjusted plan.
- Do not refactor unrelated files.
- Work with existing user changes; do not revert unrelated work.
- Use `investigate-lite` before changing code if the issue is not understood.
- Use `guardrails-lite` if the implementation starts expanding.
- Run the smallest meaningful verification for the change.

## Workflow

1. Read the handoff and matching Business Partner review.
2. Inspect current git status before editing.
3. Re-read relevant project instructions.
4. Implement the approved or adjusted scope.
5. Run relevant verification: tests, typecheck, build, lint, or targeted manual checks.
6. Write implementation notes next to the handoff:

`<handoff-basename>.implementation-notes.md`

## Notes Structure

```markdown
# Implementation Notes: <Plan Name>

## Summary

## Files Changed

## Verification

## Deviations From Plan

## Follow-Ups
```

## Response

Return:

- What changed
- Files touched
- Verification run and result
- Implementation notes path
- Any follow-up needed
