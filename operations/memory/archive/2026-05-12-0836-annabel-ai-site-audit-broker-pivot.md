# Checkpoint: Annabel AI Site Audit Broker Pivot

Date: 2026-05-12
Project: `projects/consulting/prospects/cooldown/annabel-ai-site`

## Current Direction

Annabel's personal site is shifting away from "I implement websites and automations" toward a more scalable role:

> AI business auditor + implementation matchmaker.

Annabel does **not** want to become the Cooldown-style implementer who gets stuck fixing bugs, QA issues, Shopify edge cases, and client revision loops. The better lane is to own:

- the diagnostic layer
- the audit/report
- prioritization and roadmap
- client trust
- agency matching
- optional light advisory over implementation quality

Agencies should do the build work. Annabel can potentially charge for the audit and/or receive transparent referral revenue from agencies when she sends them qualified implementation clients.

## Knowledge Base Source

Annabel provided:

- `/Users/annabelfilippini/Downloads/Knowledge Base-20260406084428.md`
- Source community mentioned: `https://www.skool.com/ainative`

The knowledge base contains a strong AI audit methodology:

- stakeholder interviews
- end-user workflow interviews
- process/workflow mapping
- 4 business engines: Acquisition, Delivery, Support, Internal
- friction tags: time sink, wait/handoff, quality risk, compliance/data risk
- keystone step selection
- QDOAA: Question, Delete, Optimize, Accelerate, Automate
- opportunity matrix scoring
- reality-check workshop
- 90-day roadmap
- value/ROI slides

This can become Annabel's audit product and method page.

## Offer Concept

Possible core offer:

> I audit small businesses for practical AI opportunities, turn the findings into a clear roadmap, and connect owners with the right implementation partner.

Possible simpler line:

> I help small businesses figure out what to automate, what not to automate, and who should build it.

Potential deliverables:

- business snapshot
- website/customer journey review
- workflow map
- automation opportunity matrix
- top 3 quick wins
- 90-day roadmap
- ROI/value summary
- agency-fit recommendation
- implementation brief the owner can hand to an agency

Potential revenue streams:

1. Paid audit from the business.
2. Transparent referral fee or revenue share from implementation agencies.
3. Optional advisory retainer where Annabel reviews progress and protects scope, without being the bug fixer.

Important: avoid public language like "monopoly among agencies." Public framing should be "trusted implementation partner network" or "agency matchmaker."

## Site Structure State

The site has been split from one long page into a small static multi-page site:

- `index.html`
- `website-audit.html`
- `ai-systems.html`
- `toolkit.html`
- `lab.html`
- `about.html`
- `contact.html`

Shared assets:

- `styles.css`
- `script.js`
- `assets/img/annabel-headshot-cutout-web.png`

Current local preview:

- `http://127.0.0.1:4174/index.html`

The local server was restarted on port `4174` with:

```bash
python3 -m http.server 4174
```

from:

```text
projects/consulting/prospects/cooldown/annabel-ai-site
```

## Current Homepage Flow

Annabel likes Jenna Kutcher's site flow:

- hero with person centered
- giant name behind portrait
- page flows down from portrait into a big paragraph section
- circular "nice to meet you" badge overlapping the transition
- bold editorial text with colored/highlighted words

Current home page now follows that flow:

- hero still shows Annabel's cutout portrait with oversized `Annabel / Filippini`
- top hero kicker: `Michigan grad • Okta analyst • AI builder`
- left callout: `I love tinkering with AI...`
- right callout: `...and making it useful for real businesses.`
- CTA buttons: `Send me your website` and `Explore my skills`
- immediately below hero: `home-about` section
- overlapping circular badge says `AF` in the center and `NICE TO MEET YOU` around the ring
- badge rotates via CSS animation and respects `prefers-reduced-motion`

Home about copy currently says:

> I am a University of Michigan School of Information graduate who studied Information Analysis: the collaboration of technology, people, data, and design.

> Now I am starting at Okta, geeking out over AI, and helping small businesses use new tools to work more on the business, not only in it.

Snapshot pills:

- Michigan School of Information
- Incoming Okta Product Analyst
- AI systems + website audits

## Recent Files Changed

Primary files:

- `projects/consulting/prospects/cooldown/annabel-ai-site/index.html`
- `projects/consulting/prospects/cooldown/annabel-ai-site/styles.css`

New pages created earlier in this session:

- `projects/consulting/prospects/cooldown/annabel-ai-site/website-audit.html`
- `projects/consulting/prospects/cooldown/annabel-ai-site/ai-systems.html`
- `projects/consulting/prospects/cooldown/annabel-ai-site/toolkit.html`
- `projects/consulting/prospects/cooldown/annabel-ai-site/lab.html`
- `projects/consulting/prospects/cooldown/annabel-ai-site/about.html`
- `projects/consulting/prospects/cooldown/annabel-ai-site/contact.html`

Note: this project sits under `projects/`, which is ignored by the root `.gitignore`, so root `git status` may not show changes.

## Verification

Verified:

- `http://127.0.0.1:4174/index.html` returns `200 OK`
- in-app browser loads the homepage
- DOM contains the new AF badge/about content
- browser console reported no errors after the latest homepage check

Screenshot capture in the browser plugin has sometimes timed out, but DOM/title/console checks worked.

## Next Best Steps

1. Visually review the current hero-to-about flow in the in-app browser.
2. Tune the about copy to sound more Annabel and less formal.
3. Decide whether the site should pivot fully to "AI Audit + Agency Matchmaking" as the primary offer.
4. Rework the page architecture around the new business model:
   - Home
   - Get an Audit
   - What You Get
   - For Agencies
   - Method / Toolkit
   - Lab / About
   - Contact
5. Turn the knowledge base into Annabel's branded audit methodology without copying private community language too directly.
6. Design the audit output concept: gorgeous report, opportunity matrix, 90-day roadmap, agency handoff brief.
7. Add a future "For Agencies" page that explains partner criteria, referral expectations, and how agencies receive implementation-ready leads.

## Open Questions

- Should "Website Audit" remain a standalone service, or become one component of the broader AI Business Audit?
- Should the homepage headline shift from personal-intro first to offer-first?
- What should the paid audit be called?
  - AI Opportunity Audit
  - Small Business AI Audit
  - AI Systems Audit
  - Business Automation Audit
  - Practical AI Roadmap
- How transparent should referral/revenue share language be on the public site?
- Should Annabel remain lightly involved during implementation as a client-side advisor?
