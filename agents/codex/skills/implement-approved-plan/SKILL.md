---
name: implement-approved-plan
description: Implement a Claude handoff only after Codex has reviewed it against the repo. Use when given an approved or amended handoff and asked to make code changes, run verification, and write implementation notes.
---

# Implement Approved Plan

Use this skill after `review-claude-plan`.

Claude owns the intended outcome.
Codex owns the code changes, repo fit, tests, and verification.

## Inputs

The user should provide a handoff path, usually:

`/Users/annabelfilippini/Documents/AI-OS/agents/shared/handoffs/active/<slug>.md`

The matching Codex review should be next to it:

`<handoff-basename>.codex-review.md`

If the review file is missing, stop and run `review-claude-plan` first.

## Rules

- Do not implement an unreviewed plan.
- If the review verdict is `Blocked`, stop and explain the blocker.
- If the review verdict is `Needs Changes`, implement the adjusted plan only if the review clearly defines it. Otherwise stop and ask for confirmation.
- Keep edits scoped to the approved or adjusted plan.
- Do not refactor unrelated files.
- Work with existing user changes; do not revert unrelated work.
- Run the smallest meaningful verification for the change.

## References

After this skill has been used on a real implementation, maintain:

`references/good-bad-examples.md`

Capture compact examples of implementations that stayed aligned with the reviewed plan, plus bad examples where scope drifted, verification was weak, or the implementation ignored the review.

## Workflow

1. Read the handoff and matching Codex review.
2. Inspect current git status before editing.
3. Re-read relevant project instructions.
4. Implement the approved or adjusted scope.
5. Run relevant verification: tests, typecheck, build, lint, or targeted manual checks.
6. Write implementation notes next to the handoff:

`<handoff-basename>.implementation-notes.md`

Use this structure:

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
