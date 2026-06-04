---
name: aios-starting-point-audit-tom
description: Run the AIOS Starting Point Audit on Tom Filippini's 4-company entity (AIH / CFS / Falcon / FSL). Applies Mansel Scheffel's framework — 6-Layer Business Brain, 4 Pods, Friction Tags, QDOAA, Opportunity Matrix, Money Slide — to existing materials in Tom's Obsidian vault and public channels. Produces normalized canon per company, a pilot recommendation, a deep dive on the pilot, and a setup checklist. Tom runs this himself in Claude Code on his laptop.
audience: Claude Code running in Tom's vault. Tom is the operator; Annabel is the builder, available on screenshare twice (~20 min setup, ~20 min review).
output-root: <vault>/aios-audit/
version: v0 (Tom is the first pilot; promote to general skill after this run)
---

# AIOS Starting Point Audit — Tom's 4-Company Entity

You are running an audit against Tom Filippini's Obsidian vault and public materials for four companies (AIH = holding, CFS, Falcon, FSL). You apply Mansel Scheffel's AIOS framework against everything Tom already has — vault notes, websites, LinkedIn, sent Gmail, Granola transcripts, newsletter archive, testimonials — and produce a diagnostic + canon + pilot recommendation. Tom only enters typed/spoken input at two points: pre-flight setup and the gap-question voice memos. Everything else is autonomous on his laptop.

## Operating principles (read before acting)

1. **Read what already exists. Don't ask Tom to fill out forms.** The audit's job is to extract structure from materials, not to elicit it from scratch. Forms come out only when extraction genuinely fails (the gap-question pass in Phase 4).
2. **Mansel's QDOAA rule is non-negotiable.** Walk every flagged workflow through Question → Delete → Optimize → Accelerate → Automate, in that order. AI is the last step. Do not recommend automation for a step QDOAA says should be deleted, optimized, or accelerated first.
3. **Closed loops or it doesn't ship.** Every Quick Win the audit recommends must specify its three nested loops (L1 skill / L2 workflow / L3 brand). A heater that can't become a thermostat doesn't make the slate. See the *Closed-loop architecture* section below for what gets measured at each level. This is Annabel's thermostat principle and the difference between "this works" and "this is ChatGPT." The 🔁 Open Loop friction tag is the diagnostic; the L1/L2/L3 spec is the prescription.
4. **One pod at a time.** The deep pass goes against one pod in the pilot company. Cross-pod recommendations wait until that pod's loop is running clean for 2+ weeks. Mansel's strongest rule.
5. **Voice memos beat typed forms when Tom needs to give input.** Mansel's 7 discovery questions go to him as voice prompts, not a typed survey. Audio gets transcribed and slotted.
6. **Don't modify originals.** All audit outputs land in new files under `<vault>/aios-audit/`. Tom's vault notes are untouched.
7. **Cite every claim.** Every score, every tag, every recommendation links back to the source quote in the vault, the URL it came from, or the transcript it was lifted from. Tom should be able to challenge any output and trace it.
8. **Propose, don't decide.** Pilot company, AIOS-level recommendation per company, editing-surface pick for Josh, setup checklist — all proposed with reasoning. Tom confirms on the review screenshare.
9. **Tom is fluent. Don't paraphrase product names.** Use Cowork, Anthropic Team plan, Claude Code, Obsidian, Granola, Beehiiv, Blotato, Supabase, Cloudflare, OAuth, MCP, Helicone, Portkey by name. No "the team Claude app" — Tom knows what Cowork is.
10. **Don't spin up paid services without approval.** The setup checklist is a *plan*. Provisioning is Tom's call.
11. **Per-company isolation is enforced at the skill layer, not the storage layer.** One vault parent + per-company subfolders, voice isolation via a `company` parameter, not four separate vaults.

## Closed-loop architecture (the thermostat principle, read before Phase 3)

Reference: `dad-pilot/loops-explained-2026-05-14.md` and `dad-pilot/site/index.html#loops`.

Every skill the audit recommends has to be designed around three nested feedback loops, on three different time scales:

| Loop | Time scale | What's measured | What changes | Storage / cron |
|---|---|---|---|---|
| **L1 · Skill** | days | Per-execution outcome (email sent vs draft, reply received, LinkedIn impressions/reactions, post edits) | Next draft reads what worked. Rubric tightens. | Supabase row per execution. Read on next invocation. |
| **L2 · Workflow** | weeks | Aggregate patterns (top objections, recurring themes, themes without skills, edit reasons) | Erica updates a rule, promotes a new skill, retires a dead one. | Cloudflare cron (weekly). Writes summary to vault. |
| **L3 · Brand** | months | Voice / ICP / offer drift. High-engagement phrases that don't match canon. Buyer language that doesn't match `icp.md`. | Monthly diff proposed against `voice.md` / `icp.md` / `offer.md`. **System proposes. Humans approve.** | Cloudflare cron (monthly). Writes PR-style diff to vault. |

**Heater vs thermostat sequencing.** Mansel's "ship a working version first" + Annabel's loop architecture combine to a 2-stage build for every Quick Win:

- **Stage 1 (heater, weeks 1-4):** skill ships with rubric + canon reads. No engagement data yet; uses seed pool of past top-engagement examples.
- **Stage 2 (thermostat, weeks 5-6+):** L1 logging turns on (Supabase rows per execution), feedback flows back into next invocation. L2 cron lights up. L3 cron lights up later (needs a month of L1+L2 data).

The 90-day slate (Phase 5e) must label each Quick Win with its heater ship date and its thermostat close date. Both required. A Quick Win without a thermostat plan is a future open loop and gets sent back to QDOAA.

**Substrate that closed loops require** (the audit checks for these in Phase 5b):

- **Supabase tables** — one row per execution per skill. Example schemas from CFS LinkedIn skill: `linkedin_posts(id, posted_at, impressions, reactions, comments, shares, theme_tag, engagement_rate)`, `voice_evidence(excerpt, signal_type, skill_source, captured_at)`, `calls(theme_tag, ingested_at, transcript_ref)`. The audit drafts the table list per Quick Win, not the full DDL.
- **Cloudflare cron + polling** — weekly L2 rollup, monthly L3 diff. The audit notes which crons are needed; provisioning is Tom's call after review.
- **Signal sources per pod** — Granola transcripts (sales themes, ICP language, objections), LinkedIn analytics (engagement per post), Gmail reply data (email outcomes), Beehiiv (open/click rates for newsletter loop). The audit confirms each Quick Win has a measurable signal source. If it doesn't, the Quick Win goes back to QDOAA.

**Loop-readiness score** is part of the per-company AIOS-level recommendation (Phase 1d). A company with no closed loops anywhere today scores low on loop-readiness, which biases the AIOS-level toward *Cleanup-before-automation* or "ship the heater Phase 1, thermostat Phase 2." Companies that already have one functioning loop (e.g., Beehiiv newsletter with open-rate dashboards being looked at) score higher.

## What Tom needs ready before you start (Phase 0, ~20 min on screenshare with Annabel)

Ask him in chat:

1. **Vault path.** Absolute path to the root of his Obsidian vault on this laptop.
2. **Company URLs.** AIH, CFS, Falcon, FSL — root domain each.
3. **OAuth approvals.** Gmail (sent folder only, filtered to outbound), Granola (transcript API — requires Business plan or higher; flag if he's on a tier that doesn't expose it), LinkedIn (personal + company pages). One-click each in the browser. Tokens land in the local OS keychain, never leave the machine.
4. **Existing tool accounts and plan tiers.** Anthropic Team plan (seat count, who has Cowork access), Beehiiv (tier), Granola (tier), anything else paid. The audit needs this so the setup checklist doesn't double-spend.
5. **Scan exclusions.** Vault folders, channels, or accounts to skip. Default is the whole vault and all channels above.
6. **Whether to scan personal LinkedIn and personal Gmail.** Useful for founder-voice signal and 6-Layer Brain Layer 1 (Identity) scoring. If he'd rather not, work from company channels only — slightly less precision, no big deal.

Write his answers to `<vault>/aios-audit/_run/pre-flight.md`. If any answer is missing, stop and surface the gap to Tom — don't fabricate.

## Phase 1 — Light pass: all 4 companies (autonomous, Day 1 PM → Day 2)

For each of AIH, CFS, Falcon, FSL:

### 1a. 6-Layer Business Brain — score each layer 0–5

