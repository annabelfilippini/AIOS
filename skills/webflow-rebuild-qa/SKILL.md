---
name: webflow-rebuild-qa
description: Webflow rebuild and QA workflow for turning a static HTML or Vercel preview into a client-editable Webflow site, using Vital Health lessons about Designer limits, Data API reliability, staging-only publish, CMS/editability, mobile QA, link checks, placeholder blockers, and client review readiness.
---

# Webflow Rebuild QA

Use this when a client site preview, static HTML mockup, or Vercel build needs to
be rebuilt, checked, or prepared inside Webflow so the client can edit it.

Related skills: `client-website-refresh`, `review-claude-plan`,
`implement-approved-plan`.

## Non-Negotiables

- Treat Vercel/static HTML as a preview unless the client explicitly wants a
  custom-code site.
- Webflow CLI/API cannot turn static HTML into editable Designer pages. Rebuild
  the design in Webflow using the preview as reference.
- Publish to `.webflow.io` staging first. Do not publish to a custom domain
  unless Annabel explicitly approves live launch.
- Prefer native Designer/CMS fields for content the client will edit.
- Use custom code only for polish or behavior that does not need routine client
  editing, and name that tradeoff.
- QA the published staging site on desktop and mobile before sharing it.

## Workflow

1. Read the client/project docs, current preview, Webflow status, and blockers.
2. Identify source of truth: live current site, static preview, snapshot files,
   assets, client notes, and approved copy.
3. Map which elements must be client-editable: pages, bios, services, resources,
   announcements, testimonials, promotions, contact details.
4. Rebuild layout natively in Webflow where editability matters.
5. Use CMS collections only where repeatable client-owned content benefits from
   structure.
6. Use Data API for reliable site/page/CMS/script/publish operations when
   available.
7. Use Designer element/style work in focused bursts. If calls timeout, retry
   with the Designer tab foregrounded.
8. Publish to staging, cache-bust, and verify the published output.
9. Run the QA checklist and report blockers plainly.

## References

- Read [qa-checklist.md](references/qa-checklist.md) before sharing a staging
  link or calling a site ready.
- Read [webflow-gotchas.md](references/webflow-gotchas.md) when using Webflow
  Designer, CLI, Data API, scripts, or staging publish.
- Read [good-bad-examples.md](references/good-bad-examples.md) for Vital Health
  examples to repeat or avoid.
