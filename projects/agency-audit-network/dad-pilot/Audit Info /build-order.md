---
title: Aviation AIOS — Build Order
type: plan
status: proposed
venture: aviation
audience: internal
tags: [aios, build-order, phases, composio, pilot]
summary: Current v3 build order: Erica-first employee pilot, Tom/Josh owner layer, Supabase operational brain, Render workers, and information hygiene lint. Historical CFS-first sections retained below for context.
created: 2026-05-14
modified: 2026-05-15
---

# Aviation AIOS — Build Order

> **2026-05-15 v3.1 supersession:** implement `../plan-v3-2026-05-15.md` as the current rollout. The older Tom-first/CFS-first sequence below is retained as historical design context only. **Read with v3.1 corrections:** Render replaces Cloudflare for hosting; Phase 1 ships Tom seat AND Erica seat in parallel on shared template workers; Phase 0 lint workers are scaffold-only.

## Current v3.1 build order

| Phase | Goal | Done when |
|---|---|---|
| **0 — Spine and security** | Supabase RLS, Render AIOS service (Tom-owned account), Tom + Josh + Annabel + Erica seats provisioned, scaffold health/lint jobs | Tom/Josh can see owner views via Supabase queries; Erica cannot see owner/private rows; health/lint scaffold rows write successfully; RLS smoke tests pass |
| **1 — Tom queue + Erica queue heaters (parallel)** | Tom's cross-venture decision queue (Claude Code MCP) AND Erica's first scoped FSL workflow (Cowork) both shipped on shared `ingest-template` + `draft-decisions` workers | Tom approves 5+ drafts with edit_distance < 500; Erica completes 5 real FSL tasks without technical help; no cross-seat data leakage; validator has flagged ≥1 bad draft to Annabel's queue |
| **2 — Owner brief + Josh's editing surface** | Owner daily brief (cross-company), Josh's canon-editor + approval-queue interface, L1 logging on Phase 1 workers | Tom and Josh can ask "what changed today?" and get useful company-level signal; Josh can edit canon files without Annabel intermediating |
| **3 — Connector expansion** | Add Composio/direct API feeds after the pilot shape works | At least one FSL source and one communication/calendar source flow into Supabase with visibility and audit logging |
| **4 — Thermostat and active cleanup** | Turn on L1/L2 measurement and activate the lint workers (tables already exist from Phase 0) | Low-risk stale items auto-archive, important conflicts flag for review, and every cleanup action is inspectable |

Build against `sql/schema-v1.sql`, which includes the operational tables plus the information-hygiene tables (kept empty until Phase 4 activation) and sensitivity/access helpers. Do not use the historical CFS-first sections below as active sequencing.

Six phases. Each phase has a single shippable goal, hard prerequisites, and a measurable signal that says it's done. No phase ships before the prior phase is done — including the measurement signal, not just the code.

| Phase | Goal | Duration target |
|---|---|---|
| **0** | Spine provisioned | Week 0–1 |
| **1** | Decision queue (heater) | Week 1–2 |
| **2** | Decision queue (thermostat) | Week 2–3 |
| **3** | CFS automated ingestion + daily brief (heater) | Week 3–5 |
| **4** | FSL/Falcon ingestion + meeting prep (heater) + briefs thermostat | Week 5–8 |
| **5** | Erica's Cowork seat + her pipeline (separate audit) | Week 8+ |

Durations are targets. Phase doesn't ship on a calendar — it ships when its signal hits.

---

## Phase 0 — Spine provisioned (v3.1)

**Goal:** All substrate pieces live, empty, and accessible from this laptop. Schema is multi-tenant from day one. Tom owns every account; Annabel is admin on each.

