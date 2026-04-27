# Handoffs

This folder is the paper trail between Claude planning and Codex implementation.

## Active

`active/` contains current plans waiting for Codex review or implementation.

## Archive

`archive/` contains completed, killed, parked, or superseded handoffs.

## Workflow

1. Claude runs `/decision-pipeline`.
2. Claude writes a handoff into `active/`.
3. Codex reviews the handoff against the real repo.
4. Codex either amends the plan, implements it, or blocks with a reason.
5. Completed handoffs can move to `archive/`.
