# SOP: Review Claude Handoff

## Trigger

Annabel provides a Claude handoff or asks whether a Claude plan is safe to implement.

## Inputs

- Handoff path, usually `AI-OS/agents/shared/handoffs/active/<slug>.md`
- Relevant project repository or project folder
- Any explicit CEO constraints or amendments

## Steps

1. Read the handoff.
2. Identify the likely project/repo and relevant files.
3. Inspect the repo and project instructions.
4. Compare the handoff against repository reality.
5. Decide whether the verdict is `Approved`, `Needs Changes`, or `Blocked`.
6. Write the review next to the handoff as `<handoff-basename>.codex-review.md`.
7. Keep the review concrete enough that implementation can start if approved.

## Output

A Codex review file with:

- Verdict
- Codebase reality check
- Required plan changes
- Risks found
- Adjusted implementation plan
- Verification plan
- Notes for Claude

## Approval Requirement

No approval is needed to write the review.

Approval is needed before implementing any plan that is not clearly `Approved` or explicitly adjusted in the review.

## Final Artifact Location

Write the review next to the source handoff in `AI-OS/agents/shared/handoffs/`.
