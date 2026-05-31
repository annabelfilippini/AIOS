---
date: 2026-05-31
time: 10:45
project: revero-website-refresh
status: paused
next-session: Make `projects/revero-website-refresh/mockups/homepage-preview.html` look less AI-generated and more like a credible, polished virtual clinic site.
---

# Session: Revero HTML Preview Needs Human Polish

## What we worked on

- Tested the new `client-website-refresh` process on Revero.
- Audited the current site and created a claims matrix before writing mockup copy.
- Drafted a conservative homepage redesign spec.
- Built the first HTML preview at:
  `projects/revero-website-refresh/mockups/homepage-preview.html`
- Started a local preview server:
  `http://127.0.0.1:8028/homepage-preview.html`
- Browser-checked desktop and mobile. Only console issue was missing favicon.

## Decisions made

- Keep the first Revero preview conservative because the site is health care adjacent.
- Do not use "reverse disease," "heal," "get off meds," or patient outcome numbers in hero/proof copy.
- Treat onboarding, app, support, payment, labs, devices, and clinical workflow as external systems.
- Recommended primary CTA: `Get started`.
- Recommended secondary CTA: `Book a free info call`.

## Open questions

- Annabel's current reaction: the HTML exists, but the next goal is to make it look less AI-generated.
- Which direction should visual polish take: more premium clinical, more startup/health-tech, or more warm human clinic?
- Should the preview use more real Revero imagery, custom graphics, or a cleaner editorial layout with fewer stock/funnel cues?

## Next steps

1. Reopen `http://127.0.0.1:8028/homepage-preview.html` or restart the local server from `projects/revero-website-refresh/mockups`.
2. Review the current preview visually before editing.
3. Reduce AI-generated feel:
   - less generic card-grid rhythm
   - more intentional typographic hierarchy
   - less repetitive blue/white medical SaaS styling
   - better image composition and section pacing
   - more specific, less template-like microcopy
   - remove "Preview note" from the topbar or make it an internal-only comment
4. Keep the claims matrix constraints intact.
5. Re-QA desktop and mobile after edits.

## Context to preserve

- Core source files:
  - `projects/revero-website-refresh/audit/claims-matrix.md`
  - `projects/revero-website-refresh/strategy/homepage-redesign-spec.md`
  - `projects/revero-website-refresh/mockups/homepage-preview.html`
- Existing screenshots:
  - `projects/revero-website-refresh/mockups/revero-preview-desktop.png`
  - `projects/revero-website-refresh/mockups/revero-preview-mobile.png`
- The current preview is a safe first draft, not a finished visual direction.

## System refinement candidates

- Add a "less AI-generated website polish" checklist to `client-website-refresh`
  after the next session validates what actually improves the page.