**Tasks (Tom approves spend; Annabel executes):**
1. Subscribe to Anthropic Team plan. Tom = billing owner. Add Annabel as member (build/ops). Add Erica as a member, seat reserved (don't activate her workspace until her Phase 1 workflow is wired). Add Josh as a member.
2. Create Supabase project `aviation-aios` under Tom's account. Annabel added as project admin. Run `sql/schema-v1.sql` as a single transaction. **RLS on from the start.** Tables include operational rows (`companies`, `employees`, `canon_docs`, `calls`, `drafts`, `clients`, `newsletters`, `skill_runs`) plus the information-hygiene tables (`information_lint_runs`, `stale_items`, `conflict_flags`, `cleanup_actions`, `canon_update_candidates`) which stay empty until Phase 4.
3. Create Render account under Tom's billing. Add Annabel as a team admin. Deploy a hello-world TypeScript service to verify build/deploy works.
4. Scaffold the `health-check` worker as a Render scheduled job. Cron set to weekly Sunday 22:00 MT, body is a no-op — only logs "scaffold check" to a `health_checks` row. The scheduled job firing reliably is the test.
5. Scaffold the `information-lint` scheduled jobs (freshness, conflict, canon, drift, access) — no-op bodies in Phase 0. They activate in Phase 4.
6. Decide on Composio subscription (see Composio call below). Default: defer until Phase 3.

**Done when:**
- Tom can run `select count(*) from companies` in Supabase from this laptop as the founder JWT (returns all rows), and as an Erica-shaped test JWT (returns only FSL).
- The Render hello-world service is live; the `health-check` scheduled job has fired at least once and written a scaffold row.
- Anthropic Team billing is active with Tom as owner and Annabel + Erica + Josh as members.
- All RLS smoke tests in `sql/schema-v1.sql` section 6 pass.

**Cost estimate (monthly):**
- Anthropic Team plan: ~$30/seat × 4 = ~$120
- Supabase: free tier sufficient for v1; ~$25 if it grows
- Render: ~$7/mo per web service + ~$0–10/mo for scheduled jobs depending on count
- Composio (if subscribed): ~$50–100, tier dependent
- **Total at Phase 0:** ~$130–270/mo depending on Composio call

---

## Phase 1 — Tom queue + Erica queue (parallel heaters, v3.1)

**Goal:** Both seats are using the system. Tom validates draft quality (high-judgment first reader); Erica validates non-technical-employee UX. Shared workers, two seats.

**Shared scaffold tasks (done once, used by both seats):**
1. Build `ingest-template.ts` as a **parameterized worker** taking `{source, venture, auth_method, parse_fn}` config. Never as a one-off. Adding the 5th or 10th seat later must be a config row, not new code.
2. Build `classify-signals` worker (Claude API call, classifies `relevance_to_seat` per active seat).
3. Build `draft-decisions` worker (Claude API call with `canon_docs` context, produces a draft) **followed by the validator step** that writes `validation_status` and routes the row either to the seat's queue (passed) or to Annabel's review queue (flagged). Validator rubric per the architecture's "Pre-surface validation" section.
4. Build the Render-hosted MCP service exposing `get_queue`, `mark_resolved`, `get_flagged` to Claude Code (Tom) and Cowork (Erica). Per-seat auth.
5. Extract canon → `canon_docs` (one-time seed; daily refresh comes in Phase 2).
6. Write `aviation/aios/_templates/skill-spec.md` — the template seats use to propose new skills. Not exercised until Erica proposes her second skill, but cheap to write now.

**Tom seat tasks:**
7. Intake mechanism: MCP paste/forward inside Claude Code (no inbound email — Tom is technically fluent and uses Claude Code daily). Tom drops items into the queue via a `submit_to_queue` MCP tool. No domain or email routing needed.
8. Validator rubric tuned for cross-venture decision drafts (reply_email, approve_send, choose_path, brief_review).

**Erica seat tasks:**
9. Pick Erica's first FSL workflow before Phase 1 starts: member email drafting, trip prep, sales follow-up, or content drafting. 20-min conversation with Tom + Evan to lock.
10. Add the picked workflow as a `loops` row + drafter prompt + validator rubric. Approved by Tom.
11. Wire Cowork to the Render MCP with Erica's scoped JWT. Smoke-test that she sees only FSL-scoped rows.

**Done when:**
- Tom approves 5+ drafts from his queue with edit_distance < 500 over a week.
- Erica completes 5 real FSL work items from her queue without technical help.
- No owner-only or private data appears in Erica's view (verified by RLS smoke test against live rows, not just empty tables).
- Validator has flagged ≥1 bad draft to Annabel's review queue (proves the gate works).
- Annabel's flagged-queue rate is <30% across both seats (if higher, validator rubric is too strict).

**Why both seats in parallel:** Tom is the highest-judgment first reader — he catches drafter regressions in week 1 before they reach Erica. Erica onboards in parallel so the non-technical-employee learning isn't deferred 4–6 weeks. Shared workers mean adding her seat is config + prompt, not new code.

---

### Phase 1 — historical Tom-only version (reference only)

The original v3 plan staged Erica alone in Phase 1. v3.1 reverses that based on draft-validation risk; the prior phrasing is retained below as historical context. Do not implement.

> **Goal:** Tom can manually feed items into the queue and get drafted, validated responses back.
>
> **Tasks:**
> 1. Build `tom-queue@<domain>` inbox as the first instance of the `ingest-template` worker. (v3.1 note: inbox replaced by MCP paste — no domain needed.)
> 2. Build `classify-signals` worker.
> 3. Build `draft-decisions` worker with validator step.
> 4. Build `claude-code-tools` MCP server on Cloudflare. (v3.1 note: now Render.)
> 5. Extract canon to `canon_facts` table.
> 6. Write skill-spec template.

---

## Phase 2 — Decision queue (thermostat) + health-check live

**Goal:** L1 logging on for Workflow 1. Tom sees a weekly L2 rollup. System health is monitored, not assumed.

**Tasks:**
1. Add L1 logging to `claude-code-tools`: every time Tom approves/edits/rejects, write to `executions` with `edit_distance`, `latency_ms`, `validation_passed`, timestamps.
2. Build `extract-canon` daily cron (refreshes `canon_facts` from vault at 03:00).
3. Build weekly L2 rollup query, surfaced as a Sunday-evening summary to Tom in Claude Code.
4. **Activate the `health-check` worker.** Replace the Phase 0 no-op body with the real checks per architecture: OAuth expiry (any token expiring in next 14 days), connector errors over last 7 days, model deprecations, cron staleness, canon atom delta, monthly spend estimate. Output writes to `health_checks` and any non-empty `flags_for_annabel` triggers an email to Annabel + a line in Tom's Sunday summary.
5. Add the first L2 → drafter-prompt feedback: whichever `decision_type` had highest median edit_distance gets its drafter prompt rewritten.
6. Add the first L2 → validator-rubric feedback: any check class that produced >50% false-positive flags gets relaxed; any hallucination class that slipped through gets a new check.

**Done when:**
- 4 weeks of L1 data accumulated.
- At least one drafter-prompt change has been made based on L2 signal.
- At least one validator-rubric change has been made based on L2 signal.
- `health-check` has fired 4 times and Annabel has reviewed every flag.
- Edit_distance trend is flat or declining (not climbing).

If edit_distance climbs week-over-week for 4 consecutive weeks, the workflow is misdesigned — stop, rethink, do not ship Phase 3. If `health-check` flags an unresolved item for 2 consecutive weeks, treat it as Phase-3-blocking until cleared.

---

## Phase 3 — CFS automated ingestion + daily brief (heater)

**Pilot venture: CFS.** Reasoning below.

**Goal:** Stop manually feeding the queue. Signals from CFS systems land automatically, classifier filters them, queue fills on its own.

**Tasks:**
1. `ingest-front-cfs` worker — pulls CFS inbox items from Front API. Filter: items not yet replied to, where charter@ is the recipient and the sender isn't on the team.
2. `ingest-art-cfs` worker — pulls AOG events from ART. **Blocked on Samuel exposing an ART API or webhooks.** If ART doesn't have an API in Phase 3 window, skip this worker, revisit in Phase 4.
3. `ingest-airtable` worker (CFS bases only at first) — pulls Airtable changes.
4. `morning-brief` worker (heater) — assembles overnight signals into a markdown brief, emails Tom at 06:00 MT weekdays.

**Done when:**
- CFS signals flow into `signals` table without Tom touching anything for a full week.
- Tom receives 5 morning briefs in a row, each with at least 3 signal items.
- Tom's manual queue forwards drop to <2/day (system is catching what he used to forward manually).

---

## Phase 4 — FSL/Falcon ingestion + meeting prep + briefs thermostat

**Goal:** Cover the remaining ventures and ship the second-priority workflow.

**Tasks:**
1. `ingest-hubspot-fsl` — pulls FSL deal/contact updates.
2. `ingest-airtable` extended to FSL bases.
3. `ingest-m365-calendar` — Tom's calendar diffs.
4. `meeting-prep` worker (heater) — 60 min before each calendar event, drops a prep `decisions` row.
5. Add L1 logging to morning brief (open tracking, follow-up engagement).
6. (Optional) `ingest-falcon` — if Falcon's London team has a system worth integrating. Defer if not.

**Done when:**
- All 4 venture signal sources are live and flowing (FAH=Falcon may stay manual if no API).
- Meeting prep brief lands for 5 consecutive meetings.
- Morning brief has 2 weeks of L1 data; first L2 action taken (cut a section, change ordering).

---

## Phase 5 — Erica's Cowork seat (separate audit)

**Goal:** Activate Erica's seat and run the *Erica pilot AIOS audit* per prior decision.

This phase is scoped by a **separate audit** that kicks off after Phase 4 is stable for 2+ weeks. Erica is at FSL, Senior Member Flight Specialist + marketing/sales. Her workflows are different from Tom's and need their own design.

**Don't pre-design Erica's workflows here.** The architecture (Supabase + Cloudflare + Cowork) is shared; the workflow loops are not.

**Pre-Phase-5 prerequisites (write these before the Erica audit starts, not during):**
- `aviation/aios/_onboarding/erica-day-1.md` — what Erica literally sees when she logs into Cowork on her first day. What's in her queue (likely empty at first), how to ask Cowork "what data is queryable from Supabase," how to read her own L1 trend, how to propose her first skill via `_templates/skill-spec.md`.
- Confirm RLS policies actually scope Erica out of Tom's queue (smoke test by querying as the Erica seat before her first real session).
- Confirm `canon_facts` is populated for FSL (her primary venture) — she should be able to pull voice/ICP/offer atoms on day one.

**Trigger for Phase 5:**
- Phase 4 has been stable for 2+ weeks (no drafter regressions, signals flowing reliably).
- Erica is ready (separate conversation, not a system question).
- A fresh audit document for Erica's pipeline is written.
- The three pre-Phase-5 prerequisites above are done.

---

## Pilot venture call: CFS first

**Recommendation: CFS is the first venture for automated ingestion (Phase 3).**

Why:

- **Highest decision throughput.** CFS has 24/7 AOG operations, multiple team members, an active inbox at `charter@`, and recurring escalations. More signal → more value from the queue → faster heater-to-thermostat transition.
- **Most mature canon.** CFS has a deep vault (intel/wiki, transcripts, terminology guardrails). The canon-extraction worker has the richest substrate to atomize for CFS, so drafts will be highest-quality from day 1.
- **Tom's escalation surface.** Tom is in CEO mode but CFS escalations *do* come to him (vendor relationships, ops-team-blocker calls, partner asks). FSL is more Evan's lane; Falcon is more London's. CFS is where Tom's "CEO touch" gets pulled in operationally.

Why not FSL first:

- FSL is Tom's founding venture but day-to-day is Evan/Erica's lane. Tom's decision throughput from FSL is lower than from CFS.
- FSL canon is strong (Access, Elevated) but the operational system (HubSpot) is more straightforward to integrate later.

Why not Falcon first:

- Falcon is mid-acquisition/integration. The team is in London. Integration adds complexity (timezone, system-of-record clarity) that we don't need in Phase 3.

Why not AIH first:

- AIH is the parent layer. There's no operational system to ingest from — AIH decisions emerge from the venture layer, not the other way.

---

## Composio call: subscribe in Phase 0 if first worker hits HubSpot/Airtable/M365/Slack; else defer

**Recommendation: subscribe in Phase 0 conditionally.**

What Composio replaces:

- HubSpot OAuth + API client → one Composio call.
- Airtable auth + client → one Composio call.
- M365 Graph OAuth + client → one Composio call.
- Slack OAuth + client → one Composio call.

What Composio does NOT replace:

- **ART** (CFS internal platform, Samuel's build) — direct API. Composio won't have it.
- **Front** — depends on Composio coverage at subscribe time. Check before Phase 1.
- Vault file reads (Obsidian Sync, local FS).
- The Supabase write side — that's a Postgres client, not Composio.

Decision criteria for Phase 0:

- If the first Phase 1 worker needs only Cloudflare Email Routing + Supabase + Claude API → **defer Composio.** No subscription needed for Phase 1.
- If the first Phase 3 worker (likely `ingest-front-cfs` or `ingest-hubspot-fsl`) hits a Composio-supported connector → **subscribe at start of Phase 3.**
- Lowest tier that covers needed connectors. Don't overbuy.

If subscribed and one connector turns out to not be supported well, fall back to direct API for that connector only. Don't unsub.

Defer signal that would flip to "no":

- If Composio's tier pricing changes significantly between Phase 0 and Phase 3.
- If a connector we need (e.g., Front) isn't supported and is critical → re-evaluate then.

---

## What blocks build progress

| Blocker | Phase it blocks | Mitigation |
|---|---|---|
| ART API access | Phase 3 ART ingestion | Ask Samuel; defer ART, ship Front+Airtable for CFS Phase 3 |
| Front API tier | Phase 3 Front ingestion | Confirm with CFS team; upgrade Front tier if needed |
| Tom's edit_distance climbs | Phase 2 → Phase 3 | Stop. Rethink drafter prompt design. Do not push more volume into a bad queue. |
| Composio supported-connector regression | Phase 3 | Direct API for that connector; don't unsub |
| Vault Obsidian Sync conflict on Tom's machines | Phase 2 canon extraction | Run extraction only from Mac Studio (canonical). Document. |

---

## Cross-references

- Architecture: `architecture.md`
- Workflow loops: `workflow-loops.md`
- Starting-state findings: `vault-findings.md`
