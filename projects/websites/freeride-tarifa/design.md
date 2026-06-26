# Freeride Tarifa Design Brief

This is the project-specific design direction for the Freeride Tarifa rebuild.
Read it after `projects/websites/design.md` and before editing
`index.html`, `lessons.html`, `rent.html`, `tarifa.html`, `stay.html`, or future
Freeride pages.

## North Star

Freeride should feel like a cinematic Tarifa kitesurfing trip led by real,
warm, expert people. The site can be dramatic, image-led, and a little mythic,
but it still has to sell lessons, rentals, kite camp, yoga, and WhatsApp
booking clearly.

The current live site already has the ingredients: IKO lessons, rentals, stays,
Tarifa guidance, WhatsApp access, and years of beach content. The redesign's
job is to make those ingredients feel like a premium sports-travel experience
instead of a crowded kiteschool directory.

Simple positioning:

> Learn, ride, stay, and belong in Tarifa.

Do not turn the site into a fake athlete manifesto. Free Ride is not one
professional rider's personal archive. It is a school, camp, rental desk, and
local host. The drama should come from Tarifa wind, real students, instructors,
water, gear, flags, town life, and the beginner-to-independent journey.

## Reference Translation

Use references as ingredients, not templates.

### Mathieu Crepel

Take:

- immersive outdoor documentary energy,
- chaptered storytelling rather than generic sections,
- huge fragmented words when they create movement,
- coordinates, years, places, and counts as editorial texture,
- a feeling that the sport is a whole world.

Translate for Freeride:

- chapters such as `Wind`, `Learn`, `Ride`, `Stay`, `Tarifa`, `After kite`,
  `Yoga`, and `Book`,
- real student and instructor stories instead of athlete trophies,
- Tarifa coordinates, wind facts, beach names, IKO levels, lesson progression,
  and camp highlights as texture,
- one or two big word moments such as `WIND`, `FIRST RIDE`, or `TARIFA`, not
  giant fragmented typography in every section.

Avoid:

- copying Mathieu's personal-athlete tone,
- poetic lines like "born in the wind" unless Annabel explicitly asks,
- achievement-stat strips that make a school feel like a corporate dashboard.

### Radian

Take:

- product-film pacing,
- full-bleed action media,
- distinct sections with different jobs,
- concise claims paired with proof,
- a final CTA that feels confident rather than needy.

Translate for Freeride:

- hero video or image sequence, then a clear learning/rental/stay pathway,
- action footage for emotion and close coaching photos for trust,
- lesson levels explained like a progression system,
- rental gear explained with practical rules, rescue support, and who qualifies,
- WhatsApp and booking CTAs always clear.

Avoid:

- over-engineered product-spec language,
- repeating the same feature-card rhythm,
- making every section dark and high-adrenaline. Beginners need reassurance.

### Santic-Style Structure

Take:

- calm information architecture after a dramatic opening,
- top-level pages or tabs for real user choices,
- sticky left rail on deep pages,
- a large white or pale content field with big black headings,
- fewer, stronger modules.

Translate for Freeride:

- keep `Lessons` as a real page, not a homepage section,
- keep `Rent` as a real page for independent riders,
- future top-level pages can include `Kite Camp`, `Yoga`, `Tarifa`, and
  `Contact` if the project expands,
- use a left rail for pages with a sequence: levels, pricing, syllabus, FAQ, or
  requirements.

Avoid:

- making the homepage become a white corporate brochure after the hero,
- hiding the emotional material on Instagram while the website shows only
  tables and cards.

## Audience

Design for three people at once:

- the beginner who is excited but nervous,
- the solo traveler who wants a real trip and social proof,
- the independent rider who needs rental gear, spot knowledge, and rescue
  confidence.

The site should make WhatsApp feel natural. These businesses are reachable,
human, and quick to talk to. The design should keep that strength visible.

## Asset Strategy

Freeride's Instagram is the strongest visual source. Prioritize real Freeride
content over generic kitesurf stock.

Use the shortlist in `research/instagram-media-shortlist.md`.

Best image/video categories:

