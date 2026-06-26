# Website Design Preferences

This file is the shared design memory for websites Annabel creates in
`projects/websites/`. Read it before starting or revising a website in this
folder.

This is layer 1 of three. See `CLAUDE.md` in this folder for how the layers fit
together:

1. this file: global taste and standards for every site;
2. `<project>/design.md`: that site's brand direction and iteration log;
3. `<project>/content.md`: that site's verified facts, the source of truth that
   keeps the build from inventing things.

Project-specific design briefs should live inside that project's folder when a
site needs a stronger art direction, client strategy, or build instruction than
this shared preference file can responsibly hold. Use this file for durable
cross-project taste. Use the project brief for what the next builder should
actually make on that site.

Each site's own brief lives at `projects/websites/<project>/design.md`. Keep
project names, client specifics, and named external inspirations (a particular
person, brand, or website you are referencing) in that project brief, never in
this global file. This file should read as durable taste true for every site.

## Ship gate (run before showing Annabel)

Run this list against the actual built page before presenting any site or
preview. These are non-negotiable craft hygiene, deliberately separate from art
direction (lane, references, imagery, section rhythm) which is meant to vary site
to site. Uniqueness lives in the art direction; consistency lives in this gate.
If an item fails, fix it before sharing. Do not present and explain.

1. **Headings are plain titles.** Every heading is a plain functional label or
   short noun phrase (Courses, Where to stay, Reviews, Why [Brand], Book a
   session). Never a sentence, clause, or aspirational line, EVEN WHEN it is the
   client's own real copy. The earlier "lift the client's own words" allowance
   was a loophole Annabel flagged: their real sentence ("What changes everything
   is not kitesurfing, it is how you learn it") is still wrong as a title. The
   client's real sentences belong in body copy, the hero lede, or a clearly
   styled pull-quote, not in an h1/h2.
2. **No orphan subtitles.** No explanatory second-sentence line under a heading.
   Headings stand alone unless the line carries real, specific information.
3. **Punctuation is clean.** No dashes as punctuation anywhere. No trailing
   periods on headers. A brand word carries no punctuation the real brand lacks.
4. **Images are clear and well-framed.** Every image is sharp, centered or
   composed on its actual subject, and not the same image reused across sections.
5. **Images are really sourced.** When an image is missing, pull a real one from
   the client's own site, Google, or Instagram (use the right tool, e.g.
   `gallery-dl` for Instagram), download it locally rather than hotlink, flag
   licensing, and clearly mark any placeholder for replacement before launch.
6. **Copy is real and checked.** Names, prices, hours, ratings, and claims are
   fact-checked. No filler, no copy that could describe any competitor.
7. **Nav state is honest.** The active nav item matches the current page or
   section.
8. **One lane, held.** The page stays in a single vibe lane, not a sampler of
   several.
9. **Verified in a browser.** Checked in a real browser at desktop and mobile
   widths, console clean, links and CTAs work.

## Current Direction

The strongest taste signal is cinematic, editorial, image-led web design:
full-bleed photography, high-contrast typography, restrained copy, and a sense
that the site belongs to a boutique hotel, restaurant, florist, artist, journal,
or thoughtful personal brand rather than a generic startup.

For travel, itinerary, walking, retreat, adventure, and place-based sites, the
direction can lean more outdoor-editorial: expansive real landscapes, unusual
lime or chartreuse type, soft olive fields, and print-layout looseness. It
should feel like an art-directed travel poster or independent tour booklet, not
a booking engine.

For athlete, adventurer, maker, or personal-brand sites, another strong lane is
kinetic documentary editorial: oversized fragmented words, full-body portrait
and action photography, coordinates, achievement stats, projects, causes,
partners, and timelines woven into a story. It should feel alive and mythic,
but still useful.

Important: inspiration references are ingredients, not a checklist. Do not try
to include every pattern from this file in one website. Pick the few strongest
ideas that fit the project, then leave the rest out. A good page can use the
hero type from one reference, the image scale from another, and none of the
other modules.

Also apply this within iterations of the same site. If Annabel likes one section
from an earlier draft, preserve it and combine it with the stronger structure
from a later draft. Do not recreate the entire site every time a new reference
appears. Mix and match the best proven pieces.

For client work, choose one dominant vibe lane before designing. A client site
should feel internally coherent, not like a sampler of every taste signal in
this file. The soft luxury/editorial lane and the experimental black/poster
lane are both liked, but they are different worlds:

