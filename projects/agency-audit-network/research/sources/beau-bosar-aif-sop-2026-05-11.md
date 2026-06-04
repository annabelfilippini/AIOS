# Bo Sar — How to Sell the AI-First Framework as a Service (full delivery SOP)

Captured: 2026-05-14
Source: https://www.youtube.com/watch?v=6ZhELfCPl40
Channel: Bo Sar (@bo-sar) — Bogdan Bosar, AI-First Academy (aif.academy)
Published: 2026-05-11 · Length: 35:42 · Views at capture: 2,522 · Likes: 118

## Why this matters for Annabel's audit work

Bo's video is the closest public articulation of the same audit-then-implement model Annabel is building (Audit → Build → Train → Maintain). Two things are directly transferable: (1) the **six-layer business brain** as a structuring concept for what an audit should map, and (2) the **three-tier pricing ladder** which separates DIY/static brain from full-service/live brain.

## Headline framework: AI-First delivery in 6 phases over 30 days

| Phase | What happens | Key deliverable |
|-------|--------------|-----------------|
| 0. Setup | Client pays, gets questionnaire + 33-lesson curriculum. Audit plug-in starts mapping skills/agents from questionnaire | Draft workspace blueprint by day 3 |
| 1. Discovery | One 90-min call w/ owner + key leads, recorded via Fathom/Fireflies | Audit doc: plain-English summary + process map + automation priorities + department blueprint + 90-day roadmap |
| 2. Business brain build | Build the static or live brain (see layer model below) | Workspace queryable by Claude |
| 3. Install | 60–90 min screen share to clone workspace, install MCPs, wire CLAUDE.md hooks. Co-work clients: one-click plug-in pack install | Working system on client's machine(s) |
| 4. Skills + workflows | Build skills/agents/workflows for 1–2 highest-leverage departments (usually sales/outreach, marketing, or client onboarding) | At least one fully running department, 5+ skills, 1–2 workflows, daily morning brief |
| 5. Team training | 3 × 90-min workshops (recorded → onboarding material for future hires) | Team operating as "standard setters" instead of executors |
| 6. Handoff | Three artifacts shipped | Runbook + escalation matrix + skill catalog |

After handoff → retainer pitch ($2.5K–5K/mo): maintain brain + build hours + advisory.

## The six layers of the "business brain"

Every business brain has the same six layers regardless of industry. The contents differ; the structure doesn't. This is the auditing scaffold.

1. **Identity** — Mission, products, ICP, brand voice, founder POV. Almost never changes. Answers "who are we and what do we sell."
2. **Critical context** — What's true right now: quarterly goals, active campaigns, current team roster, current pricing, deals in flight. Refreshes monthly/quarterly.
3. **Working memory** — What's in flight this week: current sprint, in-progress deals, this week's content calendar. Doesn't persist past the week.
4. **Episodic memory** — The *why* behind decisions: why we paused outbound to X, why we doubled down on Y segment, why we fired Z vendor. The layer that compounds most over time. This is what companies forget at employee turnover.
5. **Long-term knowledge** — Playbooks, won/lost deals, case studies, customer interviews.
6. **Background decay/promotion** — Data decays automatically; frequently-cited data gets promoted up the layers. Keeps the brain healthy without manual gardening.

**How Claude actually uses the brain (progressive disclosure):**
- Identity loads at every session start (via `session-start` hook)
- Critical context loads at session start (via `session-start` hook)
- Working memory loads on demand
- Long-term knowledge gets searched only when the question calls for it
- Search layers keyword + semantic + entity matching (so "Acme" finds the call even if the rep wrote "declined")
- A `pre-compact` hook ensures critical context survives Claude's compression of long sessions
- Without hooks, CLAUDE.md is probabilistic (~9 of 10). Hooks make memory deterministic.

## Static brain vs. live brain (the pricing differentiator)

| | Static brain | Live brain |
|---|--------------|------------|
| Audience | Solopreneurs, small business | Teams, mid-size + |
| Update mechanism | Owner edits manually (or asks Claude to save) | Auto-ingestion via webhooks |
| Tech stack | CLAUDE.md hierarchy + manual KB | Cloudflare workers → private GitHub vault → client machine pull |
| Sources auto-fed | None | Fathom/Fireflies, HubSpot/CRM, Slack, GitHub, etc. |
| Maintenance | Light: periodic CLAUDE.md drift review | Heavy: hosting, token rotation, webhook refresh jobs, API drift adaptation, failure monitoring + dead-letter queue, backfills, new-source onboarding, filter-rule tuning |
| Retainer fit | Optional | Mandatory |

