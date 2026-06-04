---
title: Aviation AIOS — Target Architecture v1
type: design
status: proposed
venture: aviation
audience: internal
tags: [aios, architecture, supabase, render, cowork, claude-code, composio]
summary: Operational architecture for the aviation AIOS — Supabase as the operational company brain, Render service + scheduled jobs as the limbs, Anthropic Team plan covering Claude/Cowork seats, Composio as a tactical connector layer inside workers. Audit output, 2026-05-14; v3 supersession 2026-05-15; v3.1 corrections (Tom + Erica parallel in Phase 1, Render locked, Cloudflare references obsolete) 2026-05-15.
created: 2026-05-14
modified: 2026-05-15
---

# Aviation AIOS — Target Architecture v1

> **2026-05-15 v3.1 supersession:** implement `../plan-v3-2026-05-15.md` as the current direction. The architecture below remains useful for Supabase/RLS/worker concepts. Read with these v3.1 corrections in mind:
> - **Tom and Erica both ship in Phase 1** on shared template workers, not Erica alone.
> - **Render** hosts the AIOS MCP/API service and scheduled jobs. Any reference to "Cloudflare Workers" or "Cloudflare Email Routing" below is obsolete — read as "Render service" or "Render scheduled job."
> - Tom and Josh are full co-owner seats. Josh's Phase 2 interface is canon-editor + approval-queue, not a full developer dashboard.
> - Phase 0 lint workers stay scaffold-only; active lint workers wait until Phase 4. Lint *tables* stay in `sql/schema-v1.sql` (idempotent empty).

This file is the operational spine for Tom's aviation AIOS at the AIH/CEO layer. It is not a diagnostic. It says where state lives, where compute runs, and which seat is whose.

Four constraints shape the design:

- **Tom and Josh are co-owner seats.** Day-to-day operations sit with Erin (COO), Evan (FSL VP), Erica, and venture leads. The AIOS surfaces owner decisions and company-wide health to Tom/Josh while keeping employee work scoped.
- **Architecture spine is fixed:** Supabase + Render + Cowork/Claude Code, on the Anthropic Team plan. Composio is a tactical accelerator inside workers, not the spine.
- **Supabase is the company's operational brain, not just Tom's queue.** Every seat reads from and writes to permissioned operational tables. Source systems and the vault remain authoritative. Supabase stores the live queryable layer: signals, decisions, queues, audit logs, extracted canon facts, workflow health, access scopes, lint findings, and cleanup actions. Tom and Josh see cross-seat owner rollups; employees see only their scoped work.

## Information hygiene / lint layer

The AIOS must continuously clean and validate its own operational memory. This prevents stale drafts, duplicate signals, old briefs, outdated facts, and overshared sensitive information from becoming the context employees rely on.

Scheduled lint workers:

| worker | schedule | does |
|---|---|---|
| `freshness-lint` | daily | auto-archives low-risk stale drafts, old queue items, duplicate signals, resolved workflow rows, and outdated brief rows |
| `conflict-lint` | weekly | compares Supabase facts against source systems and vault/canon, then flags contradictions |
| `canon-lint` | monthly | proposes canon updates from repeated edits, stale terms, and newly approved facts |
| `connector-drift-lint` | weekly | catches OAuth expiry, failed syncs, schema drift, stale cron runs, and connector errors |
| `access-lint` | daily | checks whether sensitive items are scoped too broadly or owner-only items leaked toward employee queues |

Default policy: low-risk stale operational clutter can auto-archive; canon, CRM, finance, HR, customer commitments, source-system records, and access policies require human approval before changing.
- **Nothing is provisioned yet.** Phase 0 of the build order is the spine. See `build-order.md`.

---

## Layered model

