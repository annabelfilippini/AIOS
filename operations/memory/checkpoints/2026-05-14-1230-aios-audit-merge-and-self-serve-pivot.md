---
date: 2026-05-14
time: 12:30
project: agency-audit-network
status: paused
next-session: Resume the self-serve audit conversation — Annabel rejected the multi-choice AskUserQuestion. Ask plainly in chat what she wants the fillable format to look like before restructuring the 56KB paid-audit-playbook.md.
---

# Session: AIOS Starting Point Audit — Mansel/Bo/Mark merge, then self-serve pivot

## What we worked on

1. Authenticated scrape of Mark Kashef's `skool.com/earlyaidopters` AI Consulting Playbook (16 modules). Captures live in `research/sources/kashef-earlyaidopters-2026-05-14/`. Module 14 ("Mastering Engaging Workshops") has full written body — 5-part flight-plan structure. Module 6 ("$20K Audit Automation") describes the n8n/Gamma/11Labs video-audit pipeline.
2. Wrote merged paid-audit playbook at `research/templates/paid-audit-playbook.md` (~56KB). Mansel's audit is the spine (interviews verbatim, Step Cards, friction tags, QDOAA, scoring matrix, Money Slide). Bo layered: 6-layer Business Brain, DRI/AI-Founder roles, open-loop tag, test harness, living-doc framing. Mark layered: Red Flags, Autopsy Protocol, Chinese Menu pricing, 5-part flight plan presentation, video-deliverable option.
3. Moved `templates/` → `research/templates/`. Updated path refs in `README.md`, `AGENTS.md`, `PLAN.md`, and synthesis files.
4. Wrote `research/audit-shape-decision-2026-05-14.md` reconciling all docs → recommended audit shape.
5. Made two follow-up edits to the playbook: Page 1 now commits to one of four AIOS-level recommendations (Personal / Team / Company / Cleanup-before-automation); client-facing product name *AIOS Starting Point Audit* introduced in Section 0 and used in the engagement-shape and four-phase tables.

## Decisions made

- Client-facing product name: **AIOS Starting Point Audit**. CTA: *"Find Your AI Operating System Starting Point."* Internal name: "the paid audit."
- Vocabulary: pods + Operations (not engines + Internal).
- Pricing bands (consultative version): $1.5K solo → $3K–$5K small biz → $5K–$10K product brand → $10K+ mid-market. Anchor on ROI Stack × 10–20%.
- Deliverable identity: living Notion doc, not PDF. PDF is an export. Video option deferred to phase 2.
- Personal / Team / Company / Cleanup framing is Annabel's packaging — Mansel doesn't have these tiers (per `mansel-audit-structure-check-2026-05-13.md`).

## Open questions

1. **The big pivot Annabel raised at end of session:** the audit goes on her website, users fill it themselves, no Annabel interviews. The current 56KB playbook is Annabel-led (interviews, mapping, workshop, presentation) — needs major restructuring. I offered an AskUserQuestion with format options (Notion template / Tally form / hybrid) and Annabel-role options (self-serve / reviewed / both tiers). **Annabel rejected the multi-choice form and invoked `/checkpoint`.** Reason not yet stated — possible she wanted conversational back-and-forth instead of pre-structured options. Resume by asking plainly in chat.
2. Pricing for self-serve version (was $1.5K–$10K consultative — self-serve typically lower, $99–$799 range).
3. Whether to keep the consultative playbook as the high-touch tier AND build a self-serve tier, or replace consultative entirely with self-serve.

## Next steps

1. Reopen the self-serve format question with Annabel in plain chat (no multi-choice).
2. Once format is locked, restructure `research/templates/paid-audit-playbook.md`:
   - Mansel's interview question sets → self-fill prompts (the questions stay verbatim, framing changes)
   - Phase 9 (validation workshop) + Phase 10 (presentation) drop entirely
   - Mark's Autopsy Protocol drops (no calls)
   - Add a generated agency-handoff-brief section that auto-populates from the user's inputs
3. Pilot on Dad's employee — still the cleanest first test.
4. After pilot, decide whether to build the Mark-style video automation (phase 2 productization).

## Context to preserve

- Source captures live in `research/sources/`:
  - `kashef-earlyaidopters-2026-05-14/` — authenticated Skool capture (Mark's 16 ACP modules, full JSON + markdown extract)
  - `mansel-ainative-2026-05-14/` — Mansel's module tree + bodies
  - `bo-sar-*.md` and `beau-bosar-aif-sop-2026-05-11.md` — Bo transcripts
- Mansel's downloaded Knowledge Base (full Phase 1 audit) at `~/Downloads/Knowledge Base-20260406084428 (2).md`.
- Skool authenticated access works via Tom Filippini's account: cookie at `~/Documents/skool/skool-curl.txt` (was an RTF, converted with `textutil`). Token rotates — re-export before next authenticated pull.
- Scrape scripts at `/tmp/kashef-sweep.mjs`, `/tmp/kashef-modules.mjs`, `/tmp/kashef-extract.mjs` — preserved for re-run if needed.

## System refinement candidates

- Annabel rejected an AskUserQuestion with previews on a product-shape decision. Possible signal: she prefers conversational sketching for open-ended product decisions, not pre-structured forced-choice. Worth confirming next session before saving as a memory. (Reference: this session ended right after the rejection.)
