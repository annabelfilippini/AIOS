---
date: 2026-05-15
time: 09:35
project: agency-audit-network
status: complete
next-session: Annabel sits with Tom for the Phase 0 batched session per `dad-pilot/Audit Info /annabel-handoff.md`. The handoff now opens with a "2026-05-15 patches" section — read that first; it summarizes what changed since the v0 audit and points into the four design docs. The Supabase schema is the load-bearing change: RLS-on from Phase 0, `seats` table, `seat_id` scoping on decisions/loops/executions, `validation_status` columns, new `health_checks` table.
---

# Session: Pressure-test Tom's aviation AIOS against Mansel/Bo/Mark and write five patches into the audit docs

## What we worked on

Annabel got the audit back from running it on Tom's laptop (outputs in `dad-pilot/Audit Info /`: `architecture.md`, `build-order.md`, `workflow-loops.md`, `vault-findings.md`, `annabel-handoff.md`). She wanted to pressure-test the structure against the three named frameworks in her research vault — Mansel's AIOS framework, Bo Sar's AI-first business framework, Mark Kashef's implementation-substance frame — to make sure the system would evolve over time and scale to Tom's employees (Erica + future hires), not just Tom-on-day-1.

Synthesis surfaced five concrete gaps. All five were written into the docs as load-bearing additions, not appendix notes. The Supabase reframe (company shared brain, not Tom's queue) and the RLS-on-from-Phase-0 decision are the biggest changes — they flip a one-way door the original audit had quietly left open ("RLS off in v1, single-user until Cowork comes online" → which would have meant rewriting every worker's queries at Phase 5).

## Decisions made

- **RLS on from Phase 0**, not "off in v1." Flipped because turning RLS on with three seats already querying is a real migration touching every worker. The data shape encodes multi-tenancy from day one even though only Tom uses it at first.
- **Supabase reframed as the company's shared brain.** Every seat reads from / writes to the same operational tables. Tom (owner) sees cross-seat aggregates; each member seat sees only their own queue + shared `canon_facts`. The reframe is in the architecture's "Four constraints" intro and the new "What each seat sees" section.
- **New `seats` table; `seat_id` columns added** to `decisions`, `loops`, `executions`. Loops are now per-seat-per-workflow (Tom's `decision_queue` and Erica's `content_draft` are separate rows even though both are drafter loops).
- **Worker template pattern** (`ingest-template.ts` parameterized by `{source, venture, auth_method}`) from Phase 1, not Phase 4. The first ingestion worker (`tom-queue` inbox) is built *as* the template — adding the 5th or 8th system later is a config row, not new code.
- **Pre-surface validation** layer between drafter and seat queue. Drafter writes a draft → validator runs a fixed rubric (canon citation, decision_type ↔ signal_type match, allowed-actions check, hallucination check on dollar amounts/dates/names) → passes go to seat queue; flagged route to Annabel's review queue. Bo's "test harness before surfacing output" principle made concrete.
- **`health-check` worker** scaffolded in Phase 0 (no-op cron firing weekly Sun 22:00 MT to prove the cron works), goes live in Phase 2 with real checks (OAuth expiry, connector errors, model deprecations, cron staleness, canon atom delta, monthly spend estimate). Output writes to new `health_checks` table; non-empty `flags_for_annabel` triggers email + Sunday-summary line. Mansel's quarterly health check, weekly instead.
- **Skills self-service pattern** documented (`aviation/aios/_templates/skill-spec.md` to be written in Phase 1). Pattern: seat writes spec → Annabel reviews feasibility → Tom approves (`loops.approved_by = Tom`) → Annabel scaffolds (usually template config or drafter variant) → ships heater first. This is the path by which the system goes from 3 Tom-workflows to whatever shape the company needs in year 2.
- **Pre-Phase-5 prerequisites added to build-order:** Erica day-1 onboarding doc, RLS smoke test for her seat, FSL `canon_facts` populated. Erica doesn't get a Cowork seat activated until these exist.
- **Friday weekly-check-in updated** in the handoff: health flags join the message starting Phase 2.

