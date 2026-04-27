---
name: review-claude-plan
description: Review a Claude-generated handoff against the actual repository before implementation. Use when given a handoff file from AI-OS/agents/shared/handoffs/active and asked to assess feasibility, risks, scope, or implementation fit. Do not edit product code.
---

# Review Claude Plan

Use this skill before implementing a Claude handoff.

Claude owns intent, scope, and product judgment.
Codex owns repository reality, implementation judgment, and verification planning.

## Inputs

The user should provide a handoff path, usually:

`/Users/annabelfilippini/Documents/AI-OS/agents/shared/handoffs/active/<slug>.md`

If no path is provided, list recent files in the active handoff folder and ask which one to review.

## Rules

- Do not edit product code.
- Do not treat Claude's plan as binding.
- Inspect the relevant repo/files before judging the plan.
- Prefer the existing codebase's patterns over the handoff's guesses.
- Keep the review concrete enough that implementation can start immediately if approved.

## References

After this skill has been used on a real plan, maintain:

`references/good-bad-examples.md`

Capture compact examples of reviews that correctly approved, amended, or blocked a plan. Include bad examples where the review was too vague, skipped repo inspection, or rubber-stamped Claude.

## Workflow

1. Read the handoff.
2. Identify the likely project/repo and relevant files.
3. Inspect those files and local project instructions.
4. Decide whether the plan is:
   - `Approved`
   - `Needs Changes`
   - `Blocked`
5. Write a review file next to the handoff:

`<handoff-basename>.codex-review.md`

Use this structure:

```markdown
# Codex Plan Review: <Plan Name>

## Verdict

Approved / Needs Changes / Blocked

## Codebase Reality Check

## Required Plan Changes

## Risks Found

## Adjusted Implementation Plan

## Verification Plan

## Notes For Claude
```

## Response

Return:

- Verdict
- The most important adjustment, if any
- Review file path
- Whether implementation can proceed
