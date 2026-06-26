---
date: 2026-06-20
time: 19:30
project: aios / compound-engineering
status: complete (audit script built + verified, design.md trunk wired, weekly schedule live)
next-session: Act on the audit findings — the 6 never-reused skills (adversarial-review-lite, plan-eng-review-lite, markdown-lint-operating-docs, guardrails-lite, investigate-lite, wayloft-qa-sweep): delete or wire into a workflow. And the 9 design files: begin promoting per-project lessons up into ~/.claude/design.md so the count consolidates instead of drifting. First weekly audit fires Mon 2026-06-22 08:30 (baseline, no delta yet).
---

# Session: Compound-engineering audit — measured it, made it repeatable, scheduled it

## What this session resolved

Annabel asked "do I use compound engineering a lot" and wants to make sure her
AI-OS is growing as she grows, especially for website/platform dev. Turned that
from vibes into a measured answer, built a permanent audit tool, fixed the
weakest compounding area (design), and put it on a weekly cadence.

## The measurement (the answer)

System IS compounding but unevenly. ~7.5 weeks old, accelerating: memory+checkpoint
files 3 (Apr) to 80 (May) to 142 (Jun). But reuse concentrates in a few
workhorses; a long tail is built-once-and-forgotten.

- Workhorses (reused 3+): checkpoint (110, process not domain), geo (14),
  instagram-carousel (12), client-website-refresh (9), shopify-redesign (4),
  webflow-rebuild-qa (3).
- Never reused since built (6): adversarial-review-lite, plan-eng-review-lite,
  markdown-lint-operating-docs, guardrails-lite, investigate-lite, wayloft-qa-sweep.
- Gone cold (8): decision-pipeline / implement-approved-plan / review-claude-plan
  untouched since Apr 27; shopify-redesign + client-opportunity-map + skool-digest
  cold since May 14.
- Build rate is outpacing reuse rate. That's the leak.

## 1. Audit script (BUILT + verified)

`operations/memory/scripts/compound-audit.mjs` — zero-dep Node, reads the memory
tree. Inventories skills/templates, counts reuse via substring match across
operations/memory, flags dead (0 refs) + cold (>coldDays since last ref), shows
activity-per-month, and design-file drift count.
Flags: `--json`, `--full`, `--coldDays N`. Caveat baked into how you read it:
substring matching inflates generic names (checkpoint 110, geo 14). Directional,
not forensic. It caught 3 more dead skills than my manual pass.

## 2. Design layer = the weakest compounding area (FIXED the mechanism)

Data showed website/platform design (the thing she most wants to compound) is
the LEAST consolidated: 9 scattered design.md/DESIGN.md files, global trunk only
54 lines and 3 days old, no feedback loop upward. Nine parallel forks drifting.

Per her instruction (don't touch CLAUDE.md, it already routes to design.md),
added two sections INSIDE ~/.claude/design.md:
- **Trunk and overrides** — declares it the single source of truth; per-project
  DESIGN.md files are override layers that inherit, not forks; trunk wins conflicts.
- **Keep this growing** — the feedback loop: after a build teaches a reusable
  lesson, promote it up into the trunk (project-agnostic) before the project
  closes. Test: "true on the next unrelated site?" yes = trunk, no = override.

## 3. Weekly schedule (LIVE)

Scheduled task `weekly-compound-audit`, cron `30 8 * * 1` (Mon 08:30 local).
Each run: saves a dated JSON snapshot to `operations/memory/audits/`, computes
week-over-week delta vs the prior snapshot (dead count, revived cold skills,
design drift, workhorse count), and lands one verdict: compounding UP/FLAT/LEAKING
+ the one thing to fix. The snapshot history is itself the compounding part —
builds a trend line over weeks. First run Mon 06-22 = baseline, no delta yet.
Runs only while the Claude app is open (fires on next launch if closed).

## Key decisions

1. Measure before advising — pulled real counts from the memory tree, didn't
   answer from vibes.
2. Make the audit a permanent script, not a one-off — the tool itself compounds.
3. Design feedback-loop rule lives in design.md, NOT CLAUDE.md (her call; CLAUDE.md
   stays a thin router).
4. Weekly not monthly — she wants to keep tabs closely; snapshot history makes
   weekly meaningful rather than noisy.

## Next steps

- Clear the dead-skill tail: delete or wire up the 6 never-reused skills.
- Start consolidating the 9 design files up into the trunk (drives the count down).
- Watch the first real delta on Mon 06-29 (06-22 is baseline).
