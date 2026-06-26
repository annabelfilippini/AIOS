---
date: 2026-06-07
time: 15:06
project: vital-health-webflow-review
status: in-progress
next-session: Convert the local Google reviews mock into a native Webflow CMS section, then decide whether the review sync should auto-publish or draft for approval.
---

# Session: Vital Health Google review feed direction

## What we worked on

- Continued Vital Health review work after the address, service pillar, shop routing, and homepage cleanup checkpoints.
- Discussed adding Google reviews/testimonials to the bottom of the homepage.
- Clarified that Annabel wants 5/5 star Google reviews only, shown as a scrolling bottom menu, without Vital Health manually entering each review.
- Updated the local static review page:
  - `projects/websites/vital-health-review/home-review.html`

## Decisions made

- Use 5-star individual Google reviews only. Do not refer to "4.9-star reviews"; 4.9 is an aggregate business rating, not an individual review rating.
- Avoid Elfsight/widget-style embeds for the preferred path because Annabel wants the section to feel native to the site.
- Recommended production architecture:
  - Google Business Profile API -> small scheduled sync -> Webflow CMS -> native scrolling review rail.
- Do not put Google/API secrets in frontend Webflow custom code.
- For the visual mock, use placeholder explanatory review cards rather than fake patient testimonials.
- Added a native scroll rail preview at `#google-reviews` with Google review labels, stars, reviewer/date metadata, and "View on Google" links.
- Changed the first auto-marquee attempt into a calmer horizontal scroll rail because the marquee left awkward empty space at some desktop moments.

## Open questions

- Whether Vital Health is comfortable auto-publishing public 5-star Google reviews directly, or whether the sync should create Webflow CMS drafts for clinic approval.
- Whether HIPAA/FTC posture requires explicit clinic/legal approval before republishing patient review text, even if the review is already public on Google.
- Whether the final Webflow section should include a visible "Read all reviews on Google" link and/or live aggregate rating count.
- Which hosting path to use for the sync script: Vercel cron, GitHub Actions scheduled workflow, Render cron, or Google Cloud Function.

## Next steps

- In Webflow staging, create a `Google Reviews` CMS collection with fields such as review ID, reviewer name, review text, star rating, review date, Google source URL, visibility/publish state, and optional service category.
- Rebuild the local `#google-reviews` rail natively in Webflow as a CMS Collection List.
- Ask Vital Health for Google Business Profile access or an authorized OAuth flow for the verified clinic listing.
- Write a small sync script that pulls Google Business Profile reviews, filters to `FIVE` star reviews with text, upserts by review ID into Webflow CMS, and publishes or drafts based on the chosen approval policy.
- Publish to Webflow staging only and QA desktop/mobile, footer positioning, scroll behavior, attribution links, and page performance.

## Context to preserve

- Current local preview URL: `http://127.0.0.1:8765/home-review.html#google-reviews`.
- Local server was started from `projects/websites/vital-health-review/` on port `8765`.
- Markup checks passed after the review-section edits:
  - `article 4/4`
  - `section 6/6`
  - `div 87/87`
- Browser DOM checks confirmed the review rail renders with 4 cards and horizontal overflow on mobile/default and desktop viewport sizes.
- The local review file remains untracked in AI-OS git status, consistent with the larger dirty-tree warning from earlier checkpoints.

## System refinement candidates

- Add a reusable client-website checklist item for testimonials/reviews: source, attribution, health/privacy risk, auto-publish policy, CMS fields, and third-party API secret handling.
