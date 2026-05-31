---
date: 2026-05-22
time: 14:32
project: site / agency-audit-network
status: in-progress
next-session: Push the free AI Starting Point Audit to Tally after a rotated TALLY_TOKEN is available.
---

# Session: free audit preview and Tally handoff

## What we worked on

- Built a smaller free audit entry point for Annabel's site at `projects/site/free-audit.html`.
- Added site routes/CTAs for the free audit across the current site.
- Created a Tally API builder for the free audit at `projects/agency-audit-network/scripts/build-tally-free-audit.mjs`.
- Updated the Tally free audit wording so it clearly says Annabel manually reviews submissions and sends a short readout.

## Decisions made

- The free audit is a lead-in, not a replacement for the paid audit.
- The free audit should collect a focused 8-question preview plus basic contact information.
- The free audit output expectation should be: after submit, Annabel reviews answers and sends back where AI may belong first, what friction is showing up, and the next recommended step.
- The paid audit remains deeper: Step Cards, friction tagging, QDOAA cleanup, ROI, Quick Wins, success criteria, implementation constraints, and agency-ready handoff.

## Open questions

- The free Tally form still needs to be created or updated once a rotated `TALLY_TOKEN` is available.
- After the Tally form exists, decide whether the site should embed/link directly to Tally or keep the local instant-preview version as the front door.
- Decide whether submission responses should stay manual for early learning or later become email drafts via automation.

## Next steps

- Export the rotated Tally token in the shell.
- Run `node projects/agency-audit-network/scripts/build-tally-free-audit.mjs` from `/Users/annabelfilippini/Documents/AI-OS`.
- Save the returned Tally form ID if this creates a new form.
- Wire the live Tally URL into the site if Annabel wants Tally to be the primary capture form.

## Context to preserve

- Do not store or reveal Tally tokens.
- Annabel disliked the stock phrase "plain English"; `SOUL.md` now says to avoid "plain English" / "plain-English" in drafts and explanations.
- The current free Tally copy says: "After you submit, I'll review your answers and send back a short starting-point readout: where AI may belong first, what kind of friction is showing up, and the next best step I'd recommend."

## System refinement candidates

- Consider adding a small reusable Tally form builder pattern or template for future audit forms.
