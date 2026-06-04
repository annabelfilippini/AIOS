# Sava's — Redesign Copy Spec

Mode: redesign-only (no audit.md). Rebuild the homepage to elevate — not erase — Sava's identity. Every verbatim string is fenced; unfenced text is free description the HTML agent can paraphrase. Zero fabricated facts — every prose line traces to `facts/verified-facts.md`.

## Design Library References

From `~/Documents/AI-OS/wiki/wiki/design-library.md` → Restaurant / Hospitality (premium casual / approachable luxury tier — Sava's is upscale-casual, not fine-dining).

**Execution cues (library + scraped refs):**
- Hero = ONE full-bleed image with warm color grade (interior or signature dish) — never a four-image grid or carousel (fixes the current homepage pattern).
- Typography pair: editorial serif (headlines) + clean sans (body). Never all-sans Montserrat. Sava's brand fonts are Brandon Grotesque (heading) + Aktiv Grotesk (body) per `branding.json` — keep the body sans, pair headlines with an editorial serif that matches the "most spirited institution" voice (e.g., Fraunces, Canela, GT Super).
- Tagline-as-hero (Wild Ginger): the institution line goes H1, not buried.
- Dual-identity About paragraph with inline press quote (King) — neighborhood + celebratory in one sentence.
- Dayparts labeled by name (King): `BRUNCH` / `HAPPY HOUR` / `DINNER`.
- Menu rendered inline as typed prose (Sarma): dish bold, ingredient list lowercase, price trailing — NEVER e-commerce cards with "Add" buttons.
- Parent-group lockup as its own tile row (La Semilla): Sava's / Dixboro House / Aventura.
- Reservation CTA in nav + hero + footer (library rule).
- Press/reviews: real publications with links — Michigan Daily, Ann Arbor Independent.

**Anti-patterns (avoid):**
- Carousel of 4 nearly-identical food shots as hero.
- "Experience our cuisine"/"Welcome to"-style generic headlines.
- PDF-only menu or menu-as-image-tiles (La Semilla mistake — do not repeat).
- Emojis (knife-and-fork, sparkles, chef-hat).
- Stock food photography.
- Reservation CTA buried in footer.
- Audit-tag pills or diff annotations on the final mockup.
- Bar/interior/food shot inside a chef/founder portrait slot.

**Reference-specific overrides** (from `reference/reference-summary.md`):
- Tagline-as-hero (Wild Ginger).
- Inline-prose menu with evocative section headers (Sarma) — section names in Sava's voice: "Brunch Always," "Share & Start," "The Burger Program," "From the Kitchen," "From the Bar."
- Dual-identity About paragraph with inline Michigan Daily quote (King).
- Parent-group tile row + signature-dish hero + live Instagram grid (La Semilla).

**Brand DNA that MUST survive:**
- Palette: `#DDBD6B` primary gold + `#A54223` accent rust + warm cream/off-white background. Not default-black, not Squarespace-gray.
- Voice: "Ann Arbor's most spirited dining institution" — warm, confident, celebratory. Not "relaxed" or "muted."
- Positioning: neighborhood brunch institution AND graduation-weekend destination AND happy-hour bar — one room, three rhythms.
- Photography: real bi-level interior, real brunch plates, real cocktails. Existing Squarespace CDN imagery is strong — lean on it.

---

## Section Inventory

### === SECTION 1: ANNOUNCEMENT BAR ===
Thin horizontal strip, full-width, palette = rust (`#A54223`) ground + cream text. One-line dismissible. Links to Tock Graduation Weekend page.
Copy: `DO NOT REWRITE: "Graduation Weekend 2026 · April 30 – May 3 · Reserve your table"`
Link target: `https://www.exploretock.com/savas/experience/529823/graduation-weekend-2026`
Audit finding (internal — do NOT render): Current homepage surfaces Graduation Weekend only via pop-up `WEB POP-UP (3).png`; dedicated bar is more findable.

### === SECTION 2: NAV ===
Sticky, minimal. Left: wordmark (Sava's). Center: Menu · Brunch · Happy Hour · Private Events · About. Right: Reservations (primary button, rust fill) + Pulpo Group toggle (small secondary).
- `Menu` link target: `assets/savas-menu.pdf` (target="_blank" rel="noopener") — CTA maps to PDF per skill rule, not to on-page anchor.
- `Reservations` link target: `https://www.exploretock.com/savas`
- `Pulpo Group` toggle reveals a 3-tile popover (Sava's / Dixboro House / Aventura) — does NOT navigate off-domain on hover.
Image: wordmark SVG if `branding.json` logo URL exists; else text-lockup "SAVA'S" set in editorial serif display.

### === SECTION 3: HERO ===
Full-bleed single-image hero. Warm color grade. Image choice (from scrape/): the bi-level dining-room interior shot (`_F8A3233-2.jpg` or `DSC_3613.jpg` or similar from verified Squarespace CDN URLs in `scrape/homepage.md`). The room is Sava's most under-surfaced asset per Yelp reviews ("elegant, and notably has two levels").
Layout: image full-bleed. Overlay centered-left: wordmark small + tagline + dual CTA. Hours chip pinned bottom-right.

Eyebrow: `DO NOT REWRITE: "Ann Arbor · Since 2007"`
Headline: `DO NOT REWRITE: "An Ann Arbor institution serving inventive local food and outstanding hospitality since 2007."`
  (Verbatim from Tock per `verified-facts.md` — this is the single official sentence.)
Subhead: free prose — something along the lines of "Brunch through dinner, seven days a week, on State Street." (HTML agent can paraphrase; nothing invented.)
Primary CTA: `DO NOT REWRITE: "Reserve a Table"` → `https://www.exploretock.com/savas`
Secondary CTA: `DO NOT REWRITE: "See the Menu"` → `assets/savas-menu.pdf` (target="_blank")
Hours chip (small, pinned): free label (e.g., "Open today · 9:00 AM – 10:00 PM") — use today's hour range from verified-facts; all-week hours live in footer.

### === SECTION 4: DUAL-IDENTITY PARAGRAPH + INLINE PRESS QUOTE ===
Single editorial paragraph, center-column, max 640px width, editorial serif at ~22–26px with generous leading. King-style: one continuous sentence of restraint. Press quote inline within the paragraph, set in italics with an inline attribution dash.
Free prose (HTML agent paraphrases around the fenced quote):
- Opening sentence frames the dual identity: a Monday brunch, a Wednesday happy hour, a Saturday graduation dinner — one room, three rhythms. (Paraphrase freely; do not invent specifics.)
- Then the verbatim press quote, inline:

Inline press quote: `DO NOT REWRITE: "Sava's will always be the classiest and most impressive first date, fifth date or who-knows-what date."`
Attribution: `DO NOT REWRITE: "— The Michigan Daily, Best of Ann Arbor 2019"`
Attribution link: `https://www.michigandaily.com/arts/best-ann-arbor-2019-romantic-dinner-savas/`

- Closing sentence can echo the existing homepage voice — paraphrase "Ann Arbor's most spirited dining institution" without quoting it (the H1 already carried the institutional line).

### === SECTION 5: DAYPART GUIDE ===
Three-column row, equal width, editorial section headers all-caps with tracked spacing. Each column: daypart name + hour line + 2 signature items + CTA. No photos in this section — typography carries it (Sarma / King pattern). Mobile: stacks vertically.

Column 1 — BRUNCH
Label: `DO NOT REWRITE: "BRUNCH"`
Hours: `DO NOT REWRITE: "Daily · 9:00 AM – 3:00 PM"` (per Tock daypart split in verified-facts)
Signature lines (verbatim dish names from verified list):
- `DO NOT REWRITE: "Huevos Rancheros"`
- `DO NOT REWRITE: "French Toast"`
- `DO NOT REWRITE: "Egg White Omelette"`
Body: free prose — "Large Sunday brunch buffet" reference acceptable (Google editorial).
CTA: `DO NOT REWRITE: "Reserve for Brunch"` → `https://www.exploretock.com/savas`

Column 2 — HAPPY HOUR
Label: `DO NOT REWRITE: "HAPPY HOUR"`
Hours: `DO NOT REWRITE: "Monday – Friday · 3:00 PM – 6:00 PM"`
Signature lines:
- `DO NOT REWRITE: "Bang Bang Shrimp"`
- `DO NOT REWRITE: "Sweety Fries"`
- `DO NOT REWRITE: "Truffle Fries"`
Body: free prose — "half off appetizers and cocktails" line is supported by Yelp reviewer Mj J. (cite as general not verbatim); paraphrase.
CTA: `DO NOT REWRITE: "See the Bar Menu"` → `assets/savas-menu.pdf` (same PDF; bar menu is part of it)

Column 3 — DINNER
Label: `DO NOT REWRITE: "DINNER"`
Hours: `DO NOT REWRITE: "Sunday – Thursday · 4:00 PM – 10:00 PM"` and below: `DO NOT REWRITE: "Friday – Saturday · 4:00 PM – 11:00 PM"` (Tock split + weekend close per verified-facts)
Signature lines:
- `DO NOT REWRITE: "Greek Lamb Burger"`
- `DO NOT REWRITE: "Capellini Marlon"`
- `DO NOT REWRITE: "Lamb Shank"`
Body: free prose — "The cuisine is primarily American… some Mediterranean options" (quotable Yelp; paraphrase for this block).
CTA: `DO NOT REWRITE: "Reserve for Dinner"` → `https://www.exploretock.com/savas`

### === SECTION 6: SIGNATURE DISHES (INLINE MENU TEASER) ===
Sarma-style inline prose menu. Single column max-width 820px, editorial serif for dish names, body sans for descriptions, right-aligned price column. Section header: "A taste of the menu." Each line = dish bold + ingredient list lowercase + price trailing. Ends with "See the full menu" → PDF.

Section header (paraphrasable — free prose).

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
  Description: `DO NOT REWRITE: "served on a slice crispy rice, toast with spicy sweet sauce"` (Yelp verbatim)
  Price: — (not verified) — omit the price column for this line; show em-dash.

Dish 4:
  Name: `DO NOT REWRITE: "Cheesecake"`
  Description: `DO NOT REWRITE: "bruleed, strawberry jam, berries"`
  Price: `DO NOT REWRITE: "12"`

CTA (bottom of section): `DO NOT REWRITE: "See the Full Menu"` → `assets/savas-menu.pdf` (target="_blank") — per skill rule, PDF not on-page anchor.

### === SECTION 7: THE ROOM ===
Two-column 60/40. Left column (60%): a single real interior photograph — the bi-level dining room or bar; select from `scrape/homepage.md` CDN list (`_F8A3233-2.jpg`, `DSC_3613.jpg`, `_F8A3242-2.jpg`, `_F8A5730.jpg`) — pick the one where the bi-level structure reads clearly. Right column (40%): short paragraph about the room, 216 S State St address with inline `tel:` + maps link, line about private dining.

Free prose (paraphrase around fenced strings):
- Reference the "contemporary bi-level eatery" editorial line (Google), "notably has two levels" (Yelp Ned I.), and that the room is downtown on State Street near the University. No specific invented history.

Address block (verbatim):
- `DO NOT REWRITE: "216 S State Street · Ann Arbor, MI 48104"`
- Phone link: `DO NOT REWRITE: "(734) 623-2233"` with `href="tel:+17346232233"`
- Maps link: open `https://maps.google.com/?q=Sava's+216+S+State+St+Ann+Arbor+MI+48104` in new tab
- Private events line (paraphrasable): point to `https://www.exploretock.com/savas/private-dining`

CTA: `DO NOT REWRITE: "Book a Private Event"` → `https://www.exploretock.com/savas/private-dining`

### === SECTION 8: REVIEWS / VOICE OF GUEST ===
Three-column editorial quote row. Each quote in an editorial serif, ~24–28px, italic, with attribution set smaller in a sans below. No star ratings. No "Testimonials" header. Section label: one quiet eyebrow line.

Quote 1:
  Body: `DO NOT REWRITE: "The vibe, the cocktails, the food the people and the service were all top notch."`
  Attribution: `DO NOT REWRITE: "— Larry Kush, Google"`

Quote 2:
  Body: `DO NOT REWRITE: "The interior is elegant, and notably has two levels. The combination of the beautiful ambiance and the high quality food make Sava's a desirable destination."`
  Attribution: `DO NOT REWRITE: "— Ned I., Yelp Elite All-Star, June 2025"`

Quote 3:
  Body: `DO NOT REWRITE: "Had a wonderful brunch experience at Sava's. The ambiance was excellent, and the huevos rancheros were excellent and a great portion size."`
  Attribution: `DO NOT REWRITE: "— Nisha N., Yelp, February 2026"`

### === SECTION 9: PULPO GROUP LOCKUP ===
Three-tile row (La Semilla pattern). Each tile: small image, property name in display serif, one-line role, outbound link. Section eyebrow: "Part of the Pulpo Group."

Tile 1 — Sava's
  Name: `DO NOT REWRITE: "Sava's"`
  Role: `DO NOT REWRITE: "Ann Arbor · Since 2007"`
  Link: `/` (self)

Tile 2 — Aventura
  Name: `DO NOT REWRITE: "Aventura"`
  Role: free prose — if sister-property role not verified, use "Spanish tapas · Ann Arbor" only if confirmable; otherwise paraphrase neutrally (e.g., "Ann Arbor").
  Link: `https://www.exploretock.com/aventura`

Tile 3 — Dixboro House
  Name: `DO NOT REWRITE: "Dixboro House"`
  Role: free prose — "Ann Arbor" (role not verified beyond location).
  Link: `https://www.exploretock.com/thedixboroproject`

Section note: neither `Aventura` nor `Dixboro House` has verified descriptor copy in `verified-facts.md` beyond "Partners" on Tock + "Ann Arbor" location. Keep their tile copy minimal; the tile is about acknowledgement + navigation, not marketing.

### === SECTION 10: INSTAGRAM STRIP ===
4-column photo grid pulling from @savas_ann_arbor. Since the scrape didn't capture live IG posts, the HTML agent should use 4 real Squarespace CDN images from the homepage scrape (food / interior / cocktail plates) as a static stand-in, with an outbound link to Instagram. Each image square-cropped.
Section eyebrow: `DO NOT REWRITE: "@savas_ann_arbor"`
CTA (text link): `DO NOT REWRITE: "Follow on Instagram"` → `https://instagram.com/savas_ann_arbor`

### === SECTION 11: FOOTER ===
Three-column dark-ground footer on warm dark (NOT default black — try a deep rust or warm charcoal that reads against the palette).

Column 1 — Visit
  Label: `DO NOT REWRITE: "Visit"`
  Address: `DO NOT REWRITE: "216 S State Street, Ann Arbor, MI 48104"`
  Phone: `DO NOT REWRITE: "(734) 623-2233"` (tel: link)
  Email: `DO NOT REWRITE: "info@savasannarbor.com"`

Column 2 — Hours (all dayparts, verbatim from verified-facts)
  Label: `DO NOT REWRITE: "Hours"`
  Lines (each verbatim):
  - `DO NOT REWRITE: "Sunday – Thursday · 9:00 AM – 10:00 PM"`
  - `DO NOT REWRITE: "Friday – Saturday · 9:00 AM – 11:00 PM"`
  - `DO NOT REWRITE: "Happy Hour · Monday – Friday · 3:00 PM – 6:00 PM"`

Column 3 — Reserve & Follow
  Label: `DO NOT REWRITE: "Reserve & Follow"`
  Primary CTA: `DO NOT REWRITE: "Reserve a Table"` → `https://www.exploretock.com/savas`
  Secondary text link: `DO NOT REWRITE: "Private Events"` → `https://www.exploretock.com/savas/private-dining`
  Secondary text link: `DO NOT REWRITE: "Catering"` → `https://www.ezcater.com/catering/savas-3`
  Social icon row (inline SVG only, never text/emoji): Instagram → `https://instagram.com/savas_ann_arbor`, Facebook → `https://facebook.com/savasannarbor`

Footer base strip (below columns): wordmark + `DO NOT REWRITE: "© 2026 Sava's · Part of the Pulpo Group"` + small "Built for Ann Arbor" tagline (free).

---

## Global Rules for Phase B Agent

- Download every image used in the mockup into `prospects/savas/mockups/assets/`. Never hotlink Squarespace CDN URLs.
- Image source priority: (1) Squarespace CDN URLs inside `scrape/homepage.md` and `scrape/homepage-metadata.json`; (2) if a better angle exists on the live site, fetch from there. Do NOT use stock photography.
- Verify each image with `sips -g pixelWidth -g pixelHeight` before committing. Hero must be ≥1920px native width. Signature-dish tiles must be crop-safe square/landscape.
- Menu CTAs (nav Menu, hero See the Menu, Section 6 See the Full Menu) all target `assets/savas-menu.pdf` with `target="_blank" rel="noopener"`. File will 404 until Annabel supplies the PDF — structure is right.
- No chef/founder portrait slot exists in this spec — no named founder surfaced in `verified-facts.md` (Team = not verified). Do not invent one.
- No audit-pill annotations anywhere.
- No emojis. SVG icons only (Instagram, Facebook, phone, pin, clock).
- Responsive at ≤768px. Daypart columns stack; dish rows preserve prose structure; Pulpo tiles stack.
- Typography: load body Aktiv Grotesk (or closest fallback — Inter as safe fallback) + headings Brandon Grotesque; pair display headline with an editorial serif (Fraunces or Canela or GT Super) for the H1 + section labels. Keep pairing to two families max.
- Palette: `#DDBD6B` gold (primary), `#A54223` rust (accent / CTA fill), `#FFFDF7` cream background, `#1C1613` warm near-black text. Gray text `#5B5C62` only for captions/meta. No default `#000`.
- Motion: hero image quiet Ken Burns (optional), hover lift on Pulpo tiles, underline-on-hover on text CTAs. No autoplay video. No parallax.

## Output

Write to: `prospects/savas/mockups/homepage-redesign.html`
Assets to: `prospects/savas/mockups/assets/`
