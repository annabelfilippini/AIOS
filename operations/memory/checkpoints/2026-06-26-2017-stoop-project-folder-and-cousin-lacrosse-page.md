---
date: 2026-06-26 20:17
project: stoop
status: in-progress
type: checkpoint
slug: stoop-project-folder-and-cousin-lacrosse-page
---

# Stoop — project folder set up + v1 cousin lacrosse page built

Follows `2026-06-26-1546-stoop-kids-market-concept-preview.md`. Name locked as
**Stoop**. Renamed `projects/kids-market/` → `projects/stoop/` (git mv, history
kept) and built the first real v1 page.

## Folder now
```
projects/stoop/
  CLAUDE.md              ← project router / source of truth (decisions, shape, NEXT)
  preview.html           ← original two-view concept (market + a kid's stand)
  cousin-lacrosse.html   ← v1: the cousin's lacrosse page (this session's build)
  shots/                 ← shot-market.png, shot-stand.png
  references/            ← empty
```

## Concept decisions locked this session (in CLAUDE.md)
- **Kid is the first customer.** Flow: open Stoop → make account → build a
  personal page → "go live" → people request → payment + pickup arranged direct.
- **Link-first, feed-second.** Every kid gets a shareable profile (Linktree/Beacons
  pattern, not Etsy). Feed fills in *behind* the link. This dissolves the
  double-empty cold-start: launch needs one kid with a link, not a full block.
- **Payments off-platform in v1** — kid shares Venmo, sorts pickup directly. Stoop
  touches no money → no Stripe, no minor-account, no COPPA payment knot.
- **Hyperlocal is a hard rule** (Nextdoor's loose-geo noise is the anti-pattern):
  verify the *specific* neighborhood, feed only ever shows your blocks. Pickup-only
  self-enforces it. NOTE: feed-era only — does NOT bite v1 (a single shared page
  works regardless of geo). Don't build geo-verification for one page.
- **AI page builder stays lazy in v1** — questions + templates, no live model. The
  kid-voice rewrite / custom theme model is a later layer.
- **Cousin v1 = lacrosse coaching** (Maddie, 14). Service wedge dodges
  cottage-food/inventory entirely.

## What was built — cousin-lacrosse.html (verified working)
Single self-contained HTML, reuses the warm-paper Stoop language. Sections:
hero (avatar, title, byline, fact chips) → **booking** → about + gallery.
- **Customization:** "🎨 Make it yours" swatch row, 6 themes (pink/lacrosse/sky/
  sun/purple/coral) swap CSS vars live + persist to localStorage. Defaults **pink**
  (cousin's want). Lacrosse = green+navy sporty.
- **Matured the design:** dropped bunting + Caveat marker font (was tuned for
  ~8yo; real users are ~13-14). Still friendly, less party-flyer.
- **Month calendar:** full month grid, open days show "N open" pill, tap a day →
  time chips below → pick one → sticky request bar. Booked slots strike through
  (recurring Thu 4:45 / Sat 10:30). Month nav capped 3 months out, no past.
- **Availability = fixed weekly pattern** (Tue/Thu 4-5:30pm, Sat mornings). The
  per-kid availability editor is NOT built — deliberate v1 shortcut.
- **Request flow:** day→time→"Request this lesson" modal (who it's for, phone/
  email, note) → confirmation. Routing goes through a grown-up but the explicit
  "goes to her mom" copy was **removed this session** (Annabel: it's implied).

Verified via playwright: 6 swatches, month grid, day/slot selection, theme swap +
persist, request modal all fire. Only console error is favicon 404 (harmless).

## NEXT (pick one)
- **Availability editor** — let the kid set her own open times (the real next
  build; pattern is hardcoded now).
- **Deeper personalization** — beyond color: lacrosse/stick motifs, her own photo
  as hero, custom title font. The "true lacrosse themed" ask.
- **The builder flow** — the 4-5 questions a kid answers to generate a page like
  this from nothing (still unbuilt; this page was authored directly).
- **The feed** — where pages collect, with the hyperlocal scoping rule.

No code committed (concept/preview stage). Working files in `projects/stoop/`.