- **Soft editorial/luxury lane:** cinematic photography, cream/ivory space,
  elegant serif or italic serif, hospitality/wellness calm, restrained sections,
  quiet practical detail. Best for health, wellness, hospitality, retreats,
  personal brands, florists, boutique services, and clients who need trust.
- **Experimental black/poster lane:** black or brown-black fields, oversized
  all-caps sans type, point-cloud or abstract luminous imagery, monospace
  details, asymmetry, attitude, and fewer soft romantic gestures. Best for
  nightlife, culture, fashion, music, edgy retail, creative studios, campaigns,
  drops, or brands that can carry a bolder voice.
- **Outdoor editorial/travel lane:** full-bleed landscape, chartreuse or pale
  lime display type, practical route/place details, olive fields, and tour
  booklet looseness. Best for travel, adventures, itineraries, outdoor brands,
  and place-based guides.
- **Kinetic documentary/person lane:** person-as-world storytelling, fragmented
  words, action/portrait/terrain imagery, coordinates, timelines, stats, and
  projects woven into one scroll. Best for athletes, makers, adventurers, and
  personal archive sites.
- **Soft UI / tool dashboard lane:** calm pale palette (for example blue or
  lavender), rounded panels, soft shadows, one big readout, compact metric
  cards, a left rail, friendly sans type, and an optional charming illustrated
  character. Best for personal tools, dashboards, planners, and weather or data
  apps where clarity and calm matter more than editorial drama. This is the one
  lane that intentionally uses rounded corners and soft cards, so the sharp-
  corner default below does not apply to it. Keep each tool's specific palette
  and character in its own project brief.

Do not combine high-attitude black poster sections with soft wellness/editorial
sections on the same client site unless there is a clear brand reason. If two
references feel like different businesses, treat them as different possible
directions and pick one.

Useful words for the direction:

- Cinematic
- Editorial
- Boutique
- Romantic
- Tactile
- Expensive but not sterile
- Softly dramatic
- Photo-first
- Personal and atmospheric
- Outdoor-editorial
- Art-directed travel
- Print-magazine looseness
- Kinetic documentary
- Athlete profile energy
- Mythic but grounded

## Visual References From Annabel

The first inspiration batch shows these repeat patterns:

- Full-bleed hero images with a dark or warm overlay and white or cream text.
- Large centered headlines with huge scale and generous breathing room.
- Editorial serif or script typography paired with clean sans-serif support text.
- High-contrast type combinations: delicate italic serif plus modern sans,
  ornate script plus crisp uppercase tracking, or sharp serif plus restrained
  body text.
- Food, flowers, gardens, hotels, and intimate lifestyle photography as the main
  design material, not decoration after the fact.
- Motion-blur or soft-focus imagery that feels alive and candid.
- Pale cream, butter yellow, ivory, black, forest green, warm brown, blush pink,
  and deep floral tones.
- Sharp-edged cream, white, or outline buttons, often placed directly over
  imagery.
- Sparse visible navigation and copy. The image and type carry the feeling.
- Split editorial pages with one black or dark panel and one pale cream panel.
- Image grids where photos are large, rectangular, and cinematic rather than
  tiny thumbnails.
- FAQ or content cards can sit on a soft gradient/pink wash, but should feel
  airy and intentional.

The newer travel/adventure references add these signals:

- Expansive landscape heroes with mountains, sky, water, valleys, grass, or
  walking terrain as the main emotional hook.
- Large pale-lime or chartreuse serif headlines directly over photography.
- Small, minimal brand labels above the headline rather than heavy navigation.
- Copy that feels like a tour booklet: short, practical, and atmospheric.
- Deep olive or muted green backgrounds behind editorial content pages.
- Sparse page furniture: small section labels, numeric indexes, and compact
  descriptions placed with a lot of negative space.
- Asymmetrical image collages where photos sit at different heights and widths,
  like a magazine spread.
- Mixed image crops: one wide landscape, one vertical scenic image, one darker
  silhouetted human-scale detail.
- Text and images do not need to align to a rigid card grid when the page is
  meant to feel editorial.
- Nature imagery can be bright and open, not only dark, warm, or moody.

Athlete, adventurer, maker, and personal-archive sites can use a profile-as-world system:

