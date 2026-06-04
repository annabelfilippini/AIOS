# Sava's — Redesign Copy Spec v2 (Editorial / Photo-Forward)

v1 lived at `mockups/homepage-redesign.html` and was structurally correct but section-heavy (11 sections). v2 rebuilds around **Cutler & Co** (Melbourne) as the primary reference and **Feather & Bone** (Hong Kong) as secondary. Annabel's instruction: "Sava's has such good imaging — make it special."

The move: let the photography be the page. Fewer sections, more breath, editorial typography, left-rail reservation block, an 8-image grid as the anchor.

## Design Library References (v2)

**Primary — Cutler & Co** (`reference/cutler-and-co/`)
- **Top bar:** wordmark set ultra-minimal top-left ("CUTLER"); right-aligned nav links as small caps, widely spaced: *Reservations · Menu · Shared · Private Dining · Gift Voucher · Journal · Sundays at Cutler*. No icons, no dropdowns, no search. Savas adapts to: *Reservations · Menu · Brunch · Happy Hour · Private Events · About*.
- **Hero:** ONE constrained-width editorial image (not full viewport), warm color grade, centered on the page with generous negative space above and below. Savas pick: a bi-level room interior OR the most-photographed signature shot.
- **Left rail + right editorial block:** the *signature Cutler move*. Left column (sticky-short or top-aligned, ~240px wide): `Make a Reservation` link + `LOCATION` + `OPENING HOURS` + `CONTACT` blocks, each with small-caps label and 2-3 lines of body. Right column: editorial paragraph(s) — "Welcome to Cutler" style — one short sentence per paragraph, two paragraphs total.
- **8-image editorial grid:** the anchor. 4×2 grid (or 3×3 on wider screens), small ~8–12px gutters, all real imagery (no duplicates), mix of food + interior + people. This is the page's center of gravity. Savas has ≥10 real Squarespace CDN images already downloaded locally — more than enough.
- **Full-bleed photo moment:** a single people-dining / room-at-service photo, full browser width, occasionally with a short editorial caption line beside it. Savas's bi-level room at service is the shot.
- **Restraint:** no carousels, no grids of nav cards, no feature-bullet lists, no "Book a Table" pill buried in footer, no fabricated awards.
- **Motion:** none visible. Static imagery trusted to carry the brand. Mimic.

**Secondary — Feather & Bone** (`reference/feather-and-bone/`)
- **Photo-over-nav hero:** full-bleed photograph with nav links floated over the top of the image (DINE · SHOP · EXPERIENCES set in white over a sizzling-meat hero). Directly applicable to Savas's hero IF we choose the full-bleed approach. *Applied selectively* — v2 defaults to Cutler's constrained hero, but the top announcement bar + transparent nav treatment is worth taking.
- **Small circular logo stamp:** "ABOUT US" circular mark above editorial paragraph. A subtler Savas adaptation could place the wordmark as a small circular stamp above the editorial block, not just in the nav.
- **News / journal module (optional):** three-card news grid for seasonal events (Graduation Weekend, Wellington Wednesdays). Savas has ≥1 seasonal event (Graduation Weekend 2026) — a small journal strip would surface it better than the current pop-up.

**Carried forward from v1 refs** (stay as secondary execution cues, not dominant):
- Sarma: inline-prose menu typography (dish bold + ingredients lowercase + price trailing).
- King: dual-identity paragraph + inline press quote.
- Wild Ginger: tagline-as-H1.
- La Semilla: parent-group lockup line.

**Brand DNA that MUST survive (unchanged from v1):**
- Palette: `#DDBD6B` gold + `#A54223` rust + `#FFFDF7` cream bg + `#1C1613` ink. v2 pushes MORE cream and white space (Cutler-like). Rust reserved for CTAs.
- Voice: "Ann Arbor's most spirited dining institution" — warm, confident.
- Positioning: neighborhood + celebratory + all-day (one room, three rhythms).
- Photography: real Squarespace CDN imagery only. Already downloaded locally in `mockups/assets/` from v1.

