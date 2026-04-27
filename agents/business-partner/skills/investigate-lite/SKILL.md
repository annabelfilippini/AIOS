---
name: investigate-lite
description: Root-cause investigation for bugs or confusing repo behavior. Use before fixing when the cause is not yet proven.
---

# Investigate Lite

This skill borrows the useful parts of gstack `/investigate` without importing the full workflow.

Use it when something is broken, flaky, surprising, or not yet understood.

## Core Rule

Do not fix before you know the cause.

Gather evidence, form hypotheses, test them, then change code.

## Workflow

1. State the symptom precisely.
2. Identify the expected behavior.
3. Inspect the relevant files, tests, logs, or data.
4. List likely causes.
5. Test the smallest hypothesis first.
6. Confirm root cause.
7. Recommend fix and verification.

## Evidence Standard

Good evidence:

- failing test
- reproducible command
- log line
- code path trace
- data/state mismatch
- browser or UI reproduction

Weak evidence:

- vibes
- guessing from filenames
- fixing the first suspicious line
- changing several things at once

## Output

Return:

- Symptom
- Root cause, if proven
- Evidence
- Fix recommendation
- Verification plan
- Unknowns

If root cause is not proven, say that directly.
