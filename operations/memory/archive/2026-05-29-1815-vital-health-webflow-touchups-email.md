---
date: 2026-05-29
time: 18:15
project: consulting / vital-health
status: touchups-live-on-staging; client email drafted; founder-story decision routed to Julie via Rob
next-session: Send/await Rob's reply on the client email (hosting cost OK? + Julie's call on the founder story). Two original blockers still gate a live custom-domain publish — real testimonials (Home) and medical-claim sign-off (Services). CLAUDE.md em-dash rule still pending Annabel's approval.
---

# Session: Vital Health Webflow — Touchups Live + Client Email

Supersedes `2026-05-29-1802-vital-health-webflow-touchups.md`.

## Site state (unchanged from 18:02 checkpoint — all live + verified)
Staging `vital-health-9bf311.webflow.io` (subdomain only, `customDomains: []`).
Verified via curl: 0 em-dashes on every page; "Hope and Healing" gone; Contact
Portal row removed; Services 4 jump links now forest green (`.svcpg-jumplink`,
#1F4D2A in published CSS). About team heading → "The team that stays with you";
"three sets of eyes" line rewritten. Home founder stat → "established by founder
Dr. Joseph Feste". Full edit detail in the superseded 18:02 checkpoint.

## NEW this session: client email to Rob
Annabel is sending Rob an email (handing the site to the original owners). Final
draft includes:
- Site moved to Webflow so anyone can edit/add promos.
- Flag: Webflow hosting = $40/mo ongoing, billed to Vital Health. Asks if OK.
- **Founder-story question routed to Julie** (Annabel was unsure, wanted Rob to
  ask Julie): About page tells Dr. Joseph Feste's founding story. He no longer
  sees patients. Annabel already reworded it to read as history/legacy, not
  present practice. Email asks Julie whether to keep as-is, trim, or remove
  entirely. (This resolves the "About founder narrative" follow-up by deferring
  to the client rather than editing unilaterally.)
- Backend next steps: patient portal retail items, connect Cerbo, let Julie's
  team add hormones to a client's cart for checkout.
- Pricing: website $700 (1 day @ $95/hr). Backend also $95/hr. Itemized invoice
  every Friday for actual hours. Stripe.

Email kept in Annabel's plainer, direct voice; no em-dashes.

## Still open / needs Annabel
1. **CLAUDE.md em-dash rule** — auto-mode classifier blocked the self-edit to
   `~/.claude/CLAUDE.md` Voice & Tone. Needs Annabel to approve/apply. Proposed:
   "Never use the em-dash (—) to tack on or expand a thought. Rewrite as two
   sentences, use a comma, or restructure. Applies to all writing."
2. **Founder story** — now awaiting Julie's call via Rob (see email above).
3. **Live-publish blockers** (unchanged): real testimonials (Home), medical-claim
   sign-off on Services (semaglutide / exosome 96%→7% / testosterone ~50%).

## Gotchas (reconfirmed)
- Designer `element_tool` times out mid-batch (~every other large call); retry
  with Designer tab foregrounded; re-query "—" to see what landed. Batches of
  ~5-6 set_text were the sweet spot. Data API (pages/sites) never timed out.
- Component-internal text: `de_component_tool open_canvas {component_id}`, edit,
  then `open_canvas {page_id}` to exit / switch pages.
- Webflow caches published HTML; curl-grep live URLs to verify.

## Key IDs (additions this round)
- New style: svcpg-jumplink (8c37938b-4684-9fb6-de8f-22d731be0176)
- Home hero image (alt fixed): 2912fcca-10a7-e746-265f-608f4d140fac
- (Site/page/footer/script IDs in earlier checkpoints.)
