# Handoffs

This folder is the paper trail between Garry planning and Business Partner implementation.

## Active

`active/` contains current plans waiting for Business Partner review or implementation.

## Archive

`archive/` contains completed, killed, parked, or superseded handoffs.

## Handoffs Vs QA

Use a handoff when Garry mode is passing intent, scope, product judgment, or implementation direction to Business Partner across modes or sessions.

Use `agents/shared/qa/` instead when code already exists and Business Partner is reviewing a branch, diff, PR, or concrete change for bugs, regressions, missing tests, and readiness.

## Workflow

1. Garry runs `/decision-pipeline`.
2. Garry writes a handoff into `active/`.
3. Business Partner reviews the handoff against the real repo.
4. Business Partner either amends the plan, implements it, or blocks with a reason.
5. Completed handoffs can move to `archive/`.