Source: Mansel's framework, captured at `research/sources/mansel-ainative-2026-05-14/captured-module-bodies.md`.

| Layer | What's in it | What to scan for |
|---|---|---|
| **1. Identity** | Who this company is, what it stands for | About page, founder LinkedIn, brand guidelines in vault |
| **2. Critical context** | Voice, ICP, offer, business shape, goals | Website copy, sent emails, sales decks, proposals |
| **3. Working memory** | Active engagements, in-flight work | Vault project notes, Granola recent transcripts, sent email last 30 days |
| **4. Episodic memory** | Past clients, prior work, case studies | Testimonials, case study docs, completed-project folders |
| **5. Long-term knowledge** | SOPs, playbooks, internal training | SOP folders, training docs, onboarding materials |
| **6. Background decay** | What used to be true and no longer is | Outdated tagged notes, archived folders, deprecated docs |

For each layer, score 0–5 with three evidence quotes pulled from his materials. If a layer scores ≤ 1, note the cheapest unblock to get it to 3.

Output: `<vault>/aios-audit/diagnostic/<company>/6-layer-brain.md` — table + radar chart data + evidence quotes with file paths and URLs.

### 1b. Pod inventory — which of Mansel's 4 pods are active

Mansel's 4 pods: **Acquisition / Delivery / Support / Operations.** For each pod in this company, write:

- **Active?** (yes / partial / no)
- **Materials found** (vault notes, channels, tools)
- **Who runs it today** (Tom, Josh, Erica, contractor, nobody)
- **Visible friction** (signals from the friction tag pass below)

If the company has no employees in a pod, mark it "founder-only" and skip to the next.

Output: `<vault>/aios-audit/diagnostic/<company>/pod-inventory.md`.

### 1c. Friction tag pass — scan for signals

Across Granola transcripts, sent emails, public testimonials, case studies, and vault notes, tag every signal with Mansel's 5 tags:

- 🟡 **Time Sink** — takes way longer than it should
- 🟠 **Wait / Handoff** — sitting in queue or waiting on another team
- 🔴 **Quality Risk** — high error rate, inconsistent output, complaints
- 🟣 **Compliance / Data Risk** — could cost real money if it breaks
- 🔁 **Open Loop** — work that started and never closed; missing feedback

Each tag links to the quote that justifies it. Three quotes per tag minimum, or note the tag is "absent in materials" (not "absent in reality" — extraction has limits).

Output: `<vault>/aios-audit/diagnostic/<company>/friction-signals.md`.

### 1d. Loop-readiness score (0–3) per company

Before the AIOS-level call, score the company on closed-loop maturity:

- **0** — no measurement anywhere. Outcomes not logged. Voice / ICP / offer never get revised from signal.
- **1** — one measurement source exists (e.g., Beehiiv open-rate dashboards, LinkedIn analytics looked at) but no feedback into the next execution. Heater only.
- **2** — at least one L1 loop closed (engagement data influences next draft). No L2 / L3 yet.
- **3** — L1 + L2 running. Brand loop (L3) optional but mature companies have a monthly review motion.

Loop-readiness biases the AIOS-level recommendation below. Output as a one-line field in the AIOS-level file with the evidence (e.g., "L1 partial — LinkedIn analytics tracked, but no signal fed into next-post drafts").

### 1e. AIOS-level recommendation per company

Pick **one** of Annabel's four framings (her packaging on top of Mansel's framework; not Mansel's tiers):

- **Personal AIOS** — single operator, no team handoffs to design around
- **Team AIOS** — small team, clear handoffs, ready for shared context layer
- **Company AIOS** — multiple pods active, ready for cross-pod orchestration
- **Cleanup-before-automation** — process is too broken for AI to amplify; QDOAA pass needed before any AI layer

Reasoning: 3-5 sentences citing the 6-Layer scores, pod inventory, friction density, and **loop-readiness score**. Loop-readiness ≤ 1 biases the recommendation toward staged delivery (ship heater Phase 1 / thermostat Phase 2) regardless of which AIOS-level lands.

Output: `<vault>/aios-audit/diagnostic/<company>/aios-level.md`.

### Per-company expectations

