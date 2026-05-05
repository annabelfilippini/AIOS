# QA

This folder holds lightweight Codex QA passes on work built elsewhere, usually by Claude Code.

QA is not the same as a handoff.

- Use QA when there is already code, a branch, a diff, a PR, or a concrete change to review.
- Use a handoff when Claude/Garry is passing intent, scope, and product judgment to Codex for later review or implementation.
- Keep QA artifacts short, practical, and tied to the exact change under review.

## Active

`active/` contains current QA reviews that still need fixes, re-review, or Annabel's decision.

## Archive

`archive/` contains completed QA reviews after findings are resolved, accepted, or intentionally skipped.

## Naming

Use a date and clear slug:

`YYYY-MM-DD-project-or-branch.codex-qa.md`

## Workflow

1. Claude Code builds or changes something.
2. Claude Code summarizes the branch, files changed, verification run, and known risks.
3. Codex/Business Partner reviews the diff, branch, PR, or selected files.
4. Codex writes findings using `agents/shared/templates/codex-qa-review.md`.
5. Claude Code or Codex fixes only approved findings.
6. Codex re-reviews when requested.
