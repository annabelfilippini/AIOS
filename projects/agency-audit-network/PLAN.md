# Agency Audit Network Plan

Created: 2026-05-12
Last updated: 2026-05-12 (rewritten after Garry/BP stress-test)

## Working Name

Agency Audit Network. Working name only — better external names later.

## The Bet

Most small businesses do not know what to ask an AI agency for. Many AI agencies do not know how to source qualified clients. Annabel can sit between them with a high-trust audit and earn from both the diagnosis and the routing.

The long-term shape is a multi-track audit + agency-matching network. The next 14 days are about proving one track works.

## v1 Scope (this is the only thing being built now)

**ICP — Track 1 only:**

Owner-operated product brands, often on Shopify, often Denver-based, roughly 2–20 people, ~$500k–$5M revenue, currently running zero or near-zero AI/automation. Cooldown is the prototype customer — the audit content should be specifically useful for businesses like theirs (product brands, e-commerce ops, owner doing too much).

**Distribution:** Cooldown referrals are the primary warm pipeline. Family network is a secondary v2 testing pool — those businesses tend to be larger and have more systems, which is a different audit shape.

**Out of scope until v2/v3:**

- 10–50 person businesses with some functional structure (added in v2 once Track 1 has 3+ paid audits and Annabel has buyer access)
- 100–500 person mid-market orgs (added in v3 only after Track 2 ships; full playbook from `Knowledge Base-20260406084428.md` fits here)
- Cold client outreach (warm business intros only in v1)
- Mass partner scraping or bulk DMs
- Self-serve marketplace, dashboards, partner membership fees

## Audit Shape — Two Tiers

v1 is two products that share a framework: a free **Quick Read** that demonstrates competence and a paid **Deep Audit** that delivers the diagnosis. The Quick Read qualifies and warms; the Deep Audit is the actual product. Tier 1 funnels into Tier 2.

The full mid-market audit playbook (`~/Downloads/Knowledge Base-20260406084428.md`) is built for 100–500 person orgs. It does not fit Cooldown-scale businesses. The framework is portable; the scaffolding is not.

### Tier 1 — Quick Read (free or token)

**Purpose:** Demonstrate competence + identify specific automation opportunities for one named business. Funnels into the paid Deep Audit.

**Format:** 1–2 pages, polished doc or PDF, sent to a named business. Personalized from their website (+ optional 15-min call).

**Content:**
- Brief read of the business (what they sell, who to, where they likely lose time)
- 3–5 specific automation components Annabel would build or recommend (customer support flow, post-purchase email, returns triage, ad ops, inventory automation, etc.)
- One-line "why this matters for you" per component
- Soft CTA: "Want the full version that prioritizes by ROI, scopes effort, and is ready to hand to an agency or implement yourself? $X for the Deep Audit."

**Production time target:** 30–90 min per Quick Read after the first.
**Price:** Free for first 5 (lead gen + credibility). Optional $50–$100 token after to qualify intent.
**Discipline:** Cap Quick Reads at 5 in v1. Do not become a free-work treadmill.

### Tier 2 — Deep Audit (paid)

**Purpose:** Thorough, agency-handoff-ready diagnostic. Prioritizes opportunities, quantifies impact, gives the business a real decision-making artifact.

**Keeps from the full playbook:**
- 4-engine map (Acquisition, Delivery, Support, Internal)
- Friction tags: time sink / wait-handoff / quality risk / compliance risk
- Opportunity matrix scoring (Impact × Confidence) with penalty for Effort/Risk
- Keystone identification ("if this fails, everything else collapses")
- ROI math: founder hours saved × hourly value
- DoD + Kill/Pivot per recommendation

