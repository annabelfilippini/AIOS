# GitHub CLI Commands

Safe defaults:

```bash
gh auth status
gh repo view
gh pr view
gh pr checks
gh issue view
```

Approval required:

```bash
gh pr merge
gh repo delete
gh release create
gh secret set
```

Prefer read-only commands unless Annabel explicitly asks for a publishing or
permission-changing action.