- Treat the person as a world, not just a bio. Blend origin story, terrain,
  projects, cause, timeline, partners, and contact into one immersive scroll.
- Use documentary outdoor imagery: portraits, surfboards, snowboards, boats,
  mountains, water, camps, gear, and action moments.
- Big words can be broken into stacked fragments across the page, creating a
  physical sense of motion and scroll rhythm.
- Add concrete metadata where it adds romance: coordinates, places, years,
  competition stats, project counts, partner counts, and timeline counts.
- Navigation can be minimal but characterful, with labels that feel native to
  the person or brand.
- Achievement stats should feel like editorial texture, not corporate KPI
  cards.
- Sustainability, cause, or mission content can sit inside the same visual
  language as the adventure story instead of becoming a separate nonprofit
  section.
- The page can move between portrait, action, landscape, and sponsor/project
  moments without overexplaining every transition.
- Let playful brand language in sparingly when it feels authentic to the person.

Premium product and adventure pages can use a strong product-film flow system:

- Let the page move like a product film: cinematic hero, product reveal,
  feature sequence, action/story section, image gallery, then a clear CTA.
- Keep sections visually distinct but connected by one product world. Change
  the job of each section instead of repeating the same feature-card rhythm.
- Use a sticky or indexed section rhythm when it helps the product feel
  engineered and explorable, but keep the labels purposeful.
- Pair motion-heavy action imagery with concise product claims, specs, and
  practical details so the drama still feels useful.
- Let full-bleed product or action photography carry transitions. Avoid filling
  every break with extra copy, badges, or decorative proof strips.
- For premium product pages, the flow should feel confident and sequential:
  show the object, explain what changes, prove it in use, then invite action.

The newer non-hero section references add a stronger below-the-fold system:

- Non-hero sections should still feel art-directed. Do not let the page become
  a generic stack of centered cards after a strong hero.
- Pale cream editorial sections can carry practical content through quiet
  grids: three tall image cards, small labels, serif headings, compact metadata,
  and generous space around the group.
- A thin moving or repeated text line can act like a magazine footer/header
  between sections when the phrase is genuinely brand-relevant.
- Process steps work well as quiet numbered blocks on a pale band: `01`, `02`,
  `03`, a short title, and one or two lines of copy. Keep them minimal.
- Team, provider, author, or guide sections should use real portraits with
  compact bios rather than generic profile cards.
- Deep green, black, or brown-black bands can create a strong mid-page reset.
  Pair them with sparse facts, tiny icons, coordinates, service promises, or
  operational details instead of a heavy paragraph.
- FAQ sections can be extremely airy: a narrow centered column, thin rules,
  expandable rows, and a small italic or serif heading.
- Comparison tables can feel editorial if they are centered, lightly ruled, and
  spare. Use them to clarify a choice, not to mimic SaaS pricing pages.
- CTA sections can sit over a soft, abstracted image texture or pale photo wash,
  with centered type and one clean action.
- Footer sections should feel designed: restrained columns, useful links, and
  enough space to close the page elegantly.

Specific non-hero composition patterns worth reusing:

- **Image-backed about band:** a large rectangular image panel with centered
  serif headline and readable body copy directly over the image. Use botanical,
  landscape, fabric, interior, or atmospheric detail imagery.
- **Dark article split:** a tall image on one side, black background on the
  other, oversized serif heading, italic metadata, short paragraphs, and one
  restrained button.
- **Experimental black proof band:** black field, luminous abstract or
  point-cloud image, oversized sans labels, monospace details, and very sparse
  copy. Use for locations, store/service personality, drop zones, or archives.
- **Details page block:** pale textured background, one refined line drawing or
  etched illustration, large serif title, and carefully typeset practical
  details such as date, venue, address, hours, or route.
- **Poster copy spread:** oversized all-caps sans copy placed asymmetrically,
  with italic or handwritten annotations used sparingly for attitude.
- **Three-image caption grid:** three strong vertical photos, each with a short
  caption or phrase underneath. Let the photos do most of the persuasion.
- **Full-bleed contact/photo section:** a real campaign-style image as the
  entire section background, large brand word or mark, and contact details set
  as part of the composition.
- **Image-led trust section:** a large real image with oversized trust/proof
  type and a short checklist of benefits. If the reference uses rounded pills,
  translate them into sharp labels, thin rules, or squared-off callouts.