```
LAYER                  WHAT IT IS                         WHO/WHAT IT SERVES

Substrate (read)       Obsidian Vault canon              ←  authoritative voice/ICP/offer
                       (aviation/aih,cfs,falcon,fsl/canon)   per-venture truth
                              │
                              │ daily atomization
                              ▼
Brain                  Supabase (Postgres + auth)         ←  operational company state
                       - signals, decisions, canon_facts,    owner views, employee queues,
                         loops, executions, lint findings    cleanup/audit history
                              ▲
                              │ reads/writes
                              ▼
Limbs                  Render service + scheduled jobs    ←  ingestion + drafting
                       - hourly pulls (Front, HubSpot,       Tom never opens these;
                         ART, Airtable, M365)                runs invisibly
                       - daily vault canon extraction
                       - AM brief assembly
                              │
                              │ tool calls via
                              ▼
Connectors             Composio (where supported)         ←  Gmail, M365, HubSpot,
                       Direct API (where not)                Slack, Airtable, Front
                                                             ART is direct API (AIH custom)
                              ▲
                              │ surfaces to
                              ▼
Seats                  Claude/Cowork                      ←  Tom/Josh owner seats
                                                              Erica's scoped employee seat
                                                             both on Anthropic Team plan
```

---

## Supabase — the company's shared brain

One Postgres project, owned by Tom/Josh with RLS on from Phase 0. Tom and Josh are co-owner seats and see all company-level data, health, lint, and cross-seat rollups. Erica is the first scoped employee seat and reads only her own queue, approved FSL context, shared `canon_facts`, and her own L1/L2 rollups. The current schema also includes lint/cleanup tables for information hygiene; see `../sql/schema-v1.sql`.

The point of RLS-on from day one is not security paranoia — it's that the data shape encodes the multi-user design *before* a second user exists. Flipping RLS on later, with three seats already reading from the same tables, is a migration that touches every worker. Doing it now costs nothing.

### `seats`

One row per human seat on the system. Drives RLS policy.

| column | type | notes |
|---|---|---|
| id | uuid pk | |
| name | text | "Tom Filippini", "Erica Neibauer" |
| email | text | maps to Anthropic Team membership |
| role | enum | owner, member |
| workflows_active | uuid[] | foreign keys to `loops.id` — which workflows this seat participates in |
| created_at | timestamptz | |

Tom is the only `owner` in v1. Owners see all rows across all seats. Members see only rows where `seat_id = their seat`.

### `signals`

Raw events from any venture system. Render workers write here. Signals are *not* seat-scoped — they're venture-scoped, and the classifier later decides which seats they're relevant to.

| column | type | notes |
|---|---|---|
| id | uuid pk | |
| venture | enum | aih, cfs, falcon, fsl |
| source | text | front, hubspot, art, airtable, m365, vault, manual |
| source_ref | text | external system's record id |
| signal_type | text | email, deal_update, aog_event, calendar, doc_change, escalation |
| raw_payload | jsonb | source-shaped data |
| seen_at | timestamptz | when the worker captured it |
| processed_at | timestamptz nullable | when the brain classified it |
| relevance_to_tom | float nullable | 0-1, classifier output |

### `decisions`

Items that need a seat's call. Drafts attached. This is the queue.

| column | type | notes |
|---|---|---|
| id | uuid pk | |
| seat_id | uuid fk → `seats` | whose queue this lands in |
| signal_id | uuid fk | source signal |
| venture | enum | aih, cfs, falcon, fsl |
| decision_type | text | reply_email, approve_send, choose_path, brief_review, content_draft, etc. |
| summary | text | one-line: what the seat is deciding |
| context | text | 2-3 paragraph brief |
| draft_action | jsonb | shaped per decision_type (reply text, options, etc.) |
| status | enum | queued, presented, approved, edited, rejected, expired, **flagged** |
| validation_status | enum | passed, flagged, pending |
| validation_notes | text nullable | why validator flagged (if `flagged`) |
| edit_distance | int nullable | chars changed between draft and final, post-action |
| presented_at | timestamptz nullable | when the seat saw it |
| resolved_at | timestamptz nullable | when the seat acted |

A draft only reaches a seat's queue (`status='queued'`) if `validation_status='passed'`. Flagged drafts route to Annabel's review queue, not Tom's or Erica's. See "Pre-surface validation" below.

### `canon_facts`

Extracted atoms from `aviation/<co>/canon/`. Refreshed daily by a worker.

