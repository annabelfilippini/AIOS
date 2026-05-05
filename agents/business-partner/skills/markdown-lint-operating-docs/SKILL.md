---
name: markdown-lint-operating-docs
description: Run practical Markdown linting for AI-OS operating docs without noisy generated/reference files.
---

# Markdown Lint Operating Docs

Use this skill to make Markdown linting repeatable without burning context on
generated or reference-heavy files.

## Good Examples

- Add a repo lint config before trying to fix thousands of generated errors.
- Exclude noisy stores such as `knowledge/**`, `projects/**`, and archives.
- Disable `MD013` for prose-heavy agent docs unless hard wrapping is requested.
- Fix real operating-doc errors: table syntax, inline HTML placeholders, trailing
  whitespace, missing final newlines, and malformed headings.
- Report what linting did and did not prove.
- Verify GitHub freshness separately with `git fetch` or `git ls-remote`.

## Bad Examples

- Running `npx markdownlint-cli2 "**/*.md"` across the entire repo and treating
  scraped/reference output as product work.
- Spending time wrapping every prose line to 80 characters when context clarity
  matters more.
- Saying "everything is organized" just because Markdown lint passed.
- Forgetting that `origin/main` may be stale until a fetch or remote check runs.
- Committing lint fixes before `npx markdownlint-cli2` and `git diff --check`
  both pass.

## Core Idea

Markdown linting checks formatting, not whether docs are strategically organized.

It can verify:

- heading/table/list syntax
- trailing whitespace and final newlines
- inline HTML and bare URLs
- configured style rules

It cannot verify:

- whether agent roles are semantically correct
- whether docs are concise enough for context budgets
- whether GitHub is current, unless Git is checked separately

## Workflow

1. Check Git state first:

   ```bash
   git status --short --branch
   git rev-list --left-right --count origin/main...main
   ```

2. If remote freshness matters, fetch or verify the remote:

   ```bash
   git fetch origin
   git ls-remote origin refs/heads/main
   ```

3. Look for an existing Markdown lint config:

   ```bash
   find . -maxdepth 2 \( -name '.markdownlint*' -o -name '.markdownlint-cli2*' \) -print
   ```

4. Run the configured linter when config exists:

   ```bash
   npx markdownlint-cli2
   ```

5. If no config exists, run a first pass with likely ignores:

   ```bash
   npx markdownlint-cli2 "**/*.md" "!knowledge/**" "!projects/**" "!operations/memory/**"
   ```

6. If output is huge, do not blindly fix everything. Identify noisy categories:

   - generated/scraped/reference files
   - knowledge vaults
   - archived memory/checkpoints
   - prose line-length false positives

7. Add or update `.markdownlint-cli2.jsonc` so future runs are useful:

   ```jsonc
   {
     "config": {
       "MD013": false
     },
     "globs": [
       "**/*.md"
     ],
     "ignores": [
       "knowledge/**",
       "projects/**",
       "operations/memory/**"
     ]
   }
   ```

8. Fix remaining real lint errors in operating docs.

9. Re-run:

   ```bash
   npx markdownlint-cli2
   git diff --check
   ```

10. Summarize scope and limits clearly:

    - number of files linted
    - error count
    - excluded folders
    - rules disabled
    - whether Git/GitHub was verified separately

## AI-OS Defaults

For AI-OS, lint the operating docs and exclude noisy stores by default:

- `knowledge/**`
- `projects/**`
- `operations/memory/**`
- `agents/garry/commands/**`

Disable `MD013` unless Annabel specifically wants hard 80-character wrapping.
Long prose lines are usually less harmful than wrapped agent instructions.

## Commit Guidance

Commit the lint config and fixes only after:

- `npx markdownlint-cli2` passes
- `git diff --check` passes
- Git status contains only intentional lint/config changes

Use a commit message like:

```text
Add markdown lint config
```
