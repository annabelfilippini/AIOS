---
name: decision-pipeline
description: Turn an idea into a clear decision and Codex-ready handoff. Use when Annabel wants to evaluate, stress-test, scope, or plan an idea before implementation.
argument-hint: "[idea or project]"
context: fork
allowed-tools:
  - Bash
  - Read
  - Write
---

# Decision Pipeline

Use this skill to help Annabel think clearly before code exists.

The output is not just chat advice. Create a durable handoff file in:

`/Users/annabelfilippini/Documents/AI-OS/agents/shared/handoffs/active/`

## Core Rule

Claude owns intent, judgment, scope, and the decision record.
Codex owns repository reality, implementation, verification, and code changes.

Do not over-specify implementation details that Codex should discover from the repo.
Mark assumptions clearly.

## References

After this skill has been used on a real idea, maintain:

`references/good-bad-examples.md`

Capture compact examples of handoffs that worked well and handoffs that were confusing, overbuilt, or too vague. Do not create fictional examples.

## Workflow

### 1. Clarify The Idea

Restate the idea in one sentence. Identify:

- The user or buyer
- The pain or desire
- The current workaround
- What would be meaningfully better

If the idea is too vague to evaluate, ask one pointed question and stop.

### 2. Stress-Test It

Challenge the idea directly:

- What has to be true for this to work?
- What fails first?
- What would make this not worth building?
- What is the hidden maintenance burden?
- What is the smallest real-world test?

Be candid. Do not polish weak thinking.

### 3. Decide

Give one verdict:

- `Build now`
- `Prototype first`
- `Research first`
- `Park`
- `Kill`

Include the main reason and the tradeoff.

### 4. Scope The Smallest Useful Version

Define the smallest useful version that proves the decision. Keep it buildable in one focused Codex session when possible.

Include:

- In scope
- Out of scope
- Acceptance criteria
- Risks and assumptions

### 5. Write The Handoff

Write a markdown file named:

`YYYY-MM-DD-slug.md`

Use today's date and a short lowercase slug from the idea.

Use this structure:

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

## Questions For Codex To Verify

## Codex Handoff

Codex should inspect the relevant repo/files before implementing. Treat this plan as directional, not binding. If the codebase suggests a smaller or safer path, amend the plan before coding.
```

### 6. Report Back

In chat, return only:

- Verdict
- Recommended next action
- Path to the handoff file
- Any question Annabel must answer before Codex reviews it

Keep the response tight.
