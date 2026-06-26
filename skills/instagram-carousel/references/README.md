# references/

Layer 1 of Annabel's 3-layer carousel style stack.

## The 3-layer style stack

| Layer | File | Holds |
| --- | --- | --- |
| **1. Universal style** | `references/style.md` (this folder) | Annabel's invariants — apply to every brand, every carousel type |
| 2. Brand character | `<project>/media/brand_context/voice-profile.md` + `visual-identity/tokens.json` | Who the brand IS — voice, palette, fonts, logo |
| 3. Brand media guide | `<project>/media/design.md` | Project-specific social/media taste, especially when formal brand_context files are missing |
| 4. Brand direction | `<project>/media/brand_context/carousel-direction.md` | What Annabel wants THIS brand's carousels to do, beyond brand character |

The renderer reads the available layers and merges in order: universal → brand character → brand media guide → brand direction. Later layers override earlier on conflicts.

## `style.md`

Annabel's universal taste — every rule applies to every brand, every carousel type. Read top to bottom before drafting any copy or photos.

Sections:

- **Typography** — fonts, sizes, italic rules
- **Photography** — photo style, AI prompt vocabulary
- **Copy** — what to write, what to avoid
- **Layout / Composition** — slide architecture
- **TEXT-ON-PHOTO LEGIBILITY** — the highest-priority rule (caught twice)
- **Voice** — Annabel's plain-direct register
- **Don't do this** — hard avoidances
- **Category modifiers** — rules that activate based on the brand's category (preventive medicine, chronic care, etc.)
- **Working principles** — meta-rules carried across every run
- **Health-brand category playbook** — required "moves" derived from external ad analysis (for health/wellness brands)
- **Uncategorized** — hook fallback when keyword match fails (recategorize next run)

## How entries get added

The `listen-for-corrections.sh` hook in `~/.claude/hooks/` fires on every user message during a carousel run. When it matches a negative-feedback phrase ("I don't like X", "change the Y", "don't use Z"), it runs `scripts/save_correction.py` which:

1. Detects whether the correction is **universal** (default) or **brand-specific** (says "for VH", "for this brand", names the brand)
2. Appends a structured entry to the right file:
   - Universal → `references/style.md`
   - Brand-specific → `<project>/media/brand_context/carousel-direction.md` (creates it if missing)

Entry format:

```text
- [YYYY-MM-DD] <rule, one sentence, imperative>
  Source: <where it came from>
  Quote: "<Annabel's verbatim words>"
  Applies to: <carousel type | category | "all">
```

## Auditing past runs

The `## Edit log` at the bottom of each file tracks when entries were seeded vs hook-grown. If a rule turns out to be wrong (Annabel changes her mind), edit the entry rather than deleting it — leave a strikethrough or a `[REVISED YYYY-MM-DD]` line so the history stays readable.

## Why these files matter

Without them, every carousel run reinvents the wheel and re-makes mistakes. With them, the skill gets sharper every time Annabel uses it.

The skill's pre-ship audit (`scripts/preship_audit.py`) reads all three layers and lints rendered slides against every rule. Failures block ship.