- close-up student success,
- instructor plus student,
- Freeride rash guards, flags, boards, kites, and beach setup,
- beginner waterstart and bar coaching moments,
- group or solo-traveler camp atmosphere,
- Tarifa aerials, old town, cafes, beach transitions,
- kite plus yoga or wellness moments.

Rules:

- Do not hotlink Instagram CDN images in production.
- Local screenshots and captured frames are preview placeholders only.
- For a client-ready version, request original photos and MP4s from Freeride.
- Reels should become native video moments if originals are available.
- Use YouTube embeds only if they still feel current and polished.
- AI-generated imagery is allowed for concept exploration or missing campaign
  scenes, but it should look like plausible documentary campaign photography in
  Tarifa. Do not invent fake instructors, fake testimonials, fake logos, or
  fake client-owned moments.
- If AI images are used, label them internally as concept assets and replace
  with client originals before a final production handoff.

## Page Architecture

### Homepage

Job: make Freeride feel unforgettable within five seconds, then route the user
to the right action.

Recommended flow:

1. Full-bleed cinematic hero using real kite or beach media.
2. Minimal top nav with `Lessons`, `Rent`, `Kite Camp`, `Yoga`, `Tarifa`,
   `Contact`, and `Book` or `WhatsApp` when those pages exist.
3. A kinetic media collage or short film strip using Instagram content.
4. A simple choice section: learn, rent, stay.
5. Human coaching proof: instructors, student moments, IKO/safety reassurance.
6. Tarifa as a trip: wind, beaches, town, after-kite, yoga.
7. One strong WhatsApp booking CTA.

The homepage should not explain every price, package, and beach in detail. It
should make the world feel desirable and send users to focused pages.

### Lessons

Job: make beginners feel safe and make intermediates understand the progression.

Recommended rail chapters:

- Beginner
- Intermediate
- Advanced
- Roadmap
- Prices
- FAQ

Content should explain the path from first kite control to independent riding.
Use level names, IKO language, rescue/safety support, and price clarity. Pair
each level with one real image that shows coaching or attainable progress.

### Rent

Job: qualify independent riders and make rental feel safe, clear, and premium.

Recommended rail chapters:

- Who can rent
- Gear
- Spots
- Rescue
- Prices
- WhatsApp

Rental should not look like a generic equipment table. It should feel like:
"You are an independent rider, Tarifa is powerful, and Freeride has the local
gear, spot knowledge, and support to help you ride well."

### Tarifa

Job: sell Tarifa as a destination so a kite trip feels like a real holiday, not
just lessons. Built (2026-06-11) as an eat / drink / party local guide.

Contains: a real coastline map, the kite spots, and a venue guide (breakfast,
lunch, dinner, beach bars & nightlife, yoga) built from Freeride's own advertised
lists. Each card is a local photo + Google rating + review count linking to the
venue. Keep it honest (show weak ratings too) and use the shared `.venue` card
pattern.

### Stay

Job: turn "where do I sleep" into part of Freeride's kite + stay funnel. Built
(2026-06-13) as its own top-level page, promoted out of the Tarifa page.

Contains: a split hero, the four rated properties Freeride advertises (hotel, spa
hotel, old-town hostel, coliving kite house) as `.venue` cards linking to
Freeride's own booking pages, an honest pointer to Freeride's apartments and
beach-house categories, and a WhatsApp-first CTA. Facts live in content.md under
"Where to stay". Photos need clearance before any live launch.

### Kite Camp And Yoga

Future pages should sell the full trip, not just a bundle.

Use:

- solo traveler proof,
- group atmosphere,
- lodging and town context,
- beach-to-yoga rhythm,
- clear inclusions and exclusions,
- WhatsApp-first inquiry.

## Visual System

Mandatory:

- sharp corners,
- no pill buttons,
- no rounded cards,
- no decorative blobs or default gradients,
- no generic blue/white startup layout,
- no abstract inaccurate route map as decoration.

Palette:

- base: black, off-white, salt white, sea-shadow gray,
- accent: Freeride green, kite blue, rescue red only where meaningful,
- optional drama: acid-lime or pale chartreuse for one or two oversized display
  moments,
- let sky, sand, water, and gear colors come from photography.

Typography:

- Work Sans can stay for practical clarity.
- Add a stronger display type only if it helps the cinematic direction.
- Display type can be oversized and fragmented in a few places.
- Body copy should stay plain, direct, and easy to scan.
- Do not use ornate script or romantic travel copy for practical lesson details.

Layout:

- start with a full-bleed hero,
- let the first viewport signal Freeride, Tarifa, and kitesurfing immediately,
- use one cinematic dark opening and then calmer editorial content,
- alternate large media, rail chapters, and practical tables instead of card
  grids everywhere,
- keep top-level user choices separated into pages,
- use big white or pale sections when the user needs clarity,
- use dark sections when the content is emotional, atmospheric, or video-led.

## Copy Direction

Voice should be confident, human, and specific.

Good:

- `Tarifa kitesurfing, taught by people who know the wind.`
- `From first kite control to independent rides.`
- `Lessons, rental gear, kite stays, yoga, and local spot guidance.`
- `Message us on WhatsApp and we will help you choose the right day.`

Avoid:

- `born in the wind`,
- `where dreams meet the ocean`,
- `unlock your potential`,
- `experience freedom like never before`,
- any line that sounds like a generic adventure template.

Use real facts only. Fact-check prices, IKO certification, lesson lengths,
locations, accommodations, rental requirements, insurance, rescue support, and
contact links before presenting them as final copy.

## Instagram-To-Website Pipeline

For a dramatic version, build around the content pipeline:

1. Audit public Instagram and current site media.
2. Shortlist posts by website role, not just beauty.
3. Capture temporary preview frames locally.
4. Ask Freeride for the original assets for selected posts.
5. Replace screenshots with originals.
6. Add short native video moments where motion materially improves the page.
7. Keep a fallback still image for every video section.

Best initial production ask to the client:

- 3 hero-quality kite or beach videos,
- 6 student/instructor photos,
- 3 camp/group photos,
- 3 Tarifa lifestyle photos,
- 2 yoga/wellness photos,
- current logo files,
- current prices and booking rules,
- permission to use featured guest/student images.

## Success Criteria

The next Free Ride concept is successful when:

- it feels more memorable than typical kitesurfing school sites,
- it still makes booking and WhatsApp easy,
- a nervous beginner understands they will be supported,
- an independent rider can find rental expectations quickly,
- the Instagram energy finally appears on the website,
- the site feels like Freeride Tarifa, not Mathieu, Radian, Santic, or a generic
  AI adventure template.

## Next Build Direction

Continue from the current local prototype rather than starting over blindly.

Preserve:

- cinematic homepage opening,
- top-level `Lessons` page,
- top-level `Rent` page,
- Santic-style rail structure for focused pages,
- sharp-corner visual system,
- Instagram-derived local asset direction.

Improve next:

- make the homepage less like a collage demo and more like a directed film
  sequence,
- replace any generic or weak image slots with the strongest Instagram-derived
  student, instructor, beach, town, and kite/yoga material,
- make the below-hero homepage simpler and more decisive,
- give lessons and rental pages more emotional media at the top while keeping
  their practical rail clarity,
- add a clearer client asset request list before any production handoff.

## Iteration Notes (running log)

Newest first. Capture what Annabel approved, liked, or rejected during a build so
preferences compound instead of resetting each session.

### 2026-06-14 (pm) — Sponsor brand-photo hover, lighter bands, scroll-reveal rollout

