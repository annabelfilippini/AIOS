# Skool Agency Sourcing Workflow

Created: 2026-05-12

## Goal

Use Annabel's subscribed Skool communities, especially Mansel and Mark's accounts, to find active people who appear to run AI agencies, then qualify them as potential implementation partners for the Agency Audit Network.

The output is not a raw member dump. The output is a short list of agency candidates with evidence, fit notes, and a respectful outreach path.

## CLI Connection

Use the canonical Skool CLI connection:

```bash
node operations/annabel-press/scripts/skool-press.mjs status
node operations/annabel-press/scripts/skool-press.mjs sync --public-only
node operations/annabel-press/scripts/skool-press.mjs sync
```

Current known config:

- `operations/annabel-press/skool/accounts.json`
- `operations/annabel-press/app/data/skool.js`

Current account configured:

- Early AI-dopters / Mark Kashef: `https://www.skool.com/earlyaidopters`

Still needed:

- Mansel's Skool community URL.
- Annabel approval/session method if authenticated member-only data is needed.

## Safety Rules

- Run public-only sync first.
- Use authenticated sync only after Annabel explicitly approves the session method.
- Do not store Skool passwords, cookies, tokens, or exported sessions in AI-OS.
- Do not save raw private member content as durable project material.
- Do not bypass access controls, paywalls, rate limits, or platform protections.
- Prefer candidate summaries, profile links, and evidence snippets over full scraped archives.
- Treat Skool DM/contact data as private unless the member has made a business contact path public.
- Use opt-out-friendly, specific, one-to-one outreach.

## What To Look For

High-signal agency indicators:

- Bio says agency, automation studio, AI consultant, implementation partner, no-code agency, Make/Zapier/n8n specialist, Clay specialist, GoHighLevel specialist, or AI systems builder.
- They post case studies, build breakdowns, client wins, workflow diagrams, templates, or walkthroughs.
- They answer other people's technical questions with useful implementation detail.
- They mention a niche: coaches, med spas, dentists, real estate, ecommerce, local service businesses, B2B outbound, recruitment, or similar.
- They link to a website, LinkedIn, X, YouTube, newsletter, or booking page.
- They show capacity and willingness to take clients.

Low-signal or skip indicators:

- Pure course consumer with no proof of implementation.
- Generic "AI enthusiast" profile.
- No public contact path.
- Spammy self-promo without examples.
- Unclear pricing, niche, or delivery style.

## Candidate Tracker

Use `research/templates/skool-agency-candidate.md` for each promising partner and save notes in `partners/`.

Minimum fields:

- Person/agency name.
- Skool profile/community source.
- Why they seem active.
- Agency evidence.
- Specialty.
- Public contact path.
- Fit score.
- Outreach status.

## Manual Workflow

1. Confirm the target Skool communities in `operations/annabel-press/skool/accounts.json`.
2. Run `skool-press status`.
3. Run public-only sync to check shape and visible signals.
4. Review the generated Skool data for account-level signals and useful links.
5. If public-only data is not enough, ask Annabel to approve an authenticated sync using a temporary local session export.
6. Identify people who appear to run agencies.
7. For each candidate, verify with public sources before outreach.
8. Create a partner note from `research/templates/skool-agency-candidate.md`.
9. Send a small number of personalized messages, not a blast.
10. Track who replies, who is credible, and who accepts referral terms.

## Outreach Angle

The ask should be partner-oriented, not client-begging:

> I'm building a small audit-led referral network for businesses that want AI automation but need help choosing the right implementation partner. I noticed you seem active in [community] and work on [specific specialty]. Are you open to being considered for matched client referrals if the fit is right?

## First Pass Target

- 2 communities: Mansel and Mark.
- 20 candidate profiles.
- 10 verified public contact paths.
- 5 outreach messages.
- 3 agency interviews.
- 1 written referral-fee conversation.

