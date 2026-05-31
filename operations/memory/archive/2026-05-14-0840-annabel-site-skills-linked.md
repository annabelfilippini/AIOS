---
date: 2026-05-14
time: 08:40
project: agency-audit-network
status: paused
next-session: Continue polishing the standalone Skills page and decide when to export or publish the `site-draft` files.
---

# Session: Annabel Site — Skills page linked into site

## What we worked on

Continued the personal site Skills page work from the prior checkpoint:

- `operations/memory/checkpoints/2026-05-13-1140-annabel-site-skills-page.md`

Current browser page:

- `file:///Users/annabelfilippini/Documents/AI-OS/projects/agency-audit-network/site-draft/skills.html`

## Decisions made

- Skills should be a **standalone page**, not an inline section on the homepage.
- The page should showcase **skills Annabel uses**, not suggest Annabel helps others implement skills.
- The page should not imply that `skills.sh` is a real public executable command. It is currently visual language / metaphor only.
- The headline should read: **"The things I make repeatable."**
- The Skills page should be reachable from the site navigation.

## Files changed

- `projects/agency-audit-network/site-draft/skills.html`
  - Removed Annabel's portrait from the hero.
  - Made the large background `skills.sh` more transparent.
  - Shifted the large background `skills.sh` farther right so it does not overlap the white headline as much.
  - Changed headline from "The things I can make repeatable." to "The things I make repeatable."
  - Reframed hero and footer copy so the page is about Annabel's own skill library/workflows.
  - Added copy clarifying that `skills.sh` is a visual metaphor, not a public command yet.
  - Marked `AIOS Starting Point Audit` as an offer workflow from the agency audit project, not a standalone `SKILL.md` file.

- `projects/agency-audit-network/site-draft/index.html`
  - Updated the nav item `Skills` to link to `skills.html`.

- `projects/agency-audit-network/site-draft/work-with-me.html`
  - Updated the nav item `Skills` to link to `skills.html` instead of the old `index.html#skills`.

## Actual skills/workflows shown

Actual `SKILL.md` files represented:

- `skills/client-opportunity-map/SKILL.md`
- `skills/skool-intelligence-digest/SKILL.md`
- `agents/shared/skills/small-business-shopify-redesign/SKILL.md`

Workflow represented but not yet a standalone skill file:

- `AIOS Starting Point Audit` from `projects/agency-audit-network/`

## Important copy guardrails

Use:

> This is a library of the skills I use in my own work.

Avoid:

> Run this command to get access.

Avoid:

> I help people implement skills.

## Verification

- Confirmed `skills.html` exists.
- Confirmed `index.html`, `work-with-me.html`, and `skills.html` all link the Skills nav to `skills.html`.
- Prior local preview showed `skills.html` rendering and no browser console errors.

## Next steps

1. Refresh the in-app browser if the file view looks stale.
2. Decide whether the nav labels for Lab/About/Contact should become separate pages or remain placeholders.
3. If publishing/exporting a packed HTML, export from `site-draft` only after Annabel approves the current source files.

## System refinement candidates

- Generate the Skills showcase from real `SKILL.md` metadata in the future to avoid drift between public copy and actual capabilities.
- If `skills.sh` becomes real, define the exact local CLI behavior before using command examples publicly.
