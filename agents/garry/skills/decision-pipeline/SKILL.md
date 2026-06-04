---
name: decision-pipeline
description: Turn a business or product idea into a clear decision and implementation-ready handoff. Use after Garry has clarified the customer, pain, scope, and next move.
argument-hint: "[idea or project]"
context: fork
allowed-tools:
  - Bash
  - Read
  - Write
---

# Decision Pipeline

Garry owns intent, judgment, scope, and the decision record.

Business Partner owns repository reality, implementation, verification, and code changes.

## Core Rule

Do not over-specify implementation details that Business Partner should discover from the repo.

Mark assumptions clearly. Keep the handoff directional, buildable, and reviewable.

## Workflow

1. Clarify the idea.
2. Stress-test it.
3. Decide.
4. Scope the smallest useful version.
5. Write the handoff.
6. Report back tightly.

## Verdicts

Use one:

- `Build now`
- `Prototype first`
- `Research first`
- `Park`
- `Kill`

Include the main reason and the tradeoff.

## Handoff Location

Write a markdown file named:

`YYYY-MM-DD-slug.md`

Location:

`/Users/annabelfilippini/Documents/AI-OS/agents/shared/handoffs/active/`

## Handoff Structure

```markdown
# <Idea Name>

## Decision

Verdict:
Reason:
Tradeoff:

## Goal

## Desired Behavior

## User / Buyer

## Pain Or Opportunity

## Stress Test

## Smallest Useful Scope

## Non-Goals

## Acceptance Criteria

## Risks And Assumptions

## Questions For Business Partner To Verify

## Business Partner Handoff

Business Partner should inspect the relevant repo/files before implementing. Treat this plan as directional, not binding. If the codebase suggests a smaller or safer path, amend the plan before coding.
```

## Response

Return only:

- Verdict
- Recommended next action
- Path to the handoff file
- Any question Annabel must answer before Business Partner reviews it
