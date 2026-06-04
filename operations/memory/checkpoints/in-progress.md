---
date: 2026-06-02
time: 09:35
project: instagram-carousel-skill
status: batch-2a-plus-done
next-session: Batch 2b — extend save_correction.py with a universal-vs-brand-specific classifier (write to <project>/media/brand_context/carousel-direction.md when the prompt names a specific brand). Also extend preship_audit.py to read the full 3-layer style stack. Then decide role renderers (Batch 3) vs auto-discovery (Batch 4) next.
---

# In progress: instagram-carousel skill generalization

## Batch 1 — engine refactor (DONE — earlier today)

- `render_slides.py` refactored to role-based dispatch.
- Six legacy renderers renamed; new `slides: [{role, copy, photo}, ...]` schema; legacy shim translates v5 `copy.slide_N_*` keys.
- Regression: all 6 v5 slide HTMLs byte-identical (SHA match).

## Batch 2a — preferences architecture (DONE — this session)

- Annabel greenlit 3-layer style stack: universal (skill) + brand character (`brand_context/voice-profile.md` + `visual-identity/tokens.json`) + brand direction (`brand_context/carousel-direction.md`).
- Migrated 38 entries from `skills/instagram-carousel/references/preferences.md`:
  - ~33 entries → `references/style.md` (universal)
  - ~3 entries → `references/style.md` under new `## Category modifiers` section (preventive=bright, ICP skews older for preventive)
  - 1 entry → `projects/vital-health-webflow-migration/brand_context/carousel-direction.md` (the VH-proven slide 1 opener: person at window, back-only, warm drink)
  - ~2 entries → deleted (hook noise; the listener over-broadly matched casual user-message text earlier in session)
- Old `preferences.md` deleted.
- Updated all 5 doc files (SKILL.md, skill README.md, references/README.md, inspiration/README.md, plus hook comment) to reference the new structure.
- Updated `save_correction.py` to write to `references/style.md` instead of `preferences.md`. Verified hook routing still works (smoke test: "the colour palette feels too muted" → § Photography; "don't use em-dashes ever" → § Typography).
- Confirmed VH brand_context already has the layer-2 character files (`voice-profile.md`, `visual-identity/`, `positioning.md`, `icp.md`, `samples.md`) — no foundation-skill work needed.

## Batch 2a-extension — brand_context relocated to media/brand_context (DONE — 2026-06-02 morning)

- Moved `projects/vital-health-webflow-migration/brand_context/` → `projects/vital-health-webflow-migration/media/brand_context/` per Annabel's new convention ("everything media-related goes in `<project>/media/`").
- Updated all 5 source-of-truth refs in `~/Documents/AI-OS/skills/instagram-carousel/`: SKILL.md, README.md, references/README.md, references/style.md, scripts/save_correction.py — all now point at `<project>/media/brand_context/`.
- Added foundation-skill compatibility note in SKILL.md §1: foundation skills (mkt-brand-voice, etc.) are plugin-owned and still write to `<project>/brand_context/` (legacy location). The skill reads the legacy folder if present and flags Annabel to move it once. Plugin updates are out of scope for this repo.
- Confirmed no leftover `<project>/brand_context/` at root for VH.
- Scope decision: did NOT touch project-local `.claude/skills/mkt-*` runtime adapters — they're plugin-managed snapshots; editing them would get blown away on next update.



- **Hook classifier (Batch 2b)** — `save_correction.py` still writes everything to `references/style.md`. Brand-specific corrections (those that name a brand or say "for VH" / "for this brand") should route to `<project>/brand_context/carousel-direction.md` instead. Classifier needs: detect brand name from active project brand_context, detect "for X" phrasing, auto-create carousel-direction.md if missing.
- **Multi-layer reading in `preship_audit.py`** — currently reads one file (`style.md` after the rename). Needs to load + merge the full 3-layer stack and lint against the merged ruleset.
- **Role renderers** — only 6 brand-intro roles. SKILL.md description still promises ad/educational/testimonial/list/story arcs without renderers for them.
- **Brand-context auto-discovery** — `discover_brand.py` not built. Skill still assumes brand_context exists.

## Decisions made

- Inspiration/ stays brand-agnostic only. Brand-specific past work lives in `<project>/media/<date>-<slug>/`. (Carried from earlier in session.)
- The peptide carousel is not the next priority — Annabel said "no rush." Skill correctness first.
- 3-layer architecture chosen over 2-layer or single-file-with-sections. Cleaner separation between "brand character" (foundation-skill territory) and "brand direction" (per-skill, per-brand).

## Open questions

- After Batch 2b, do Batch 3 (role renderers) or Batch 4 (brand-context auto-discovery) next? Auto-discovery is more architecturally important; role renderers are more visibly useful.
- Should there be a layer 4 (per-carousel direction inside the run folder) for one-off direction that shouldn't pollute the brand-direction file? E.g. "for this specific 4th of July promo, use red accents." Probably not — feature creep.
