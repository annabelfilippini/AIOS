---
date: 2026-06-08
time: 12:30
project: vital-health-webflow-review
status: paused
next-session: Decide whether structural Hormone/Regenerative/Peptide additions (bullet lists, new pep cards, consultation notes) are worth doing now or held for client review.
published-to: https://vital-health-9bf311.webflow.io (Batch A + B + C all live; all high-risk clinical claims removed; soft language live across all 5 pillars)
---

# Session: Vital Health — Batch C body copy shipped (safety claims removed)

## What happened

- Continued from Batch B success into Batch C — body copy rewrites across all 5 pillar sections of `/services`.
- Held to the "small changes only" discipline — single-action set_text on parent Paragraph elements with single String children. Skipped any rewrite that would require remove + insert structural surgery.
- Shipped 18 paragraph rewrites end-to-end with one publish + curl verification at the end.
- Curl verified the high-priority safety claim removals are gone from live staging.

## Batch C safety claim removals — all verified gone from staging

- ❌ `18% of bodyweight after 6 to 8 weeks` semaglutide claim
- ❌ `96% stem cell concentration at birth to just 7% by age 80` exosome claim
- ❌ `epigenetic, turning off genes that manifest disease and turning on longevity promoting genes` peptide claim
- ❌ `sexual arousal enhancement, improved sensation, pelvic floor strengthening` PT-141 description
- ❌ `Thirty minutes` consultation length (now `Sixty minutes`)
- ❌ `cornerstone of this work is exosome therapy` regenerative framing
- ❌ `appetite suppressant` rigid framing (now `may help regulate appetite and fullness`)

## Batch C writes — by pillar

| Pillar | Writes | Notes |
|---|---|---|
| Hormone | 2 (lede + For men) | For women paragraphs SKIPPED — require structural bullet list expansion |
| Weight | 3 (Semaglutide, Tirzepatide, both-medications) | All high-risk claims removed |
| Peptide | 8 (tagline + lede + explainer + 5 pep cards) | Critical: epigenetic claim removed |
| Regenerative | 4 (tagline + lede + exosome explainer + IV menu) | Critical: 96%/7% stem cell claim removed |
| Schedule | 1 (Thirty → Sixty minutes) | Matches new clinic intake length |

All landed via single-action `set_text` on parent Paragraph elements. One write on a String child surprisingly succeeded (IV menu paragraph) when earlier in the session it had timed out — the bridge appears to be more reliable on long-running connections than on cold/freshly-activated ones, or single-child Paragraph Strings behave differently than multi-child Heading Strings. Worth more diagnostic if it becomes a blocker.

## Structural work deliberately skipped today

These are in the source HTML but not yet in Webflow staging — would require remove_element + element_builder/whtml_builder surgery and are larger than today's "no big changes" discipline:

- **Hormone For women section** — source splits live's merged paragraph into multiple paragraphs with embedded bullet lists (Heart disease, Dementia, etc.; Fatigue, Weight gain, etc.). Live currently shows the bullets as inline-text inside the paragraph. Source structure is more readable.
- **Hormone For men "Men with low testosterone may experience" bullet list** — doesn't exist in live, would add ~11 li elements.
- **Weight pillar svc-note** — "Schedule a complimentary consultation to understand whether GLP-1 therapy is right for your goals and health history. Coverage and pricing are reviewed during the visit." Doesn't exist in live yet.
- **Peptide pillar svc-note** — "This is not a complete peptide list. Additional protocols may include Human Growth Hormone, Cerebrolysin, LL-37, Thymosin Beta-4, and other peptide options. We'll walk through what is indicated during your 60 minute consultation." Doesn't exist in live.
- **Regenerative pillar additional pep-grid** — source has a second card grid (Nutrient IVs, Ozone Therapy, NAD+ & Glutathione, Young Plasma) under the IV menu paragraph. Doesn't exist in live.
- **Batch D** — diagnostics testing cards. HOLD pending clinic PDF.

## Decisions

- Ship safety improvements first, do structural restructures in a separate dedicated session. The 18 single-action paragraph rewrites carry most of the clinical-claim risk anyway; bullet list cosmetics are second-order.
- Keep using the "parent Paragraph with single String child = safe set_text target" pattern going forward.
- One write per call, one publish at the end of the batch, one curl verification covering all expected changes.

## Open questions

- Are the Hormone For women bullet lists important enough to justify structural surgery in a dedicated session, or is the current merged-inline-text form acceptable for live launch?
- Should the new Peptide consultation note ("This is not a complete peptide list…") be added before clinic launch, or is the current state acceptable?
- Same question for the new Weight pillar svc-note and Regenerative additional pep-grid.
- When is the diagnostics PDF expected so Batch D can ship?

## Files touched

- (none — all changes were Designer writes via Webflow MCP, no local file edits this session)

## Next session restart plan

1. Confirm the answer to the structural-surgery question (above): worth doing or hold?
2. If yes — plan the structural batch the same way: load the source for each section, identify each element to add/remove/edit, plan single-action ops one at a time.
3. Designer activation handshake, page switch to Services, re-discover ids, execute.
4. If no — Services page is shipped for now; pivot to other pages (Home / About / Contact / Shop) or batch D when the PDF arrives.

## Context to preserve

- Site ID: `6a15e6f364922623e13946da`
- Services page ID + component scope: `6a15f430cbd0f7ef0469e27f`
- Designer activation link: `https://vital-health-9bf311.design.webflow.com?app=dc8209c65e3ec02254d15275ca056539c89f6d15741893a0adf29ad6f381eb99`
- Live staging Services URL: `https://vital-health-9bf311.webflow.io/services`