Annabel's feedback on the morning's pass: (1) liked the muted→full-colour sponsor
grid but wanted the hover to show a kitesurfing image tied to each brand ("they use
Eleveight for kites, show someone kitesurfing with an Eleveight kite ... for each
sponsor"); (2) roll the scroll reveal out to the other pages; (3) the near-black band
is unappealing, make it lighter and on-vibe.

- **Sponsor hover → brand action photo. APPROVED — Annabel loves this component (2026-06-14).** Kept the resting muted-logo grid (she likes
  it). On hover/focus each cell now fades in the brand's own kitesurfing/ocean action
  photo with the brand name (↗); the logo fades out under a bottom scrim. Touch devices
  show the photo directly (no hover). One brand-relevant action photo sourced per
  partner — see content.md "Partners and sponsors" for the per-brand image, source and
  licensing. New markup: `.sponsor-logo` / `.sponsor-photo` / `.sponsor-name`.
- **Lighter band.** New `--mist: #e8f1ed` sea-glass token + `.band-soft` modifier (ink
  text, green-dark accents). Applied to the homepage POSITIONING band ("Learn, ride,
  stay, and belong") and, for consistency, the Tarifa WIND band ("The most reliable
  wind in Europe"). Decision: only the flat text bands were lightened. The crew band
  ("people who know the wind") and every photo-backed section (hero, wind chapter, CTA)
  stay dark, per global design.md ("dark sections for emotional / atmospheric /
  video-led content; do not make every section dark"). Easy to also lighten the crew
  band if she wants.
- **Scroll reveal rolled out** to lessons / rent / tarifa / stay (was homepage-only).
  Same IntersectionObserver fade+lift (`.reveal` → `.in`, 0.75s, 30px lift), with
  prefers-reduced-motion + no-IO fallbacks. Rail pages (lessons/rent): each
  `.content-block` reveals, and the reveal observer runs alongside the existing rail
  active-state observer (verified no conflict). Card pages (stay/tarifa): section
  intros, venue/spot cards, guide heads and CTA reveal as they enter view. Heroes left
  visible above the fold.
- Verified in a real browser (Playwright on the local server, since Claude_Preview only
  paints the top of this page reliably): sponsor photos load and reveal on hover; both
  bands compute to the sea-glass colour; below-fold `.reveal` elements start at opacity
  0 and animate to 1 on scroll on all four pages.
- **Open:** (1) sponsor action-photo clearance for production — ideally get one approved
  photo per brand from Free Ride (see content.md). (2) Jeewin's portrait sunset crops to
  sun + rider (kite tip cut) in the 3:2 cell — acceptable, easy to swap. (3) Confirm
  whether to also lighten the crew band. (4) Carried: partner-logo trademark clearance.

### 2026-06-14 — Crepel-style scroll reveal + partners logo grid (homepage)

- **Scroll-reveal animations** added to `index.html`, matching the Mathieu Crepel
  reference (his real site, mathieu-crepel.com, confirmed this session: "sections
  fade and move up as you scroll"). Implemented with one `IntersectionObserver`
  that adds `.in` to `.reveal` elements (fade + 30px lift, 0.75s ease) as they
  enter view; full-bleed chapter image also gets a slow `.reveal-zoom` scale-down
  (1.14 → 1). Applied to the positioning band, wind chapter, the three choice
  cards (staggered via `--rd`), crew heading + cards, reviews head, partners, and
  CTA. **`prefers-reduced-motion` fully respected** (everything shows instantly,
  no transition), and a no-IntersectionObserver fallback reveals all.
- **Partners / sponsors section** (new, before the CTA). Annabel asked to make
  Free Ride's sponsors "look like Mathew's." Crepel's site presents partners as a
  **grid of logos** (dark on pale, thin dividers, "Supported by" label), muted by
  default and coming alive on hover. Built the Free Ride version as a 4×2 logo
  grid (2-col on mobile) of the **8 real partners** Free Ride advertises
  (Eleveight, Ketos, Mystic, Billabong, Kitetrip Planner, Jeewin, Nereide,
  Surfrider). Default state = **grayscale + 0.45 opacity**; on hover the cell goes
  white and the logo snaps to **full colour + slight scale-up** (this is the
  "their company logo appears" behaviour, done with logo-only assets). Touch
  devices show full-colour logos (no hover dependency).
- **Considered then dropped:** a first pass used a vertical name-list with a
  cursor-following logo card. It honoured the words ("hover → logo appears") but
  did **not look like Crepel's grid**, so it was replaced with the grid to match
  the named reference. Can revert to the cursor-follow variant if Annabel prefers
  the flashier version over fidelity to his site.
- **Partner logos stored locally** in `assets/web/sponsors/` (16 files: a wordmark
  and a secondary mark per brand; both turned out to be Free Ride's blue-recoloured
  logos, no action photos). Sourced from Free Ride's own homepage "Our partners"
  block. See content.md for the licensing note.
- **Scope:** homepage only this pass. Scroll-reveal can roll out to lessons / rent
  / tarifa / stay after Annabel approves the feel.
- Verified in preview: no console errors; below-fold `.reveal` elements start
  hidden (opacity 0, translateY 30px) and flip to visible on scroll; all 8 partner
  logos load; grid is grayscale by default and full-colour on hover. Screenshot
  tooling needed the documented reload+resize workaround and only paints the
  top-of-page reliably (hid sections above to capture the grid).

### 2026-06-13 — Stay promoted to its own top-level page (tab)

- **Stay is now its own tab/page.** Promoted the `#stay` block from a section on
  `tarifa.html` into a standalone `stay.html` top-level page (per the Santic-style
  "top-level pages for real user choices" rule and the "Learn, ride, stay, and
  belong" positioning). The four cards were **moved, not duplicated** — the section
  was removed from `tarifa.html`, which now flows after-kite guide → CTA.
- **Nav order:** Freeride / Lessons / Rent gear / Tarifa / **Stay**, on all five
  pages. Annabel chose Tarifa then Stay (Stay last), matching the original
  checkpoint order.
- **New page build:** split hero (kicker "Kite & sleep", h1 "Where to stay", green
  "Plan your stay on WhatsApp" + dark "See lesson packages"). Hero image is
  `oldtown.jpg` (the owned old-town street where the kite houses/hostels are),
  chosen so the hero is not a reused card image (no within-page repeat). Section
  "Beds a few minutes from the beach" with the same four verified `.venue` cards.
  Stay-specific dark CTA on `grab.jpg`: "Tell us your dates, we will sort the room."
- **Honest "more ways to stay" line** under the cards links Freeride's
  `/tarifa-holiday-rentals/` (apartments) and `/tarifa-holiday-beach-houses/`
  (beach houses & bungalows) category pages, with **no fabricated ratings or
  photos** (they are categories, not single rated properties). Building those out
  as full cards still needs scraped photos + verified one-line descriptions.
- **Typo fixed:** dropped the broken "Every one minutes from the beach" guide-sub
  from the old section; the new page uses a clean section title instead.
- Verified in preview: page loads, Stay tab active and correctly ordered on all
  pages, four cards + all images render, no console errors, 2-col responsive at
  tablet width, and `tarifa.html` no longer contains `#stay`.

### 2026-06-13 — "Where to stay" hotels section added to the Tarifa page

- **Built the deferred Hotels ask** as a new `#stay` section ("Where to stay in
  Tarifa", eyebrow "Kite & sleep"), placed after the eat/drink/party guide and
  before the CTA. Uses the identical `.venue` card pattern: photo + Google rating
  chip + a vibe chip (Beachfront / Spa hotel / Old town / Coliving) + one-line
  description. Four cards in the default 4-col grid (2-col on tablet, 1-col on
  mobile).
- **Four properties Freeride advertises**, from
  freeridetarifa.com/vacation-rentals-in-tarifa/: Hurricane Hotel (★4.5), Hotel
  La Residencia (★4.7), Hostal Africa (★4.5), Surfers Residence (★4.8). Facts and
  ratings live in `content.md` under "Where to stay".
- **Cards link to Freeride's own property pages, not Google** (decision to make).
  Hotels are part of Freeride's kite + stay funnel, so "See the place ↗" sends
  users to Freeride's page to book, while the Google rating chip stays as the
  trust badge. Easy to flip to Google-review links if Annabel prefers strict
  consistency with the eat/drink cards.
- **Review counts deliberately omitted.** The Google Maps scrape could not read
  counts reliably (returned "20" for Hurricane, echoed the prompt's "1234" for
  Surfers, a "0"), so cards show the rating only with "See the place" rather than
  a fabricated "X reviews". Ratings are place-verified and stable across two
  scrapes, flagged [recheck].
- **Images:** single hero photos pulled from Freeride's own CDN (their marketing
  images for these properties), each showing the best pool/rooftop with the sea.
  Avoided the multi-photo collage og:images. In `assets/web/venues/`
  (hotel-hurricane, hotel-residencia, hostal-africa, surfers-residence).
- **Open:** verify Google review counts directly before launch if counts are
  wanted on the cards; get photo clearance for a live client launch.

### 2026-06-13 — Facts moved into content.md (new source of truth)

- Created `content.md` as this project's verified-facts layer: business basics,
  lesson and rental price tables, IKO roadmap, the Tarifa venue guide with
  ratings, and a source log. From now, pull facts from `content.md`, not from
  memory or this brief. This `design.md` stays look/feel/voice plus the decisions
  log.
- Flagged recheck-before-launch: all Google ratings and review counts (captured
  2026-06-11) and lesson/rental prices (live site, June 2026). Flagged
  unconfirmed: whether the homepage names "Oleg" (instructor) and "Leah" (rider)
  are real people, per the no-invented-people rule.

### 2026-06-11 — Tarifa page becomes an eat/drink/party local guide

- **Real map replaces the SVG locator.** Annabel asked to swap the hand-drawn
  SVG kite-spot map for a real interactive map of the coastline (she pasted a
  Google Maps view). Shipped a keyless OpenStreetMap embed framed on the kite
  coast (Valdevaqueros → Tarifa), marker at Los Lances, because Google's keyless
  `output=embed` won't frame reliably without a paid API key. This supersedes
  the 2026-06-10 "SVG locator is the wanted map" note: a real accurate map is now
  the default here. (If she later wants the exact Google look live, that needs an
  API key or a static image.)
- **Removed from #after:** the town-stats band (incl. "5 min from beach to old
  town") and the white-streets + yoga photo trip-grid. The text-only favourites
  cards were replaced by real photo cards.
- **New "Eat, drink and party in Tarifa" guide** with five category rows pulled
  from Free Ride's own advertised lists (the-best-places-to-eat / the-most-
  famous-beach-bars): Breakfast, Lunch, Dinner, Beach bars & nightlife, Yoga.
  Each card = local downloaded photo + name + real Google star + review count,
  the whole card linking to that venue's Google reviews. Agua + Balneario carry
  a green "Freeride pick" tag (she loves them for music + watching pro kiters).
- **Show real ratings, even weak ones.** Annabel chose to display Balneario 3.3
  and The Chiringuito 3.7 honestly rather than hide them.
- **Image sourcing lesson:** RestaurantGuru CDN images are watermarked collages —
  unusable; re-sourced clean single photos from venue sites + Tripadvisor CDN and
  visually checked all 20. Images live in `assets/web/venues/`.
- **Deferred:** Shopping skipped this pass (research thin — only SOLOR + Tarifa
  Soul strong). **Next ask:** a Hotels section using the identical card pattern,
  from the hotels Free Ride advertises.

### 2026-06-10 — Tarifa map, distinct imagery, town-as-destination

- **Kite-spot locator map: yes, for this project.** Annabel asked for and
  approved an on-brand SVG map on the Tarifa page showing the town and the three
  kite beaches (Los Lances, Valdevaqueros, Balneario) pinned, so visitors can
  picture where they will ride. This is the wanted kind of map: geographically
  faithful, branded, a real orientation aid — not the abstract decorative route
  art previously rejected.
- **No reused imagery within a page.** The aerial beach shot had been used ~4x
  and made the Tarifa page feel like the homepage. Each section gets its own
  image; keep the hero aerial unique to the hero.
- **Captions must be accurate and non-redundant.** Drop captions that restate the
  place name ("The old town, after kite") or mismatch the section ("Every level
  gets real water time" on a town/after-kite section). A caption should describe
  what the image actually shows in that section's context.
- **Sell Tarifa as a destination, not just a beach.** The homepage town section
  now leads with real sourced numbers (300+ restaurants, 40,000+ traveler
  reviews, top tables 4.5–4.8★) and named real favourites with ratings (Café
  Azul, Bar El Francés, Ola Ola, SOLOR). Use defensible numbers, not fragile
  exact counts.
- **Nav active state must match the current page** (Lessons tab active on the
  Lessons page, etc.).
- **Photo licensing:** do not put scraped venue/town photos on the live site.
  Town and named-venue photos need Free Ride's own shots or per-venue permission.
  The only owned town image right now is the old-town street; everything else is
  a flagged placeholder (see `TODO(photos)` in `index.html`).