- **AIH** — light scan (founder identity, holding structure, brand-level material). Likely *Personal AIOS* — no Erica equivalent. Expected outputs are sparse; don't fabricate to fill them.
- **CFS** — full scan. Pilot candidate. Likely *Team AIOS*.
- **Falcon** — full scan. Other pilot candidate. Structurally similar to CFS but brand-distinct.
- **FSL** — full scan. Most different of the three. Expected to land as *Cleanup-before-automation* or "pilot later" — flag this honestly if the friction density says so.

## Phase 2 — Pilot recommendation (autonomous)

Apply Mansel's priority formula across the four companies:

```
Priority = (Impact × Confidence) − (Effort + Risk + (6 − Adoption) + (6 − Data Readiness))
```

- **Impact** — Cost-of-Inaction estimate for each company's biggest visible friction (rough; refine in Phase 3)
- **Confidence** — how much data was extractable. Companies with more Granola transcripts, vault material, channel volume score higher
- **Effort** — net-new infrastructure needed vs. what's in place
- **Risk** — compliance signals, data sensitivity, customer-facing failure modes
- **Adoption** — readiness of whoever runs the pod day-to-day
- **Data Readiness** — clean, accessible, permissioned?

AIH is excluded (holding-co, no operational pod to pilot). The remaining three rank.

Write the ranking with score breakdown and reasoning. **Default expected winner: CFS or Falcon** (similar shape, more material than FSL). If FSL wins, double-check the inputs before locking — that would surprise.

Output: `<vault>/aios-audit/pilot-recommendation.md`.

**Don't auto-decide.** Surface the ranking to Tom on the review screenshare. He confirms.

## Phase 3 — Deep pass on the pilot (autonomous)

For the pilot company only, pick **one pod** (likely Acquisition or Delivery — wherever Erica will work first per the `plan-v1` notes). Apply Mansel's Step Cards + QDOAA + Opportunity Matrix to one workflow within that pod.

### 3a. Step Cards

Pick the workflow with the highest friction density in Phase 1c. Map it step-by-step. For each step, capture Mansel's 9 data points + 4 pain indicators:

**9 data points:** systems used, inputs/outputs, volume, doing time, wait/queue time, error/rework rate, SLA, data sensitivity, controls.
**4 pain indicators on each step:** ⏱️ Time Sink, ⏳ Wait/Handoff, ⚠️ Quality Risk, 🔒 Compliance Risk. Plus 🔁 Open Loop if applicable.

What's unknown from the materials, mark `(extraction gap — voice memo)` and pull it into Phase 4.

Output: `<vault>/aios-audit/pilot/<company>/workflow-step-cards.md`.

### 3b. QDOAA pass

Walk the step list through Q → D → O → A → A:

- **Question:** Why does this step exist? Why are there N steps to produce one output?
- **Delete:** Which steps serve no purpose?
- **Optimize:** Which can be improved manually (better handoffs, better tools, fewer hops)?
- **Accelerate:** Which can be faster without adding headcount?
- **Automate:** What remains as a candidate for AI?

Mansel's literal claim: most processes have 30–40% of steps that can be cut without AI. Apply that lens honestly — don't shortcut to "automate everything."

Output: `<vault>/aios-audit/pilot/<company>/qdoaa.md` — each step labeled with its QDOAA verdict + reasoning.

### 3c. Opportunity Matrix

Score every surviving (post-QDOAA) automation candidate on the 2×2 (Impact × Effort). Pull Quick Wins (low effort × high impact) into a ranked list.

For each Quick Win:
- **Definition of Done** — what "shipped" means (heater + thermostat both, see below)
- **Kill / Pivot threshold** — what makes us stop or change approach
- **DRI assignment** — Tom, Josh, Erica, Annabel, or external
- **Loop spec** — required, all three levels:
  - **L1 (skill, days):** what gets logged per execution + what signal feeds the next invocation (e.g., "log impressions/reactions/comments to `linkedin_posts`; next draft reads top-engagement posts from last 90 days")
  - **L2 (workflow, weeks):** what weekly cron surfaces + what Erica/DRI is expected to update (e.g., "weekly cron rolls up theme_tag frequencies; Erica promotes any theme that appears 3+ weeks running to a dedicated skill")
  - **L3 (brand, months):** what monthly diff proposes against canon (e.g., "monthly diff against `voice.md` — any high_engagement_phrase that doesn't match canon voice gets surfaced as a proposed voice update; Tom approves")
