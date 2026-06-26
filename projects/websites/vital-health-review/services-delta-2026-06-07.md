# Services Page — Webflow vs Local HTML Delta

Date: 2026-06-07
Target file: `projects/websites/vital-health-review/services-review.html`
Live baseline: `https://vital-health-9bf311.webflow.io/services` (curl confirms NONE of the prior 3f.1 Designer changes published)
Designer state: unknown after reload — treat as old state until proven otherwise via fresh query

## Strategy

Work in small batches (2–3 Designer writes per call). Snapshot after each batch. Publish to `.webflow.io` subdomain only. Curl-verify after every publish. Do NOT push to custom domain in this session.

---

## Batch A — Structural (low risk, safe to ship without further sign-off)

1. **Hero h1**: `Four pillars of integrative care.` → `Five pillars of integrative care.`
2. **Section reorder** (current → target): Peptide, Hormone, Weight, Wellness, Diagnostics → Hormone, Weight, Peptide, Regenerative, Diagnostics
3. **Anchor rename**: section `id="wellness"` → `id="regenerative"`
4. **Meta description**: replace four-pillar wording with `Hormone optimization, weight management, peptide therapy, regenerative medicine, and advanced diagnostics and early detection, guided by labs, goals, and the full clinical picture.`

## Batch B — Section headings (low risk)

5. **h2**: `Medical Weight Loss` → `Weight Management`
6. **h2**: `Wellness & Rejuvenation` → `Regenerative Medicine` (with emph span around "Medicine")
7. **h3**: `How peptide therapy works` → `How peptide therapy is considered`
8. **h3**: `Our peptide protocols` → `Protocols we may discuss`

## Batch C — Body copy (risk reduction — replaces strong/old claims with softer language)

Each of these REPLACES copy already live with softened copy. Net effect: less risk on the published site, not more. But it is a lot of writes.

- **Hormone Optimization** body: replace with local copy (softens testosterone-decline framing, women/men bullet groups, ninety→60 min, "labs and clinical picture" wording).
- **Weight Management** body: remove `18% bodyweight after 6 to 8 weeks` semaglutide claim; soften GLP-1 copy; replace `appetite suppressant` with appetite/fullness regulation wording.
- **Peptide Therapy** body: replace with local copy (personal-intro wording, remove epigenetic/longevity-promotion claims, add "How peptide therapy is considered" section, refreshed protocol cards: Ipamorelin, Sermorelin, BPC-157, CJC-1295, MOTS-c, Thymosin-alpha1, PT-141, Semax/Selank, plus the "not a complete list, additional options discussed during the 60 minute consultation" note).
- **Regenerative Medicine** body: replace with local copy (exosomes as cellular messengers, IV nutrient/ozone/NAD+/glutathione, young plasma discussion language, remove old numeric exosome/stem-cell concentration claim, remove `stem cell` and `epigenetic` from any remaining copy).
- **Schedule section**: `Thirty minutes` → `Sixty minutes`; remove `ninety` references.

## Batch D — New diagnostics section (HOLD)

Per change inventory: Advanced Diagnostics testing card names (DNA testing, Galleri, GlycanAge, NexGen, Cognivue, carotid ultrasound, HRV, body composition, heavy metals, GI MAP, full body MRI) are marked DRAFT pending final clinic PDF. **Do not push the testing-card content until Annabel says the clinic PDF is approved.** The section anchor and h2 from Batch A/B can ship without the cards — leave existing diagnostics content in place under the new heading until cards are approved.

## Out of scope for this session

- Home, About, Contact, Shop pages — separate deltas, do those in their own sessions.
- Global footer and nav changes — already shipped in Batch 5 last session.
- Custom-domain publish — staging only.

## Risk notes

- Live staging shows ZERO of the prior 3f.1 Designer changes. The 21:40 checkpoint's "in Designer only" partial work may have rolled back during reload. Re-discover element IDs in current Designer scope before writing — do not trust the checkpoint's IDs.
- The Designer Bridge times out on writes when the tab is backgrounded. Keep the Designer tab in foreground for the whole session. Probe with `get_current_page` before each batch.
