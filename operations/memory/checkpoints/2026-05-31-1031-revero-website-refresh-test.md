---
date: 2026-05-31
time: 10:31
project: revero-website-refresh
status: initial-audit-complete
next-session: If Annabel wants to continue, build a claims matrix first, then draft a homepage redesign spec before any HTML preview.
---

# Session: Revero Website Refresh Harness Test

## What we did

Tested the new `client-website-refresh` process on https://www.revero.com/.

Created:

- `projects/revero-website-refresh/CLAUDE.md`
- `projects/revero-website-refresh/audit/intake.md`
- `projects/revero-website-refresh/audit/current-site-audit.md`
- `projects/revero-website-refresh/strategy/redesign-brief.md`
- local source captures for Home, About, Membership, FAQ
- desktop and mobile browser QA screenshots and snapshots

## Main findings

- Revero has a strong underlying offer: virtual clinic, medical care, nutrition
  therapy, coaching, remote monitoring, and app-based support for chronic
  conditions.
- The site feels like a conversion funnel that accumulated duplicate sections,
  repeated CTAs, old hidden builder blocks, and uneven copy.
- Browser QA found 53 H1 elements total on the home page, 23 visible H1s on
  desktop, four visible Join Now labels, and four visible Free Info Call labels.
- The first accessible region is cookie consent, which weakens the first
  impression.
- Health claims and testimonials need a claims matrix before any redesign
  amplifies them.
- Recommended scope shape: Website Trust Refresh + Enrollment Flow Coordination,
  not a replacement for onboarding, app, support, payment, or clinical systems.

## Process refinement

Updated `skills/client-website-refresh` references to add a mandatory claims
matrix for health, wellness, finance, legal, and other trust-sensitive sites.

Logged material skill use with Annabel Press.

## Next steps

1. Ask Annabel whether to continue to claims matrix and redesign spec.
2. If yes, extract every claim/testimonial/pricing/availability statement into a
   matrix.
3. Draft homepage redesign spec.
4. Only then build an HTML preview.