**Anti-patterns (carry forward):**
- No 4-image hero carousel (the original site's pattern).
- No "Experience our cuisine"-style generic copy.
- No e-commerce menu cards.
- No emojis / no text social icons.
- No PDF-only menu buried behind a button.
- No audit-tag pills or "before/after" annotations.
- No bar/food shot inside a chef/founder portrait slot (none required in v2 either).

---

## Section Inventory v2 (9 sections, not 11)

### === SECTION 1: TOP BAR + NAV (Cutler pattern) ===
Full-width, pinned (not sticky — Cutler doesn't sticky). White/cream ground.
- Left: wordmark "SAVA'S" set in display serif (Fraunces 400 all-caps) at ~22px, tight letter-spacing, black or warm-ink color.
- Right: nav links, small-caps 11–12px, ~32px horizontal gap, warm-ink color.
  - `DO NOT REWRITE: "Reservations"` → `https://www.exploretock.com/savas`
  - `DO NOT REWRITE: "Menu"` → `assets/savas-menu.pdf` (target="_blank" rel="noopener")
  - `DO NOT REWRITE: "Brunch"` → `#brunch`
  - `DO NOT REWRITE: "Happy Hour"` → `#happy-hour`
  - `DO NOT REWRITE: "Private Events"` → `https://www.exploretock.com/savas/private-dining`
  - `DO NOT REWRITE: "About"` → `#about`
- Below nav: a thin cream-ground announcement strip (one line only):
  - `DO NOT REWRITE: "Graduation Weekend 2026 · April 30 – May 3 · Reserve now"` → `https://www.exploretock.com/savas/experience/529823/graduation-weekend-2026`
  - Strip uses warm-rust text on cream (not a rust fill — Cutler's palette is quiet).

### === SECTION 2: HERO IMAGE (Cutler constrained pattern) ===
ONE image, constrained width (~max-width 960px, centered), ~100px margin top + bottom. Warm color grade. Real Sava's CDN. Pick the single strongest bi-level-room-at-service shot from `mockups/assets/` — `PulpoGroup_04.jpg` (the curated hero Savas's own site uses) is the default choice since it shows the full room with rust booths + State Street windows. Crop to landscape ~3:2. No overlay text, no CTA — let the image speak.

Below the hero image, centered beneath, a single thin italic editorial line (serif):
- `DO NOT REWRITE: "216 S State Street · Ann Arbor · Since 2007"`

### === SECTION 3: LEFT RAIL + RIGHT EDITORIAL BLOCK (Cutler signature move) ===
Two-column layout, max-width ~1200px, centered. Left column ~240px; right column ~680px with ~80px gap between.

**Left rail** (top-aligned, all small-caps labels for headers):
- CTA: `DO NOT REWRITE: "Make a Reservation"` → `https://www.exploretock.com/savas` (styled as an underlined text link, not a filled button — Cutler uses a text link, not a CTA fill)
- Divider line.
- Label: `DO NOT REWRITE: "LOCATION"`
  - `DO NOT REWRITE: "216 S State Street"`
  - `DO NOT REWRITE: "Ann Arbor, MI 48104"`
- Label: `DO NOT REWRITE: "HOURS"`
  - `DO NOT REWRITE: "Sunday – Thursday · 9:00 AM – 10:00 PM"`
  - `DO NOT REWRITE: "Friday – Saturday · 9:00 AM – 11:00 PM"`
  - `DO NOT REWRITE: "Happy Hour · Mon – Fri · 3 – 6 PM"`
- Label: `DO NOT REWRITE: "CONTACT"`
  - Phone link: `DO NOT REWRITE: "(734) 623-2233"` with `href="tel:+17346232233"`
  - `DO NOT REWRITE: "info@savasannarbor.com"`

**Right column** (editorial, Fraunces serif or similar, ~22–24px with generous 1.6 leading):
Eyebrow (small caps tracked): `DO NOT REWRITE: "Welcome to Sava's"`

Then two paragraphs of editorial body. These paragraphs can paraphrase around the fenced verbatim strings. Use Cutler's pacing (short, declarative, no hype). Savas's verbatim institutional line is the anchor of paragraph 1; the Michigan Daily quote is the anchor of paragraph 2.

Paragraph 1 — anchor sentence (verbatim, from Tock):
`DO NOT REWRITE: "An Ann Arbor institution serving inventive local food and outstanding hospitality since 2007."`
Surrounding prose may paraphrase around it — brunch, happy hour, and dinner in one bi-level room on State Street, seven days a week. No invented history, no invented founders.

Paragraph 2 — anchor press quote (verbatim, inline within the prose, italicized):
`DO NOT REWRITE: "Sava's will always be the classiest and most impressive first date, fifth date or who-knows-what date."`
Attribution inline at end of sentence, smaller: `DO NOT REWRITE: "— The Michigan Daily, Best of Ann Arbor 2019"`
Attribution link: `https://www.michigandaily.com/arts/best-ann-arbor-2019-romantic-dinner-savas/`

### === SECTION 4: EDITORIAL IMAGE GRID (Cutler's anchor move) ===
The soul of v2. 8 real images in a 4-column × 2-row grid at desktop (max-width ~1200px), ~10px gutter, ~12px radius (or none for Cutler purity — prefer none). All images from `mockups/assets/`:
- `_F8A3233-2.jpg`
- `DSC_3585.jpg`
- `_F8A3796.jpg`
- `_F8A3242-2.jpg`
- `DSC_3613.jpg`
- `558-DSC_9276.jpg`
- `_F8A4283.jpg`
- `_F8A5730.jpg`

Grid rules:
- Every image `object-fit: cover; aspect-ratio: 1/1` (square cells). Cutler uses squares.
- No captions, no overlays, no hover states that reveal text. Pure image wall (Cutler).
- Mobile: collapses to 2-column × 4-row.
- No section header — the grid speaks for itself (Cutler doesn't label this section either).

### === SECTION 5: FULL-BLEED ROOM + PRESS PULL-QUOTE ===
One full-browser-width image (100vw, ~70–80vh tall max). Pick one of the bi-level interior shots NOT already used as the hero (e.g., `DSC_3613.jpg` if PulpoGroup_04 is the hero). Warm color grade.

Overlaid (centered, bottom-third of image, against a small 40%-opacity warm-dark scrim band):
- Pull-quote: `DO NOT REWRITE: "The cuisine is primarily American, but there are some Mediterranean options… The combination of the beautiful ambiance and the high quality food make Sava's a desirable destination."`
- Attribution (smaller, small-caps): `DO NOT REWRITE: "— Ned I., Yelp Elite, June 2025"`

(If the Ned I. quote is too long for the scrim, shorten at the ellipsis and keep the attribution. No invented edits.)

### === SECTION 6: MENU — INLINE PROSE (Sarma pattern, preserved) ===
Max-width 720px, centered. Editorial, typed like a menu card. Section eyebrow small-caps:
`DO NOT REWRITE: "A Taste of the Menu"`

Four dishes (verbatim from v1 spec — facts unchanged). Render each dish as: dish name bold serif + em-dash + ingredients lowercase sans + right-aligned price (two-column grid or flexbox row, dish+desc on left, price on right).

Dish 1:
  Name: `DO NOT REWRITE: "Greek Lamb Burger"`
  Description: `DO NOT REWRITE: "house ground lamb, feta, salt roasted beet, pepperoncini, pickled red onion"`
  Price: `DO NOT REWRITE: "26"`

Dish 2:
  Name: `DO NOT REWRITE: "Salt Roasted Beets"`
  Description: `DO NOT REWRITE: "dehydrated kalamata olives, buckwheat relish, goat cheese, harissa vinaigrette"`
  Price: `DO NOT REWRITE: "14"`

Dish 3:
  Name: `DO NOT REWRITE: "Bang Bang Shrimp"`
  Description: `DO NOT REWRITE: "served on a slice crispy rice, toast with spicy sweet sauce"`
  Price: — (not verified) — em-dash in price column.

Dish 4:
  Name: `DO NOT REWRITE: "Cheesecake"`
  Description: `DO NOT REWRITE: "bruleed, strawberry jam, berries"`
  Price: `DO NOT REWRITE: "12"`

CTA below (underlined text link, Cutler style — not a filled button):
`DO NOT REWRITE: "See the Full Menu"` → `assets/savas-menu.pdf` (target="_blank" rel="noopener")

### === SECTION 7: DAYPARTS — ONE-LINE EACH (Cutler restraint) ===
Three-row block, max-width ~820px, centered. Each row: one-line label + hours + reservation link. No photos, no signature dishes (those live in Section 6). Deliberately quiet.

Row 1:
- Label: `DO NOT REWRITE: "Brunch"` (display serif)
- Hours: `DO NOT REWRITE: "Daily · 9:00 AM – 3:00 PM"`
- Link (right-aligned): `DO NOT REWRITE: "Reserve →"` → `https://www.exploretock.com/savas`

Row 2 (anchor id="happy-hour"):
- Label: `DO NOT REWRITE: "Happy Hour"`
- Hours: `DO NOT REWRITE: "Monday – Friday · 3:00 – 6:00 PM"`
- Link: `DO NOT REWRITE: "See the Bar Menu →"` → `assets/savas-menu.pdf`

Row 3:
- Label: `DO NOT REWRITE: "Dinner"`
- Hours: `DO NOT REWRITE: "Sunday – Thursday · 4:00 – 10:00 PM · Friday – Saturday · 4:00 – 11:00 PM"`
- Link: `DO NOT REWRITE: "Reserve →"` → `https://www.exploretock.com/savas`

Horizontal rule between each row (hairline, #1C1613 at 10% opacity).

### === SECTION 8: PULPO GROUP — EDITORIAL BLOCK (La Semilla lockup, Cutler restraint) ===
Single editorial paragraph centered, max-width 620px, followed by a thin three-tile row.

Editorial paragraph — paraphrase around the fenced sentence (keep the Pulpo Group lockup verbatim; surrounding text is free prose naming the Ann Arbor location only):
`DO NOT REWRITE: "Sava's is part of the Pulpo Group — a family of Ann Arbor restaurants."`

Three-tile row (max-width 960px, centered, 32px gutter). Each tile is minimal: tiny thumbnail (square, 120px) + display-serif name + one-line role + outbound underlined link. Cutler-restrained — no cards, no backgrounds, no filled buttons.

Tile 1 — Sava's
  Name: `DO NOT REWRITE: "Sava's"`
  Role: `DO NOT REWRITE: "Downtown · Since 2007"`
  Link: `/`

Tile 2 — Aventura
  Name: `DO NOT REWRITE: "Aventura"`
  Role: `DO NOT REWRITE: "Ann Arbor"`
  Link: `https://www.exploretock.com/aventura` (target="_blank")

Tile 3 — Dixboro House
  Name: `DO NOT REWRITE: "Dixboro House"`
  Role: `DO NOT REWRITE: "Ann Arbor"`
  Link: `https://www.exploretock.com/thedixboroproject` (target="_blank")

(Role lines stay minimal — only "Ann Arbor" is verified for Aventura + Dixboro per `verified-facts.md`. Do not invent cuisine descriptors.)

### === SECTION 9: FOOTER (Cutler restraint) ===
Minimal footer, cream ground, ~60px top padding, ~40px bottom. Three columns, or one three-column row at desktop stacking to a single column at mobile.

Column 1 — Visit:
- Header: `DO NOT REWRITE: "Visit"`
- `DO NOT REWRITE: "216 S State Street, Ann Arbor, MI 48104"`
- Phone link: `DO NOT REWRITE: "(734) 623-2233"` (tel:)
- `DO NOT REWRITE: "info@savasannarbor.com"`

Column 2 — Reserve:
- Header: `DO NOT REWRITE: "Reserve"`
- `DO NOT REWRITE: "Reservations"` → Tock (underlined text link)
- `DO NOT REWRITE: "Private Events"` → Tock private dining
- `DO NOT REWRITE: "Catering"` → ezCater

Column 3 — Follow:
- Header: `DO NOT REWRITE: "Follow"`
- Two SVG icons (Instagram + Facebook, inline SVG, ~20px, warm-ink color with rust on hover). No text labels. No emoji.
- Instagram → `https://instagram.com/savas_ann_arbor`
- Facebook → `https://facebook.com/savasannarbor`

Footer base (below columns, thin):
- Wordmark centered: "SAVA'S" (serif, small)
- Copyright line: `DO NOT REWRITE: "© 2026 Sava's · Part of the Pulpo Group"`

---

## Global Rules for Phase B Agent (v2)

- **Reuse existing assets.** Every image in `mockups/assets/` from v1 is already downloaded locally and verified. Do NOT re-download. Available files: `_F8A3233-2.jpg`, `_F8A3242-2.jpg`, `_F8A3796.jpg`, `_F8A4283.jpg`, `_F8A5730.jpg`, `558-DSC_9276.jpg`, `DSC_3585.jpg`, `DSC_3613.jpg`, `PulpoGroup_04.jpg`, `savas-logo.png`.
- **Pulpo Group tile thumbnails:** since no separate Aventura/Dixboro images exist, use small crops of existing imagery OR a neutral cream-ground initial-letter thumbnail (just the letter "A" and "D" in the display serif, centered). Do NOT fabricate property shots. Prefer the initial-letter approach for honesty.
- **Menu CTAs:** every "Menu" / "See the Full Menu" / "See the Bar Menu" points to `assets/savas-menu.pdf` with `target="_blank" rel="noopener"`. PDF 404 is expected.
- **No carousels, no autoplay, no parallax.** v2 is static and quiet — Cutler's whole point.
- **Typography:** load Fraunces (display + italic) from Google Fonts for headings + editorial body. Keep Inter for small-caps labels, nav, meta. Two families max.
- **Palette:** `#FFFDF7` cream bg, `#1C1613` warm ink body, `#A54223` rust for links/underlines, `#DDBD6B` gold for small accents (dividers, hover tint). Lots of white space. Cutler pushes cream, not gold.
- **Mobile (≤768px):** two-col grid, single-column footer, dayparts stack to 2 lines each (label + hours, then link), left rail + editorial block stacks.
- **Motion:** underline-on-hover for text links. No image hover zoom. No Ken Burns on hero. Keep it still.
- **Deliverable path:** write to `mockups/homepage-redesign-v2.html`. Do NOT overwrite `mockups/homepage-redesign.html` (v1 stays for comparison).

## Output

Write: `prospects/savas/mockups/homepage-redesign-v2.html`
Assets: reuse `prospects/savas/mockups/assets/` (already present; no new downloads)
