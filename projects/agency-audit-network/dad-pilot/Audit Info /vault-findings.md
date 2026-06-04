---
title: Aviation Vault — Starting-State Findings
type: findings
status: draft
venture: aviation
audience: internal
tags: [aios, vault-findings, canon-state, stale-facts]
summary: What the audit found in the aviation vault on 2026-05-14 — per-venture canon strength, stale facts, integration map, gaps. Informs architecture.md and build-order.md.
created: 2026-05-14
modified: 2026-05-14
---

# Aviation Vault — Starting-State Findings

This file is the read-pass output of the 2026-05-14 audit. It does not propose architecture (see `architecture.md`) or build order (see `build-order.md`). It says what was actually in the vault on this date and what it implies for the AIOS build.

Scope: vault-only scan. OAuth-gated sources (Gmail, Granola, LinkedIn) were skipped per the audit scope decision. Those gaps are noted below for fill-in when OAuth is wired.

---

## Per-venture canon strength

| Venture | Canon depth | Voice/ICP/offer clarity | Stale facts found |
|---|---|---|---|
| **AIH** | Strong | Strong — "cryptic prestige," holding-co posture, brand defaults all in `aih/AGENTS.md` and `aih/canon/`. | Yes — Salesforce references for CFS data (see below). |
| **CFS** | Deepest | Strong — three pillars of value, terminology guardrails, full directory map. Wiki has 45+ articles per project CLAUDE.md, plus recent meeting transcripts (Dec 2025 – Apr 2026). | Yes — Salesforce listed as CFS trip system; actual stack is ART + Front + Airtable per Tom (audit input, 2026-05-14). |
| **Falcon** | Mid | Strong on terminology (insurance language correct) and JetSure Stack. Brand reset on 2026-04-27 — canon is current. | Currency: USD confirmed. No stale facts found. |
| **FSL** | Strong | Strong — Access Elevated design system, Cormorant + Instrument Sans, deposit model documented. Hospitality-forward photography doctrine. | None found. |

**Implication for AIOS:** all four ventures have enough canon depth that `canon_facts` extraction will produce useful atoms from day 1. No venture is so thin that its drafter would have to fabricate.

---

## Stale facts to fix

These are the only stale facts found in the scan. Listed here for surface-and-fix, not buried in the design docs.

### 1. CFS trip system: Salesforce → ART + Front + Airtable

**Where it's wrong:**
- `aih/AGENTS.md` line 137: `[PULL FROM SALESFORCE] for CFS trip and pipeline data.`
- `cfs/AGENTS.md` line ~185: `Salesforce — Trip data (10K+ trips), pipeline, customer records — CFS team`

**What's right (per Tom, 2026-05-14):** CFS trip data lives in **ART** (AIH internal platform, Samuel Tanner's build). Front is the email/ticketing layer. Airtable is project/ops tracking.

**Fix scope:** small canon update on both files. Do NOT do this fix as part of this audit — it's a venture canon edit. Surface in `_proposed/canon-updates-2026-05.md` if/when Workflow 1 L3 generates the proposal, or do it manually as a separate task.

### 2. Anything else?

No other stale facts surfaced in the scan. FSL canon was just reset (2026-04-21–27), Falcon canon was just reset (2026-04-27), AIH has the April rebuild archive. The vault is in good shape.

---

## Integration map (what the AIOS workers need to talk to)

Per-venture system inventory, from canon + Tom's audit answers:

### CFS

| System | Role | Composio? | API access status |
|---|---|---|---|
| ART | Trip + AOG events (system of record) | No — AIH custom | TBD; ask Samuel |
| Front | Inbound charter@ email / ticketing | Check at Phase 1 | TBD |
| Airtable | Ops/project tracking | Yes | Standard auth |
| QBO | CFS financials (Peter) | N/A — finance lane | N/A for AIOS |
| Slack | Internal comms | Yes | Standard auth |
| Cloudinary | Brand assets | N/A | N/A |
| Trainual | Training (legacy, transformation in progress) | N/A | Skip |

### FSL

| System | Role | Composio? | API access status |
|---|---|---|---|
| HubSpot | CRM + pipeline + members | Yes | Standard auth |
| Airtable | Ops/project tracking | Yes | Standard auth |
| Microsoft 365 | Email (Tom + team) | Yes (Graph) | Standard auth |
| QBO | FSL financials (Peter) | N/A — finance lane | N/A for AIOS |
| Slack | Internal comms | Yes | Standard auth |

### Falcon

| System | Role | Composio? | API access status |
|---|---|---|---|
| Xero | Falcon financials | N/A — finance lane | N/A for AIOS |
| (London team's underwriting stack) | Insurance binding/claims | TBD | Likely defer — Phase 4 or later |

### AIH

No operational systems at AIH layer. AIH decisions emerge from venture-level signals. No direct ingestion target.

**Implication for build order:** CFS (3 sources) + FSL (3 sources) cover 95% of Tom's signal surface. Falcon is light-touch in v1. AIH is composite, not direct.

---

## Vault structure observations

Each venture follows a consistent structure:
```
aviation/<co>/
  AGENTS.md          ← orientation (authoritative)
  CLAUDE.md          ← compatibility pointer to AGENTS.md
  canon/             ← brand DNA, voice, design, terminology
  reference/         ← product, pricing, scope, intel
  outputs/           ← deliverables (current; archived in outputs/.archive/)
  _archive/          ← prior canon/structure preserved
  assets/            ← logos, fonts
  intel/             ← CFS only — wiki + transcripts + raw evidence
```

CFS is the only venture with an `intel/` folder — that's where the wiki and meeting transcripts live. For the AIOS, `canon_facts` extraction reads from `canon/` only. `intel/` and `reference/` are out of scope for v1 atomization (they update frequently and aren't authoritative).

---

## Gaps the audit could not fill (vault-only constraint)

These need OAuth or interactive Tom input later:

| Gap | Why it matters | How to fill |
|---|---|---|
| Tom's actual outbound email voice | Calibrating drafter for non-canon voice (personal vs venture) | OAuth Gmail/M365 when AIOS is ready; sample last 90 days of sent items |
| Granola transcript content | Meeting voice + ICP language + objection samples | Granola API at Business tier; subscribe when meeting-prep workflow ships |
| Tom's LinkedIn voice (personal + 4 company pages) | Founder-voice signal | OAuth LinkedIn or scrape via direct profile reads when needed |
| Newsletter archive | Tom doesn't have one currently per scan | N/A unless one is launched |
| Tom's actual daily/weekly time distribution | Currently inferred from "CEO mode" answer | Could be measured via M365 calendar + Granola once integrated |

---

## What the audit did NOT touch

Per Tom's instruction (`don't delete folders or docs`) and the audit scope decision:

- No files were deleted or modified.
- No canon files were edited (including the Salesforce stale fact — surfaced only, not fixed).
- No new folders outside `aviation/aios/` were created.
- No content from `_archive/` was reactivated.
- No OAuth flows were initiated.
- No external services were provisioned.
- No spending was committed.

---

## Cross-references

- Architecture spine: `architecture.md`
- Tom's workflow loops: `workflow-loops.md`
- Phase-by-phase build: `build-order.md`
- Source audit document (Desktop, not in vault): `tom-personal-aios-audit-2026-05-14.md`
