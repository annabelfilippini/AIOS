---
title: Annabel Handoff Brief — Aviation AIOS Build
type: handoff
status: active
venture: aviation
audience: annabel
tags: [aios, handoff, annabel, phase-0]
summary: Self-contained brief for Annabel to take over the aviation AIOS build with minimal Tom involvement. Read this + the 4 design docs in this folder, then start.
created: 2026-05-15
modified: 2026-05-15
---

# Annabel Handoff Brief — Aviation AIOS Build

You are taking over the build for Tom's aviation AIOS. Tom designed this with me on 2026-05-14. He wants to be pulled in only for spend approval, OAuth/credential handover, and ongoing daily use of the system once it's live. Everything else is yours.

## 2026-05-15 v3.1 supersession — current direction

Use `../plan-v3-2026-05-15.md` as the current implementation plan. It supersedes both v2 and the older Tom-first sequencing in this folder.

Locked changes (v3.1):

- **Tom and Erica both ship in Phase 1** on shared template workers. Tom validates draft quality from Claude Code; Erica validates non-technical-employee UX from Cowork. Not Erica alone.
- Tom and Josh are full co-owner seats. Josh's interface is a canon-editor + approval-queue (Phase 2), not a full developer dashboard.
- Claude Code is Tom's primary interface (he's technically fluent). Claude/Cowork is Erica's primary interface.
- Supabase is the operational company brain, not the sole source of truth.
- **Render** hosts the AIOS MCP/API and scheduled jobs. Tom owns the account; Annabel is admin. All Cloudflare references in older docs are obsolete.
- Composio is preferred for supported connectors but not subscribed until a Phase 3 worker needs it.
- Phase 0 ships scaffold-only lint workers; active lint workers wait until Phase 4. The 5 lint tables exist in `sql/schema-v1.sql` from Phase 0 (idempotent empty) to avoid a Phase 4 migration.

## 2026-05-15 patches — read before Phase 0

After the original audit, the architecture was pressure-tested against Mansel, Bo, and Mark's frameworks. Five patches were added to the docs to make the system survive over time and scale to Tom's employees (Erica + future hires) without a painful migration mid-build:

1. **Supabase as the company's shared brain**, not just Tom's queue — RLS on from Phase 0, seat-level data scoping in the schema. See `architecture.md` → "Supabase — the company's shared brain" and "What each seat sees."
2. **Worker template pattern** — first ingestion worker in Phase 1 is built as `ingest-template.ts` parameterized by `{source, venture, auth_method}`, not as a one-off. See `architecture.md` → "Cron workers" and `build-order.md` Phase 1.
3. **Pre-surface validation** — drafts pass through a validator step before reaching any seat's queue; flagged drafts route to Annabel's review queue. See `architecture.md` → "Pre-surface validation" and `build-order.md` Phase 1.
4. **Health-check worker + ritual** — scaffolded in Phase 0 (no-op), goes live in Phase 2 catching OAuth expiry, model deprecations, cron staleness, vault drift, spend drift. See `architecture.md` → `health_checks` table and "Cron workers."
5. **Skills self-service** — pattern for seats to propose new skills (`_templates/skill-spec.md`) so the system evolves without Annabel writing every new skill. See `architecture.md` → "Skills self-service" and `workflow-loops.md` → "Skill self-service."

These are not optional appendices — they're load-bearing for the system working past month three. The original audit was a good v0; this is the v1 plan.

## Read this first

Four design docs sit next to this one. Read in this order:

1. `architecture.md` — Supabase + Render + Anthropic Team plan + Claude Code/Cowork. What runs where.
2. `build-order.md` — Phase 0 → 5 with exact tasks and "done when" gates.
3. `workflow-loops.md` — the 3 Tom-workflows and their L1/L2/L3 measurement design.
4. `vault-findings.md` — what's in the aviation vault, what's stale, what gaps exist.

After reading: you should be able to start Phase 0 the same day.

## Your scope: Phases 0 → 4 (v3.1)

