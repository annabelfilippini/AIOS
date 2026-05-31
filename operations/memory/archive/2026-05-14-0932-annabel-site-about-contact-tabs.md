---
date: 2026-05-14
time: 09:32
project: agency-audit-network
status: active draft
next-session: Continue from `projects/agency-audit-network/site-draft/`; About, Contact, Work With Me, Skills, and Lab are all real source pages with wired nav.
---

# Session: Annabel Site - About and Contact Tabs

## What Changed

Added two standalone source pages:

- `projects/agency-audit-network/site-draft/about.html`
- `projects/agency-audit-network/site-draft/contact.html`

Updated nav links across:

- `index.html`
- `work-with-me.html`
- `skills.html`
- `lab.html`

Also changed the Work With Me agency partner CTA to route to:

- `contact.html#agency`

## About Page Direction

The About page is a credibility/story page. It uses the existing Annabel portrait and expands the homepage About copy into:

- AI, systems, and human judgment positioning
- University of Michigan School of Information
- incoming Okta Product Analyst
- AI-OS builder
- small business / audit work

## Contact Page Direction

Contact is a routing page, not a live form yet. It has three paths:

- Business owners -> `work-with-me.html#audit-start`
- Agencies -> `work-with-me.html#agency-partners`
- Collaborators -> `lab.html`

No personal email address, fake form submission, or payment link was added. Public contact/email/form destination still needs Annabel's choice before launch.

## Verification

Preview URL:

- `http://127.0.0.1:8765/projects/agency-audit-network/site-draft/`

Browser QA passed:

- Home, Work With Me, Skills, Lab, About, and Contact all load directly.
- About and Contact nav links exist on all six pages.
- About and Contact pages show active nav state.
- No browser console errors on the checked pages.
- Mobile check at 390px wide passed for Home, Work With Me, About, and Contact.
- Fixed the old Home/Work mobile behavior where nav links were hidden; they now use horizontal scrolling like the newer pages.

## Open Items

- Choose the real public contact destination: email, Tally, Typeform, Google Form, or custom static form backend.
- Choose Stripe/payment destination for the paid AIOS audit CTA.