The live-brain piece most agencies underprice/underexplain is *maintenance* — it's the defensible, recurring revenue piece.

## Pricing tiers

- **Tier 1 — DIY ($5K–$8K):** Client builds static brain themselves via pre-recorded modules. You do one install screen share + one fully running department. Weekly group community call for 6 months, uncapped attendance (economics work because it's 1 hr/wk regardless).
- **Tier 2 — Full service ($10K–$25K):** Anchor tier, where most engagements should land. You build live brain + auto-feed layer + two departments. 1:1 sessions throughout. Custom webhooks, real engineering, compounding brain.
- **Tier 3 — Premium ($25K+, plus travel):** Compressed into one intensive week, on-site install + workshops. For large teams or regulated industries.
- **Retainer ($2.5K–$5K/mo):** Maintenance + build hours + advisory access. Mandatory for Tier 2/3 live-brain clients.

## The discovery call asks for four things

1. **Actual process map** — where workflows live and where they break
2. **Department structure** — real or aspirational
3. **Imagination gap** — what they wish was possible but assume isn't
4. **Tools/platforms** — what they already use that have APIs to wire into

## Audit document structure (Bo's version)

One file with two layers stacked:
- **Top layer:** Plain-English summary the owner can show to leadership
- **Underneath:**
  - Process map
  - Automation priority list
  - Department blueprint
  - 90-day roadmap

Lives in the client's workspace as a **living document**, not a one-time PDF. Updates as departments are added.

## "Plug-in pack" model (for Claude Co-work clients)

Per-vertical bundles: agencies, e-commerce, coaching, services. Each pack bundles preconfigured skills + connector permissions + department structures. Published to a private marketplace. One-click install per team member. Bo is dedicating his next video entirely to this.

## Asset library (what makes this scale to 10+ clients)

Five categories:
1. Pre-recorded curriculum — 33 click-by-click lessons across foundations + concepts + Claude Code
2. Prompts + templates — discovery questionnaire, audit doc template, audit plug-in, process map template, runbook, escalation matrix, skill catalog, KPI tracker
3. Department starter packs — marketing, sales, delivery, operations, finance, client management
4. Co-work plug-in packs — industry-specific, installable in one click
5. Workshop decks — three 90-min sessions, slide by slide

The argument: without 80% prebuilt, you can't take on more than 1–2 clients without burning out.

## Roles model Bo introduces in Workshop 2

Borrowed from Jack Dorsey's reorg:
- **IC (individual contributor)** — anyone in the company who *builds*
- **DRI (directly responsible individual)** — owns a specific outcome

The mental shift: team members are no longer the people who execute every task. They define the standards. AI iterates against those standards. They monitor output and refine standards.

## Direct lifts for Annabel's audit

1. **Adopt the six-layer brain as the audit's mental model.** When auditing Dad's employees, every gap can be tagged to a layer (e.g., "no episodic memory layer — institutional knowledge walks out the door").
2. **Two-tier audit output, mirroring Bo's audit doc.** Plain-English summary on top, structured detail underneath. Already in your Quick Read template — extend the Deep Audit to match.
3. **"Living audit" framing.** Position the Deep Audit as a living document inside the client's workspace, not a static PDF. This is a Bo idea that pairs directly with Mansel's pod-mapping approach.
4. **Discovery call = the four questions above.** Cleaner than a free-form interview.
5. **Pricing ladder template.** Don't try to invent pricing tiers — adapt Bo's static/live distinction. Audit Quick Read = pre-Tier 1. Audit Deep = Tier 1 anchor. Implementation referrals to partners = Tier 2+.
6. **Plug-in pack thinking for verticals.** Dad's employees / product brands could each get a starter pack tailored to their vertical.

## Open questions to take into the Mansel sweep

- Does Mansel's "pod" model map cleanly onto Bo's "department" model? Best guess: yes (Acquisition/Delivery/Support/Operations ≈ Sales/Delivery/Client Mgmt/Ops).
- Mansel's "Context Audit" blueprint vs. Bo's "audit document inside the workspace" — same artifact, different name? Worth comparing once we have Mansel's blueprint captured.
- Bo says hooks make CLAUDE.md memory deterministic. Mansel's framework doesn't (publicly) discuss hooks. Could be a gap Annabel fills in her own audit template.

## Links from the description (worth capturing later if useful)

- aif.academy/go/yo-sop — start your AI-first agency
- framework.aif.academy/ — make your business AI-first
- bohdanbosar.gumroad.com/l/aemtfp — free SOP PDF (worth grabbing)
- youtu.be/bk46OxGjOFo — referenced "previous video" with the framework breakdown