- **Local recommendations / venue guide grid:** when a site promotes nearby
  businesses (restaurants, bars, shops, hotels, studios), present them as
  image-led cards: one appealing photo of the food or venue, the venue name, its
  real Google star rating and review count, and the whole card linking out to
  that venue's Google reviews (a `google.com/maps/search/?api=1&query=Name+Town`
  URL is a reliable keyless deep-link). Group the cards by category with a small
  section header per group (e.g. Breakfast, Lunch, Dinner, Beach bars, Yoga,
  Hotels) and add an optional "[Brand] pick" tag on the owner's favourites.
  Annabel wants this as the way to
  advertise a destination's best spots and send traffic to them. Show the real
  rating even when it is mediocre if she asks for honesty; keep cards a uniform
  image-with-gradient-caption tile so the photos carry the section.

## Hero Preferences

- Prefer immersive full-bleed image heroes for branded, personal, hospitality,
  restaurant, travel, floral, event, and editorial sites.
- Put text directly over the image with careful contrast, not inside a card.
- Let the brand, place, offer, or person be obvious in the first viewport.
- For business heroes, prefer the real logo, the business name, or a plain
  title treatment over vague poetic intro phrases. Keep the scale intentional,
  not page-consuming. Avoid lines like "born in the wind" unless Annabel
  explicitly asks for that tone. They can read cheesy on client sites.
- Do not add punctuation to a brand word or wordmark unless the actual brand
  includes it. A brand name is not a sentence.
- Use overlays when needed, but keep the underlying image visible and rich.
- A strong hero can be centered, but asymmetrical left-aligned hero text also
  works when the image composition supports it.
- Large hero type should feel designed and proportionate, not default
  browser-big.
- Avoid split text/media hero layouts for this collection unless the reference
  is intentionally editorial and the image still dominates.
- For outdoor travel heroes, try huge elegant serif type in pale lime,
  chartreuse, cream, or white over an actual landscape. The type can be centered
  and dreamy, as long as the place still reads clearly.
- Use small uppercase labels sparingly. Remove them when they repeat the
  headline or add no real orientation.
- Let the hero feel like a poster: one strong image, one clear line, or just
  the brand word. It does not need a proof strip, three facts, or summary cells
  in the first viewport when the hero already has enough presence.

## Shape Language

- Use sharp corners by default for the editorial, cinematic, travel, and brand
  lanes. (Exception: the soft UI / tool dashboard lane uses rounded corners and
  soft cards on purpose.)
- In those default lanes, do not use rounded corners for buttons, headers,
  cards, tabs, badges, image frames, panels, or booking modules.
- Avoid pill buttons and rounded rectangular UI unless Annabel explicitly asks
  for that specific project.
- Do not invent circular badges, soft cards, or rounded logo containers as
  decoration. Only preserve circular forms when they are part of an existing
  brand asset or necessary icon.
- Prefer clean square geometry, hard edges, thin rules, strong crops, and
  editorial grid tension.

## Typography

- Favor elegant serif, italic serif, and occasional expressive script for display
  moments.
- Pair expressive display type with clean, modern sans-serif body text.
- Use all-caps tracking for small labels only when they add real orientation.
  They are optional, not section furniture.
- Use italic words inside headings when they add rhythm or romance.
- Keep direct explanatory headings in one font and color. Do not add italics or
  color shifts just to make them feel designed.
- Keep long paragraphs readable. Do not use ornate script for body copy.
- Let typography have contrast: big/small, serif/sans, roman/italic.
- Avoid generic tech/SaaS heading styles unless the site truly needs that mode.
- For travel/adventure pages, a luminous serif headline can be almost absurdly
  large. Keep support text small, clean, and understated so the page does not
  become loud everywhere.
- Numeric markers like `01`, `02`, and tiny tour labels can add editorial
  structure without making the interface feel like a dashboard.
- For athlete/persona sites, consider fragmented oversized words or short
  stacked phrases that reveal across the scroll. Keep body copy quiet so the
  display type can carry movement.
- Stats can be typeset as plain editorial facts rather than boxed metrics. Keep
  numbers and labels aligned so the strip feels intentional.

## Photography And Image Treatment

- Choose images that show real texture: food, glassware, fabric, flowers,
  gardens, water, warm lights, hands, tables, movement, interiors.
