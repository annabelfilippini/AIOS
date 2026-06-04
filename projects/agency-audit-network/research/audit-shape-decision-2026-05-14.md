# Audit Shape Decision — what the paid audit should actually look like

Written: 2026-05-14
Purpose: reconcile every doc in `research/` (top-level synthesis files + `research/templates/`) into one set of decisions about the shape, structure, length, pricing, and naming of Annabel's paid audit. The new `research/templates/paid-audit-playbook.md` implements these decisions; this file is the rationale.

## What every doc agrees on (the spine — keep as-is)

These show up consistently across `aios-readiness-audit-offer-brief.md`, `audit-system-synthesis-2026-05-14.md`, `audit-system-synthesis-2026-05-14-bo-first-draft.md`, `mansel-aios-framework-2026-05-12.md`, and the Mansel Knowledge Base. They are not in tension. They become the audit's spine:

1. **The 4 Pods** — Acquisition / Delivery / Support / Operations. Same model in every doc. Use "pods" not "engines" (Mansel's current Skool vocabulary, and his community is one of the audiences).
2. **Fix the process before automating it** — Mansel's QDOAA sequence (Question → Delete → Optimize → Accelerate → Automate). Bo agrees. Mark Kashef agrees. The audit must surface this *before* recommending tools.
3. **Friction tags** — Time Sink / Wait / Quality Risk / Compliance Risk. Mansel's labels. Bo adds open-loop / closed-loop. All useful, all kept.
4. **Keystone identification** — the one step that, if broken, makes the rest moot. Mansel's framing; Bo and Mark both use the same logic.
5. **2×2 Opportunity Matrix** — Impact × Effort, with Quick Wins / Big Swings / Nice-to-haves / Deprioritize. Universal.
6. **The audit is not the final product — the 90-day slate is.** Every source says the audit *fails* unless it ends with a co-signed 2–3 Quick Wins plan with DoDs.
7. **Money Slide / ROI math is non-negotiable.** Mansel's calculator (hours saved × loaded $/hr + revenue uplift via reallocation) is the standard.
8. **One pod at a time.** Mansel's strongest rule. Don't audit four pods in one engagement.

## Where the docs disagree (the decisions to make)

### Decision 1 — Pricing

| Source | Recommendation |
|---|---|
| `aios-readiness-audit-offer-brief.md` | $300–$500 lightweight → $750–$1,500 polished |
| `mansel-aios-framework-2026-05-12.md` | Quick Read $0–$100, Deep Audit $300–$1,000, agency referral ~10% of $5K+ build |
| `audit-system-synthesis-2026-05-14.md` | Mansel's actual band for the audit alone: $10K–$70K (mid-market) |
| `paid-audit-playbook.md` (new) | $1.5K (solo) → $5K (small business) → $10K+ (product brand or mid-market department) |

**Decision: tiered by client shape, anchored on ROI Stack × 10–20%.**

- Solo / single employee: $1,500 floor. (Dad's employees fit here.)
- Small business 3–10 employees: $3K–$5K.
- Product brand (Cooldown shape): $5K–$10K.
- Mid-market department: $10K–$30K.

The $300–$500 placeholder in the offer brief was set before the full Mansel + Bo + Mark capture. The depth of the playbook now justifies higher pricing because the audit produces: living business-brain doc, Opportunity Matrix with DoDs, test harness specs for top 3 wins, 90-day slate, partner referral brief. That is not a $300 deliverable.

**First-engagement note.** Run 1–2 audits at the lower end of each band (or free in exchange for testimonial + case study permission) before locking pricing. The offer brief already says this — keep it.

### Decision 2 — How long is the audit document?

| Source | Recommendation |
|---|---|
| `templates/quick-read.md` | 1–2 pages, free, sales funnel |
| `audit-system-synthesis-2026-05-14.md` (Section 10) | 5-page Quick Read for v1 |
| `audit-system-synthesis-2026-05-14-bo-first-draft.md` | 6-page paid audit with 6-layer brain as centerpiece |
| `aios-readiness-audit-offer-brief.md` | 5–7 page report |
| `paid-audit-playbook.md` (new) | 8–12 pages in a living doc |

**Decision: two delivery formats from the same engagement.**

1. **Living Notion / Drive doc — 8–12 pages, default.** This is what the client keeps and updates. It's the artifact that makes the audit a *product*, not a one-off PDF that gets forwarded once and forgotten.
2. **PDF summary — 5 pages, exported from the living doc.** For when the client needs to forward something to their CFO or a vendor. Generated from the same content, formatted to print.

The video-audit option (Mark Kashef's $20K Audit Automation, where Gamma + 11Labs + n8n generate a 5-min personalized video) is **phase 2**. Build it after 5+ manual audits, when the playbook is stable. Mansel's "don't automate a broken process" rule applies to the audit itself.

### Decision 3 — Personal / Team / Company routing

| Source | Position |
|---|---|
| `aios-readiness-audit-offer-brief.md` | 3 explicit AIOS levels: Personal / Team / Company / "Cleanup before automation" |
| `mansel-audit-structure-check-2026-05-13.md` | Confirms Mansel doesn't separate these — Annabel's packaging |
| `paid-audit-playbook.md` (new) | Not addressed |

**Decision: routing layer for the website, output recommendation in the audit.**

The Personal / Team / Company / Cleanup framing is Annabel's. It's not Mansel's structure. Use it two places:

1. **Website mini-audit (free)** — visitor picks "for me / my team / my company." Routes them to the right paid tier.
2. **Paid audit Page 2 deliverable** — one of: *"You need a Personal AIOS"* / *"Team AIOS"* / *"Company AIOS"* / *"Cleanup first — your process is too broken to automate yet."* This is the headline recommendation that frames everything else.

This needs to be added to the new playbook. *(Open follow-up — see Section "Edits to the new playbook" below.)*

### Decision 4 — Deliverable identity (the deepest tension)

| Source | Position |
|---|---|
| Mansel (Knowledge Base + AIOS Consulting Playbook) | Deck / PDF — "5 non-negotiable slides" + Money Slide |
| Bo Sar | "Audit ≠ PDF. Audit = living document inside the client's workspace" |
| Mark Kashef (Module 6) | Audit as auto-generated personalized 5-min video with voice clone |
| `aios-readiness-audit-offer-brief.md` | 5–7 page report + 30-min review call |
| `paid-audit-playbook.md` (new) | Living doc + Quick Read PDF + future video option |

**Decision: Bo's framing wins.** The audit deliverable is a *living document* in the client's workspace. The Mansel-style deck is the *presentation* of the audit (what Annabel walks them through in the findings call), not the audit itself. The PDF is an *export* of the living doc for stakeholders who need a file to forward.

This is the single biggest shift from the offer brief. The offer brief says "5–7 page report" — that's an old framing. Update it.

### Decision 5 — Product name

| Source | Name |
|---|---|
| `aios-readiness-audit-offer-brief.md` | CTA: "**Find Your AI Operating System Starting Point**" — Paid: "**AIOS Starting Point Audit**" |
| Synthesis files | "Deep Audit" |
| `paid-audit-playbook.md` (new) | "Paid Audit Playbook" (internal name only) |

**Decision: keep the offer-brief name.** *AIOS Starting Point Audit* is good — it's specific, it's outcome-framed ("starting point" = before-the-build positioning), and it differentiates from generic "AI audit" competitors. The CTA *"Find Your AI Operating System Starting Point"* is the verb the website should use.

Internally Annabel can keep calling it "the paid audit" or "the Deep Audit" — that's fine for working docs. Client-facing it's *AIOS Starting Point Audit*.

### Decision 6 — Audit scope: founder-only vs founder + one team member

| Source | Position |
|---|---|
| `aios-readiness-audit-offer-brief.md` | Open decision — "whether the paid audit should initially be founder-only or optionally include one team member interview" |
| Mansel | Always interview stakeholders *separately* from end-users, even if it's the same small team |
| `paid-audit-playbook.md` | Both phases included (Phase 1 stakeholder + Phase 2 end-user) |

**Decision: include one end-user interview by default in the paid audit.** Mansel's strongest finding: the gap between what leadership *thinks* is happening and what's *actually* happening is where the dollars are. Even at the small-business tier, get 30 min with one frontline person who actually executes the workflow.

For the solo / single-employee tier, the founder is both stakeholder and end-user — but run the two phases in two separate conversations (stakeholder hat first, end-user hat second) so the answers are honest.

## The recommended audit shape (final)

A 1–2 week engagement that produces a living document in the client's workspace + a 30-minute findings call where Annabel walks them through it.

### Structure of the living document

| Page | Section | Source |
|---|---|---|
| **1** | Plain-English summary (3 sentences) + AIOS level recommendation (Personal / Team / Company / Cleanup) | Offer brief + Bo |
| **2** | Six-Layer Business Brain radar chart + scored current state | Bo |
| **3** | Pod scope (which one pod we audited, why, what's out of scope) | Mansel |
| **4** | Tagged process map of the audited workflow (Step Cards + 5 friction tags + open-loop check) | Mansel + Bo |
| **5** | Opportunity Matrix (2×2 + scored backlog with DoD + Kill criteria) | Mansel |
| **6** | Top 3 Quick Wins — each with DoD, Kill / Pivot, DRI assignment, test harness rules | Mansel + Bo |
| **7** | 90-day roadmap | Mansel |
| **8** | Money Slide — Cost of Inaction + projected savings + payback | Mansel |
| **9** | Partner referral brief (optional, if client wants build help) | Annabel |
| **10** | Maintenance recommendation (optional, sold separately if engaged) | Mansel |

Total: ~8–10 pages in Notion. Exportable to a 5-page PDF that strips the appendices.

### Engagement flow (1–2 weeks)

1. **Qualification call** — 20 min free. Apply Mark Kashef's red-flag screen (Module 3). If owner has never used Claude / ChatGPT, sell them a workshop, not an audit.
2. **Intake form** — async, sent before the interview. Captures business identity + 6-layer brain baseline + tool stack + KPIs at risk.
3. **Stakeholder interview** — 60–90 min with the owner / leader. Use Mansel's Phase 1 question set verbatim.
4. **End-user interview** — 30–60 min with one frontline person. Use Mansel's Phase 2 question set verbatim.
5. **Optional shadowing** — 30 min watching the workflow live. Strongly upgrades the confidence score in the Opportunity Matrix.
6. **Map + score (Annabel internal work)** — 4–6 hours. Build the living doc.
7. **Validation workshop** — 60 min. Walk the client through the Opportunity Matrix and the top 3 Quick Wins. Apply Mark's "Autopsy Protocol" before finalizing. *Don't end this call without a signed 90-day slate.*
8. **Findings presentation** — 30 min. Apply Mark's 5-part flight-plan structure (Sell the dream → Show the path → Announce the flight plan → In-flight service → Land the plane).
9. **Partner introduction (optional)** — if client wants build help, send the partner brief.

Steps 7–9 can collapse into a single 60–90 min final session for small-business engagements.

### Pricing decision (final)

| Client shape | Price | What's included |
|---|---|---|
| Solo / single employee | **$1,500** | One pod, founder-as-both-roles, 5-page PDF + living doc |
| Small business 3–10 | **$3K–$5K** | One pod, separate stakeholder + 1 end-user interview, full living doc |
| Product brand (Cooldown shape) | **$5K–$10K** | Two pods (Acquisition + Delivery), full playbook, optional video summary |
| Mid-market dept | **$10K–$30K** | Full playbook + sensitivity bands on Money Slide + partner-ready spec |

Anchor on Mansel's ROI Stack Worksheet: total annual value × 10–20%. The bands above are floors; if the ROI Stack number justifies higher, charge higher.

**First 2–3 audits at the floor (or free) in exchange for testimonial + case study permission.** Already in the offer brief, still right.

### Free funnel (`research/templates/quick-read.md`)

Keep the existing Quick Read as the free funnel. It does its job:
- 1–2 pages
- Sketches the AIOS in pod-shape
- Ends in a CTA to the paid AIOS Starting Point Audit
- 5 free Quick Reads cap during v1 (don't burn the funnel)

One update to make to `quick-read.md`: add a single radar-chart score of the 6-layer brain (0–5 each). It's the teaser for the deeper Bo-style assessment in the paid audit. *(Open follow-up — see below.)*

## Edits the new playbook should pick up

The new `research/templates/paid-audit-playbook.md` is 98% aligned with these decisions, but two updates are worth making:

1. **Add the Personal / Team / Company / Cleanup output recommendation to Page 1 of the deliverable structure (Section 15 of the playbook).** Right now Page 1 is "plain-English summary + radar chart." It should also be the place where Annabel commits to one of the four AIOS-level recommendations, framing everything that follows.
2. **Use the production-facing product name throughout.** Rename internal references to *"AIOS Starting Point Audit"* in client-facing language wherever the playbook talks about what the client receives.

## Open follow-ups for Annabel

These are decisions the docs don't settle and the new playbook doesn't address. Worth deciding before the first paid engagement:

1. **First pilot client** — Dad's employee (small-business / single-employee tier) is the cleanest first run. Run free in exchange for testimonial. Pilot the engagement flow above end-to-end.
2. **Notion vs Drive vs ClickUp** — pick one workspace where Annabel hosts the living document. Notion is the default; Drive is fine if the client uses Google Workspace. Decide once and template it.
3. **Quick Read update** — add the 6-layer brain radar to the Quick Read template as the upsell teaser.
4. **AnnabelFilippini.com mini-audit copy** — the 7–10 question free quiz on the website that routes Personal / Team / Company. Specs are in the offer brief (Section "Free Mini-Audit") but the actual questions haven't been written.
5. **Whether to reach out to Mansel directly** — already flagged in `mansel-aios-framework-2026-05-12.md` and the synthesis. Defer until Cooldown case study + first paid audit are both in hand.

## Why this shape works

It is opinionated where the docs disagree, conservative where they converge, and sized for Annabel's actual ICP (owner-operators and small businesses, not mid-market). It picks up the strongest contribution from each source — Mansel's depth, Bo's living-doc framing and 6-layer brain, Mark's video deliverable + flight-plan presentation — without trying to be all three at once. And it leaves room for the productization moat (Mark's video automation) to come *after* the manual playbook is proven, not before.
