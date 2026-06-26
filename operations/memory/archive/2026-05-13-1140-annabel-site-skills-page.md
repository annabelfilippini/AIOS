---
date: 2026-05-13
time: 11:40
project: agency-audit-network
status: paused
next-session: Continue refining `projects/agency-audit-network/site-draft/skills.html` as a showcase of Annabel's actual AI-OS skills/workflows, not a public command line product.
---

# Session: Annabel Site — separate Skills page

## What we worked on

Annabel wanted the Skills tab of her personal site to feel inspired by `skills.sh` / `printingpress.dev`, while matching the existing homepage visual direction. We read the Agency Audit Network project context first so the page language aligned with the audit-led AIOS work.

Important context read:

- `projects/agency-audit-network/AGENTS.md`
- `projects/agency-audit-network/README.md`
- `projects/agency-audit-network/PLAN.md`
- `projects/agency-audit-network/templates/aios-readiness-audit-offer-brief.md`
- Actual local skill files under `skills/` and `agents/shared/skills/`

## Decisions made

- **Do not edit the downloaded packed HTML directly.** The current browser URL points to `file:///Users/annabelfilippini/Documents/AI-OS/projects/agency-audit-network/site-draft/skills.html`; durable work should happen in the project source folder.
- **Keep Skills as a separate page.** Annabel did not want to interfere with homepage changes. Created `projects/agency-audit-network/site-draft/skills.html`.
- **Do not imply Annabel helps people implement skills.** The page should showcase the skills/workflows she uses, not sell skill implementation.
- **Do not imply `skills.sh` is a real public command.** The first draft had command-like text. Annabel correctly challenged this. Copy now says `skills.sh` is a visual metaphor, not a public command yet.
- **Use actual skills where possible.** Actual skill files found:
  - `skills/client-opportunity-map/SKILL.md`
  - `skills/skool-intelligence-digest/SKILL.md`
  - `agents/shared/skills/small-business-shopify-redesign/SKILL.md`
- **AIOS Starting Point Audit is a workflow/offer, not a standalone skill file.** The page now labels it as an offer workflow from the agency audit project, not a `SKILL.md`.

## Files changed

- `projects/agency-audit-network/site-draft/skills.html`
  - New standalone Skills page.
  - Visual direction: coral hero, forest library section, Fraunces/Public Sans, large translucent `skills.sh` background wordmark.
  - Removed Annabel portrait from the hero after feedback.
  - Made background `skills.sh` more transparent and shifted right to avoid overlapping the white headline.
  - Hero headline now: **"The things I make repeatable."**
  - Copy now frames the page as a library of workflows Annabel uses in her own work.

- `projects/agency-audit-network/site-draft/index.html`
  - Cleaned out the earlier inline Skills section that had been added before Annabel asked for a separate page.
  - Restored Skills nav to `href="#"` to avoid changing homepage routing while Annabel is making other site edits.
  - Preserved Annabel's existing `work-with-me.html` link.

## Current page content stance

Use this framing:

> This is a library of the skills I use in my own work: small, reusable operating instructions that turn messy context into repeatable workflows.

Avoid this framing:

> Run this command to get access to my tools.

Avoid presenting fake commands as executable. If keeping command-line aesthetics, label them as visual language or examples of internal workflow names.

## Verification performed

- Started a local preview server for `site-draft` and opened `skills.html` in the in-app browser.
- Confirmed the page rendered.
- Checked browser warnings/errors: console was clean.
- Visually checked hero and skill list after removing portrait and changing the background wordmark.

## Next steps

1. Decide whether homepage nav should eventually link to `skills.html` once Annabel is ready.
2. Consider creating an actual top-level canonical skill for the AIOS Starting Point Audit if it becomes durable and repeatable enough.
3. If the site is exported again into a packed `.html`, use the project `site-draft` as source of truth and only export when Annabel explicitly asks.

## System refinement candidates

- A future `skills.html` page should probably be generated from actual `SKILL.md` frontmatter plus manually curated descriptions, so the public showcase cannot drift into made-up capabilities.
- If `skills.sh` becomes a real artifact, define what it actually does before using executable-looking commands on the website.
