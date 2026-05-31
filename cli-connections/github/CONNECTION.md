---
name: github
display_name: GitHub CLI
binary: gh
audience:
  - garry
  - business-partner
runtime:
  - claude
  - codex
visibility: private
related_skills:
  - review-claude-plan
  - implement-approved-plan
safe_commands:
  - gh auth status
  - gh repo view
  - gh pr view
  - gh pr checks
approval_required:
  - gh pr merge
  - gh repo delete
  - gh release create
---

# GitHub CLI Connection

Use this connection for repository inspection, PR review, issue lookup, and
shipping support when a project already uses GitHub.

## Safe Uses

- Check authentication status.
- Inspect repositories, pull requests, issues, checks, and releases.
- Read CI status and linked metadata.

## Requires Approval

- Merging pull requests.
- Deleting repositories, branches, issues, releases, or assets.
- Creating releases or making public-facing publishing changes.
- Changing repository settings, secrets, permissions, or collaborators.

## Verification

- Run `scripts/check-installed.sh` before assuming `gh` is available.
- Run `scripts/check-auth.sh` before using authenticated commands.

Do not store GitHub tokens, SSH keys, deploy keys, or repository secrets in this
folder.
