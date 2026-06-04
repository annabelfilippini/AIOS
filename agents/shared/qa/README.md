# QA

This folder holds lightweight QA passes on work built elsewhere, regardless of which runtime built it.

QA is not the same as a handoff.

- Use QA when there is already code, a branch, a diff, a PR, or a concrete change to review.
- Use a handoff when Garry mode is passing intent, scope, and product judgment to Business Partner for later review or implementation.
- Keep QA artifacts short, practical, and tied to the exact change under review.

## Active

`active/` contains current QA reviews that still need fixes, re-review, or Annabel's decision.

## Archive

`archive/` contains completed QA reviews after findings are resolved, accepted, or intentionally skipped.

## Naming

Use a date and clear slug:

`YYYY-MM-DD-project-or-branch.codex-qa.md`

## Workflow

1. A builder runtime creates or changes something.
2. The builder runtime summarizes the branch, files changed, verification run, and known risks.
3. Business Partner reviews the diff, branch, PR, or selected files.
4. Business Partner writes findings using `agents/shared/templates/qa-review.md` or its successor runtime-neutral template.
5. The builder runtime, or another explicitly chosen runtime, fixes only approved findings.
6. Business Partner re-reviews when requested.
