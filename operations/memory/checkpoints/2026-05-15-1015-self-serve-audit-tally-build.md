---
date: 2026-05-15
time: 10:15
project: agency-audit-network
status: in-progress
next-session: Open https://tally.so/forms/rjJo05/edit, review the audit form Annabel hasn't seen yet, add the 5A↔5B logic jump, replace the Section 6 Google Sheets TODO, publish, then embed on site-draft/audit.html.
---

# Session: Self-serve audit doc + Tally form build

## What we worked on

1. Created new self-serve audit spec at `projects/agency-audit-network/research/templates/self-serve-audit.md` — Mansel's KB (`~/Downloads/Knowledge Base-20260406084428 (2).md`) as the spine, Bo layered minimally (6-Layer Brain at Section 2, DRI + open-loop tag in Step Card, acceptance rules format on Quick Win cards), Mark Kashef intentionally not cited after Annabel removed his red-flag self-screen.
2. Archived old consultative playbook: `paid-audit-playbook.md` → `paid-audit-playbook.archived.md` with banner pointing to the new file.
3. Compared Tally vs Typeform; recommended Tally Pro ($29/mo) over Typeform — completion-rate evidence beats polish on a 60–90 min form.
4. Reverse-engineered Tally's undocumented API block schema (see Context to preserve).
5. Built the 343-block audit form via Tally API: form ID `rjJo05`. Build script saved at `projects/agency-audit-network/scripts/build-tally-audit.mjs`.
6. Cleaned up 5 throwaway test forms from Annabel's Tally workspace.

## Decisions made

- **One product, not two.** The consultative ($1.5K–$30K Annabel-led) version is retired. Only the self-serve, user-filled, PDF-output audit exists going forward.
- **Mansel-spined, Bo layered minimally, Mark deferred.** Bo earns Section 2 (Brain), the DRI field, the open-loop tag, and the acceptance-rules format. Mark's flight plan / Autopsy / Chinese Menu / video automation reserved for possible Phase 2.
- **Deliverable is a PDF**, not a Notion living doc. (Reverses Bo's framing — Annabel's audience wants the PDF artifact.)
- **Tally Pro** picked over Typeform after honest comparison. Completion rates on long forms favor Tally's section-at-a-time UX.
- **Both 5A (Sales Discovery) and 5B (End-User Workflow) included inline** with skip instructions; conditional logic jump to be added manually in Tally UI (5-min task).
- **Pricing, Stripe, auto-PDF gen deferred** until after manual test runs. Mansel's "don't automate a broken process" rule applied to the audit product itself.

## Open questions

1. Section 6 (Map your process) has a `TODO` placeholder — needs a real Google Sheets Step Cards template URL before going live.
2. Annabel hasn't reviewed the form in the Tally UI yet. Some questions may read awkwardly one-at-a-time and need trimming.
3. Pricing for the self-serve audit — still not decided.

## Next steps

1. Annabel opens https://tally.so/forms/rjJo05/edit and reviews the form end-to-end.
2. **Rotate the Tally API token.** Old token (`tly-1yY5...`) was used in this session and is in the conversation history — treat as compromised.
3. Add the 5A↔5B logic jump in Tally UI: "if engine = Acquisition → skip 5B; else skip 5A."
4. Build Google Sheets Step Cards template for Section 6; update the form to link to it.
5. Publish form (currently DRAFT) and grab embed code.
6. Embed in a new `site-draft/audit.html` page (Task #4 still pending).
7. Test by filling out as a user end-to-end.

## Context to preserve

- **Tally API schema, reverse-engineered** (was undocumented):
    - Each block needs unique UUID v4. `groupType` MUST match `type` for most blocks (TITLE, INPUT_TEXT, INPUT_EMAIL, TEXTAREA, LINEAR_SCALE, FILE_UPLOAD, etc.).
    - Headings use `HEADING_1`/`HEADING_2`/`HEADING_3` (underscore, not number-suffix).
    - **Option blocks** (`MULTIPLE_CHOICE_OPTION`, `DROPDOWN_OPTION`, `CHECKBOX`): share a `groupUuid` across all options; `groupType` is the plural form (`MULTIPLE_CHOICE` / `DROPDOWN` / `CHECKBOXES`); every option needs explicit `isFirst` and `isLast` booleans in payload.
    - `LINEAR_SCALE` cannot be the first input block in a form; precede it with a simple input.
    - Tally normalizes `html: "text"` payload into `safeHTMLSchema: [["text"]]` on retrieval.
    - All these gotchas are documented in the header comment of `scripts/build-tally-audit.mjs`.
- Tally workspace ID for Annabel: `3ye6Kp`. Form ID: `rjJo05`.
- Old playbook (consultative version, ~1044 lines) archived but not deleted — useful reference if Annabel ever revisits.
- Recent prior checkpoint to look at: `2026-05-14-1230-aios-audit-merge-and-self-serve-pivot.md`.

## System refinement candidates

- The 15 min of Tally API trial-and-error could be permanent. The header comment block in `scripts/build-tally-audit.mjs` captures every quirk. If Annabel builds more Tally forms (intake, scorecards, agency-side requests), the script is a working template — copy it, swap the content. Worth promoting to a shared skill if Tally usage compounds.
- Annabel rejected pre-structured AskUserQuestion forms last session and again wanted plain chat for product-shape decisions. Strong pattern: open-ended product decisions = conversational sketching, not forced multi-choice.