- For travel pages, prioritize real place texture: mountains, coastlines, lakes,
  valleys, paths, grass, weather, silhouettes, street corners, shopfronts, and
  lived-in local details.
- Prefer cinematic crop, soft grain, blur, motion, and shallow depth of field
  over sterile stock imagery.
- Darkened or warm-tinted image overlays are welcome when they improve legibility.
- Use full-bleed images and large editorial image blocks.
- Do not repeat the same image across major sections or multiple cards in the
  same content set. Either source distinct images for each role, or remove
  images from that set.
- Avoid tiny decorative imagery that does not carry meaning.
- If using AI-generated images, make them look like real campaign photography,
  not glossy synthetic placeholders.
- Respect image licensing on client sites. Do not place scraped photos, paid
  stock previews, or a specific business's own copyrighted images on a live
  client site without permission — naming a real venue in copy is fine (facts),
  but its photos are not ours to use. Use owned, client-provided, or genuinely
  free-license imagery (Unsplash/Pexels/Wikimedia, terms checked). Mark any
  preview-only placeholders clearly and replace them before launch.
- For adventure/tour pages, combine scale and intimacy: one grand establishing
  landscape, one mid-distance walking or route image, and one small human detail
  or silhouette.
- Let some images breathe independently on the page. They do not always need
  captions, borders, or equal card sizes.
- For athlete/adventurer pages, use the person in context. A portrait alone is
  weaker than a portrait plus terrain, gear, weather, action, or evidence of the
  life around them.
- Mix archival-feeling photos, polished campaign shots, and imperfect candid
  details when the story needs depth.
- **Keep the subject whole.** On a full-bleed hero or chapter band, the main
  subject (rider, person, hero object) must read as a complete thing, not be
  cropped to a fragment. When `object-fit: cover` clips a portrait source to its
  empty vertical middle, set `object-position` deliberately so the meaningful
  part is in frame (e.g. `center 18%` to lift a jumping rider's whole body into
  view, `center 72%` to pull a coastline + water up from the bottom). Tune it in
  the browser and verify before calling the image done.
- **Sharp, high-resolution source only.** Never use a blurry video / reel poster
  frame as a key band image when a real photo exists. Reel and grid stills are
  soft; prefer full-size photo files (~1440px+) or raw originals.
- **Crop out photographer/watermark text** before placing an image on a page,
  even when the photo is legitimately the client's to use.

## Color

- Strong liked colors from this batch: black, ivory, cream, butter yellow,
  forest green, deep olive, warm pastry brown, amber, blush pink, rose, and
  saturated floral accents.
- Pink can work when it feels fashion/floral/editorial, not default candy UI.
- Green can work when it feels botanical, garden, mossy, or cinematic.
- Black backgrounds are welcome when paired with warm imagery and elegant type.
- Avoid flat corporate blue/purple gradients unless the project specifically
  calls for them.
- Add acid-lime, pale chartreuse, and luminous yellow-green as accent or hero
  type colors, especially against landscape photography or deep olive fields.
- Olive backgrounds can be quiet and editorial. Pair them with muted light text,
  lime accents, and real photography so the page does not become flat military
  green.
- Bright blue sky and green land are allowed to carry the palette when the
  photography is strong. Do not over-filter every outdoor image into darkness.

## Layout

- Build the usable experience first, not a marketing placeholder.
- Put the primary user workflow or strongest brand signal in the first viewport.
- Use bold section contrast: full-bleed image, then dark editorial panel, then
  pale airy section.
- When a site starts feeling busy, simplify the information architecture before
  polishing components. A calm, structured layout can work well: top-level
  tabs for the real site sections, one large white content canvas, a sticky
  left scroll rail, plain black headings, one meaningful image, and sparse
  stats or content blocks.
- Keep true top-level pages separate when Annabel says they are separate tabs.
  For example, a Lessons or Services page should live on its own page/tab
  rather than appearing below the homepage scroll.
- The left rail pattern is useful for service pages with multiple scroll
  chapters. Let it follow the user through one tab at a time and name the real
  decision path, such as About, Instructors, Location, Options or Beginner,
  Intermediate, Advanced, Pricing, Roadmap, Syllabus.
- Do not default to stylized map or route-line sections. Annabel did not like
  an abstract decorative map treatment, especially when the geography is
  not accurate. Use maps only when the project truly needs location utility and
  the map can be verified.
