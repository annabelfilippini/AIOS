# Free your Mind — Design Brief

Project direction for the FyM redesign. Read after `projects/websites/design.md`
(global taste) and alongside `content.md` (facts) before building.

## North Star

Make a visitor feel the warmth and rush of a Tarifa kite trip at once: sun, wind,
water, and a crew that actually looks after you. It must sell the school (book a
course / camp) and lean on the two things that make FyM different: the holistic
kite + yoga soul, and the "No Wind? No Pay" guarantee. Primary action: message on
WhatsApp.

## Vibe Lane

**Warm cinematic / kinetic** — the kinetic-documentary energy (full-bleed action
photography, big editorial type, dark cinematic chapter bands, motion on scroll,
real reviews) but warmed all the way up. This is a deliberate correction: the
earlier 2026-06-14 build was soft-editorial/wellness and Annabel found it too
stark, clean, and boring for a kitesurf camp. We keep the premium editorial
craft but inject heat, scale, and movement so it feels alive.

It borrows STRUCTURE from the Freeride site (hero, chapters, choice grid, reviews,
CTA, scroll-reveal) but must NOT look like a Freeride clone — Freeride is a
competitor in the same town. The separation is color, type, and soul: Freeride is
cold near-black + acid-lime + heavy sans, adrenaline-only. FyM is warm
espresso/sand + sunset coral + serif-led, with a holistic kite+yoga warmth.

## Brand

- Colors:
  - Ink (warm near-black): `#1A1512`
  - Sand / paper (light sections): `#F4ECDD`
  - Cream highlight: `#FBF6EC`
  - Accent (single): **sunset coral** `#E8623A` (golden-hour heat, kite energy).
    One accent only — do not add a second loud color.
  - Sea-teal `#2C5A55` allowed ONLY as a quiet deep tone for the yoga/calm note,
    never as a second accent.
- Type: **Fraunces** (high-contrast serif, display + headlines; italic for the
  word "Mind") + **Inter** (body, labels) + a monospace (**Space Mono**) for
  small uppercase labels, stats, and numeric markers (the kinetic-doc texture).
- Logo: their real cyan/yellow mark, `assets/web/brand/logo.png`. Bright vs the
  warm palette — acceptable as the brand mark; offer a one-color treatment later
  if it fights the palette. Footer can use a text wordmark if the logo's dark ink
  disappears on dark.
- Wordmark rule: "Free your Mind" — no added punctuation.
- Voice: plain, warm, direct, a little playful. No marketing taglines, no
  dashes as punctuation. Good lines: "We teach all year, in small groups, at
  your own pace." · "No wind, no pay. If it will not fly, you do not pay." ·
  "Ride the strait where the Atlantic meets the Mediterranean."

## Audience

1. First-timers who want a calm, safe way into kitesurfing (warmth + small groups
   + no-wind guarantee matter most).
2. Improvers / independent riders who want good gear, supervision, and camps.
3. Trip-seekers who want kite + yoga + Morocco, the whole holiday built for them.

## Page Architecture

Full site now built: Home + 5 inner pages (Courses, Offers, Stay, Tarifa,
Contact). Nav = Home · Courses · Offers · Stay · Tarifa · Contact, all internal.
WhatsApp is the standing action on every page.