You own design + execution of:
- **Phase 0:** spine provisioning on Render + Supabase, RLS smoke tests, all seats provisioned with Tom as admin/owner on every service
- **Phase 1:** Tom queue + Erica queue heaters in parallel on shared template workers
- **Phase 2:** L1 logging + owner brief + Josh's canon-editor surface
- **Phase 3:** connector expansion (Composio + direct APIs), CFS/FSL ingestion
- **Phase 4:** thermostat L1/L2 active, lint workers activated

Phase 5 (additional employee seats, e.g. Peter) is a separate audit after Phase 4 is stable for 2+ weeks.

## What to ask Tom for, all at once

Batch these into a single 30–60 min session with Tom. Don't drip-ask. The goal is to walk away from one sitting with everything you need for Phases 0–4.

### Spend approval

Tom needs to approve a monthly spend envelope. v3.1 numbers:
- Anthropic Team plan (Tom owner + Josh + Annabel + Erica seats): ~$30/seat × 4 = ~$120/mo
- Supabase: free tier in v1, may grow to ~$25/mo
- Render: ~$7/mo per web service + ~$0–10/mo for scheduled jobs depending on count
- Composio (conditional, may defer): ~$50–100/mo
- **Cap to ask for:** ~$300/mo upper bound across all services for the v1 build. Anything above, come back.

### Account creation (Tom signs in, you operate — Tom = admin/owner on every account)

Walk Tom through signing up in this order. Tom's billing card on every account. Capture credentials in his password manager, not yours.
1. **Anthropic Team plan** — Tom = owner. Add yourself + Josh + Erica as members.
2. **Supabase** — create project `aviation-aios` under Tom's account. Tom = owner. You get added as project admin so you can run migrations and inspect tables; Tom keeps the ability to remove your access at any time.
3. **Render** — create account under Tom's billing. Tom = owner. You get added as a team admin so you can deploy services and edit scheduled jobs; same revocability principle.
4. Composio — defer until Phase 3 unless Phase 1 needs a connector you can't roll yourself.

The admin model: **Tom can see and use everything you build, and can revoke your access whenever he wants.** No service is held under your personal account.

### OAuth handovers (Tom approves in browser, ~5 min each)

