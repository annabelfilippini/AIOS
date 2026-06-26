# Addict Kite School — Design Brief

Project direction for the Addict redesign. Read after `projects/websites/design.md`
(global taste) and alongside `content.md` (verified facts) before building.

## North Star

Make a visitor feel the bright, high-energy rush of a Tarifa kite session in the
first second: turquoise water, blue sky, real instruction, a crew that has fun
and looks after you. The site must sell lessons (pre-book a course, save -10%)
and carry the brand's own idea: kitesurfing gets in your head, you become ADDICT.
Primary actions: Pre-book (WhatsApp / form) and See prices.

## Vibe Lane

**Bright outdoor-action editorial.** Full-bleed daylight action photography,
big confident display type, generous air, practical course/price/spot detail laid
out like a clean sport brochure. Energetic and a little playful (the "addict"
concept), never moody or romantic.

This is a deliberate separation from the sibling **FreeYourMind** Tarifa build,
which is warm espresso/sand + sunset coral + Fraunces serif, romantic/holistic,
"no wind no pay." Addict must NOT borrow that. Addict is **cool, bright, sporty,
graphic**: blue + orange brand color over turquoise water, a bold grotesque (not
a serif), and a punchier rhythm. If a section starts feeling warm-cream and
romantic, it has drifted into FyM's lane — pull it back to bright and sporty.

Bright daylight imagery carries the palette on purpose (global design.md allows
this for outdoor): do not over-filter the photos into darkness.

## Brand

Two real brand colors, from the logo (orange kitesurfer in a gray head, blue
dashed ring). Treat orange as the action/accent, blue as the ocean/structure
tone, graphite as ink. Disciplined, not a rainbow.

- Orange (primary accent / CTAs): `#F26522`
- Ocean blue (secondary / deep section bands): `#1693C6`, deep `#0E5C82`
- Graphite ink (the head gray, near-black text): `#23282B`
- Light: clean cool white / sky `#FFFFFF` and `#EEF4F8` (cool off-white, NOT
  cream — cream belongs to FyM)
- Turquoise comes from the photography itself, not as a flat fill.

Type (bold grotesque, no serif — serif is FyM's):

- Display / headlines: **Archivo** (heavy + expanded grades) for confident,
  athletic poster headlines that echo the bold "ADDICT" wordmark.
- Body / UI: **Hanken Grotesk** (warm, readable grotesque, not Inter).
- Figures / labels: **Space Mono** for prices, durations, hours, knots, levels,
  small uppercase labels — the technical "conditions" texture a kite school earns.

Logo: their real mark, `assets/web/brand/logo.png` (stacked) and
`logo-banner.png`. Favicon `assets/web/brand/favicon.png`. Wordmark rule: no
added punctuation; "ADDICT" can be set in caps because the real wordmark is caps.

Voice: plain, direct, friendly, a little playful. No marketing taglines, no
dashes as punctuation. Lift their real phrases: "Become ADDICT to kitesurfing",
"more than a school, a true kite family", "your safety is our priority", "every
student has a kite". Headings stay plain labels (Courses, The spot, Reviews,
Stay, Book) — never a sentence, even their own.

## Audience

1. First-time / beginner travellers who want a safe, fun, well-run way into
   kitesurfing on holiday (small groups, all gear, certified instructors).
2. Improvers / autonomous riders who want semi-private/private coaching with
   radio helmet, or just gear rental.
3. Trip-planners who want the whole package: lessons + studio/kite-house stay.

## Page Architecture

Start with a strong single homepage (this build). Inner pages can follow if
approved: Courses, Stay, Tarifa, Team, Contact. Standing action on every surface:
Pre-book (-10%).

Homepage flow (draft):
hero (full-bleed turquoise rider, logo + "Kitesurfing school in Tarifa", two
CTAs + a small "366 reviews · 99% 5-star · OLK certified" proof line) → who we
are / kite family (bright band, 10 years, small groups, the Romain quote as a
pull-quote) → Courses (the real decision: Group / Semi-private / Private, with
max students, kites, radio, from-price in mono) → The spot / Tarifa (wide
establishing photo, why Tarifa, what's included strip) → Reviews + accolades
(366 / 99% / OLK, two real TripAdvisor quotes) → Stay (studios, Kite House,
wellness — compact) → full-bleed pre-book CTA → designed footer (contact,
languages, socials).

## Asset Strategy

Their own redesign, so their own photos are fine (confirm before live launch).
Use the curated `assets/web/photos/site/` set, distinct image per role:

- `hero-rider.jpg` — hero (rider carving on turquoise water; set object-position
  so the whole rider stays in frame).
- `tarifa-spot.jpg` — The spot (wide beach, kites, mountains + wind turbines).
- `lessons.jpg` — Courses / beginners (beach briefing, red Eleveight kite).
- `coaching.jpg` — semi-private/private (instructor radioing out to sea).
- `team-care.jpg` — kite family / who we are (smiling rider sorting lines).
- `setup.jpg` — included/gear note (rigging an ORANGE kite — on-brand color tie).

Instagram pull (`assets/web/photos/instagram/`) is backup / gallery only. Brand
files in `assets/web/brand/`. Do not hotlink; everything local. Mark any
placeholder for replacement before launch.

## Do / Avoid

Do:

- Keep it bright, cool, and sporty. Let the turquoise/blue photography lead.
- Orange for action only (CTAs, key numbers); blue for structure; graphite ink.
- Use mono for every figure (prices, hours, knots, review count).
- Lean lightly on the "in your head / become addict" idea where it's tasteful.

Avoid:

- Cream/sand/coral warmth or serif display (that is FreeYourMind, not Addict).
- Sentence headings or invented taglines.
- Dark moody over-filtered photos. Soft drop-shadow cards. Rounded pill UI.
- Repeating the FyM section rhythm beat-for-beat.

## Iteration Notes (running log, newest first)

### 2026-06-23 — Brand study + first homepage build

- Studied the real business (live site, prices, team) before building. Brand is
  bright blue + orange, energetic, "kite family", 10+ years, Los Lances Beach.
- Chose bright outdoor-action editorial lane, explicitly differentiated from
  FreeYourMind's warm serif lane per Annabel's instruction.
- Building homepage first for review.
