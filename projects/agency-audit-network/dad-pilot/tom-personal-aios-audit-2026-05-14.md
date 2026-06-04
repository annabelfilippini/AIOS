# Tom's Personal AIOS Audit — 4-Company Entity

**Date:** 2026-05-14
**Operator:** Annabel, running Claude Code at Tom's laptop with Tom available for input.
**Premise:** Before building skills for Erica or anyone downstream, get Tom's own system solid. The audit reads what's already on his laptop and in his channels and produces a stronger personal AIOS for Tom across his 4 companies (AIH / CFS / Falcon / FSL).
**Supersedes:** `audit-intake-tom-2026-05-14.md` and `aios-starting-point-audit.md` (Mansel-framework versions) for this run. Those files are kept as iteration history.

---

## The one-paragraph summary

The audit gets a clean picture of three things: (1) Tom's current system — what's in his Obsidian vault, what tools and accounts already exist, what's misconfigured, where the silos are; (2) Tom's own workflows across the 4 companies — what's recurring, what eats his time, what could close into a loop; (3) each company's voice, customer, offer, business shape, and goals. The audit produces it by reading what's already there, not by handing Tom a form. Annabel sits with Tom at his laptop, OAuths the integrations together, then the scan runs autonomously. Tom answers a short batch of gap questions out loud, and the outputs land in his vault.

---

## How the audit runs

Annabel runs Claude Code on Tom's laptop. His vault, Gmail, Granola transcripts, LinkedIn — none of it leaves the machine. Tokens stay in his local OS keychain. Annabel is the operator at the keyboard; Tom is the input source at the desk.

No screenshare. No solo voice-memo handoff. The audit is conversational where it needs input from Tom and autonomous where it doesn't.

---

## What the audit reads (autonomous, after the pre-flight)

**Entity-wide scan:**

- Tom's Obsidian vault — every note, every linked file, every folder. Indexes structure and content. Notes which folders look organized vs which are a midden.
- Tool stack inventory — what's already set up (Granola, Beehiiv, Anthropic Team plan, Claude Code, Cowork, any CRM, calendar tooling, doc tooling) and what plan tier each is on.
- Tom's own usage patterns — last 30 days of Granola transcripts (what he spends meeting time on), last 30 days of sent email (what he writes vs delegates), Obsidian note activity (where he captures vs where notes go to die).
- Cross-company information flow — where Tom is the bottleneck because something lives in his head, where decisions get re-litigated because no decision log exists, where the same answer gets written multiple times.

**Per-company scan** (full for CFS / Falcon / FSL; lighter for AIH):

- Vault notes / subfolders / tags for that company. Every document, deck, PDF, brand guideline, proposal, case study. OCR on images.
- Company website — every page. Copy, offer language, headlines, About, services.
- Company LinkedIn page. Posts, About, recent activity.
- Tom's personal LinkedIn (founder voice signal). Last 90 days of posts and comments.
- Tom's sent Gmail, filtered to outbound emails he wrote himself. Voice samples.
- Granola transcripts where relevant. Sales calls, client calls, partner calls — ICP language, objections, customer wording.
- Newsletter archive if there is one. Tone samples.
- Public testimonials and case studies.

For AIH (holding co) the scan is lighter — identity, structure, founder-level voice. No operational canon needed.

---

## What the audit produces

Seven deliverables, all written into Tom's vault under `aios-audit/` and `canon/`:

### 1. Tom's personal context map

The thing the original audit didn't produce. A picture of *Tom* as the operator of this entity, separate from any one company:

- His role across the 4 companies (where he's CEO-shaped, where he's CFO-shaped, where he's salesperson-shaped, where he's signing checks only).
- His daily and weekly rhythms — recurring meetings, recurring decisions, recurring outputs (newsletters, board updates, partner check-ins).
- Where his attention currently goes vs where it should go.
- The 3-5 workflows that are *his*, not Erica's or Josh's — the ones that have to be strong before any team-facing system gets layered on.

File: `aios-audit/tom-context.md`.

### 2. System inventory + target architecture

What Tom has now vs the target state. Tools, plan tiers, integrations, silos, misconfigurations.

The target architecture is the federated AIOS shape — Obsidian vault (canon layer) + Anthropic Team plan (Cowork + Claude Code on one bill) + a small operational data store + a polling/cron layer — annotated for Tom's actual existing stack so the diff is concrete, not aspirational.

**Composio evaluation goes here.** See the dedicated section below. Net call: does Composio replace custom MCP / OAuth work for Tom's integration layer, or does it sit alongside, or is it not worth it for a 4-company shape.

Files: `aios-audit/setup/inventory.md`, `aios-audit/setup/target-architecture.md`.

### 3. Per-company normalized canon

For each of the 4 companies, written to `canon/<company>/_normalized/`:

```
canon/cfs/_normalized/
  voice.md         ← how CFS talks
  icp.md           ← who CFS sells to
  offer.md         ← what CFS sells
  business.md      ← what CFS is
  goals.md         ← what CFS wants in 6-12 months
  _gaps.md         ← what couldn't be extracted
  _evidence.md     ← quotes from materials backing every claim
  _loops.md        ← which signals feed which file on the brand-loop scale
```

These are the durable identity files. They feed every future skill — Tom's, Erica's, whoever's.

### 4. Tom's workflow loop map

For each of the 3-5 workflows the audit identifies as *Tom's* in the personal context map, specify the three nested feedback loops (reference: `loops-explained-2026-05-14.md`):

- **L1 (day scale):** what gets measured per execution of this workflow. Example: Tom drafts a board update → measure how much edit he does vs the seed draft, log it.
- **L2 (week scale):** what aggregates and what rule Tom updates as a result. Example: weekly rollup of which board-update sections always need heavy edits → adjust the seed prompt.
- **L3 (month scale):** what monthly diff gets proposed against the canon files. Example: phrases Tom keeps editing into his drafts get surfaced as candidates for `voice.md` updates.

Each workflow is staged as *heater* (ships first, no measurement) → *thermostat* (logging on, signal feeds back). A workflow that has no measurable signal doesn't make the build queue — that's a sign the loop architecture isn't designed yet.

File: `aios-audit/tom-workflow-loops.md`.

### 5. Setup checklist

Exact accounts to create, plan tiers to pick, settings to configure, in order, with monthly cost estimates. Includes the Composio decision (subscribe, defer, skip) with rationale. Tom approves spend before anything provisions.

File: `aios-audit/setup/checklist.md`.

### 6. Pilot company recommendation

Of the 4 companies, which one gets the first deep build *for Tom's personal AIOS* — not for Erica yet. The pilot is whichever company has:

- The most material to extract from (so day-1 drafts are non-trivial).
- The clearest of Tom's own workflows present (so the loop architecture has something real to wrap around).
- The highest cost-of-inaction for Tom's time (so the payback is visible to Tom himself).

Expected default: CFS or Falcon. AIH is too light. FSL is the most different from the others — likely flagged as "round-2" once the pattern is proven on CFS or Falcon.

File: `aios-audit/pilot-recommendation.md`.

### 7. Build order for Tom-first

The sequenced plan: which Tom-workflow gets the first skill, what substrate it needs, what the heater looks like, what the thermostat close criteria are. This is what Annabel builds after the audit locks. Erica's pipeline gets sequenced *after* Tom's first 2-3 personal skills are running with closed loops.

File: `aios-audit/build-order.md`.

---

## Composio evaluation (read this before deciding setup)

Composio is an agent-tool integration platform — one SDK and one auth surface that exposes hundreds of apps (Gmail, GCal, Slack, Notion, LinkedIn, GitHub, HubSpot, etc.) to AI agents. For Tom's 4-company entity, three questions to answer in the audit:

### Q1. Does Composio replace custom OAuth / MCP for the data-collection layer of *this audit*?

Today the audit needs read access to Gmail (sent), Granola (transcripts), LinkedIn (personal + 4 company pages), plus whatever's in the vault. Custom path: 3-4 separate OAuth flows + the Granola tier check. Composio path: one auth surface, unified read.

**Decision criteria:** if Composio supports all four sources at the tier Tom would subscribe to, and the auth time-savings + ongoing token-management offset the subscription cost, it's worth it. If it covers 3 of 4 and one (likely Granola) still needs a custom integration, the savings are smaller and it becomes a "nice to have" not "core."

### Q2. Does Composio fit the *operational* substrate Tom's AIOS will need?

Once Tom's personal skills start running — board updates, partner emails, newsletter drafts, decision logs — they need to read/write to the same apps. Composio's value compounds here: every skill reuses the same auth + tool exposure layer. The alternative is custom MCP servers per app, which is more work but more controllable.

**Decision criteria:** if Tom intends to keep his stack roughly as-is (Gmail, GCal, Notion if any, LinkedIn, Beehiiv, Granola) and Composio supports each one, it's the integration layer. If his stack is heavily Obsidian-native and most operations stay local-first, Composio is over-scoped — local MCP servers + a small number of custom integrations is enough.

### Q3. Does Composio change the answer for Erica's skills downstream?

If Composio becomes Tom's integration layer, Erica's skills inherit it for free. If not, Erica's stack gets its own integration decisions. Don't pre-commit; note it as a downstream implication and revisit when Erica's audit kicks off.

### Output

The Composio call lands in `aios-audit/setup/composio-decision.md` with:
- What Composio would replace in Tom's stack (the diff).
- Monthly cost vs custom-integration time saved.
- A clear yes / no / defer recommendation with reasoning.
- If yes: which integrations get migrated in what order.
- If defer: what signal would flip the decision to yes later.

---

## Pre-flight (~15 min with Tom at his laptop)

Before the autonomous scan, Annabel and Tom walk through:

1. **Vault path.** Absolute path. Annabel notes it in the run-log.
2. **OAuth.** Gmail (sent only), Granola (transcript API — needs Business tier or higher; if Tom is on Personal, flag and decide whether to upgrade or skip transcripts), LinkedIn (personal + 4 company pages). One-click each.
3. **Composio decision baseline.** Does Tom currently have a Composio account? If no, the audit defers the actual subscription decision to the deliverable; for the audit itself it uses direct OAuth per integration.
4. **Tool stack readout.** Tom names what's paid for and the plan tier. Anthropic Team plan (seat count + who has Cowork access), Beehiiv tier, Granola tier, Notion/ClickUp if any, any CRM, anything else.
5. **Exclusions.** Vault folders, channels, accounts to skip. Default is the whole vault and the channels listed above.
6. **Personal LinkedIn / personal Gmail OK to scan?** Useful for founder-voice signal. If not, work from company channels only.
7. **What's currently *Tom's* daily/weekly rhythm.** Quick verbal capture — what's on his calendar this week, what's recurring, what he wishes he didn't have to do. This seeds the personal context map; the audit refines it from materials but starting from Tom's own framing is faster than backing into it.

Annabel writes the answers to `aios-audit/_run/pre-flight.md`. Anything missing, the audit stops and surfaces — no fabrication.

---

## Gap questions (Tom + Annabel, ~15 min in person)

The audit will hit extraction gaps. Annabel asks Tom directly at his desk — no separate voice-memo solo pass. Likely buckets:

1. **Goals for the next 6-12 months per company.** Revenue, hires, new product, exit. Rarely in documents.
2. **Why each company exists separately.** Strategic reason CFS is distinct from Falcon, etc.
3. **ICP exclusions per company.** Who does each company actively say no to and why.
4. **Tom's own time allocation.** Where is he spending his attention vs where should he be.
5. **What would be most valuable to Tom personally if a skill drafted it for him tomorrow.** Forces a prioritization signal — board update? Partner email? Sales follow-up? Granola summary?

Annabel slots the answers back into the relevant canon and personal-context files. Citations updated.

---

## Per-company expectations

- **AIH** — light pass. Founder identity + holding-co structure. Likely Personal AIOS shape — no operational pod beyond Tom himself.
- **CFS** — full pass. Pilot candidate. Tom's role is clearer here, more material exists.
- **Falcon** — full pass. Other pilot candidate. Structurally similar to CFS, brand-distinct.
- **FSL** — full pass. Most different. Likely flagged as round-2.

---

## What the audit explicitly will not do

- Will not modify originals. Everything lands in new `aios-audit/` and `canon/<co>/_normalized/` subfolders.
- Will not auto-provision paid services. Setup checklist + Composio call are *plans*. Tom approves spend.
- Will not recommend automating a workflow that doesn't have a measurable signal yet. No signal → no thermostat → not on the build queue. Fix the workflow manually or instrument it first.
- Will not design Erica's pipeline. That's the next audit, after Tom's first 2-3 personal skills are running with closed loops.
- Will not scan anything in Tom's exclusion list.

---

## Hard rules

- **Tom's personal system gets strong first.** Every recommendation passes the test: does this make Tom more capable as the AI Founder before any team-facing system is added?
- **Closed loops or it doesn't ship.** Every Tom-workflow gets L1/L2/L3 specified or it's not on the build queue.
- **Cite every claim.** Score, tag, recommendation traces to a quoted source.
- **Propose, don't decide.** Pilot company, Composio call, build order — all proposed with reasoning. Tom confirms.
- **No softening vocabulary.** Tom knows Cowork, Anthropic Team plan, Composio, Obsidian, Granola, Beehiiv, Blotato, Supabase, Cloudflare, OAuth, MCP. Use the real names.
- **Write to `_run/decisions.md` for every non-trivial call** (which workflows the audit picked as *Tom's*, why one company outranks another for pilot, the Composio yes/no/defer). Tom can read the trail without asking.

---

## Output layout (final state)

```
<vault>/
  canon/
    aih/_normalized/        ← founder identity only
    cfs/_normalized/        ← full canon (5 files + gaps + evidence + loops)
    falcon/_normalized/     ← full canon
    fsl/_normalized/        ← full canon
  aios-audit/
    tom-context.md          ← Tom's personal context map
    tom-workflow-loops.md   ← L1/L2/L3 specs for Tom's 3-5 workflows
    setup/
      inventory.md
      target-architecture.md
      composio-decision.md
      checklist.md
    pilot-recommendation.md
    build-order.md
    _run/
      pre-flight.md
      gap-answers.md
      decisions.md
```

---

## What runs after this audit

The build order in deliverable #7 takes over. First 2-3 Tom-workflows get heatered, then thermostated. Once Tom's own system is running clean for 2+ weeks, the next audit kicks off — Erica's pipeline at the pilot company, with the substrate (Anthropic Team plan, integration layer, Supabase if needed, Cloudflare crons) already in place from Tom's build.

`plan-v1-2026-05-14.md` (the original Erica-first plan) gets revised after this audit lands, so its starting point matches Tom's actual ending point.
