---
name: skool-intelligence-digest
description: Collect and summarize Skool community signals for Annabel Press, including account status, pricing, member counts, visible posts, useful links, and attention-worthy updates.
audience:
  - annie
  - business-partner
runtime:
  - codex
visibility: private
related_cli_connections:
  - skool-pp-cli
---

# Skool Intelligence Digest

Use this skill when Annabel wants to scrape, search, or summarize Skool
communities she legitimately owns or pays for, using the authenticated
`skool-pp-cli` local knowledge-base workflow.

## Workflow

1. Confirm the community slugs or URLs. Common current targets:
   `earlyaidopters` for Mark Kashef and `ainative` for AI Transformation
   Academy / Mansel.
2. Check auth and connectivity with:
   `tools/skool-pp-cli/bin/skool-pp-cli doctor --agent`.
3. Confirm accessible communities with:
   `tools/skool-pp-cli/bin/skool-pp-cli communities list --agent`.
4. For a bounded private scrape, prefer:
   `tools/skool-pp-cli/bin/skool-pp-cli kb sync <slug> --since 30d --max-posts-pages 2 --agent`.
5. For deeper classroom capture, add `--captions`; for a broader historical
   scrape, widen `--since` or raise `--max-posts-pages`.
6. Use `find`, `digest`, `kb stats`, or `kb sql` to inspect the local mirror.
7. Summarize the highest-signal updates: new course drops, hot threads,
   questions worth answering, links/tools mentioned, pricing/status changes, and
   communities that look stale.

## Output Principles

- Prefer concise intelligence over raw archives.
- Preserve source URLs so Annabel can jump back into Skool.
- Do not save passwords, cookies, payment details, or private member records.
- Keep paid/member-only content in the local `skool-pp-cli` database. Share
  summaries and citations in conversation unless Annabel explicitly asks for a
  deeper local export.