**Drops from the playbook:**
- Multi-stakeholder sampling (1 owner interview, not 7–15)
- Department-by-department interview tracks
- Loaded $/hr math (use owner's hourly value)
- IT/Security/Legal gates
- 30-slide presentation (replaced by 5–7 page PDF)
- Sales/Marketing/Ops/Finance/HR/CS deep dives

**Cooldown-vertical sections (product brands specifically):**
- Customer support automation (email, chat, FAQ)
- Post-purchase flow (shipping comms, review requests, win-backs)
- Returns + CX triage
- Email/SMS marketing automation (Klaviyo and similar)
- Inventory + ops alerts
- Content + ad ops
- Internal SOPs and founder time leaks

**Format:**
- 60–90 min owner interview
- 1-page Ops Canvas (4 engines, friction-tagged)
- Top 5 opportunities scored on the matrix
- 1 keystone called out
- Simple ROI: hours saved/week × $value/hr × 52 + revenue uplift estimate
- 5–7 page PDF output, beautiful but not over-designed
- Closing recommendation: self-implement / phased / agency intro

**Production time target:** 4–6 hours per audit.
**Price:** $300–$1,000 in v1. Pilot 1–2 audits free in exchange for testimonial + permission to use as case study.

**v2/v3 audits add depth, not framework changes.** Companies with more employees and more systems (dad's network later, true mid-market eventually) need 2–3 stakeholder interviews and longer output. Same engine.

## Positioning

### For Businesses

"Get a clear, beautiful automation map of your business before you hire anyone. We find where AI can actually help, what to prioritize, and whether you should do it yourself or hand it to a vetted partner."

### For Agencies (v2+)

"Get warmer clients who already know what they want to automate, scoped to fit your specialty."

### For Annabel

"Own the trusted front door. Be the diagnostic and routing layer that businesses trust because the audit is sharper than what they'd get from an agency's free discovery call."

## Pricing Hypotheses (test in order)

1. **Quick Read (Tier 1):** Free for first 5. Token $50–$100 after, to qualify intent. Not the revenue product — the funnel.
2. **Deep Audit (Tier 2):** $300–$1,000. Anchor on dollars-of-waste found, not hours-of-work. If the Deep Audit identifies $20k/year of automatable manual work, $500 is cheap.
3. **Pilot Deep Audits:** First 1–2 free in exchange for testimonial + case-study permission.
4. **Agency referral fee:** 10% of first project revenue OR fixed $250–$1,500 success fee. Test which agencies actually agree to in writing.
5. **Premium advisory (v2+):** $500–$2,000 to scope, compare proposals, and choose between agencies.

Do not start with paid agency membership. That only becomes credible after demand exists.

## Unit Economics Sanity Check

Audit production time target: 4–6 hours.
At $500 audit fee, blended rate = $80–$125/hour. Acceptable but not lucrative.
At $1,000 audit fee, blended rate = $165–$250/hour. Good.

Audit alone is a thin business at small-biz scale. The real upside is:
- Agency referral revenue ($500–$3,000 per matched deal)
- Audit-to-advisory upsell (if even 20% of audit clients want ongoing help)
- Productized small-biz implementations Annabel runs herself later

Track all three from day one. If after 5 audits none of those three downstream revenue streams shows signal, kill or heavily revise.

## 14-Day Validation Sprint (2026-05-12 to 2026-05-26)

### Days 1–2 (May 12–13): Templates

- Draft `research/templates/quick-read.md` — the Tier 1 personalized snapshot template (1–2 pages, fillable)
- Draft `research/templates/deep-audit.md` — the Tier 2 paid audit template (5–7 pages, Cooldown-vertical sections)
- Both should be functional, not pretty yet. Polish during first real audit.

### Days 3–4 (May 14–15): First Quick Reads + Cooldown Deep Audit kickoff

- Send Quick Read to Cooldown (warm — they already know Annabel)
- Identify 2 dad-network or Cooldown-network candidates for Quick Reads (names: TBD — Annabel to fill in)
- Send Quick Reads to both
- Schedule 60–90 min Cooldown owner interview for the Deep Audit pilot

### Days 5–8 (May 16–19): Run Cooldown Deep Audit + push Quick Reads to conversion

- Run + deliver Cooldown Deep Audit (free pilot in exchange for testimonial + permission to use as case study)
- Follow up with Quick Read recipients: "Want the full Deep Audit? $X"
- Goal: 1 paid Deep Audit booked from the 2 Quick Read recipients

### Days 9–11 (May 20–22): Second Deep Audit + agency conversations

- Run audit #2 (whoever paid or pilot)
- Talk to 3–5 candidate agency partners (warm contacts only)
- Ask agencies: what client do you want, what referral terms would you accept in writing
- Goal: 2 written agency referral agreements

### Days 12–14 (May 23–26): Wrap and evaluate

- Deliver outstanding audit(s)
- Score against kill/continue gate
- Decide: continue Track 1, expand to Track 2, or kill

## Kill / Continue Gate (evaluate 2026-05-26)

**Continue if at least 2 of these are true:**

- 1+ business paid for a Deep Audit
- 2+ Quick Read recipients responded positively and asked for the Deep Audit
- 2+ businesses said they want an agency intro
- 2+ agencies signed a written referral agreement
- Cooldown referred at least one warm lead from their network

**Kill or heavily revise if:**

- 0 Deep Audits completed in 14 days
- Quick Reads got no responses or zero interest in upgrading
- Deep Audits take 10+ hours each (unit economics break)
- Clients said the audit was nice but did not lead to action
- Agencies wanted leads but rejected referral terms

## First Targets (Annabel to fill names)

### Candidate businesses

1. **Cooldown** (confirmed) — sample audit, free, testimonial in return
2. **TBD from dad's network** — paid audit attempt
3. **TBD from dad's network** — paid or pilot

### Candidate agency partners

Sourcing v1 (warm first, targeted partner research second):

- Friends/contacts already doing AI/automation work for small biz
- Operators Annabel met through Cooldown work
- Skool/community contacts she has actual relationships with
- Anyone Mansel or Mark have personally vouched for (not cold-found from their content)
- High-fit agency operators found in Annabel's subscribed Skool communities, using the `skool-press` CLI workflow in `research/skool-agency-sourcing.md`

Do not scrape Skool or LinkedIn for client cold outreach in v1. For agency partners, use public-first or explicitly approved authenticated research only, verify candidates through public sources, and send small-batch, specific outreach.

## Agency Partner Pool — Notes

Small-biz audits do not match the typical "big AI agency" customer profile. Right pool for Track 1:

- Shopify automation specialists
- n8n / Make / Zapier operators serving small biz
- Fractional ops consultants who already serve $1M–$5M businesses
- AI generalists who have shipped 5+ small-biz implementations

Not the right pool for Track 1 (save for v3):

- Enterprise AI consultancies
- Big-firm automation practices
- Mid-market change management agencies

Track partner candidates in `partners/` using `research/templates/agency-partner-scorecard.md`.
For Skool-sourced candidates, start with `research/templates/skool-agency-candidate.md`, then promote strong candidates into the full agency partner scorecard.

## Risks (named, ranked)

1. **Audit takes too long to produce.** If 4–6 hours becomes 12+, unit economics break. Mitigation: hard time-box the first audit on Cooldown and measure.
2. **Audit feels nice but doesn't lead to paid action.** Mitigation: every audit ends with a concrete next-step option (self-implement / agency intro / scoped advisory).
3. **Agencies want leads but won't pay.** Mitigation: written referral terms before sending any lead. If agencies won't sign, the network half of the business is broken — re-evaluate.
4. **Cooldown's referral pipeline is one-shot if mishandled.** Mitigation: over-deliver on the Cooldown audit and the first dad-network audit. These two outputs are the marketing for everything that comes next.
5. **"Beautiful audit" turns into design time-sink.** Mitigation: cap design polish at 1 hour per audit. Use a template, swap content.
6. **Compliance/disclosure on referral fees.** Mitigation: simple disclosure line on the audit ("if we introduce you to an agency, we receive a referral fee") and written agreements with agency partners.

## First Assets To Build

1. `research/templates/quick-read.md` — Tier 1 personalized snapshot template (1–2 pages)
2. `research/templates/deep-audit.md` — Tier 2 thorough paid audit template (5–7 pages, Cooldown-vertical)
3. Sample Deep Audit PDF on Cooldown — the marketing centerpiece
4. Update `research/templates/client-audit-request.md` to fit small-biz intake (already close — trim it)
5. Update `research/templates/agency-partner-scorecard.md` to match the Track 1 partner pool (mostly fine)
6. `research/templates/skool-agency-candidate.md` — quick capture template for Skool-sourced agency operators
7. One-page referral agreement draft for agency partners
8. Simple landing page or one-pager — Quick Read offer first, Deep Audit + matching second

## Relationship To Existing Projects

- `projects/website-audit/` — borrow workflow, quality bar, visual packaging. Do not treat as source of truth for marketplace mechanics.
- `projects/consulting/` — borrow AI operating-system thinking and owner pain patterns. Do not duplicate.
- `~/Downloads/Knowledge Base-20260406084428.md` — the full mid-market audit playbook. Reference for framework, not for v1 execution. Consider moving into `research/` for durable reference.

This project owns:

- Small-biz audit shape (v1)
- Partner network sourcing and vetting
- Referral economics and written agreements
- Audit-to-agency matching mechanics
- Eventual track expansion (v2, v3)

## Immediate Next Steps

1. Move `Knowledge Base-20260406084428.md` from Downloads into `research/` so it's durable
2. Draft `research/templates/quick-read.md` (Tier 1 — fastest to build)
3. Draft `research/templates/deep-audit.md` (Tier 2 — Cooldown-vertical sections)
4. Send first Quick Read to Cooldown
5. Identify and name 2 Cooldown-network or dad-network candidates for Quick Reads
6. Schedule 60–90 min Cooldown owner interview for the Deep Audit pilot
7. Add Mansel's Skool community URL to `operations/annabel-press/skool/accounts.json`
8. Run the Skool public-only sync; use authenticated sync only with Annabel-approved session export
9. Create 10–20 Skool agency candidate notes, then pick 5 to verify manually before outreach
10. Deliver Cooldown Deep Audit by end of week 1
