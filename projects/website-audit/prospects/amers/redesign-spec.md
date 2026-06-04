# Redesign Spec — Amer's Deli

**Prospect:** Amer's Deli (Amer's Mediterranean Deli / Amer's Delicatessen)
**URL:** https://www.amersdeli.com/
**Vertical:** Restaurant → counter-service deli / campus eatery
**Positioning pick:** Heritage-forward (confirmed with user)
**Mode:** Interactive, no Stitch (`AUDIT_USE_STITCH=0`), no audit.md (redesign-only scrape)
**Scope:** Homepage single-page redesign only.

## Design Library References (vertical: Restaurant / Hospitality)

Pulled from `~/Documents/AI-OS/wiki/wiki/design-library.md` (Restaurant section).

**Execution cues to honor:**
1. **Hero is one full-bleed food or space photo**, warm color grade. Not a grid, not a carousel, not a 3-up composition. (Amer's: use the açaí bowl — visually striking, ties to the Michigan Daily feature, and is the single dish Amer's is most written-about for.)
2. **Typography pair: distinctive serif (editorial) + clean sans (UI).** NEVER all-sans Montserrat. (Amer's: Playfair Display for display + Inter for body.)
3. **Menu lives on-page as readable HTML** for featured dishes (teaser), with the full Menu CTAs routing to `assets/amers-menu.pdf` for clients who want the whole thing. Restaurant-library rule + audit-redesign rule reconciled: featured sandwiches/bowls render inline with prices; "See the full menu" → PDF.
4. **Hours + primary CTA above the fold.** Amer's primary CTA = "Order now" (Snackpass / Popmenu). Secondary = "See the menu." Both in hero + nav + footer.
5. **Photography carries identity.** Real Amer's photography already exists at `mockups/assets/` — use it. No Unsplash, no stock.
6. **Press/social proof = real publication names with links.** For Amer's: Michigan Daily feature (2022), Google rating, the self-reported "Best Sandwich / Best Deli" line in restrained marquee language.

**Anti-patterns to avoid:**
- Emojis of any kind — SVG icons only.
- Stock food photography — we already have Amer's real photos.
- Three-word abstract hero ("Fresh. Local. Delicious.").
- PDF-only menu — we want an on-page dish teaser even though the "Menu" CTA routes to PDF.
- Carousel hero, grid hero, or "feature grid of icon + one-word label."
- Testimonial carousels with unsourced quotes.

**Hop Alley Apr 2026 palette lesson:** regional identity via restrained color, not clichés. Amer's equivalent: Ann-Arbor campus-deli identity via warm ivory + espresso + brick-red accent — NOT generic blue/green/red PopMenu defaults or red-lantern / Greek-flag / college-campus-blue clichés.

## Brand DNA — must survive the redesign

Signature elements we are elevating, not erasing:

1. **The "welcome frog"** — hand-drawn ink frog with "welcome" in script. Bizarre but owned. Elevate to a stamped seal / mascot badge that appears in the hero corner, possibly repeated as a watermark in footer. File: `assets/welcome-frog.png`.
2. **"Amer, himself"** — the owner-on-the-floor presence is the strongest human differentiator (per Michigan Daily). Give it a dedicated block, not a bio page in the nav.
3. **"Not a coffee house with food… we are Amer's!"** — the existing voice line from the about copy. Keep the cadence verbatim.
4. **Chicago Reds + Yogurt Rush as sub-brands** — treat each as a named callout with its own block, not a generic menu tile.
5. **Mediterranean AND American-deli heritage side-by-side.** Falafel + reuben + lox bagel + Chicago dog is the actual menu; don't genericize to "sandwiches and more."
6. **Menu physically spans over half of the restaurant.** This is a quote we can use — it is both true and charming.
7. **Staff who remember your name.** Michigan Daily line we can lean on.
8. **"Across from the Diag" / State Street.** Give location a place, not a pin.

## Palette + Type direction

**Palette (heritage-forward, deli-warm):**
- `--espresso: #2A1D15` (deep brown — primary background for dark bands)
- `--ivory: #F3ECDE` (warm off-white — primary light background)
- `--brick: #A23A2A` (accent — Reuben-meat red, deli-awning red — use sparingly)
- `--brass: #B08B4F` (accent — pastry-case gold / deli signage brass)
- `--ink: #1A120B` (type on ivory, near-black with warm undertone)
- `--cream: #EEE3CC` (secondary ivory for card backgrounds)

**Typography:**
- Display: **Playfair Display** (serif, heritage editorial — similar to what Landini does without the cold Didone crispness). Weight 700/900.
- Body + UI: **Inter** (clean sans). Weight 400/500/600.
- Secondary script accent for "welcome" / "est. 1988" flourishes: **Caveat** or **Homemade Apple** — use sparingly (≤3 instances on the page).

## Section Inventory (copy spec)

Each section below is REQUIRED in this order. Verbatim strings fenced; `DO NOT REWRITE:` means byte-for-byte. Unfenced prose is free for the agent to paraphrase in voice.

---

### Section 1: Announcement bar

Layout: thin strip (36px), espresso background, ivory text, brass underline on the link. Full horizontal gutters aligned to nav beneath.

Copy (verbatim):
```
DO NOT REWRITE: "Open daily, 8 am – 10 pm · 312 S. State St., across from the Diag · (734) 761-6000"
```

---

### Section 2: Navigation

Layout: one nav, above the hero. Wordmark left, links center, primary CTA right. On 768px collapse to hamburger + wordmark + order CTA.

Wordmark (verbatim, rendered in Playfair Display 900):
```
DO NOT REWRITE: "AMER'S"
```

Tagline beneath wordmark (Inter 11px tracking-widest, brass):
```
DO NOT REWRITE: "MEDITERRANEAN DELI · SINCE 1988"
```

Links (verbatim):
```
DO NOT REWRITE: "Menu"
DO NOT REWRITE: "Our Story"
DO NOT REWRITE: "Catering"
DO NOT REWRITE: "Visit"
```

Primary CTA (verbatim):
```
DO NOT REWRITE: "Order now"
```

`Menu` link href → `assets/amers-menu.pdf`, `target="_blank" rel="noopener"`. (PDF will 404 until client drops it — structure is right.)
`Order now` href → `https://www.amersdeli.com/popmenu-order` (verified from homepage).
`Our Story` → `#story` anchor.
`Catering` → `#catering` anchor.
`Visit` → `#visit` anchor.

---

### Section 3: Hero

Layout: split 55/45. Left 55% = full-bleed food photo (`assets/hero-composition.jpg` — the açaí bowl shot; native 1920×1440, warm rustic wood background). Right 45% = ivory background, heritage copy block. On mobile: stacked (photo top, copy beneath). Hero ≤100vh.

Welcome-frog badge: overlay in the bottom-right corner of the photo column, translucent ivory circular seal, 120px diameter, `assets/welcome-frog.png` inside. Rotated -6deg for a stamped feel.

Eyebrow (brass, Inter tracking-widest):
```
DO NOT REWRITE: "State Street, Ann Arbor · Since 1988"
```

Headline (Playfair Display 900, 68px desktop / 44px mobile):
```
DO NOT REWRITE: "A coffee house and a delicatessen in one."
```

Subhead (Inter 400, 20px, espresso, ≤2 lines):
```
DO NOT REWRITE: "Not a coffee house with food choices. Not a delicatessen with coffee choices. We are Amer's."
```

Primary CTA (brick-filled button, Inter 600):
```
DO NOT REWRITE: "Order now"
```
→ href = https://www.amersdeli.com/popmenu-order, target="_blank" rel="noopener"

Secondary CTA (brass underline, text link):
```
DO NOT REWRITE: "See the full menu"
```
→ href = assets/amers-menu.pdf, target="_blank" rel="noopener"

Small meta row beneath the CTAs (Inter 13px, espresso/60):
```
DO NOT REWRITE: "Open 8 am – 10 pm · (734) 761-6000 · Across from the Diag"
```

---

### Section 4: Heritage marquee (dark band)

Layout: espresso background, horizontal scrolling marquee. Text in Playfair Display 40px italic, ivory, separator = brass fork-and-knife SVG. Scrolls left at ~40s per loop, pauses on hover.

Repeating phrases (all verbatim, separated by · ):
```
DO NOT REWRITE: "Best Sandwich"
DO NOT REWRITE: "Best Deli"
DO NOT REWRITE: "Best Coffee"
DO NOT REWRITE: "Best Juice Bar"
DO NOT REWRITE: "Best Restaurant"
```

Legend beneath marquee (Inter 11px tracking-widest, brass):
```
DO NOT REWRITE: "Awards + features from The Michigan Daily, Ann Arbor Observer, Ann Arbor News, Metro Times, and Oakland Jewish News."
```

---

### Section 5: Signature dishes (teaser, 4-up grid)

Layout: ivory background, 4-column card grid (768px = 2x2, 480px = 1x4). Each card = photo top (landscape 4:3), card body ivory with ink text. Card body contains: eyebrow (brass tracking-widest), dish name (Playfair 28px), one-line description (Inter 14px), price inline in Inter 600.

Section heading (Playfair 48px):
```
DO NOT REWRITE: "The menu spans over half the restaurant."
```

Section subhead (Inter 16px, espresso/70):
```
DO NOT REWRITE: "Here are four to start with."
```

**Card 1 — Açaí Bowl**
Image: `assets/hero-composition.jpg` (reused at smaller size; overhead açaí bowl on wood)
Eyebrow:
```
DO NOT REWRITE: "Signature"
```
Dish name:
```
DO NOT REWRITE: "Power Açaí Bowl"
```
Description (Inter 14px):
```
DO NOT REWRITE: "100% açaí berry base. Build your own toppings from the bar. The Michigan Daily called it their 'home base.'"
```
Price row: intentionally omit (no public price verified); instead render a brass "MARKET" label.

**Card 2 — Reuben**
Image: `assets/reuben.jpg`
Eyebrow:
```
DO NOT REWRITE: "Deli classic"
```
Dish name:
```
DO NOT REWRITE: "Reuben"
```
Description (Inter 14px):
```
DO NOT REWRITE: "Shaved pastrami and sauerkraut, grilled rye, kosher pickle on the side."
```
Price row:
```
DO NOT REWRITE: "$14.99"
```

**Card 3 — Chicago Reds**
Image: `assets/chicago-dog.jpg`
Eyebrow:
```
DO NOT REWRITE: "Amer's original"
```
Dish name:
```
DO NOT REWRITE: "Chicago Reds Dog"
```
Description (Inter 14px):
```
DO NOT REWRITE: "Vienna all-beef, neon relish, sport peppers, tomato, pickle, yellow mustard, onion, steamed poppyseed bun."
```
Price row: brass "MARKET" label (no verified price).

**Card 4 — Crêpe**
Image: `assets/puff-pastry.jpg` (actually a crêpe per the source)
Eyebrow:
```
DO NOT REWRITE: "Campus favorite"
```
Dish name:
```
DO NOT REWRITE: "Nutella & Strawberry Crêpe"
```
Description (Inter 14px):
```
DO NOT REWRITE: "Crispy yet pillow-soft, filled with warm Nutella and strawberries. A Diag-across-the-street ritual."
```
Price row: brass "MARKET" label.

CTA beneath grid (brass underline):
```
DO NOT REWRITE: "See the full menu"
```
→ href = assets/amers-menu.pdf, target="_blank" rel="noopener"

---

### Section 6: Our Story (owner block)

Layout: two-column, 50/50. Left = ivory panel, Playfair heading + Inter body copy + pull-quote. Right = image slot of the deli case interior (`assets/deli-case.jpg` — chalkboard menus behind, pastry case up front). Aspect ratio crop to ~4:5. NO founder portrait placeholder — we have no real portrait of Amer, and the Michigan Daily quote carries the human presence just as well.

Eyebrow (brass tracking-widest):
```
DO NOT REWRITE: "Since 1988 · On State Street since 1990"
```

Heading (Playfair 54px):
```
DO NOT REWRITE: "A coffee house married a deli. Then Amer opened the door."
```

Body paragraph 1 (Inter 17px, ≤4 lines, paraphrasable by agent from the verified-facts.md homepage copy):
> The concept was built in Flint in 1988 and moved to the U-M campus in 1990. Thirty-five years on State Street since — coffee, sandwiches, crêpes, salads, frozen yogurt, and an eight-page menu that physically takes up half the restaurant.

Pull-quote (Playfair italic 32px, brass left-border):
```
DO NOT REWRITE: "Often, you will find Amer, himself, behind the counter, offering opinions and advice on what to order."
```

Quote attribution (Inter 12px tracking-wide, espresso/60):
```
DO NOT REWRITE: "— The Michigan Daily, December 2022"
```

Body paragraph 2 (Inter 17px, paraphrasable):
> Amer's was an originator of a lot of things in Ann Arbor: chai teas, loose teas, fair trade coffee, raw juices, soy products. It is still the only place where the menu has both falafel and a hand-made reuben.

---

### Section 7: Sub-brands strip (Chicago Reds + Yogurt Rush)

Layout: two-column on desktop, stacked on 768px. Each half = espresso background, cream-colored card offset inside. Inside each card: display serif name, one-line descriptor, one product photo in landscape.

**Left half — Chicago Reds**
Image: `assets/chicago-dog.jpg`
Eyebrow:
```
DO NOT REWRITE: "A sub-brand at Amer's"
```
Name (Playfair 48px ivory):
```
DO NOT REWRITE: "Chicago Reds"
```
Descriptor (Inter 16px cream/80):
```
DO NOT REWRITE: "The Chicago-style hot-dog menu, served the only way it's supposed to be: dragged through the garden, never with ketchup."
```

**Right half — Yogurt Rush**
Image: `assets/frozen-yogurt-cup.jpg`
Eyebrow:
```
DO NOT REWRITE: "A sub-brand at Amer's"
```
Name (Playfair 48px ivory):
```
DO NOT REWRITE: "Yogurt Rush"
```
Descriptor (Inter 16px cream/80):
```
DO NOT REWRITE: "Six rotating flavors of self-serve frozen yogurt. Original Tart, Vanilla, Chocolate, Cake Batter, Strawberry Cheesecake, Juicy Orange."
```

---

### Section 8: Press quote block

Layout: full-bleed ivory, centered text, max-width 860px.

Eyebrow (brass tracking-widest):
```
DO NOT REWRITE: "Press"
```

Large pull-quote (Playfair 44px, espresso):
```
DO NOT REWRITE: "Amer's Delicatessen is a quintessential campus eatery with staff members who remember your name — and sometimes your exact order."
```

Attribution (Inter 13px tracking-widest, brass):
```
DO NOT REWRITE: "THE MICHIGAN DAILY · DECEMBER 2022"
```

Link on the attribution:
→ href = https://www.michigandaily.com/arts/amers-delicatessen-a-university-of-michigan-students-home-base/, target="_blank" rel="noopener"

---

### Section 9: Visit / Hours block

Layout: two-column. Left = espresso panel with hours + address + phone in heritage treatment. Right = deli interior photo slot (`assets/yogurt-machines.jpg` OR `assets/torani-shelf.jpg` — pick the warmer one by eye; yogurt-machines shows the interior shelves best).

Eyebrow (brass, left column):
```
DO NOT REWRITE: "Visit"
```

Heading (Playfair 42px, ivory):
```
DO NOT REWRITE: "On State Street since 1990."
```

Address block (Inter 18px ivory):
```
DO NOT REWRITE: "312 S. State St."
DO NOT REWRITE: "Ann Arbor, MI 48104"
```
Address block wrapped in `<a href="https://maps.google.com/?q=312+S+State+St+Ann+Arbor+MI+48104" target="_blank" rel="noopener">` — hover underline in brass.

Hours block (Inter 18px ivory):
```
DO NOT REWRITE: "Open every day, 8 am – 10 pm"
```

Phone block (Inter 18px ivory, `<a href="tel:+17347616000">`):
```
DO NOT REWRITE: "(734) 761-6000"
```

Secondary CTA (brass underline):
```
DO NOT REWRITE: "Catering inquiries →"
```
→ href = https://www.amersdeli.com/catering, target="_blank" rel="noopener"

---

### Section 10: Footer

Layout: espresso, three-column. Left = wordmark + tagline + welcome-frog watermark at 60px opacity 0.25, subtly placed. Middle = mini nav (Menu / Our Story / Catering / Visit / Order now). Right = hours + address + phone (same as Section 9, condensed) + social SVG row.

Wordmark (Playfair 900, ivory):
```
DO NOT REWRITE: "AMER'S"
```

Tagline (Inter 11px tracking-widest, brass):
```
DO NOT REWRITE: "MEDITERRANEAN DELI · SINCE 1988"
```

Footer meta (Inter 11px, cream/60):
```
DO NOT REWRITE: "© 2026 Amer's Deli. Across from the Diag."
```

Social icons row: Facebook, Instagram — inline SVG only. No other platforms verified.
- Facebook → href = https://www.facebook.com/amersdeli/, target="_blank"
- Instagram → href = https://www.instagram.com/amersdeli/, target="_blank" (if account not verified, keep icon but link to `#`; spec assumes it exists based on the site's social row — agent to verify one more time before linking)

---

## Asset inventory (already downloaded to `mockups/assets/`)

| File | Use | Dimensions | Notes |
|---|---|---|---|
| `hero-composition.jpg` | Section 3 hero + Section 5 Card 1 | 1920px wide | açaí bowl with fruit, coconut, smoothie side |
| `reuben.jpg` | Section 5 Card 2 | 1920px wide | reuben in basket on parchment |
| `chicago-dog.jpg` | Section 5 Card 3 + Section 7 left | 1920px wide | Chicago-style dog |
| `puff-pastry.jpg` | Section 5 Card 4 | 1920px wide | actually a crêpe — rename OK in mockup |
| `granola-bowl.jpg` | Standby (not required in spec) | 1920px wide | available if layout needs a 5th card |
| `deli-case.jpg` | Section 6 right column | 1920px wide | interior, chalkboard menus behind pastry case |
| `puff-pastry.jpg` | Section 5 Card 4 | 1920px wide | crêpe w/ Nutella |
| `yogurt-machines.jpg` | Section 9 right OR standby | 1920px wide | self-serve yogurt machines |
| `torani-shelf.jpg` | Standby | 1920px wide | Torani syrup bottle shelf |
| `frozen-yogurt-cup.jpg` | Section 7 right | 1920px wide | cup of frozen yogurt |
| `welcome-frog.png` | Hero badge + footer watermark | 600×508 | signature mascot |
| `amers-logo.png` / `amers-logo-alt.png` | Do NOT use — both are white-on-white at low res | — | Use typed wordmark "AMER'S" in Playfair instead |

**Menu PDF:** `assets/amers-menu.pdf` — not created; menu CTA links will 404 until client supplies. That is the correct behavior per skill.

---

## What we did NOT include (and why)

- Founder portrait slot — no real portrait of Amer exists in the scrape. Per skill rule: portrait-slot placeholder OR no slot. We chose no slot; the Michigan Daily pull-quote + deli-case photo carries the human presence without a mislabeled placeholder.
- Second location (South U / 1222 S. University) — current site footer only lists one address, Google AI Overview claim was unverified. Spec confines to 312 S. State St.
- Specific award years — only the self-reported award-category names (Best Sandwich, etc.) appear; no year is invented.
- Opening hours carousel / week-specific hours — single "8 am – 10 pm daily" is what's verified.
- Carousel or slider of any kind — anti-pattern per restaurant design library.
- Emojis — anti-pattern, SVG icons only.
- Audit-tag pills or "before/after" labels — this is a finished site, not a diff.

## Notes to Phase B agent

- Build in the order listed. No section may swap position.
- Every `DO NOT REWRITE:` fenced string appears byte-for-byte. Em-dashes, apostrophes, periods included.
- All images come from `mockups/assets/`. No hotlinks, no `popmenucloud.com` URLs remaining, no `lh3.googleusercontent.com` (no Stitch was used anyway).
- Use `@media (max-width: 768px)` breakpoint. Tested breakpoints: 1440, 1024, 768, 480.
- Exactly ONE nav above hero.
- Menu CTAs (nav "Menu", hero "See the full menu", sig-dishes "See the full menu") all point to `assets/amers-menu.pdf`.
- Welcome frog used TWICE: hero badge (rotated -6deg, stamped feel) and footer watermark (opacity 0.25).
- Marquee motion in Section 4 — pure CSS `@keyframes`, pauses on hover.
- Social icons inline SVG (Facebook, Instagram). No emoji, no text abbreviations.
- Announcement bar + nav share horizontal gutters — ≤2px drift at 1440px.
- Hero max-height 100vh.
- No section exceeds 2× neighbor vertical space (excluding hero).
- Verify every image loads, native width ≥ CSS width, before returning.
- QA runs at 1440px AND 768px per the Phase 4 checklist in `/audit-redesign` — green before return.
