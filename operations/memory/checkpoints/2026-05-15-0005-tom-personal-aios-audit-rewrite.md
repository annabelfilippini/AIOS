---
date: 2026-05-15
time: 00:05
project: agency-audit-network
status: complete
next-session: Annabel sits at Tom's laptop and runs `dad-pilot/tom-personal-aios-audit-2026-05-14.md` with Claude Code. Pre-flight (~15 min Tom-at-desk) → autonomous scan → in-person gap questions (~15 min) → outputs land in `aios-audit/` and `canon/<co>/_normalized/`. The Composio decision is one of the three things the audit must produce — review that file first when reading back through outputs.
---

# Session: Tom's audit redo — strip Mansel, refocus on Tom's own system, add Composio, keep closed loops

## What we worked on

Annabel had three audit drafts in `dad-pilot/`: the original Tom-system-focused intake (clean but no framework), a Mansel-spined rewrite (sloppy, brochure-shaped), and during this session I produced a Mansel-spined skill + Tom-facing intake pair (better but still Mansel-framed and Erica-deployment-focused). Annabel rejected the framework framing and pivoted scope: the audit is now for Tom's own AIOS first, Erica deferred. Composio added as a substrate option to evaluate. Screenshare structure dropped because Annabel is running it at Tom's laptop herself.

Wrote `dad-pilot/tom-personal-aios-audit-2026-05-14.md` (~210 lines) as the single active doc. Rebuilt `~/Downloads/tom-audit-2026-05-14.zip` with three files: the new audit doc, `plan-v1-2026-05-14.md`, `loops-explained-2026-05-14.md`.

## Decisions made

- **Audit scope reframed Tom-first.** Erica's pipeline deferred until Tom's first 2-3 personal workflows have closed loops running clean for 2+ weeks. New deliverable: Tom's personal context map (his role across the 4 companies, his rhythms, *his* workflows — separate from any company's pod).
- **Mansel framework stripped.** No 6-Layer Brain / 4 Pods / QDOAA / Friction Tags / Money Slide vocabulary. The "fix process before automating" instinct survives as "no measurable signal → not on build queue" — plain operational logic, no brand.
- **Annabel is the operator at Tom's laptop.** No screenshare framing, no solo voice-memo handoff. Pre-flight is in-person at his desk; gap questions are conversational.
- **Composio gets a dedicated decision section.** Three Qs: replaces OAuth for audit's data collection? fits operational substrate for Tom's skills? changes Erica's downstream answer? Outputs to `aios-audit/setup/composio-decision.md` as yes / no / defer with reasoning.
- **Closed loops preserved as first-class.** New deliverable `tom-workflow-loops.md` applies L1 (day) / L2 (week) / L3 (month) + heater→thermostat to Tom's 3-5 workflows, not Erica's pipeline.
- **Active doc set:** `tom-personal-aios-audit-2026-05-14.md` + `plan-v1` + `loops-explained`. The Mansel-spined pair (`audit-intake-tom-2026-05-14.md`, `aios-starting-point-audit.md`) and the two earlier intake drafts are kept as iteration history, not deleted.

## Open questions

1. **Granola tier check.** If Tom is on Personal, transcript API isn't exposed — decide at pre-flight whether to upgrade or skip transcripts for this audit.
2. **Composio current state at Tom's stack.** Whether he has any Composio account today shapes the deliverable's recommendation framing.
3. **Which workflows count as "Tom's" vs "the company's."** The audit picks 3-5 in the personal context map deliverable, but the heuristic isn't sharp yet. Refine after seeing the actual extraction.
4. **Erica plan-v1 revision timing.** `plan-v1-2026-05-14.md` is Erica-first; needs revision after Tom's audit lands, but waiting until at least the first Tom-workflow is thermostated would give a real starting point.

## Next steps

1. **Run the audit at Tom's laptop.** Annabel sits with Tom, executes `tom-personal-aios-audit-2026-05-14.md` via Claude Code.
2. **Watch for the Composio decision output.** That file is the single most-novel deliverable; read it first when reviewing outputs.
3. **After the audit locks**, sequence Tom's first 2-3 personal-workflow skills per the build-order deliverable. Each ships as heater first, thermostat closes 2-4 weeks later.
4. **Once Tom's first thermostat closes**, revise `plan-v1` for Erica and kick off her audit using the substrate Tom's build leaves in place.

## Context to preserve

- **The Composio question is new context the prior research files don't address.** Worth a future memory if the audit's recommendation comes back as "yes, subscribe" — that becomes a stack decision that affects every downstream skill, Erica's included.
- **Annabel's instinct that the Mansel-framework framing felt off for Tom.** She iterated three times before landing on system-first/Tom-first. The pattern: when a framework is the centerpiece of an audit instead of the user's actual situation, it reads as marketing not operating. Worth a feedback memory.
- **The doc lineage:** `audit-intake-2026-05-14.md` (clean original, Erica-framed) → `audit-intake-mansel-spined-2026-05-14.md` (sloppy framework brochure) → `audit-intake-tom-2026-05-14.md` + `aios-starting-point-audit.md` (better but still Mansel-spined, Erica-deployment-focused) → `tom-personal-aios-audit-2026-05-14.md` (active: Tom-first, no framework brand, Composio added).

## System refinement candidates

- **Audit framing principle worth codifying:** the audit's centerpiece is the *user's situation*, not a framework. Framework vocabulary is a *citation*, not a *spine*. Apply to the eventual self-serve AIOS Starting Point Audit product — users buying it don't want a Mansel brochure; they want their situation read back to them with structure. Save as feedback memory if pattern holds across the Erica audit.
- **The "heater first, thermostat closes weeks 5-6+" sequencing language** travels well — survived three rewrites because it answers "when does measurement turn on" without forcing a framework. Worth promoting into reusable shape for any closed-loop-aware build plan.
- **One-doc-with-operator-instructions-baked-in** (this session's final shape) is a cleaner artifact than the split intake+skill pattern when the user is also the operator. Worth a memory if Annabel ends up using this shape again.