## Open questions

1. **Tom hasn't seen the patches yet.** They were written off Annabel's judgment + the frameworks, not co-designed with Tom. Worth a 10-min walkthrough at the start of the Phase 0 batched session so he isn't surprised.
2. **Skill spec template not yet written.** Phase 1 task per build-order, but exact rubric for what "spec" includes is sketched in the docs, not formalized.
3. **RLS policy SQL not drafted.** "RLS on with owner-sees-everything, member-sees-own-rows" is the design; the actual Postgres policies need writing during Phase 0 schema migration.
4. **Validator rubric is Phase 1 v0.** Will tighten/loosen via L2 review per the build-order, but the starting rubric is currently four checks — may be too narrow or too broad once real drafts run through it.
5. **Composio call still defers in Phase 0.** Phase 1's first worker (Cloudflare Email Routing + Supabase + Claude API) doesn't need Composio — so the current answer is defer, revisit at Phase 3. Reconfirm at the Tom session.

## Next steps

1. **Phase 0 batched session with Tom** at his laptop. Walkthrough the 2026-05-15 patches section of `annabel-handoff.md` first (10 min), then run the batched session: spend approval, Anthropic Team signup, Supabase + Cloudflare account creation under Tom's billing, OAuth grants queued.
2. **Write `aviation/aios/_templates/skill-spec.md`** during Phase 1 build (cheap to write while patterns are fresh, used from Phase 5 onward).
3. **Draft RLS policies for the schema migration** before Phase 0 schema runs. Owner-sees-all + member-sees-own + role=ops-sees-flagged-validations.
4. **Health-check worker scaffold** ships with Phase 0 — no-op body, cron firing weekly, writes one row per fire to `health_checks`. Real check body comes in Phase 2.

## Context to preserve

- **The five patches map 1:1 to framework-specific gaps.** RLS-on + shared-brain framing = Mansel multi-user + Bo company-brain. Worker template = Mark repeatability. Pre-surface validation = Bo test harness. Health-check = Mansel maintenance ritual. Skill self-service = Mansel multi-user + Bo "old rule / new rule" (system evolves without scaling headcount).
- **Annabel's specific anxiety driver was "evolves over time + works for employees."** Every patch addresses one of those two axes directly. Worth keeping in mind when reviewing — if a future change loses one of these axes, the patches' purpose is being eroded.
- **The original audit had quietly punted multi-user to Phase 5** (RLS off, no seat scoping). This was the most consequential thing the framework pressure-test caught — not a missing feature, a missing decision-shape that would have created a painful migration mid-build.
- **Annabel was visibly under pressure when she asked for the pressure-test.** Quote: "this is a lot of pressuire and i want to make sure i dont mess up." The right response was concrete identification of gaps with patches she could ship, not reassurance. Worth a feedback memory if this pattern repeats.

## System refinement candidates

- **Pressure-test-a-build-plan-against-2-3-named-frameworks** is a reusable pattern, not specific to Tom's AIOS. Worth codifying as a skill or a Garry sub-routine: "given a build plan + 2-3 reference frameworks from the research vault, produce: what's strong, what's weak per framework, what to patch now vs. flag for gate-review." Compound-engineering candidate — would have saved 30 min of synthesis time this session.
- **"Supabase-as-shared-brain + RLS-on-from-day-one"** is a multi-tenant pattern that will likely repeat for future AIOS builds (Erica's audit, the eventual self-serve audit product, any client AIOS). Worth a memory if it becomes the default pattern — "for any multi-seat AI system on Postgres, encode tenancy in the schema before the second user exists."
- **The "Phase 0 schema includes future-state columns" trick** (adding `seat_id` to tables before there's a second seat) survived as the cleanest way to defer multi-user *implementation* without deferring multi-user *design*. Travels well — generalize to any "defer the feature but encode the shape" call.
- **The "skill = loops row + drafter prompt + validator rubric + L1/L2 design"** decomposition is a clean unit for cross-AIOS reuse. Worth a memory if it survives Phase 5 with Erica actually using it.