Have Tom click through these once you're at the worker stage that needs each one. Don't ask before you need them.
- Microsoft 365 (Tom's email + calendar) — needed for Phase 4 meeting prep, NOT Phase 1
- HubSpot (FSL) — needed Phase 4, ask Evan or Melissa if Tom doesn't have admin
- Front (CFS charter@ inbox) — needed Phase 3. Ask Rob Clipper (CFS ops director) if Tom can't directly grant
- ART API access — **blocker.** Tom needs to ask Samuel Tanner (CTO AIH, ART platform) for API or webhook access. No ART access = Phase 3 ships without ART ingestion.
- Airtable — Tom or the venture lead grants you base-level access

### Domain for queue inbox — NOT NEEDED in v3.1

Older drafts of this handoff required Cloudflare Email Routing for a `tom-queue@<domain>` inbox. **v3.1 drops this** — Tom is technically fluent and lives in Claude Code, so Phase 1 intake is via an MCP `submit_to_queue` tool he calls from inside Claude Code. No inbound mail infrastructure, no DNS setup, no email routing.

If a later phase needs inbound email for a non-technical seat, Render-side options at that time: Postmark Inbound Parsing, SendGrid Inbound Parse, or AWS SES.

### Erica's first FSL workflow — pick before Phase 1 starts

Pick one of: member email drafting, trip prep, sales follow-up, content drafting. Ask Tom and Evan (FSL VP) — they know Erica's day. 20-min conversation, decision locked in writing before workers get wired.

## What to do without bothering Tom

Once you have the spend envelope + accounts, you can do all of this alone:

- Supabase schema migration (5 tables per `architecture.md`)
- All Render-hosted worker code (TypeScript)
- Cron trigger setup
- Vault `canon_facts` extraction script (reads from `aviation/<co>/canon/`)
- The MCP server that Tom's Claude Code will talk to (`claude-code-tools` worker)
- Wire up Claude API for classifier + drafter workers
- Phase 2 L1 logging
- Phase 3 connector integration code
- Composio integration when subscribed
- Weekly L2 rollup queries
- Testing and dry-run drafts (use Tom's old emails / canon as input, don't ship to him)

## When to come back to Tom

These are the only decision gates that require him:

| Gate | When | What to bring |
|---|---|---|
| Spend approval beyond envelope | Any subscription beyond the agreed ~$250/mo cap | Cost, justification, alternative if any |
| OAuth grant for a system not in original list | A new system surfaces mid-build | Why it's needed, what it unlocks |
| Phase 1 → Phase 2 transition | Phase 1 done-when met (10 manual forwards, 5 approved drafts over 1 week) | Edit_distance distribution, his subjective "is this useful" |
| Phase 2 → Phase 3 transition | Phase 2 done-when met (4 weeks L1 data, edit_distance flat-or-declining) | L2 rollup view, drafter-prompt changes you made |
| Phase 3 → Phase 4 transition | Phase 3 done-when met (CFS signals flowing for a week, briefs landing) | Signal volume report, brief-engagement data |
| Anything I flagged as `[TOM TO VERIFY]` or `[ASK PETER]` in the canon | When a worker hits a canon claim that needs verification | The specific claim |
| Phase 4 stable for 2+ weeks | Trigger to kick off Erica's separate audit | Phase 4 done-when met |

## Weekly check-in shape (so Tom isn't pinged piecemeal)

Once per week, send Tom a single message with:
1. **Status:** what phase, what shipped this week
2. **Blocked on:** anything where you need him (credential, decision, OAuth)
3. **Numbers:** signal volume, draft count, edit_distance trend (once Phase 2 lands)
4. **Health flags:** anything from this week's `health_checks` that needs attention (once Phase 2 lands)
5. **Next week's plan:** what you'll ship

Friday afternoon is the default cadence unless Tom prefers otherwise. The `health-check` worker runs Sunday 22:00 MT so flags are fresh-but-not-blocking for the next Friday's message.

## What's out of scope for you

Don't:
- Edit any file outside `aviation/aios/`. Canon and reference files are off-limits.
- Update the stale Salesforce reference in [aih/AGENTS.md](../aih/AGENTS.md) or [cfs/AGENTS.md](../cfs/AGENTS.md). It's noted in `vault-findings.md` — Tom or a future canon-update pass handles it.
- Design Erica's workflows. Phase 5 is a separate audit.
- Move venture canon into Supabase. The vault stays the source of truth; workers only extract atoms from it.
- Auto-write back to ART / Front / HubSpot without Tom approving the specific action class.
- Provision anything that costs money without explicit approval.

## Tom's machine state

Tom runs Claude Code on three machines (Mac Studio = primary, Dell, this laptop). Obsidian Sync keeps the vault identical across all three. For your purposes:
- The vault is at `~/Vault/aviation/` on all his machines
- He prefers MCP servers on Render so they work from any of his machines
- His `.secrets/` directory on Mac Studio holds API keys (Mac Studio only — Windows machines embed keys in `.claude/settings.local.json` per-machine)
- Daily-driver Claude Code session is the laptop. Mac Studio runs continuously and is the canonical machine for `extract-canon` cron if you run it from a Tom-machine. (Default: run it from Render so machine state doesn't matter.)

## Open questions for Tom that come up later

Add to this list as you encounter them, don't ask immediately:

- Front API tier (does current plan support what we need?)
- Will Falcon's London underwriting stack expose anything ingestible, or stay manual?
- For Phase 5, does Annabel hand off to a separate Erica-pilot operator, or stay on?
- Newsletter / Beehiiv: not in scope for v1 since Tom doesn't have one yet. If he launches one, revisit.

## Files in this folder

- `architecture.md` — the spine
- `workflow-loops.md` — the 3 workflows
- `build-order.md` — Phase 0–5 sequence
- `vault-findings.md` — read-pass output
- `annabel-handoff.md` — this file

That's everything. Read the 4 docs, ask Tom for the batched session above, then start Phase 0.