| column | type | notes |
|---|---|---|
| id | uuid pk | |
| venture | enum | |
| atom_type | text | voice_sample, banned_phrase, icp_inclusion, icp_exclusion, offer, fact |
| atom_text | text | the actual atom |
| source_file | text | which canon file it came from |
| source_line | int nullable | |
| extracted_at | timestamptz | |

This lets workers pull "what does FSL's voice sound like" without re-reading the full canon every time.

### `loops`

Definitions of the workflow loops (see `workflow-loops.md`). One row per workflow per seat — Tom's `decision_queue` and Erica's `content_draft` are separate rows even though both are "drafter loops."

| column | type | notes |
|---|---|---|
| id | uuid pk | |
| seat_id | uuid fk → `seats` | whose loop |
| name | text | decision_queue, daily_brief, meeting_prep, content_draft, email_draft |
| l1_signal | text | what gets measured per execution |
| l2_aggregate | text | what aggregates weekly |
| l3_canon_proposal | text | what monthly diff gets proposed |
| stage | enum | heater, thermostat |
| activated_at | timestamptz | when L1 logging turned on |
| created_by | uuid fk → `seats` | who proposed this skill (see "Skills self-service" below) |
| approved_by | uuid fk → `seats` nullable | Tom approves new skills before they ship |

### `executions`

Every time a skill ran. Per-execution log feeding L1.

| column | type | notes |
|---|---|---|
| id | uuid pk | |
| loop_id | uuid fk | |
| seat_id | uuid fk → `seats` | denormalized from loops.seat_id for cheap per-seat queries |
| decision_id | uuid fk nullable | if execution was about a queued decision |
| draft_text | text | what the skill produced |
| final_text | text nullable | what the seat shipped (after edit) |
| edit_distance | int | chars changed |
| latency_ms | int | how long the worker took |
| validation_passed | bool | did the pre-surface check pass |
| executed_at | timestamptz | |

L2 rollups are queries on this table, not separate tables. Each seat sees their own rollups; Tom sees the cross-seat aggregate.

### `health_checks`

Weekly system-health snapshot written by the `health-check` worker. This is what catches silent failures — OAuth expiry, model deprecations, cron staleness, vault drift, spend drift.

| column | type | notes |
|---|---|---|
| id | uuid pk | |
| run_at | timestamptz | |
| oauth_expiring_soon | jsonb | list of connectors with tokens expiring in next 14 days |
| connector_errors_7d | jsonb | non-200 responses per connector in last 7 days |
| model_deprecations | jsonb | any model referenced by a worker that's deprecated or scheduled-for-deprecation |
| cron_silent | jsonb | workers whose last successful run is >24h old when they should run hourly/30-min |
| canon_atom_delta | int | change in `canon_facts` row count since last check |
| monthly_spend_estimate | jsonb | Anthropic / Supabase / Render / Composio current month-to-date |
| flags_for_annabel | text[] | summary list of anything requiring action |

Tom and Annabel both see the `health_checks` rows; venture-team seats (Erica, future hires) do not.

---

## Render — the limbs

One Render-hosted AIOS service exposes the MCP/API surface and runs scheduled jobs. Tom is the Render account owner (billing + admin); Annabel is added as a team member with admin access during the build. Render's scheduled-jobs feature replaces what older drafts of this doc called "Cloudflare Workers cron triggers."

Worker shapes (each is a small TypeScript function, deployed independently):

### Cron workers

**All `ingest-*` workers share one template** (`ingest-template.ts`) parameterized by `{source, venture, auth_method}`. Adding the 5th or 8th system later is a config row, not new code. This matters because the four ventures will collectively need 8–12 ingestion connectors over v1, and the wrong shape now means cloning code at every addition.

