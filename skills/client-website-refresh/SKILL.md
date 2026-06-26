---
name: client-website-refresh
description: End-to-end Annabel website refresh harness for client sites. Use when auditing an existing business website, capturing what the client dislikes, planning a higher-standard redesign with Garry and Business Partner, creating or iterating an HTML preview, rebuilding into an editable platform such as Webflow, and preparing a client proposal with next steps and rates.
---

# Client Website Refresh

Use this when Annabel wants to repeat the Vital Health style website process for
another client: diagnose the existing site, capture the client's dislikes,
design a better version, iterate with builder runtime and Business Partner, rebuild it so the
client can edit it, and produce a clear proposal.

Annie owns intake and synthesis. Garry owns scope, offer, and client-facing
logic. Business Partner owns repo reality, QA, Webflow/build judgment, and
verification.

Related skills: `client-opportunity-map`, `decision-pipeline`,
`review-claude-plan`, `implement-approved-plan`, `webflow-rebuild-qa`,
`client-proposal-pdf`.

## Operating Loop

1. Read project docs and run memory recall for the exact client/task.
2. Create or identify a project folder under `projects/<client-or-project>/`.
3. Capture what the client said, what Annabel dislikes, and what is factually
   wrong with the current site before designing anything.
4. Run a **Brand DNA audit** before designing: pull from every channel the client
   already has (live site via Firecrawl `branding`, their logo, Instagram,
   Facebook, Google) and extract their real colors, type, shape language, voice,
   founders, and personality. Build FROM their identity, not Annabel's default
   lane. See [brand-dna-audit.md](references/brand-dna-audit.md). Separate visual
   taste, factual accuracy, conversion friction, SEO, and owner-editability.
5. Route strategy/scope through Garry before treating a redesign as a build plan.
6. Build an HTML preview or static mockup first when it helps Annabel and the
   client see the direction quickly.
7. Before showing Annabel any site or preview, run the Ship Gate in
   `projects/websites/design.md` against the actual built page and fix every
   failing item. Do not present and explain.
8. Send implementation/QA reality checks to Business Partner before claiming the
   site is ready.
9. Move the approved direction into the client-editable platform only after the
   preview direction is clear.
10. Prepare a short client proposal or next-steps PDF with explicit scope, rates,
    blockers, and client responsibilities.
11. Checkpoint the decisions and add good or bad examples when Annabel has to
    correct the same issue twice.

## References

- Run the **Ship Gate** in `projects/websites/design.md` against the built page
  before showing Annabel any site or preview. It is the binary pass/fail list for
  the craft hygiene she keeps having to repeat (real headings, no orphan
  subtitles, clean punctuation, clear/sourced images, honest nav).
- Read [brand-dna-audit.md](references/brand-dna-audit.md) FIRST on any new client
  build: how to audit all their channels and build from their real brand identity
  (colors, type, voice, founders) instead of the default house lane. Includes the
  Firecrawl `branding` recipe, the plain-titles rule, and the Vercel deploy gotchas.
- Read [workflow.md](references/workflow.md) for the full phase checklist.
- Read [html-preview-quality.md](references/html-preview-quality.md) before
  creating or polishing a static HTML preview.
- Read [client-question-bank.md](references/client-question-bank.md) during
  intake, discovery calls, and manager follow-ups.
- Read [good-bad-examples.md](references/good-bad-examples.md) before writing
  copy, building a mockup, sending a review link, or drafting a proposal.

## Guardrails

- Do not imply Annabel is replacing an existing backend, portal, EHR, booking,
  checkout, or vendor system unless the client explicitly asks for that.
- Do not publish to a live custom domain until placeholders, legal/medical
  claims, testimonials, links, mobile, and client approval blockers are resolved.
- Do not bury client-editability. If the site must be editable by the client,
  choose native CMS/platform fields over brittle custom code where reasonable.
- Do not use client-facing copy that violates Annabel's voice mechanics. No
  dashes as punctuation, no fake legacy language, no decorative clauses.
- When refreshing or rebuilding an existing client site, pull real copy from
  their current site first and reuse their actual phrasing (taglines, service
  descriptions, team bios) so it reads as a refresh of their voice, not a
  rewrite. Never invent biographical details (names, ages, backstories) for
  real, identifiable people shown in photos or video; keep such captions
  experiential or use the client's own published bios.
- Do not call a static preview ready until it has passed a visual human-polish
  pass on desktop and mobile, especially for generic AI-site tells.
- Do not present any site or preview to Annabel until the Ship Gate in
  `projects/websites/design.md` passes. Fix failing items first rather than
  presenting them with an explanation.
