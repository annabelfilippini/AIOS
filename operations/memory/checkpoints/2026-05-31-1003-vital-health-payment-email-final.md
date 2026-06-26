---
date: 2026-05-31
time: 10:03
project: vital-health-webflow-migration
status: complete
next-session: Email to Rob is send-ready; if sending invoices, verify Stripe account (bank + identity) so the $700 payout isn't held
---

# Session: Vital Health payment/pricing email to Rob

## What we worked on

- Drafted and iteratively tightened the client email to Rob covering site handoff + pricing.
- Advised on payment logistics: how to accept payment, billing cadence, Stripe workflow, hours estimate.

## Decisions made

- **Site fee: $700 flat** (one day of work at $95/hr rate). Invoiced now.
- **Backend work: $95/hr.** Covers manager meetings, retail items, Cerbo connection, patient portal, hormones-to-cart flow, plus "anything else they need."
- **Billing cadence: itemized invoice every Friday** for actual hours that week (this is the transparency/safety mechanism instead of a deposit).
- **Payment tool: Stripe.** Chosen over Wave/Venmo/Zelle for professionalism + paper trail. Send invoice as a pay-by-link (card or ACH); client enters own payment info; never charge card directly.
- **Webflow hosting: $40/mo, billed to Vital Health directly** (not bundled into Annabel's fee).
- Dropped the "deposit" framing entirely (Annabel disliked it).
- Dropped explicit hours estimate (12–30 hrs / $1,150–$2,850) from the final email — Annabel chose to keep it lean; estimate exists internally if needed.
- Removed "Net 15" line and all em-dashes per Annabel's preferences.

## Open questions

- Did Annabel verify her Stripe account (bank account linked + identity confirmed) so payouts aren't held?
- Are there Cerbo/patient-portal subscription or API fees, and who absorbs them? (Email no longer states this explicitly.)

## Next steps

- Send the final email to Rob (send-ready version below is approved).
- Set up Stripe customer for Rob once, then create → pick customer → add line items → send each Friday.
- After manager meeting, the backend hours become real; track hours daily for accurate Friday invoices.

## Context to preserve

- Stripe fees: cards 2.9% + 30¢ (~$679 net on $700); ACH 0.8% capped at $5 (~$695 net). ACH preferred for larger amounts; don't add fees to price.
- Annabel writes plain/direct, no marketing-speak, NO dashes (em/en/--). Wants concise; flagged Claude's tendency toward excess wording.
- Final email lives only in this session transcript; key structure = site handoff → backend scope → pricing → Stripe → reply to confirm.
- Related: this is the lighter email version; a separate formal 2-page proposal PDF also exists (see 2026-05-31-1002 and 2026-05-30 checkpoints; payer = Dr. Feste).

## System refinement candidates

- Recurring friction: Claude adds excess wording; Annabel repeatedly trims. Already covered by Voice & Tone rules but worth reinforcing conciseness on client-facing drafts.
