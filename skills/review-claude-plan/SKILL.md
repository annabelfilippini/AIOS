---
name: review-claude-plan
description: Review a Garry handoff against the actual repository before implementation. Use when given a handoff file and asked to assess feasibility, risks, scope, or implementation fit. Do not edit product code.
---

# Review Garry Plan

Use this skill before implementing a Garry handoff.

Garry owns intent, scope, and product judgment.

Business Partner owns repository reality, implementation judgment, and verification planning.

## Core Rule

Do not treat the plan as binding.

Inspect the repo first. Approve, amend, or block based on what is actually there.

## Inputs

Handoff path, usually:

`/Users/annabelfilippini/Documents/AI-OS/agents/shared/handoffs/active/<slug>.md`

If no path is provided, list recent files in the active handoff folder and ask which one to review.

## Rules

- Do not edit product code.
- Do not rubber-stamp Garry or any builder runtime.
- Inspect the relevant repo/files before judging the plan.
- Prefer existing codebase patterns over the handoff's guesses.
- Keep the review concrete enough that implementation can start immediately if approved.
- Borrow `plan-eng-review-lite` when the plan is technically complex.
- Borrow `guardrails-lite` when scope creep is likely.

## Workflow

1. Read the handoff.
2. Identify the likely project/repo and relevant files.
3. Inspect those files and local project instructions.
4. Decide whether the plan is:
   - `Approved`
   - `Needs Changes`
   - `Blocked`
5. Write a review file next to the handoff:

`<handoff-basename>.business-partner-review.md`

## Review Structure

```markdown
# Business Partner Plan Review: <Plan Name>

## Verdict

Approved / Needs Changes / Blocked

## Codebase Reality Check

## Required Plan Changes

## Risks Found

## Adjusted Implementation Plan

## Verification Plan

## Notes For Builder
```

## Response

Return:

- Verdict
- Most important adjustment, if any
- Review file path
- Whether implementation can proceed
