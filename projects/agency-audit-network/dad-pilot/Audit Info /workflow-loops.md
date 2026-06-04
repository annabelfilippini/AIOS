---
title: Aviation Workflow Loops — v3 current + v1 historical
type: design
status: proposed
venture: aviation
audience: internal
tags: [aios, workflows, loops, heater, thermostat]
summary: Current v3 workflow loops for Erica-first pilot, Tom/Josh owner layer, and information hygiene lint; historical Tom-only loops retained below as reusable patterns.
created: 2026-05-14
modified: 2026-05-15
---

# Aviation Workflow Loops — v3 current + v1 historical

> **2026-05-15 v3.1 supersession:** use `../plan-v3-2026-05-15.md` for the current workflow rollout. **Tom's decision queue and Erica's scoped FSL workflow both ship in Phase 1** on shared template workers. Owner brief and Josh's editing surface follow in Phase 2. The Tom-only workflow loops below are retained as reusable patterns, not the active build order.

## Current v3.1 workflow loops

| # | Workflow | Seat | Heater | Thermostat |
|---|---|---|---|---|
| 1 | **Cross-venture decision queue** | Tom | Phase 1 | Phase 2 |
| 2 | **FSL daily queue** | Erica | Phase 1 | Phase 4 |
| 3 | **FSL draft/helper workflow** (one of: member email, trip prep, sales follow-up, content) | Erica | Phase 1 | Phase 4 |
| 4 | **Owner company brief** | Tom + Josh | Phase 2 | Phase 4 |
| 5 | **Information hygiene lint** | Owners/build-ops | Phase 0 scaffold | Phase 4 active |

Both Phase 1 heaters share `ingest-template` and `draft-decisions` workers — adding the second seat is a `loops` row + prompt + validator rubric, not new code. This is the load-bearing template pattern: see `architecture.md` "Skills self-service" for why one-off workers must be avoided here.

Tom's queue intake is via Claude Code MCP paste, not email — he's technically fluent and lives in Claude Code. Erica's intake is via Cowork with FSL-scoped JWT.

Erica's first helper workflow (#3) must be picked from her real workday before Phase 1 starts. The acceptance test is practical, not technical: Erica completes five real tasks from Claude/Cowork without help and without seeing owner-only or private data.

The owner brief is separate from Erica's queue. It summarizes company-level changes, unresolved sensitive items, workflow health, lint findings, and employee pilot activity for Tom and Josh without dumping raw employee operational noise into their day.

Information hygiene is a workflow in its own right. It finds stale/duplicate/contradictory information, auto-archives low-risk operational clutter, and flags important conflicts for owner review. Canon and source-system records are proposed for update, never overwritten automatically.

Tom operates in CEO mode across AIH/CFS/Falcon/FSL. Day-to-day work sits with venture leads. Tom's AIOS exists to surface *decisions* and draft *responses* — not to do ops.

Three workflows for v1. Adding a fourth before the first three are thermostated is premature. Each workflow gets staged: **heater** (ships first, no measurement) → **thermostat** (logging on, signal feeds back into the prompt/rule).

