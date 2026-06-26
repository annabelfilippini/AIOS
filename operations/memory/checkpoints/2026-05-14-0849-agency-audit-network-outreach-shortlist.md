---
date: 2026-05-14
time: 08:49
project: agency-audit-network
status: paused
next-session: Verify Lisa Baker + Matthew Lowe via Tom's authenticated Skool session, then send the Keith DM and queue the other 4 in the first wave.
---

# Session: Agency Audit Network — outreach shortlist + Keith DM draft

## What we worked on

Started from the 2026-05-13 re-scrape checkpoint. Annabel reviewed the candidate pool and triaged five operators by gut. Promoted three from "solid" to top-tier outreach, added one verify-first candidate from a prior session, and drafted the first DM (to Keith Mortier).

## Decisions made

- **Matthew Lowe (Mansel, `matthew-lowe-6062`)** — Annabel-flagged. Stays verify-first because Skool bio is generic; LinkedIn check required before DM. Memory: `project_agency_audit_matthew_lowe.md`.
- **Forrest Shaw (Mansel, `forrest-shaw-9087`)** — Annabel: "really good." Promoted from ⭐⭐ to first-wave. Lead question on intro: capacity (CIO day job + REI side practice). Memory: `project_agency_audit_forrest_shaw.md`.
- **Krzysztof "Kris" Wiselka (Mansel, `krzysztof-wiselka-7665`)** — Annabel: "also great." Promoted from ⭐⭐ to first-wave. Lead question: "what's the most recent n8n thing you shipped?" (bio reads ramping not shipping). Memory: `project_agency_audit_krzysztof_wiselka.md`.
- **Lisa Baker (`@lisa-baker-8973`)** — confirmed for outreach. Verify-first tier with Matthew. Community unknown — Tom's authenticated session needs to pull profile + identify community before DM. Scorecard `partners/lisa-baker.md` updated; memory: `project_agency_audit_lisa_baker.md`.
- **Keith DM tone calibration.** First draft was too tag-line-y ("anti-strategy mirrors ours", "no pressure either way"). Re-drafted in PLAN-voice: plain compliment, plain pitch, direct ask. Final draft preserved at bottom of this checkpoint.

## Open questions

- Should Cooldown be name-dropped as proof in the Keith DM, or kept out until call? Left out of v2 draft.
- Lisa Baker's Skool community is still unidentified — until it's known, the DM can't reference it specifically.
- Philip Couboura, Ben Williams, Fred Vinson from the Mark Kashef pool weren't reviewed this session. Worth a triage pass before the first DM wave goes out.
- Has anyone looked at ObsidianLogic.ai's site? DM implies vetting; a 60-sec skim is owed before send.

## Next steps

1. **Verify Lisa Baker** — pull profile via Tom's authenticated Skool session using the `?levels=N` pattern. Identify her community; confirm implementation positioning.
2. **Verify Matthew Lowe** — LinkedIn search for shipped work; check what businesses he serves.
3. **Skim ObsidianLogic.ai** (Keith) before sending the DM.
4. **Send Keith DM** (draft below). Then draft the other 4 first-wave messages in the same voice:
   - Bill Candelaria — "Scaling Small Businesses with AI + Automation"
   - Frank Gannon — Airtable + Make; he's explicitly looking for opportunities
   - Forrest Shaw — lead with capacity question
   - Kris Wiselka — lead with "what's the most recent n8n thing you shipped?"
5. After first wave goes out: review Mark Kashef ⭐⭐⭐ candidates not yet triaged (Couboura, Williams, Vinson).

## Context to preserve

**Outreach shortlist as of this session:**

First DM wave (5): Keith Mortier, Bill Candelaria, Frank Gannon, Forrest Shaw, Krzysztof Wiselka.
Verify-first tier (2): Matthew Lowe, Lisa Baker.

**Final Keith DM draft (in Annabel-voice, ~100 words):**

> Hey Keith — really like what you're doing at ObsidianLogic. The "not just talk about it" framing is exactly the kind of agency I'd want to send business to.
>
> Quick on me: I'm building an audit practice for small product brands (mostly Shopify, $500k–$5M revenue). Basically a clear, well-designed automation map that shows owners where AI could actually help them and what to prioritize. When a business is ready to build, I hand them off to a vetted partner — the idea being the agency gets a warmer, better-scoped client.
>
> I'd love to work with you on the partner side and send you clients when the fit looks right. Up for a quick call so I can hear what your sweet spot is?

**Tone calibration (durable for future DM drafts):** Plain, declarative, no tag-line beats. Cut "no pressure either way" / "anti-strategy mirrors ours" / "caught my eye." Use PLAN vocabulary: "automation map," "small product brands," "vetted partner," "warmer, better-scoped client."

**Files updated this session:**

- `projects/agency-audit-network/research/mansel-members-agency-candidates-2026-05-12-v2.md` — added Annabel-signal lines on Matthew Lowe, Forrest Shaw, Kris Wiselka; updated outreach order.
- `projects/agency-audit-network/partners/lisa-baker.md` — status flipped to Annabel-confirmed verify-first.
- 4 new memory entries (Matthew, Forrest, Kris, Lisa) + MEMORY.md index updated.

## System refinement candidates

- **DM-drafting voice guide.** This session calibrated the right tone twice (v1 → v2). Worth distilling into a one-page reference in `templates/` so future DMs start in the right register: open with plain compliment, pitch in PLAN-vocabulary, end with a direct ask, no tag-line beats.
- **Verify-first batch workflow.** Matthew + Lisa both need authenticated-session profile pulls before they can be DM'd. Worth scripting as a single batch step in the `skool-press` tooling: "pull profile + posts + identify community for a list of handles."
