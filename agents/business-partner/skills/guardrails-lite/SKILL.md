---
name: guardrails-lite
description: Scope and safety guardrails for Business Partner implementation. Use when work risks drifting outside the approved plan or touching sensitive/reversible boundaries.
---

# Guardrails Lite

This skill borrows useful concepts from gstack guard/freeze/careful workflows without importing the full stack.

Use it to keep implementation bounded, reversible, and aligned with the reviewed plan.

## Core Rule

If the work starts expanding beyond the reviewed plan, stop and re-scope.

## Guardrails

### Scope

- Is this in the approved or amended plan?
- Is this required for acceptance criteria?
- Is this a follow-up disguised as implementation?

### Ownership

- Is this file part of the relevant project?
- Are there unrelated user changes in this file?
- Could this edit conflict with another agent's work?

### Reversibility

- Can this change be undone cleanly?
- Does it require migration, account changes, deletion, or external side effects?
- Does it alter durable data?

### Verification

- What is the smallest check that proves this is safe?
- What would show the change failed?
- Is manual verification enough, or does this need tests?

## Stop Conditions

Stop and ask Annabel before:

- expanding scope materially
- changing architecture beyond the review
- deleting or archiving records
- touching secrets, billing, legal, finance, health, or identity systems
- making external calls or commitments
- implementing a blocked or unreviewed plan

## Output

Return:

- Continue / stop
- Reason
- Required clarification, if any
- Safe next action
