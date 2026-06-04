# Vital Health — Carousel Direction

Layer 3 of 3 in the carousel style stack. **Brand-specific direction for Vital Health's Instagram carousels.** Read after `style.md` (universal) and `media/brand_context/voice-profile.md` + `visual-identity/tokens.json` (brand character).

This file overrides defaults from layers 1 and 2 when Annabel makes a brand-specific direction call ("for Vital Health: …"). It does NOT duplicate brand character (that's in voice-profile.md and tokens.json).

The `listen-for-corrections.sh` hook auto-appends entries here when the correction names this brand or uses "for this brand" / "for VH" / etc.

---

## Category

- **Preventive medicine / integrative / wellness.** Triggers all "preventive" category modifiers in `style.md`:
  - Bright, morning light, growing, moving (not intimate/moody)
  - ICP skews older — older patient (50s+) mandatory in carousel photography
  - Health-brand playbook moves apply

## Proven openers

- **[2026-05-31] Intro slide 1 default: person at window in morning light, hands wrapped around a warm drink. Back-only, no face.** Proven across v1→v5. Sets the bright preventive tone.
  Source: v2 worked-well; v1→v2 rule
  Applies to: VH intro carousels

## Voice direction (beyond voice-profile.md)

- **Lead with the founder when the carousel arc supports it.** Dr. Julie Swett is the brand's most credible authority. ER background, 23 years, real numbers.
- **Specific over abstract.** "Ninety minutes" beats "comprehensive." "Four practitioners" beats "team-based." "Free thirty-minute call" beats "consultation."

## Visual direction (beyond visual-identity/tokens.json)

- (None yet — visual-identity tokens.json + the proven v5 build are the current source of truth.)

## What this file should NOT contain

- Brand voice (that's `voice-profile.md`)
- Palette / fonts / logo (that's `visual-identity/tokens.json`)
- Universal carousel rules (that's `skills/instagram-carousel/references/style.md`)
- Category-level rules like "preventive = bright" (that's `style.md` Category modifiers)

This file is reserved for **VH-only direction Annabel makes that doesn't fit any other layer**. Most corrections should NOT land here — they should land in layer 1.

---

## Edit log

- **2026-06-01** — Seeded from `skills/instagram-carousel/references/preferences.md` migration. Pulled the VH-proven slide 1 opener (the only entry strictly tied to VH's brand-intro arc rather than universal or preventive-category). Everything else generalized into layer 1.
