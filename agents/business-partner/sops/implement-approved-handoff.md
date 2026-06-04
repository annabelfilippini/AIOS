# SOP: Implement Approved Handoff

## Trigger

Annabel asks Business Partner to implement an approved or amended Garry handoff.

## Inputs

- Handoff path, usually `AI-OS/agents/shared/handoffs/active/<slug>.md`
- Matching Business Partner review path, `<handoff-basename>.business-partner-review.md`
- Relevant project repository

## Steps

1. Read the handoff and matching Business Partner review.
2. Stop if the review is missing.
3. Stop if the verdict is `Blocked`.
4. If the verdict is `Needs Changes`, implement only the adjusted plan if it is explicit.
5. Inspect current git status before editing.
6. Re-read relevant project instructions.
7. Implement only the reviewed scope.
8. Run the smallest meaningful verification.
9. Write implementation notes next to the handoff.

## Output

An implementation notes file with:

- Summary
- Files changed
- Verification
- Deviations from plan
- Follow-ups

## Approval Requirement

Implementation requires an existing Business Partner review that allows implementation.

If the implementation would expand scope, change architecture materially, or touch unrelated files, ask Annabel before proceeding.

## Final Artifact Location

Write implementation notes next to the source handoff in `AI-OS/agents/shared/handoffs/`.
