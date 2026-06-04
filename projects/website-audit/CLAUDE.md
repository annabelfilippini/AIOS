# Website Audit — CLAUDE.md

Personalized website audit service for small businesses. Three-part deliverable: audit + redesign mockups + dashboard preview. Manual-first approach — walk through every step with Annabel, create skills only after successful runs.

## Current Canonical Skills

Use the top-level AI-OS skills for new client website refresh work:

- `client-website-refresh` — Annie-led end-to-end harness for intake, client dislikes, audit, Garry scope, HTML preview, Business Partner QA, editable-platform build, and proposal.
- `webflow-rebuild-qa` — Business Partner/Webflow lane for rebuilding static previews into editable Webflow sites, staging QA, blockers, and live-publish readiness.
- `client-proposal-pdf` — proposal PDF lane for phases, rates, honest ranges, hosting costs, blockers, and next steps.

The older `.claude/commands/audit-*` pipeline remains useful source material for scrape, SEO, AI discoverability, mockup, package, cleanup, outreach, and video work. For high-touch client implementation, start with `client-website-refresh` and pull command details only when needed.

## Build Plan

Build plan at `BUILD-PLAN.md` in this directory.

## Target Market

- Small athletic brands (clothing, equipment) in Ann Arbor and Denver
- Restaurants in Ann Arbor and Denver

## Revenue Model

1. **Free video audit** (60-90 sec, automated) — the hook
2. **Paid detailed audit report** ($200-500, semi-automated) — the product
3. **Implementation** ($1,000-3,000, manual) — the upsell

## Kill Gate

20 personalized audits sent in 2 weeks. Fewer than 3 conversations = kill.

## Approach

Walk-through-first (Ras Mic methodology): do the full workflow manually with Claude, get every step right, then create skills from the validated run. Recursively improve skills on subsequent prospects.

## Current Phase

Manual walk-through on Pepper Pong. Steps 1-7 complete, Steps 8-9 skills drafted (provisional until validated on real send). All 9 skills exist at `.claude/commands/` (audit-scrape, seo, analyze, redesign, dashboard, package, cleanup, outreach, video). `/audit-cleanup` runs as Step 7.5 — post-deploy asset/size verify. Pepper Pong portal live at https://pepper-pong-audit.vercel.app. Outreach draft written as template (hypothetical — Tom is Dad, not sent). Next: Annabel records Pepper Pong video → Phase B upload validates `/audit-video`. Prospect #2 validates `/audit-outreach` on a real send.

Vital Health validated the higher-touch refresh lane: current site/mockup review, client feedback capture, Webflow rebuild for client editability, staging-only QA, placeholder/claim blockers, then a concise proposal PDF with phases and rates. Preserve those lessons in the canonical skills above.

## Reference Files

These are source material, not dependencies:
- `projects/ai-site-audit/cooldown-audit.md` — gold standard audit output
- `projects/ai-site-audit/cooldown-outreach-draft.md` — proven email copy/tone
- `projects/annie-intake/scripts/email-briefing.py` — Gmail SMTP pattern
- `projects/annie-intake/src/router.py` — service architecture pattern

## Conventions

- Quality over volume — the Cooldown audit converted because it was specific, not because it was automated
- Every prospect gets Annabel's review at every step before delivery
- Deliverable deployed to Vercel as a branded landing page with all three parts
- CAN-SPAM compliant when using email: unsubscribe link, physical address, honest subject lines
- Delivery channel is whatever's natural (text, DM, email) — not automated blasts
