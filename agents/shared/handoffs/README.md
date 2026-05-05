# Handoffs

This folder is the paper trail between Garry/Claude planning and Business Partner/Codex implementation.

## Active

`active/` contains current plans waiting for Codex review or implementation.

## Archive

`archive/` contains completed, killed, parked, or superseded handoffs.

## Handoffs Vs QA

Use a handoff when Claude/Garry is passing intent, scope, product judgment, or implementation direction to Codex across agents or sessions.

Use `agents/shared/qa/` instead when code already exists and Codex is reviewing a branch, diff, PR, or concrete change for bugs, regressions, missing tests, and readiness.

## Workflow

1. Garry/Claude runs `/decision-pipeline`.
2. Garry/Claude writes a handoff into `active/`.
3. Business Partner/Codex reviews the handoff against the real repo.
4. Business Partner/Codex either amends the plan, implements it, or blocks with a reason.
5. Completed handoffs can move to `archive/`.