| worker | schedule | does |
|---|---|---|
| `ingest-front-cfs` | every 30 min | (template) pull new CFS inbox items, write to `signals` |
| `ingest-hubspot-fsl` | every 30 min | (template) pull FSL deal/contact updates, write to `signals` |
| `ingest-art-cfs` | every 30 min | (template) pull ART trip/AOG events, write to `signals` |
| `ingest-airtable` | every 30 min | (template) pull Airtable changes across CFS/FSL bases, write to `signals` |
| `ingest-m365-calendar` | hourly | (template) pull Tom's calendar diffs, write to `signals` |
| `extract-canon` | daily 03:00 | re-extract atoms from vault canon, upsert `canon_facts` |
| `classify-signals` | every 10 min | for unprocessed signals, classify `relevance_to_seat` for each active seat via Claude API |
| `draft-decisions` | every 15 min | for high-relevance signals not yet in `decisions`, draft a decision + action, then run pre-surface validation |
| `morning-brief` | weekdays 06:00 MT | assemble each seat's overnight queue into a markdown brief in Supabase |
| `health-check` | weekly Sun 22:00 MT | snapshot system health (OAuth, connectors, models, crons, spend, vault) into `health_checks` |

### On-demand workers

| worker | trigger | does |
|---|---|---|
| `claude-code-tools` | MCP requests from Claude Code | exposes `decisions`, `signals`, `canon_facts` as MCP tools to Tom's Claude Code |
| `cowork-tools` | Phase 5 (Erica) | exposes Erica-scoped views as MCP tools to Cowork |

### Pre-surface validation

Before any draft reaches a human seat, the drafter runs a validation pass. The point is to catch hallucinations and shape errors *before* Tom or Erica sees them — so the system's worst output never reaches the human as a "first draft to fix."

The validator runs as a second Claude API call against a fixed rubric. Cheap version of the rubric (Phase 1):

- Does the draft cite at least one `canon_fact` row by id? (Forces grounding in vault.)
- Does the `decision_type` match the source `signal_type`? (Catches mis-routing.)
- Is the recommended action in the per-decision-type allowed-actions list? (Catches scope creep — e.g., a `reply_email` worker proposing to call a customer.)
- Does the draft reference any specific dollar amount, date, or person-name? If yes, does that string appear in the source signal payload or in `canon_facts`? (Catches the most common hallucination mode.)

