---
date: 2026-05-14
time: 09:40
project: agency-audit-network
status: complete
next-session: Pilot Mansel's 7-step audit on one of Dad's employees. Use the verbatim discovery script (synthesis §8). Write the v1 Quick Read deliverable from the pilot, then refine the Deep Audit template from real usage.
---

# Session: Mansel AIOS content captured + synthesis rewritten Mansel-first

## What we worked on

Continuation of the morning's Mansel + Bo scrape work. Annabel pushed back that the synthesis leaned on Bo Sar (whose YouTube transcripts were easy to grab) and skipped Mansel's actual AIOS substance. Acknowledged the miss, installed playwright-core (12MB, uses system Chrome), wrote an authenticated Playwright fetcher that injects auth cookies including httpOnly tokens. Captured Mansel's verbatim module bodies for 21 modules across AIOS Model, One-Person AI Transformation, and Blueprint Library. Rewrote the synthesis Mansel-first.

## Decisions made

- **Mansel is the spine of Annabel's audit, not Bo.** Bo demoted to one corroborating section. Mansel's audit IS the product Annabel sells; Bo's is a sub-step inside Phase 1.
- **The 7-step audit framework lifted verbatim from Mansel's "Audit Deep Dive" module.** QDOAA sequencing (Question→Delete→Optimize→Accelerate→Automate, in that order) is the non-obvious rule. 9-point step tagging + 4 pain indicators is the diagnostic method.
- **Maintenance retainer is the recurring revenue play.** Mansel's 3-tier ($8K/$10K/$15K) + 5 pillars + insurance-not-overhead positioning is the model. Adopt verbatim.
- **Daily Brief is the wedge skill for Dad's employees.** Both Mansel (Blueprint Library) and Bo (Phase 4) independently recommend it as the starter. Convergence = signal.
- **Pricing ceiling: 4-phase ($10–70K audit + $15–100K+ implement + $5–20K train + $8–15K/mo retainer).** Mansel's ceiling is way higher than Bo's; use Mansel's structure.

## Open questions

- Whether to capture the blueprint zip bodies (Daily Brief, Pod Mapping Skill, Onboarding Skill, AIOS Full) — blocked by Skool signed URLs. Recommendation: Annabel clicks Download manually in Skool only if a specific blueprint blocks the pilot.
- Whether to request Mansel's Audit Notion Page directly via DM as part of a partnership conversation — defer until after pilot + Cooldown proof are both real.
- Vibe Coding & Agentic Workflows (new 40-module course, not captured) — lower priority for the audit work; revisit only if implementation skill gaps surface.

## Next steps

1. Read `sources/mansel-ainative-2026-05-14/captured-module-bodies.md` in full (51KB / 1875 lines of Mansel's actual writing — start here).
2. Pilot the 7-step audit on one of Dad's employees. Use Mansel's verbatim 7-question discovery script (synthesis §8). 30-min discovery + 15-min shadow + 1-hr write-up.
3. Generate v1 Quick Read in the 5-page shape (synthesis §10).
4. Refine the Deep Audit template after pilot, don't pre-optimize.
5. Out of scope: productization, website copy, partnership outreach, video transcription.

## Context to preserve

**Files produced this session (after the earlier 09:25 checkpoint):**

- `projects/agency-audit-network/research/audit-system-synthesis-2026-05-14.md` — rewritten Mansel-first, 13 sections
- `projects/agency-audit-network/research/audit-system-synthesis-2026-05-14-bo-first-draft.md` — archived original (preserved per checkpoint rules)
- `projects/agency-audit-network/research/sources/mansel-ainative-2026-05-14/captured-module-bodies.md` — 21 module bodies verbatim (the goldmine)

**Authenticated Skool capture pattern that worked** (worth remembering): playwright-core + system Chrome + cookies parsed from Chrome's "Copy as cURL" output, injected via `context.addCookies()` which handles httpOnly tokens that direct curl can't bypass. Module URL pattern is `?md=<full-32-char-id>` not `<8-char-name-field>`. Script preserved at `/tmp/pw/mansel-expanded.mjs`.

**Security cleanup completed:** `~/Documents/skool/` is empty. Both .rtf and .txt curl files deleted.

**Supersedes:** `2026-05-14-0925-mansel-beau-audit-synthesis.md` (which was written before the Playwright pass that actually captured Mansel's content). That earlier checkpoint is preserved but its "synthesis is complete" framing is now wrong — the real Mansel-first synthesis is the one named in this checkpoint.

## System refinement candidates

- The two-pass Skool capture pattern (curl for structure → playwright-core for bodies) should be promoted into `cli-connections/skool-press/` as a documented technique. Saved one memory already (`reference_skool_resources_need_playwright.md`) but the working scripts in `/tmp/pw/` are the proof.
- The synthesis-style "lead with primary source's actual writing, demote secondary source to corroborating section" is a better default than the "compare and contrast" shape I used in the first draft. When Annabel has a clear preferred source (here: Mansel), the synthesis should center it.
