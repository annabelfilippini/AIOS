# Project Brief Generator

This is the procedure that turns a target website into a project-specific
`design.md`. It is the missing layer between Annabel's taste library
(`projects/websites/design.md`) and any single project brief.

Read this when you are asked to design or reconstruct a new website. Follow the
steps in order, then write the output using `brief-template.md`.

> Built next to the Freeride brief, but written to be reusable. Once proven,
> this and `brief-template.md` can be promoted to `projects/websites/` so every
> site uses them.

## The One Rule That Makes Briefs Work

Every design instruction must name a **mechanic or behavior**, never a feeling.

- WRONG: "Dramatic hero like Mathieu Crepel."
- RIGHT: "Full-viewport hero video, autoplays muted on load, single two-word
  headline bottom-left in oversized type, nav collapses to one menu dot
  top-right, video darkens 30% on scroll as the next section rises over it."

A feeling is not executable. A mechanic is. When the brief feels vague, it is
almost always because a section described a vibe instead of a behavior. Go back
and name the behavior.

## Inputs To Gather First

If any are missing, ask before generating:

1. Target site URL(s) and what the business actually does.
2. What the client (or Annabel) dislikes about the current site.
3. Primary conversion action (booking, inquiry, WhatsApp, purchase, signup).
4. Reconstruction level wanted, or enough to infer it (full / partial / light).
5. Asset sources: their Instagram handle, existing photos, logo, any Drive.

## Step 1 — Audit The Existing Site

- Capture the current site: structure, page list, navigation, copy, real assets.
- List what works (candidates to preserve) and what fails (must replace).
- Inventory real first-party assets: photos, video, logo, brand colors, fonts.
- Find the business's strongest latent content. For visual/experiential
  businesses this is usually Instagram, and it is almost always better than what
  is on the current site. Name it explicitly.

## Step 2 — Classify The Business And Pick One Vibe Lane

From the lanes in `projects/websites/design.md`, choose exactly one dominant
lane and state why:

- Soft editorial / luxury — health, wellness, hospitality, retreats, personal
  brands, florists, boutique services, trust-led clients.
- Experimental black / poster — nightlife, culture, fashion, music, edgy retail,
  creative studios, drops, bolder-voice brands.
- Outdoor editorial / travel — travel, adventures, itineraries, outdoor brands,
  place-based guides.
- Kinetic documentary / person — athletes, makers, adventurers, personal
  archives.

Pick ONE. Name the few secondary ingredients you will borrow from other lanes.
Never blend two full lanes on one client site without a clear brand reason.

## Step 3 — Set The Reconstruction Level

State explicitly what is preserved and what is rebuilt.

- Full (e.g. Vital Health) — rebuild IA, copy, and visual system from scratch.
- Partial (e.g. Free Ride) — keep the core offers and structure, transform the
  presentation, asset strategy, and emotional pitch.
- Light (e.g. Cooldown) — preserve most of the site, targeted upgrades to hero,
  type, imagery, and a few key sections.

## Step 4 — Define The Emotional Target

Three to five concrete adjectives describing the feeling in the first five
seconds. These become the tie-breaker for every later decision.

## Step 5 — Choose References And Translate Them

For each reference site, write three blocks. The "Translate" and "Avoid" blocks
are what stop the brief from producing a copy of the reference.

- **Take** — the specific mechanics worth stealing (hero behavior, type scale,
  motion, section rhythm). Mechanics, not vibes.
- **Translate** — how each mechanic becomes this business's content.
- **Avoid** — what NOT to borrow from this reference (tone, modules, claims that
  do not fit this business).

## Step 6 — Asset Strategy

- Map real assets to the roles they will fill on the page.
- Identify gaps. For each gap decide: Instagram scrape, client request, or
  generation.
- Asset rules: real footage for action and people; generation only for
  atmosphere and texture (light, grain, abstract water, transitions). Generated
  action shots and generated people read as fake fast.
- Write the concrete client asset request list (the files to ask for over
  WhatsApp/email before a production handoff).

## Step 7 — Page Architecture

For each page, give it a one-line **job**, then a section-by-section scroll flow
where every section also has a job (not just a name). This is the narrative the
page tells top to bottom. Keep top-level user choices as separate pages when
they are genuinely separate decisions.

## Step 8 — Visual System

Specialize the general taste file for this project: shape language, palette
(base + accents drawn from real photography), type system (display + body),
and layout rhythm (where it goes dark/cinematic vs pale/clear). Inherit defaults
from `design.md`; only restate what is specific to this site.

## Step 9 — Copy Direction

- Voice in one line.
- 3-5 "Good" example lines written in the business's real language.
- "Avoid" list of generic adventure/SaaS filler.
- No dashes as punctuation (Annabel's rule): use commas, periods, separate
  sentences.
- Fact-check rule: verify prices, certifications, locations, names, dates, and
  contact details before they become design copy.

## Step 10 — Conversion And Success Criteria

- Name the primary action and exactly where its CTAs live across the scroll.
- Write 4-6 success criteria: what makes this rebuild objectively better than
  the current site and better than competitors in the same category.

## Output

Write the result to `projects/websites/<project>/design.md` using
`brief-template.md`. Always read `projects/websites/design.md` first; the
project brief specializes and overrides it only where stated.

## Anti-Patterns The Generator Must Avoid

- Feeling-words with no mechanic ("make it dramatic", "clean and modern").
- Blending two full vibe lanes on one client site.
- Reusing the same module rhythm by habit (the four-item fact strip, identical
  numbered step cards, the same cream image grid on every site).
- Copying a reference wholesale instead of translating it.
- Treating assumptions about the business as facts. Verify, or mark as an open
  question for the client.