If all checks pass → `validation_status='passed'` and the draft goes into the seat's queue. If any check fails → `validation_status='flagged'`, `validation_notes` captures which check, and the row routes to Annabel's review queue (not the seat's). Annabel either fixes the drafter prompt or marks the draft as a false-positive flag.

Per L2 review, the rubric tightens. A check that fires too often (false positives) gets relaxed; a hallucination class that slips through gets a new check added.

### Connector strategy

| system | connector | rationale |
|---|---|---|
| Front (CFS comms) | Composio if supported, else direct API | check Composio coverage in Phase 0 |
| HubSpot (FSL CRM) | Composio | well-supported, no reason to roll our own |
| ART (CFS trips, AIH internal) | Direct API | Samuel's platform, no Composio coverage |
| Airtable (ops, both ventures) | Composio | well-supported |
| M365 (Tom's email + calendar) | Composio | Microsoft Graph via Composio |
| Slack (team comms) | Composio | well-supported |

Composio is subscribed-to in Phase 0 if any worker hits a supported connector that month. See `build-order.md` for the call.

---

## Seats — Anthropic Team plan

| seat | who | interface | role | when |
|---|---|---|---|---|
| Owner | Tom | Claude Code (his machines) | owner | **Phase 1 — first owner-seat user, ships in parallel with Erica** |
| Owner | Josh | Claude/Cowork (canon-editor + approval UI) | owner | Phase 2 (his interface is built then, but his seat is provisioned in Phase 0) |
| Member | Annabel | Claude Code | member (build/ops) | Phase 0, day 1 — for build phase only |
| Member | Erica Neibauer | Cowork (web) | member | **Phase 1 — first scoped employee pilot, ships in parallel with Tom** |
| Member | (open) | reserved | member | future hire |

Anthropic Team plan is the bill-payer. Tom is the account owner. One subscription covers seats for Tom, Josh, Annabel/build-ops, and Erica. MCP/API servers live on Render and authenticate per-seat.

### What each seat sees

The Supabase RLS policy makes this concrete, not just a UX promise:

- **Tom and Josh (owners):** all decisions, all executions, all L2 rollups across every seat, plus `health_checks`, lint findings, and cleanup history. Owners can approve new skills and authoritative cleanup actions.
- **Annabel (member, build/ops role):** sees `health_checks`, flagged validations, and everything needed to debug — but does *not* sit in Tom's or Erica's decision queue. Annabel's role retires from active operation once Phase 4 is stable; she remains the DRI for system regressions only.
- **Erica (member):** her own decisions queue, her own L1/L2 rollups, approved FSL context, the shared `canon_facts`, and the brief intended for her. She does not see owner queues, owner rollups, private finance, HR, or other employees' queues. She *can* propose new skills via the self-service pattern below.
- **Future member seats:** same scope as Erica's — own queue, own rollups, shared canon, no cross-seat visibility unless Tom grants it explicitly.

This is why RLS is on from Phase 0 before real data lands. The data shape is multi-tenant from the start, even while the first live employee workflow is still narrow.

---

## What the vault is and is not

The vault stays read-from. It is the authoritative source for venture identity (voice, ICP, offer, terminology rules). Canon files do not get edited by workers; only by Tom or by deliberate human-driven canon updates.

Workers extract *atoms* from canon into `canon_facts`. Atoms are queryable in milliseconds. Re-extraction runs daily at 03:00, picking up any vault edits.

The Obsidian Sync layer keeps the vault identical across Tom's three machines (Mac Studio, Dell, this laptop). The `extract-canon` worker can run from any one of them — the vault is the same.

---

## Skills self-service

The system is designed so seats can propose new skills without Annabel writing code for every one. A "skill" is a `loops` row + one drafter prompt + one validator rubric + an L1/L2 design.

The pattern:

1. **Seat writes a skill spec** in `aviation/aios/_proposed-skills/<seat>-<skill>.md` using the template at `aviation/aios/_templates/skill-spec.md`. Spec covers: what triggers the skill, what signal_type it reads, what decision_type it produces, the validator rubric, the L1 signal, the heater→thermostat criteria.
2. **Annabel reviews for technical feasibility** — does the substrate support it, are the data sources available, is the validator rubric tight enough.
3. **Tom approves the skill** (`loops.approved_by = Tom`) before it ships. This is the one gate that doesn't get delegated — every new skill costs API tokens and adds a thing that can fail.
4. **Annabel scaffolds the worker** (usually a config row on the `ingest-template` if it's an ingestion, or a small variant of `draft-decisions` if it's a drafter).
5. **Ships as heater first**, thermostat after 2-4 weeks of L1 data per the standard sequence.

Erica is the first non-owner seat to use this. Her likely first skills are `content_draft`, `email_draft`, or `trip_prep` — all fit the existing `draft-decisions` shape. She can propose later skills via the spec template without Annabel pre-designing every workflow.

Documented separately at `aviation/aios/_templates/skill-spec.md` (to be written in Phase 1, used from Phase 5 onward).

## What this architecture does NOT do

- Does not move venture canon out of the vault. Canon stays in `aviation/<co>/canon/`. Supabase holds operational state and atomized canon, not authoritative canon.
- Does not replace ART, HubSpot, Airtable, or Front as systems of record for the ventures. Workers read from them, do not write back unless Tom approves a specific action.
- Does not surface other seats' queues to each other. RLS enforces this at the database, not the UI.
- Does not let non-owner seats deploy new skills unapproved. Tom is the only `approved_by`.
- Does not pre-commit to Composio. Composio gets subscribed-to when the first supported connector ships in a worker.
- Does not surface ops-level noise to Tom. The classifier filter is tuned for CEO-level decisions; routine ops go to venture leads, not Tom.

---

## Open architecture questions

These need answers before Phase 1 ships, not blockers for Phase 0:

1. **ART API access** — does Samuel expose an API or webhooks for CFS trip/AOG events? If not, ART ingestion deferred until he does.
2. **Front API tier** — does the current Front plan support the API endpoints we need? CFS team to confirm.
3. **Erica's first workflow choice** — pick the first concrete FSL daily workflow from her real workday: email drafting, trip prep, sales follow-up, or content drafting.
4. **Multi-machine reconciliation** — `extract-canon` runs from one machine; which one is canonical? Default: Mac Studio, since it has all keys and runs continuously.

---

## Cross-references

- Workflow definitions: `workflow-loops.md`
- Phase-by-phase build: `build-order.md`
- Starting-state findings: `vault-findings.md`