- **Substrate dependencies** — the Supabase tables this Quick Win writes to, the Cloudflare crons it needs, the signal sources it reads. Flag any that aren't in place yet — they go on the setup checklist.
- **Heater ship date** — when Stage 1 (rubric + canon reads + seed pool) lands. Typically weeks 1-4.
- **Thermostat close date** — when L1 logging turns on and feedback flows. Typically weeks 5-6+.

**A Quick Win without a thermostat plan does not make the Matrix.** Send it back to QDOAA — either there's no measurable signal (Optimize manually first) or the loop architecture wasn't designed (Question why we're automating it).

Output: `<vault>/aios-audit/pilot/<company>/opportunity-matrix.md`.

### 3d. Money Slide — Cost-of-Inaction for top 3 Quick Wins

For each of the top 3:

```
Time saved/year:              $_____  (hours × loaded rate)
Errors prevented/year:        $_____
Capacity unlocked:            $_____  (hires avoided × loaded cost)
Conversion lift:              $_____  (deals × close rate delta × deal size)
Risk avoided:                 $_____  (compliance/churn exposure)
─────────────────────────────────────
Annual value:                 $_____
Implementation cost:          $_____
Payback (months):             _____
Confidence band:              low / med / high
```

Use loaded rates from Tom's pre-flight (employee count, rough salary band per company). If unknown, ask in Phase 4.

Output: `<vault>/aios-audit/pilot/<company>/money-slide.md`.

## Phase 4 — Gap questions (Tom, ~15 min, voice memos)

You will have hit extraction gaps in Phase 1c, 3a, and 3d. Bundle them into voice-memo prompts. Two categories:

### 4a. Mansel's 7 discovery questions (verbatim) — per company

1. *"Walk me through this company's main process end-to-end. Where does it slow down or break?"*
2. *"How many people touch the main workflow weekly? What roles?"*
3. *"How many hours does each person spend on it weekly?"*
4. *"When it fails, what happens? Lost revenue? Refunds? Rework? Compliance risk?"*
5. *"How often does it fail per month?"*
6. *"If we fixed it, what improves: speed, accuracy, capacity, conversion, risk?"*
7. *"What would solving this be worth this year if it worked?"*

For AIH, ask only #1, #6, #7 (no operational pod). For CFS / Falcon / FSL, ask all 7.

### 4b. Company-specific gap questions

Per company, surface 1-3 questions from the actual extraction gaps. Examples (don't use verbatim — generate from actual gaps):
- *"Goals for the next 6-12 months — revenue target, new hires, new offer?"* (always asked; rarely in documents)
- *"Why does this company exist separately from [other company]?"* (only if structural overlap is high and reasoning isn't documented)
- *"ICP exclusions — who do you actively say no to and why?"* (usually invisible in marketing materials)

### Delivery

Write a single file: `<vault>/aios-audit/_run/gap-questions.md`. Format as Tom-readable prompts grouped by company. Tell Tom to record voice memos (phone, Granola, whatever) and drop the audio files at `<vault>/aios-audit/_run/voice-memos/<company>/`. Tom does this solo on his time, no Annabel needed.

Once memos land, transcribe locally (Granola if running, otherwise local whisper) and slot the answers back into the relevant diagnostic / pilot files. Update citations.

## Phase 5 — Normalized canon + setup outputs (autonomous, after Phase 4)

### 5a. Normalized canon per company

For each of the four companies, write to `<vault>/canon/<company>/_normalized/`:

- `voice.md` — how this company talks (tone, vocabulary, sentence shape, 5+ representative quotes). **L3 loop spec at bottom of file:** which signal source proposes monthly updates (typically high_engagement_phrase rows from `voice_evidence` table).
- `icp.md` — who this company sells to (firmographic + psychographic + 3+ buyer quotes). **L3 loop spec:** which signal source proposes monthly updates (typically `calls.theme_tag` aggregations + reply outcomes).
- `offer.md` — what this company sells (offer language, pricing if public, headline benefits). **L3 loop spec:** which signal source proposes monthly updates (typically conversion outcomes + objection themes from sales calls).
- `business.md` — what this company is (structure, who runs what, geographic / vertical scope). No L3 loop — this is mostly static.
- `goals.md` — what this company wants in the next 6-12 months (from Tom's voice memo). No L3 loop — quarterly review motion, not automated.
- `_gaps.md` — what couldn't be extracted, why, and what would unblock it
- `_evidence.md` — quote → source path/URL for every claim above
- `_loops.md` — summary of which L3 brand-loop signals feed which canon file, where the substrate is (which Supabase table, which Cloudflare cron), and what state each loop is in (planned / heater / thermostat)

These feed Layers 1-2 of the 6-Layer Business Brain. They are the editable surface Josh and future employees touch. The `_loops.md` file is read-only for non-technical editors — it's where the system declares how the canon stays alive.

### 5b. System inventory + target architecture

- `<vault>/aios-audit/setup/inventory.md` — every tool, plan tier, what's paid for, what's missing. **Includes loop-substrate inventory:** which signal sources exist (Granola, LinkedIn analytics, Gmail metadata, Beehiiv), whether each has API access on Tom's current plan, whether any Supabase tables exist yet, whether any Cloudflare Workers are deployed.
- `<vault>/aios-audit/setup/target-architecture.md` — Mansel's federated diagram annotated for Tom's stack: Obsidian vault + sync, Anthropic Team plan (covers Cowork + Claude Code on one bill), Supabase (one project, `company_id NOT NULL` on every row, **plus per-Quick-Win measurement tables drafted in Phase 3c**), Cloudflare Workers (edge compute / polling / webhook routing, **plus weekly L2 crons and monthly L3 crons per Quick Win**), Blotato downstream of drafts, Beehiiv unchanged.
- `<vault>/aios-audit/setup/loop-substrate.md` — consolidated view across all proposed Quick Wins: every Supabase table needed, every cron job needed, every signal source needed. This is the loop infrastructure as one picture — if any row says "blocked" (e.g., Granola Personal tier doesn't expose transcript API), the corresponding Quick Win is gated until the substrate exists.

### 5c. Setup checklist

Ordered list of accounts to create, plan tiers to pick, settings to configure, with monthly cost estimates. Tom approves spend before any provisioning. File: `<vault>/aios-audit/setup/checklist.md`.

### 5d. Editing-surface recommendation for Josh

Pick **one** of three, based on what Josh already uses day-to-day (ask Tom in pre-flight if not known):

1. **Guided Obsidian, simplified view.** Vault with only the `canon/` folder visible, Live Preview mode, no plugins. Cheapest, no new tools. Josh still has to open Obsidian.
2. **Notion mirror.** Canon files mirrored into Notion, edits sync back to vault. Familiar surface for non-technical editor. Adds one tool.
3. **Per-file shared docs (Google Docs).** Each canon file as a shared doc, edits sync back. Simplest mental model, most fragile sync.

Write the recommendation with reasoning. Tom and Annabel land the final call on the review screenshare. Whatever wins is the same surface Erica and every future hire edits through — one decision, not a repeated one.

File: `<vault>/aios-audit/setup/editing-surface.md`.

### 5e. 90-day slate

The audit's actual deliverable is a co-signed plan, not a report. Write 2-3 Quick Wins committed for the pilot company. For each:

- DRI, DoD, Kill / Pivot threshold (from Phase 3c)
- **Heater ship date** (weeks 1-4) — when Stage 1 lands: rubric + canon reads + seed pool. No measurement yet.
- **Thermostat close date** (weeks 5-6+) — when L1 logging turns on and feedback flows back into the next invocation.
- **L1 / L2 / L3 spec** (from the Opportunity Matrix) — restated here so the slate is self-contained.
- **Substrate dependencies** — explicit list of Supabase tables / Cloudflare crons / signal sources that must exist before thermostat close.

The slate sequences Quick Wins so substrate gets built once and reused. Example: if Quick Win #1 needs the `linkedin_posts` table and Quick Win #2 needs `linkedin_posts` + `voice_evidence`, the slate stages QW#1 to build both tables and QW#2 to reuse them.

Tom confirms on the review screenshare; this becomes the build queue.

File: `<vault>/aios-audit/90-day-slate.md`.

## Phase 6 — Review screenshare (~20 min, Tom + Annabel)

Before this call, write a one-pager summary at `<vault>/aios-audit/_run/review-summary.md` that lists:

- Per-company AIOS-level recommendation (one-line each)
- Pilot recommendation + score breakdown
- Top 3 Quick Wins + Money Slide totals
- Editing-surface pick for Josh
- Setup checklist cost (monthly run rate + one-time provisioning)
- Open decisions for Tom to confirm

On the call, Annabel walks Tom through. Anything wrong → Tom corrects in the moment or via voice memo right after. Outputs lock when corrections are applied.

## Output layout (final state)

```
<vault>/
  canon/
    aih/_normalized/        ← founder identity only (sparse)
    cfs/_normalized/        ← full canon (5 files + gaps + evidence)
    falcon/_normalized/     ← full canon
    fsl/_normalized/        ← full canon
  aios-audit/
    diagnostic/
      aih/                  ← 6-layer, pods, friction, aios-level
      cfs/
      falcon/
      fsl/
    pilot/<chosen>/         ← step cards, qdoaa, matrix, money slide
    setup/
      inventory.md
      target-architecture.md
      loop-substrate.md
      checklist.md
      editing-surface.md
    pilot-recommendation.md
    90-day-slate.md
    _run/
      pre-flight.md
      gap-questions.md
      voice-memos/<company>/
      review-summary.md
      decisions.md          ← every decision + reasoning + timestamp
```

## Hard rules (don't break these)

- **Never modify originals.** Every output is a new file under `aios-audit/` or `canon/<co>/_normalized/`.
- **Never auto-provision paid services.** Setup checklist is a plan. Tom approves spend.
- **Never recommend automation for a step QDOAA flagged for Delete / Optimize / Accelerate.** Process cleanup wins first. This is the single most-violated rule in AI consulting and the reason most pilots fail.
- **Never recommend a Quick Win without a thermostat plan.** Every recommendation specifies L1 / L2 / L3 loops and a measurable signal source. A skill that can't close its loop is a heater pretending to be a thermostat — Mansel's QDOAA pass should have caught it. Send back.
- **Never extract from excluded folders / channels.** Tom's exclusion list in pre-flight is binding.
- **Never softens product names.** Tom is fluent — Cowork stays Cowork, Anthropic Team plan stays Anthropic Team plan, Blotato stays Blotato.
- **Never decide pilot company unilaterally.** Propose, surface reasoning, let Tom confirm.
- **Always cite.** Every score, tag, recommendation traces to a quoted source.
- **Always write to `_run/decisions.md` when you make a non-trivial call** (e.g., picking the pilot pod, choosing the workflow for Step Cards, defaulting a loaded rate, gating a Quick Win on substrate). Tom should be able to read the audit's reasoning trail without asking.

## What this skill explicitly will NOT do

- Will not interview Tom synchronously. Discovery is voice memos.
- Will not score pods Tom doesn't have employees in (the founder-only case).
- Will not run the FSL deep pass on the first invocation. FSL is light-scan + AIOS-level rec only; deep pass deferred to phase 2 once the pattern is proven.
- Will not produce a PDF. The audit is a living set of files in the vault. PDF export happens on request, separately.
- Will not recommend Cooldown-style or AnnabelFilippini.com-style brand language. The audit's voice is operational, not marketing.

## Notes for the future general skill

After this run, the Tom-specific parts (4 company names, vault layout assumptions, pilot expectations) get parameterized. The framework spine (Phases 1-6, the file layout, the hard rules) is reusable. Promote to `skills/aios-starting-point-audit/SKILL.md` once Tom's run validates it. Track delta in `<vault>/aios-audit/_run/template-feedback.md` — anything that surprised you during execution, that's the signal to revise the general version.

## References (for citation)

- Mansel framework: `projects/agency-audit-network/research/sources/mansel-ainative-2026-05-14/captured-module-bodies.md`
- Audit shape decision: `projects/agency-audit-network/research/audit-shape-decision-2026-05-14.md`
- Synthesis: `projects/agency-audit-network/research/audit-system-synthesis-2026-05-14.md`
- Build plan that runs after the audit: `projects/agency-audit-network/dad-pilot/plan-v1-2026-05-14.md`
- Loops architecture (skill / workflow / brand): `projects/agency-audit-network/dad-pilot/loops-explained-2026-05-14.md`
