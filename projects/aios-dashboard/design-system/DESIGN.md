# AI-OS Dashboard — Design System

One visual language for Annabel's personal dashboard. Every tab is built
separately for now but must mirror this so the assembled dashboard reads as one
product. Anchor: **The Edit** (`projects/style-feed/feed.html`) — quiet-luxury /
old-money. Tokens live in `tokens.css` (the source of truth).

## Feel

Warm, restrained, editorial. Think NET-A-PORTER / The Row / Aesop. Cream canvas,
near-black ink, lots of whitespace, **hairlines instead of heavy shadows**,
near-square corners. Colour is rationed — one berry accent, and (only where data
needs coding) a set of desaturated earthy tones.

## Palette (roles)

| Token | Hex | Role |
|---|---|---|
| `--bg` | `#f3efe9` | warm cream page background |
| `--card` | `#faf8f4` | lightest cream — surfaces, cards, sheets |
| `--ink` | `#1b1916` | near-black — titles, primary text, active fills |
| `--accent` | `#3a352d` | dark warm brown — secondary ink, active tab fill |
| `--muted` | `#7c756a` | taupe — labels + secondary text |
| `--line` | `#e0d9cd` | hairline borders + dividers |
| `--love` | `#b54b5a` | muted berry — the single chromatic accent |

**Functional accents** (calendar event types etc., desaturated to fit the cream):
`--fn-focus` brown · `--fn-move` sage · `--fn-water` dusty blue · `--fn-social`
berry · `--fn-home` taupe · `--fn-none` stone. Use these *only* when a tab must
distinguish categories; otherwise stay monochrome.

## Type

- **Display + poetic italic:** Cormorant Garamond (`--serif`), weights 400/500/600.
  Tab titles, big numbers, empty-state lines, "why" notes (italic).
- **UI + body + labels:** Jost (`--sans`), weights 300/400/500. Base weight 300.
- **Label convention:** uppercase, letter-spacing `.15–.3em`, `--muted`. Used for
  kickers, nav tabs, captions, brand/meta lines.

## Components (see `tokens.css` for the `.ds-*` classes)

- **Kicker** — small uppercase eyebrow above a title.
- **Display title** — Cormorant 500, `clamp(34px,5vw,60px)`.
- **Tab** — uppercase Jost; active = `--accent` fill, white text. The dashboard
  nav and any segmented control use this.
- **Pill / mini button** — hairline outline, uppercase Jost; hover darkens.
- **Hairline section** — `1px var(--line)` divider; generous padding.
- **Card / frame** — `--card` fill, `1px var(--line)` border, near-square; images
  `mix-blend-mode:multiply` on cream.
- **Poetic note** — italic Cormorant in `--muted` for nudges / empty states.

## Adding a new tab

1. Inline the `:root` tokens from `tokens.css` (tabs are self-contained HTML for
   now), or `<link>` it once the dashboard shell exists.
2. Use Cormorant for the tab's title + any poetic copy; Jost for everything else.
3. Stay monochrome unless the data needs category colour — then use `--fn-*`.
4. Hairlines, not shadows. Near-square corners. Uppercase letter-spaced labels.
5. No em-dashes in user-facing copy (Annabel's voice rule).

## Tabs

- **The Day** — calendar + to-do (tab 1). `projects/day-planner/planner.html`.
- **The Edit** — shopping feed. `projects/style-feed/feed.html` (the anchor).
