---
name: client-proposal-pdf
description: Build concise branded client proposal PDFs from markdown for Annabel's website refresh and consulting work, using the Vital Health proposal pattern for phases, rates, honest ranges, hosting costs, next steps, approval blockers, no-dash copy mechanics, and markdown-to-HTML-to-Chrome PDF generation.
---

# Client Proposal PDF

Use when Annabel needs a polished client proposal PDF, especially after a
website refresh, Webflow rebuild, backend workflow mapping, or follow-up scope.

Related skill: `client-website-refresh`.

## Shape

- Keep proposals short enough for a real client to read.
- Separate fixed-fee known work from discovery-dependent hourly work.
- Include rates, hosting/subscription costs, payment method, and next steps.
- Name blockers and client responsibilities plainly.
- Keep optional add-ons separate from the core approved work.
- Apply Annabel's voice mechanics before rendering. No dashes as punctuation.

## Workflow

1. Read the client/project context, proposal source markdown if one exists, and
   any recent checkpoints.
2. Draft or revise the proposal in markdown first.
3. Check numbers, phase names, rates, and approval dependencies.
4. Scrub dashes from client-facing copy unless they are unavoidable inside URLs
   or machine-readable identifiers.
5. Render the markdown to PDF with `scripts/build_proposal_pdf.py` or the
   project-specific renderer.
6. Visually QA the PDF pages for orphaned signatures, cramped tables, bad page
   breaks, missing logo, and unreadable text.
7. Iterate markdown or print CSS until the PDF is client-ready.

## References

- Read [proposal-structure.md](references/proposal-structure.md) before drafting.
- Read [good-bad-examples.md](references/good-bad-examples.md) before final copy
  edits or pricing language.

## Tooling

Use `scripts/build_proposal_pdf.py` for a portable markdown to styled HTML to
Chrome PDF pipeline. It intentionally supports the simple proposal markdown
shape Annabel used for Vital Health: headings, paragraphs, bullets, numbered
lists, bold, links, horizontal rules, and markdown tables.
