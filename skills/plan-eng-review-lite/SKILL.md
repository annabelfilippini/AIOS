---
name: plan-eng-review-lite
description: Engineering review for implementation plans. Use when a Claude/Garry handoff may be technically risky, overbuilt, under-specified, or mismatched with the repo.
---

# Plan Engineering Review Lite

This skill borrows the useful parts of gstack `/plan-eng-review` without importing the full workflow.

Use it inside `review-claude-plan` when technical fit matters.

## Core Rule

The repo wins over the plan.

Do not judge a technical plan without inspecting the actual files, patterns, dependencies, and tests.

## Review Questions

Use the relevant questions, not all of them every time.

### Existing System Fit

- What already exists that solves part of this?
- Is the plan inventing abstractions the repo does not use?
- Does it follow existing naming, structure, and dependency patterns?

### Minimum Change

- What is the smallest safe change that achieves the goal?
- Which parts of the plan can be deferred?
- Is the proposed architecture bigger than the current need?

### Risk

- What could break in production?
- What edge case is missing?
- What shared contract or data shape changes?
- Does this create migration, state, auth, permission, or concurrency risk?

### Verification

- What test or check would prove the change works?
- Is there an existing test pattern?
- If no test exists, what is the smallest meaningful manual or automated check?

## Verdicts

Use:

- `Technically sound`
- `Needs simplification`
- `Needs repo inspection`
- `Needs architecture decision`
- `Blocked`

## Output

Return:

- Engineering verdict
- Repo reality check
- Required plan changes
- Minimum safe implementation path
- Verification plan