| # | Workflow | First skill priority | Heater ships | Thermostat |
|---|---|---|---|---|
| 1 | **Decision queue drafter** | YES (Tom's pick) | Phase 1 | Phase 2 |
| 2 | **Daily intel brief** | Supports #1 | Phase 3 | Phase 4 |
| 3 | **Meeting prep + follow-through** | After #1 stable | Phase 4 | Phase 5 |

Reference for loop architecture: `loops-explained-2026-05-14.md` if/when that source file lands in the vault. Three nested cadences: L1 (per-execution), L2 (weekly aggregate), L3 (monthly canon proposal).

---

## Workflow 1: Decision queue drafter

**What it is:** A queue of items across the 4 ventures that need Tom's decision, each pre-drafted with a recommended action, ready for edit-and-ship or reject.

**Tom's first skill.** Selected because: (a) Tom is in CEO mode — decisions are his unique value, and (b) the queue compounds — every decision Tom approves/edits feeds the drafter for the next one.

### What lives where

- Input: `signals` rows where `relevance_to_tom >= threshold`. Threshold starts at 0.7, adjusted weekly.
- Worker: `draft-decisions` (Cloudflare cron, every 15 min).
- Output: `decisions` row with `summary`, `context`, `draft_action`, `status='queued'`.
- Surface: Tom asks Claude Code "what's my queue" → MCP tool reads from Supabase → drafts displayed inline.

### Heater (Phase 1)

Manually fed. Tom forwards/drops items into a single inbox (`tom-queue@<domain>`). Cloudflare worker writes to `signals`, classifier flags them, drafter produces a `decisions` row. No automated ingestion yet. Goal: prove the draft quality before scaling input volume.

### L1 — per-decision (Phase 2 turns this on)

Logged in `executions`:
- `draft_text` vs `final_text` → `edit_distance`
- `latency_ms` (worker draft time)
- `presented_at` → `resolved_at` (Tom's response time)
- `status` outcome (approved as-drafted / edited / rejected)

A "good" decision is approved-as-drafted with edit_distance < 50 chars. A "bad" decision is rejected or has edit_distance > 500. Phase 2 ships the L1 logging; Phase 3+ uses the signal.

### L2 — weekly (Phase 3)

Rollups against `executions`:
- Which `venture` has the most decisions queued? Where is Tom's attention actually getting pulled?
- Which `decision_type` gets the highest edit_distance? That drafter prompt needs work.
- Which `signal_type` produces the most rejected decisions? That signal is noise; raise its relevance threshold or filter it.

Weekly action: Tom (or worker) updates one drafter prompt or one filter threshold based on the worst-performing slice. Logged in a `loops` row update.

### L3 — monthly (Phase 4+)

Aggregate phrases Tom edited into drafts across all decisions in the month. If a phrase shows up in >5 edits, it's a candidate addition to the venture's `canon/copy-dna.md`. Worker drops these candidates into a single monthly markdown file: `aviation/aios/_proposed/canon-updates-YYYY-MM.md`. Tom reviews, accepts/rejects manually.

Canon never auto-updates. Tom is the only writer.

---

## Workflow 2: Daily intel brief

**What it is:** A weekday-morning brief (06:00 MT) that summarizes overnight signals across the 4 ventures, highlights anything that became a queued decision, and surfaces 1-3 things Tom should know that aren't yet decisions.

**Supporting role.** It's the "look at the system" interface for Tom on days he doesn't want to ask Claude Code his queue interactively.

### What lives where

- Input: all `signals` from the last 24 hours, plus all `decisions` queued in that window.
- Worker: `morning-brief` (weekdays 06:00 MT).
- Output: a markdown row in Supabase `briefs` table (add this table if Workflow 2 ships; defer otherwise).
- Surface: emailed to Tom + accessible via Claude Code "show me today's brief."

### Heater (Phase 3)

No personalization. The worker assembles overnight signals grouped by venture, lists queued decisions, and ships the brief verbatim. Tom reads it or doesn't.

### L1 — per-brief (Phase 4)

- Did Tom open the email? (open tracking, M365 native)
- Did any item in the brief generate a Claude Code follow-up question? (logged from Claude Code MCP tool calls)
- Did a brief item become a decision the same day?

### L2 — weekly (Phase 4)

- Which `signal_type` in the brief gets the most follow-up engagement?
- Which `venture` section gets the least attention? Possibly cut it from the brief.
- What's the right brief length? (Tom's read time correlates with brief length — find the elbow.)

### L3 — monthly (Phase 5)

Structural changes to the brief template (sections, ordering, defaults). Worker proposes structural changes monthly based on L2 rollups. Tom approves the template change manually.

---

## Workflow 3: Meeting prep + follow-through

**What it is:** For every meeting on Tom's calendar (M365): a 1-page prep brief 60 min before, and structured follow-through (commitments captured, draft replies prepared) within 30 min after.

**Wait-until #1 is stable.** Don't ship this until decision queue is thermostated, because meeting follow-through *feeds* the decision queue and you want the queue working first.

### What lives where

- Input: `signals` rows of type `calendar`, joined with venture context (who's the attendee, what's their last 5 emails, what's the latest from the venture canon).
- Workers: `meeting-prep` (runs 60 min before each calendar event), `meeting-followthrough` (runs 15 min after Granola transcript lands, if available).
- Output: `decisions` rows of type `brief_review` (pre) and `reply_email`/`approve_send` (post).
- Surface: Claude Code or email; pre-meeting brief is short enough to read on a phone.

### Heater (Phase 4)

Pre-meeting brief only. No Granola integration yet — Granola comes in Phase 5. Brief template is fixed.

### L1 — per-meeting (Phase 5)

- Was the prep brief opened? (event log)
- Did the meeting generate decision-queue items in the next 24 hours? (linked via meeting id)
- Did Tom rate the prep useful? (one-tap rating in Claude Code, optional)

### L2 — weekly (Phase 5+)

- Which meeting types get high-value prep (internal venture sync vs external partner vs board)?
- Which meeting types get ignored prep? Possibly skip prep for those types.

### L3 — monthly

Adjust prep template per meeting type. E.g., partner meetings get a "last 90 days of comms" section; board meetings get a "venture-by-venture state of play" section.

---

## What's deliberately NOT on this list

- **Sales outreach drafts (FSL or otherwise).** This is a venture-team workflow (Evan/Erica/Alli at FSL), not Tom's. Belongs in Erica's pilot AIOS audit (Phase 5).
- **AOG event response (CFS).** This is the CFS ops team's workflow (Rob/Casey/Chris/Gyasi/Heather), not Tom's. Tom only sees escalations.
- **Insurance binding (Falcon).** Falcon team in London handles this. Tom sees AIH-level summary, not transaction work.
- **Board updates.** Listed in some prior audits as a workflow, but Tom said his time is "cross-venture strategic + AIH-level" — board updates are quarterly bursts, not recurring loops. Handle one-off, not via this system.

---

## Per-seat visibility on these workflows

The three workflows above are Tom's. Each row in `decisions` and `executions` carries a `seat_id`, and Supabase RLS makes the visibility concrete:

- **Tom (owner)** sees his own queue, his own L1/L2/L3 rollups, and (uniquely) the cross-seat aggregate once other seats are active.
- **Annabel (ops)** sees the flagged-validation queue and `health_checks`. She does not sit in Tom's queue.
- **Erica (Phase 5)** will have her own loops (likely `content_draft` and `email_draft` — separate `loops` rows, separate L1/L2 rollups). She sees her own queue and her own trend, not Tom's. The shared layer between them is `canon_facts` (FSL voice/ICP/offer atoms) and the validator rubric pattern.

The same heater→thermostat sequence applies to every seat's loops. Erica's first skill ships as a heater, measurement turns on after 2–4 weeks of L1 data, same gate.

## Skill self-service — how new workflows get added

The point of skills self-service is that the system *evolves* over time without Annabel writing every new skill from scratch. A "skill" here is a `loops` row + drafter prompt + validator rubric + L1/L2 design.

When a seat wants a new skill (Erica wants `content_draft` for FSL emails; future hire wants something for their venture), the pattern is:

1. **Seat writes the skill spec** at `aviation/aios/_proposed-skills/<seat>-<skill>.md` using `_templates/skill-spec.md`. The spec is short: what triggers it, what signal_type it reads from, what decision_type it produces, what validator checks apply, what L1 measures success, when it graduates from heater to thermostat.
2. **Annabel reviews for feasibility** — substrate fit, data sources available, validator rubric tight enough.
3. **Tom approves** (`loops.approved_by = Tom`). New skills cost API tokens and add a thing that can fail; this gate doesn't delegate.
4. **Annabel scaffolds the worker** — usually a config row on the `ingest-template` or a variant of `draft-decisions`, not net-new code.
5. **Ships heater first.** Same closed-loops rule as Tom's workflows: no measurable L1 → not on the build queue.

This is the path by which the system goes from 3 Tom-workflows to whatever shape the company needs in year 2. The architecture (Supabase + Workers + canon_facts + validator + L1 logging) is shared; the workflows aren't.

## Closed-loops rule

Each workflow ships heater first (no measurement), then thermostat (L1 logging, signal feeds back). A workflow that has no measurable L1 signal does not ship. If a workflow proposed later has no L1 design, that's a sign the loop architecture isn't designed yet — finish the design before building.

---

## Cross-references

- Architecture spine: `architecture.md`
- Phase-by-phase build: `build-order.md`
- What was found in vault that informs these picks: `vault-findings.md`