- When location matters, prefer real place photography, specific written
  directions, neighborhood context, practical links, or a simple list of stops
  before inventing decorative map graphics.
- A simple locator map can work when it answers a real user question, such as
  where a town sits in Spain. Keep it grounded in real geography and use a
  clear marker, not abstract route art for its own sake. If the map is not
  trustworthy, use real place photography and verified written details instead.
- A locator map earns its place only when it answers a real "where will I be?"
  question and the geography is accurate; the dislike was always of inaccurate
  decoration, not of maps as such. When a map earns its place, prefer a real,
  zoomable map embed over an illustrated SVG. Technical note: Google Maps'
  keyless `output=embed` will not frame reliably (blank without a paid API key,
  and blocked in headless preview); use a keyless OpenStreetMap export embed
  instead (`openstreetmap.org/export/embed.html?bbox=W,S,E,N&layer=mapnik&marker=lat,lon`),
  or a real static map image. A custom branded SVG is acceptable when no accurate
  tiles are needed.
- Use tabs, side panels, split panes, filters, and editable lists when they make
  a tool more useful.
- If a preview uses tab-like page exploration, keep future site sections visible
  in the top navigation when Annabel wants to remember the eventual IA, even if
  the prototype temporarily links to the original site.
- Keep navigation state honest: the active/current nav item must reflect the page
  or section the user is on. Do not leave the homepage tab highlighted on an
  inner page. Set the active state per page and re-check it after any header
  change.
- Avoid nested cards. Use cards for repeated items, modals, and framed tools.
- Keep page sections unframed or as full-width bands.
- Give fixed-format elements stable dimensions so text, hover states, and
  dynamic content do not shift the layout.
- For itinerary, tour, and route pages, use editorial spreads as a model:
  label in one corner, index number near the center, compact description block
  elsewhere, and images staggered across the lower half.
- Do not force every destination or tour into identical cards. When the content
  is scenic or experiential, varied image size and placement can make the page
  feel much more alive.
- Keep copy blocks narrow on editorial travel pages. A few short lines with
  price, duration, route, or timing often works better than a paragraph-heavy
  layout.
- For personal adventure profiles, structure the page as chapters rather than
  standard sections: origin, terrain, proof, projects, cause, home, partners,
  contact.
- Use counts like `Projects (09)`, `Partners (05)`, or `Timeline (33)` as
  navigational texture when the site has a real archive behind it.
- Coordinates, place names, and timeline entries can make a page feel specific
  without needing heavy explanation.
- Do not default to the same four-item fact strip on every site. It works well
  as one possible rhythm, but repeated use across unrelated previews makes the
  sites feel templated. Switch up the proof/summary device: try one strong
  pullquote, a two-column detail list, a staggered image/caption sequence, a
  timeline, a single oversized number, an editorial table, a short checklist, or
  no proof strip at all.
- Do not default to three summary cells in or below a hero. Some hero pages
  should simply be a strong brand/title image with no immediate proof device.
- Likewise, do not reuse the same section sequence by habit. A site can be
  great with fewer sections, longer image-led chapters, or one memorable detail
  block instead of a standard hero/facts/grid/steps pattern.
- Sponsor / partner section (loved component, validated on Freeride 2026-06-14):
  present partners as a tight logo grid on a pale field with thin dividers, logos
  muted (grayscale plus low opacity) at rest. On hover or focus, the cell fades in
  a brand-relevant action photo (object-fit cover, slight zoom-settle) with the
  brand name and an arrow over a bottom scrim, while the logo fades out. Touch
  devices show the photo directly since there is no hover. Source one on-brand
  action photo per partner, and flag third-party logos and photos for clearance
  before any live launch. Reuse wherever a site has a real partners or sponsors list.

## Buttons And Controls

- Use sharp-cornered buttons and controls.
- Use thin-outline rectangular buttons for hotel, luxury, editorial, travel,
  restaurant, floral, and personal sites.
- Avoid pill buttons.
- Keep button copy short and human.
- For tools and planners, use familiar controls: tabs for views, toggles for
  binary settings, sliders or inputs for numbers, menus for option sets, and
  icon buttons where an icon is clearer than text.
- Preserve useful edits locally when possible for small static tools.

## Content

- Write plainly and specifically.
- Section headers should tell the reader what the section is about. Use concrete
  labels, no trailing periods, and avoid vague metaphor headings.
