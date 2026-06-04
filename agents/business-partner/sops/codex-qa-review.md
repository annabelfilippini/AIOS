# SOP: QA Review

## Trigger

Annabel asks Business Partner to QA work built in builder runtime, or builder runtime finishes meaningful implementation work and needs a second-pass review before shipping.

## Inputs

- Project or repository path
- Branch name, git diff, PR link, or concise task summary
- builder changed-files summary
- Verification already run
- Known risks, skipped tests, or uncertainty from the builder runtime

## Steps

1. Read project-specific `AGENTS.md`, `CLAUDE.md`, or README guidance before reviewing.
2. Identify the exact scope of the change.
3. Inspect the diff and the relevant surrounding code.
4. Check whether the claimed verification is sufficient.
5. Look for bugs, regressions, missing tests, edge cases, unclear UX, data risks, deployment risks, and mismatches with project instructions.
6. Prioritize findings as P1, P2, or P3.
7. Do not broaden scope or rewrite the implementation unless Annabel explicitly asks Business Partner to fix approved findings.
8. Write the QA artifact to `agents/shared/qa/active/` when the review needs a durable paper trail.
9. If the review is quick and same-session, a concise response is enough.

## Output

Use `agents/shared/templates/qa-review.md` for durable QA artifacts.

For quick reviews, return:

- Verdict
- P1/P2/P3 findings
- Missing verification
- Suggested fix prompt for builder runtime

## Approval Requirement

No approval is needed to review.

Approval is needed before Business Partner edits product code to fix QA findings unless Annabel explicitly asks Business Partner to fix them.

## Final Artifact Location

Durable QA reviews go in:

`AI-OS/agents/shared/qa/active/`