Shared CSS/JS: all pages link `assets/web/styles.css` + `assets/web/site.js`
(extracted from the homepage's inline block, byte-for-byte the same tokens, so
pages can't drift). Inner pages use `body.solid-nav` for a solid top bar from the
top, and `.page-hero` (compact ~62svh hero). Reusable components added:
`.split` (alternating image/text rows), `.lodge` (accommodation list), `.chips`
(activity tags), `.info-grid`/`.map` (contact).

Homepage flow: hero (with a small "No wind, no pay" promise pill under the CTAs)
→ who we are (warm band,
restrained facts, team) → wind chapter (dark action) → four ways into the water
(offerings grid) → Morocco chapter → reviews + TripAdvisor accolades → stay
(compact list) → full-bleed CTA → designed footer.

## Asset Strategy

Their own photos on their own redesign are fine (logo, award badges, gallery
shots). Instagram pull was blocked (see content.md) — Annabel will supply the
real IG photos/videos to feature; current photos are website-gallery stand-ins.
Do not place any non-FyM stock as if it were theirs; flag and replace before
launch. No watermarked aggregator images.

## Image Handling (get it right the first time)

Annabel's standing preferences after the 2026-06-21 image pass. Apply these
whenever placing or swapping a photo, so images come out right without a redo:

- **Show the whole subject.** Never crop the hero rider's head or body out of
  frame. On a full-bleed hero the surfer must read as a whole person, not a pair
  of legs. The hero portrait sits at `object-position: center 18%` for exactly
  this reason — tune position per image and verify in the browser before calling
  it done.
- **Sharp, high-res source only.** Never use a blurry video / reel poster frame
  as a key band image when a real photo exists. Reel stills are soft; prefer the
  IG photo posts (`*.jpg`, ~1440px) or the raw gallery stills. The Kitesurf band
  was a soft reel frame and was replaced with a crisp foil photo.
- **Portrait source in a wide band → set `object-position` deliberately.** Cover
  crops a tall photo to its vertical middle, which is usually the dead/empty part.
  Push the crop to the part that tells the story (Morocco band uses
  `center 72%` to show the coast + water + rider instead of bare hillside).
- **Pick the image that tells the section's story.** "Morocco camps" wants a
  layered destination/coast or a real camp scene, not a lone figure walking away.
- **Crop out photographer watermarks** (e.g. Carole de Travieso's) before use.
  They are the team's own photos so usage is fine, but no visible watermark on
  the live site.

## Do / Avoid

Do:

- Lead with real golden-hour FyM action photography, full-bleed.
- Use heat and motion: coral accent, scroll-reveal, slow-zoom hero.
- Surface "No wind, no pay" quietly (a small hero pill), not as a loud band.
  Annabel found the full-width coral marquee too prominent for what is really a
  reassurance line — the policy should be known, not shouted.
- Keep the kite+yoga duality visible — it is the brand's real point of difference.
- Real reviews and real accolades only.

Avoid:

- Looking like the Freeride site (no acid-lime, no cold black, no Work Sans).
- The stark/airy/calm-serif treatment that read as boring last time.
- Invented prices, bios, or review text.
- Default four-stat fact strip and identical cream card grids (global design.md).

## Iteration Notes (running log, newest first)

### 2026-06-22 — Brand-true draft (new methodology: start from THEIR side)

New parallel draft at **`index-brand.html`** (the warm-espresso `index.html` is
untouched, kept for comparison). Annabel's insight on a walk: the existing site
uses their real photos and copy but is still HER house lane (Fraunces/espresso/
coral). It is their content in her mould, and the old brief even contemplated
recolouring their own logo so it stopped "fighting the palette." This draft
inverts that: build from their real identity, audited across all channels.

- **Audit (Firecrawl branding extract + logo + About page):** their real brand is
  bright **yellow `#F8EC1E`** + **cyan `#4DC0E2`** + **magenta `#CC3366`** pop on
  white/black, type **Urbanist + Barlow** (rounded geometric sans), rounded pill
  buttons, paint-splatter logo. Their own site self-describes as playful / high
  energy / young & adventurous. Voice is a surprise: mindful and conscious
  ("feel the wind, listen to your body, let go of the noise", "part of the
  family", conscious tourism). The brand is a **duality**: loud playful surface
  over a calm, soulful core.
- **Direction chosen (Annabel): the duality.** Bright brand frame + big energetic
  moments (yellow intro band, cyan chips, splatter-energy logo) AND real
  breathing room + calm soul section in their own words. Not full-send loud, not
  quiet editorial.
- **Deliberate deviation from global design.md** (which defaults to sharp corners,
  serifs, no pills): justified by the project-override clause + "preserve brand
  assets." This is the whole point of the exercise — stop imposing house taste,
  honour their real brand. Ship Gate still fully held.
- **Build:** hero (foil-into-sun, their exact line "what changes everything is not
  kitesurfing, it is how you learn it") → yellow intro band → services cards
  (lessons/wing+surf/camps) → dark SOUL section (their reconnection copy, calm) →
  why-FyM pillars on cyan wash → founder Tanja + real story + 4-person team grid
  (Lilli, Ingo, Gonzalo, Cris) → dark Tarifa/camps chapter with destination chips
  → 5.0 TripAdvisor review marquee on warm sand → glowing dark CTA → footer.
- **Real assets:** their logo + favicon; team portraits + camp/philosophy/Tarifa
  shots pulled from freeyourmindexperience.com into `assets/web/photos/site/`;
  IG action photos + raw gallery reused. No stock.
- **Verified:** desktop + mobile (390) in Playwright, console clean, 0 broken
  images, no horizontal overflow (fixed footer 4-col grid not collapsing on
  mobile), dash punctuation scrubbed (title + awards), Tanja photo de-duplicated.
- **Headings = plain titles (Annabel flagged):** first pass used their real
  sentence as the hero H1 ("What changes everything is not kitesurfing...") and
  she pushed back — she hates sentence-phrase titles, even the client's own.
  Replaced ALL headings with plain noun titles: "Learn to kitesurf in Tarifa",
  "Lessons, camps & rentals", "Why Free Your Mind", "About Free Your Mind",
  "Kitesurfing in Tarifa", "Book your session". Rule sharpened in global
  design.md Ship Gate + memory [[feedback-no-invented-headings]].
- **Button copy (Annabel):** she dislikes "book me in" (their real button label).
  Primary WhatsApp button is **"Message us on WhatsApp"** everywhere (hero, header,
  mobile menu, bottom CTA); secondary hero button is **"Offerings"** (→ services).
  Use these on the inner pages too.
- **Hero layout:** two buttons only; the "No wind, no pay" pill sits BELOW the
  buttons on its own line, no ✦ star.
- **Offerings:** three equal cards side by side (Lessons / Wingfoiling & surf /
  Camps) so all offerings are visible together; no big spanning card.
- **DEPLOYED 2026-06-22 (Annabel: "this is epic, push to vercel"):** live at
  **https://freeyourmind-tarifa.vercel.app/** (public, no login wall). File
  structure changed for deploy: brand-true is now the canonical **`index.html`**
  (served at `/`); the old espresso version preserved as `index-espresso.html`;
  `index-brand.html` kept as an identical copy. The 5 hero/section images that
  lived in the `.vercelignore`d `instagram/` + `raw/` folders were copied into
  `assets/web/photos/site/` (hero-foil, lessons-instructor, wing-rider,
  soul-sunset, tarifa-coast) and repointed, so the deploy is self-contained and
  lean (2.4M). A `/` → `/index-brand.html` rewrite was tried first but Vercel
  served the physical index.html, hence the rename. Verified live: root serves
  the brand page, 13 images load, 0 broken, desktop + mobile.
- **Confirm before launch (still open, *.vercel.app pitch link is fine; a custom
  domain is not until these clear):** review permission for quotes; full team
  roster; current email; prices still routed to WhatsApp.

### 2026-06-21 (pm 4) — Reviews changed to a scrolling marquee (Freeride-style)

- Annabel preferred the Freeride site's reviews that scroll across. Replaced the
  static 2×2 `.review-grid` with a full-bleed `.marquee`: head ("Rated 5.0 on
  TripAdvisor" + badge) stays in a `.wrap`, the scrolling row is edge-to-edge,
  award `.accolades` follow in a `.wrap`. Mechanic copied from Freeride: track is
  `display:flex; width:max-content` animating `translateX(0 → -50%)` over 60s,
  the 4 real review cards duplicated (set 2 `aria-hidden`) for a seamless loop,
  hover pauses, `mask-image` fades both edges, and `prefers-reduced-motion`
  falls back to manual horizontal scroll. Cards use `margin-right` (not flex gap)
  so -50% loops perfectly; flex `align-items:stretch` keeps them equal-height
  with the author line bottom-aligned.
  Verified desktop + mobile (full-bleed, animating, 0 horizontal page overflow).
  Only the 4 existing real TripAdvisor quotes are used (no invented reviews).

### 2026-06-21 (pm 3) — QA pass + mobile navigation added

- Full QA across all 6 pages. Clean: 0 broken images, 0 console errors, all
  internal links + same/cross-page anchors resolve, contact details consistent
  everywhere (WhatsApp, email, IG, FB, TripAdvisor), no horizontal overflow,
  split/lodge/info-grid/card layouts all stack on mobile, contact map renders.
- **Bug found + fixed: no mobile navigation.** Below 860px the nav links were
  simply `display:none` with no replacement, so phone/tablet visitors could only
  reach Home (logo) and WhatsApp. Added a "Menu"/"Close" text toggle (`.nav-toggle`,
  on-brand mono label) on all 6 pages that drops down a full-width cream panel
  with the stacked links; toggle handler in site.js (click, link-click-closes,
  Escape, auto-close on widen). Gotcha logged: the fixed panel collapsed to its
  grid cell width until `grid-column: 1 / -1; justify-self: stretch` forced it
  full-viewport. Verified open/close + full width on mobile and no regression on
  desktop (toggle hidden, tabs inline).
- Pre-launch confirms remain (content, not bugs): camp/Morocco prices kept off,
  accommodation list drift (Casa Arcos), IKO/VDWS currency, reviewer permission,
  and the contact email still on the old `kitesurf-tarifa-spain.com` domain.

### 2026-06-21 (pm 2) — "No wind, no pay" demoted from marquee to a quiet pill

- Annabel found the full-width animated coral marquee too prominent: it shouted a
  reassurance line that should be known, not dominant. Looked at the sister sites
  for precedent — Freeride and the others never use a marquee; they fold trust
  into a calm facts strip + reviews. The moving band was the family outlier.
- Removed the `.ribbon` marquee from all four pages it appeared on (index,
  courses, offers, tarifa) and replaced it with a small static `.promise` pill
  ("✦ No wind, no pay · full refund, every time") sitting under the hero CTAs
  (homepage) / under the page-hero intro (inner pages). Subtle dark-translucent
  chip, hairline cream border, coral ✦ — present and readable, not loud.
- Verified on homepage + courses via Playwright (preview screenshot renderer was
  downscaling this session). Policy still also lives in the footer line.

### 2026-06-21 (pm) — Homepage image fixes + nav float

- **Hero "zoom out":** the surfer was cropped to legs-only. Added
  `object-position: center 18%` to `.hero-media img` so the full rider (head,
  bar, body, board, sun behind) is in frame. Tuned live in the browser (30% and
  42% were worse; 18% shows the whole subject).
- **Nav floats:** removed the divider line under the top bar
  (`.topbar` `border-bottom` → `transparent`) so the tabs read as floating.
- **Kitesurf band de-blurred:** replaced the soft reel-frame `action-1.jpg` with
  the sharp wing-foil photo `instagram/3821376578803076949.jpg` (1440×1774).
- **Morocco band reshot:** the old backpack-walker `morocco.jpg` was weak.
  Swapped to `raw/tarifa-30.jpg` (green mountains + coast + turquoise water +
  rider), cropped to remove the watermark, placed at `object-position: center
  72%` so the layered coast (not bare hillside) shows.
- Originals backed up in `assets/web/photos/_pre-imgfix-backup/`. Distilled the
  durable lessons into the new **Image Handling** section above (and promoted the
  general ones to global design.md).
- **Offerings cards realigned:** the four `.card` numbers/headings/CTAs sat at
  different heights because each card's bottom-anchored block had a different
  body-copy length. Reserved a consistent paragraph height (`.card p` →
  `min-height: 6em`, reset to 0 in the ≤560px single column) so all four line up
  at desktop (verified identical baselines at 1280 and 1440). Also tightened the
  "Kite & yoga" blurb, the one long outlier, so it wraps to the same line count.

### 2026-06-21 — Inner pages built (Courses, Offers, Stay, Tarifa, Contact)

- Extracted the homepage's inline CSS into shared `assets/web/styles.css` and JS
  into `assets/web/site.js`; rewired the homepage to link them and pointed nav +
  footer + offering cards at the new internal pages (no more links to the old
  Jimdo site). Homepage verified pixel-identical after the refactor.
- Built all 5 inner pages in the same warm-cinematic lane, using REAL copy pulled
  from their live site (courses/offers/accommodation/philosophy via Firecrawl):
  - **courses.html** — "Small groups, real progress" intro (EN/DE/FR/ES, IKO·
    VDWS·FAV, 2–4 per group) + 7 alternating `.split` rows (Beginner, Advanced,
    Private, Girls, Camps, Rental, Supervision). Prices route to WhatsApp.
  - **offers.html** — 5 `.split` offers (Kite & Yoga, Camps Tarifa, Morocco,
    Surf, Kite & Spanish) + tailor-made/group note.
  - **stay.html** — `.lodge` list of the 5 accommodations with real descriptions.
  - **tarifa.html** — destination page (why Tarifa, Costa de la Luz chapter,
    no-wind activity `.chips`).
  - **contact.html** — `.info-grid` (WhatsApp, email, address, open all year, IG,
    FB) + keyless OpenStreetMap embed.
- Held the no-invented-headings rule: headings are their words or plain labels
  ("Our specials", "Where to stay", "When there is no wind", "We answer on
  WhatsApp"). No fabricated taglines.
- Verified each page in the browser (tall-viewport + force-reveal + decode-images
  recipe, since the preview screenshot tool ignores live scroll). No broken
  images, correct active nav, shared CSS working everywhere.
- Pre-launch confirms logged to content.md: stale camp/Morocco prices kept OFF
  the pages, and the accommodation list drift (live body now shows Casa Arcos).

### 2026-06-20 — Instagram pulled + copy regrounded in their real words

- Found their live IG (the old @fym_experience handle is dead): pulled 40 recent
  posts (8 photos + 25 reels) via `gallery-dl --cookies-from-browser chrome` to
  `assets/web/photos/instagram/`. Pick-sheet at `instagram-picksheet.html`. NOT
  yet swapped into the homepage — awaiting Annabel's picks. Best image: sunset
  surf shot (♥358).
- Annabel flagged the invented taglines ("Learning to kite should feel warm,
  not scary", "Ride the strait", "Then Morocco", "A few minutes from the beach",
  "Tell us your level and your dates"). Replaced ALL section headings/copy with
  the client's real site language ("What to expect on your kitesurfing holidays
  in Tarifa", "Our specials", "Kitesurf Tarifa", "Morocco camps", "Rated 5.0 on
  TripAdvisor", "Where to stay", "Tailor made trips, all year") or plain labels.
  Body copy regrounded in their real prose (pristine waters / Costa de la Luz /
  chiringuitos / no-wind activities / "no one does it the way we do"). Promoted
  the rule to global design.md (Content): client sites use the client's own
  words or plain labels, never fabricated taglines.
- Photo swap DONE (same day): 5 real IG photos placed (sunset hero + bright foil
  band + instructor/group/gear cards); yoga, Morocco and CTA stay on their own
  gallery photos (no yoga/Morocco in the IG pull). Text-overlay graphic posts
  skipped. The two big bands now contrast (sunset hero vs daytime foil). Annabel
  delegated the picks ("you call the shots") and loves the sunset hero.

### 2026-06-19 — Restart in the warm-cinematic lane (homepage v1)

- Previous soft-editorial build (2026-06-14) was lost (never committed) AND
  Annabel decided to restart anyway: it read too stark/clean/boring for a kite
  camp. New direction agreed: more fun/energetic, inspo from the Freeride site +
  global design.md, feature their own Instagram media (IG scrape blocked, using
  their website-gallery photos as stand-in for now).
- Built homepage in warm espresso + sand + sunset-coral, Fraunces + Inter +
  Space Mono. Structure echoes Freeride but recolored/retyped to avoid a clone.
- Real TripAdvisor data wired (5.0 / 350 / #3 of 27) with verbatim quotes.
