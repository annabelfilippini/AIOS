---
name: adversarial-review-lite
description: Adversarial code or plan review. Use when Annabel asks for the harshest useful critique, when a change is risky, or before shipping user-facing behavior.
---

# Adversarial Review Lite

This skill borrows the useful parts of gstack `/review` without importing the full workflow.

Use it to find bugs, regressions, security holes, user harm, unclear behavior, and missing tests.

## Core Rule

Find the failure modes.

Do not spend time on compliments. Do not nitpick style unless it causes real risk.

## Review Lens

Think like:

- a user hitting edge cases
- a maintainer debugging this later
- an attacker looking for abuse paths
- an operator handling production failure
- a future Codex session trying to understand the code

## Questions

- What breaks if inputs are empty, malformed, duplicated, or huge?
- What happens if network, auth, storage, or third-party calls fail?
- Can this leak private data or expose actions to the wrong user?
- Does the UI show success before the action actually succeeds?
- Does the code silently swallow errors?
- Are tests covering the risky behavior, not just the happy path?
- Is there a rollback or safe failure behavior?

## Output

Lead with findings:

- Severity
- File/line if available
- Concrete failure mode
- Why it matters
- Suggested fix or verification

If there are no findings, say so clearly and name remaining test gaps or residual risk.