- On a client/redesign site, pull section and body copy from the client's
  own real words (their live site, content.md) so the copy feels like them. But
  keep HEADINGS to plain labels or short noun phrases (Courses, Where to stay,
  Reviews, Why [Brand]); a heading is never a sentence, even the client's own
  (Ship Gate item 1). Do NOT invent aspirational sentence-headings or marketing
  taglines. Rejected examples Annabel
  flagged: "Learning to kite should feel warm, not scary", "Ride the strait",
  "A few minutes from the beach", "Tell us your level and your dates". If a
  section needs flavor, lift a phrase the client actually uses (e.g. "No wind,
  no pay", "tailor made trips"), never a fabricated one. Any heading not
  traceable to the client's words is a draft to confirm, not final copy.
- When a clear explanatory header gets too long for large display type, make the
  short section name the big headline and put the explanation underneath as a
  smaller subhead. For example: big `Potential`, smaller "Why Wayloft can become
  a premium travel resource."
- Keep visible instructions minimal. The interface should mostly explain itself.
- Use short atmospheric lines when the site is emotional or editorial.
- Use practical source links when live or verified details affect decisions.
- Fact-check concrete claims before they become design copy, especially lodging,
  locations, services, pricing, instructors, certifications, dates, and contact
  details. Do not turn one example into the only option if the source lists
  multiple options.
- Avoid generic filler copy and catchy filler lines. Real content should shape
  the design.
- Image captions must be accurate and non-redundant. A caption should describe
  what the image actually shows in that section's context — not restate the
  place or section name, and not carry copy that belongs to a different section
  (e.g. a lessons line under a town/after-kite photo).
- When selling a place, destination, or experience, use real sourced numbers and
  named real examples rather than vague adjectives — e.g. "300+ restaurants",
  "40,000+ reviews", or named top-rated venues with their ratings. Prefer
  defensible figures over fragile exact counts that go stale, cite the source
  while drafting, and confirm names/ratings before launch. Naming a real venue
  is fine; using its photos without permission is not (see Photography).
- Promotional/directory exception (validated 2026-06-11): when a section exists
  to advertise other businesses and drive traffic to them (linking out to their
  Google reviews, site, or map), using each venue's own representative photo is
  the wanted approach — the site is promoting them, not passing the work off as
  its own. Still prefer owned or partner-provided shots where possible, get
  clearance before a live client launch, and NEVER use third-party aggregator
  images that carry watermarks or are multi-photo collages (e.g. RestaurantGuru
  CDN — they pass an HTTP-200 check but look unusable). Single photos from the
  venue's own site or Tripadvisor's media CDN are acceptable; always visually
  spot-check downloaded venue images, and download them locally rather than
  hotlinking so the page is self-contained.

## Avoid

- Generic SaaS landing pages for projects that should feel personal,
  hospitality-led, travel-led, lifestyle-led, or editorial.
- Decorative blobs, default gradients, and random abstract shapes.
- Hero text inside cards.
- Tiny images that feel like placeholders.
- Overcrowded copy over photography.
- Script fonts used where readability matters.
- One-note palettes with no contrast or atmospheric depth.
- Repeating favorite modules so often that they become a house template,
  especially the four-item stat/fact strip, numbered step cards, and identical
  cream image grids.
- Amplifying a reassurance or fine-print line (a guarantee, refund policy,
  "no risk" promise) into a loud full-width animated marquee or band. Such lines
  should be known, not shouted: fold them into a small hero pill, a facts tile,
  or the footer. Save high-prominence treatments for the actual headline message.

## Verification

- Open local websites in a browser after meaningful visual or interaction work.
- Check desktop and mobile-ish widths.
- Confirm text does not overlap, buttons remain readable, and main controls
  still work after edits.
- If external embeds are used, make sure the page still works when the embed is
  slow or imperfect.
- Every time you create a new website, open the finished page in a real browser
  for Annabel to review (for example `open <file>` or the localhost URL), not
  only the inline preview panel.
- When screenshotting with the Playwright MCP, pass an absolute path as
  `filename` (it otherwise saves relative to the repo root and is easy to lose).
  Before a full-page screenshot of a page that uses scroll-reveal animations,
  force-reveal the animated elements first (browser_evaluate adding the visible
  class, for example `.in`, to every `.reveal` element), or off-screen sections
  capture blank even though the page works fine for real users.
