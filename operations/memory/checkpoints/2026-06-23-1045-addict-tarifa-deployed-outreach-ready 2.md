---
date: 2026-06-23
time: 10:45
project: websites / addict-kiteschool-tarifa
status: DONE — brand-true homepage built, WhatsApp surfaced in top nav, DEPLOYED live & public to https://addict-kiteschool-tarifa.vercel.app, and an outreach blurb drafted in Annabel's voice. Ready for Annabel to send. Not yet approved by the client.
next-session: Annabel sends the WhatsApp/email pitch with the live link. If they bite, build inner pages (Courses, Stay, Tarifa, Team, Contact) in the same system and resolve the confirm-before-launch list. Optional: floating WhatsApp bubble, custom domain/cleaner alias.
supersedes: 2026-06-23-0955-addict-tarifa-brand-true-homepage.md
---

# Session: Addict Kite School — homepage built, deployed, outreach ready

Picked up the Addict site where the prior session crashed (API error right before
writing docs + building). This session: studied the real business, built the
homepage brand-true (not the FyM lane), added WhatsApp to the top nav, deployed
to Vercel, and drafted the sales blurb.

## Brand-true build (≠ FreeYourMind, per Annabel's instruction)

Studied real sources first: scraped `addictkiteschool.com` (home, prices, team),
read the logo + all 6 curated photos, and re-read FyM's design.md to differentiate.

- FyM = warm espresso/coral + Fraunces serif, romantic/holistic.
- **Addict = bright outdoor-action editorial**: cool/sporty/graphic. Orange +
  ocean blue + graphite (straight from the logo: orange kitesurfer in a gray
  head, blue dashed ring). Archivo display + Hanken Grotesk body + Space Mono
  figures. Bright turquoise photography leads. Documented the separation in
  design.md so it can't drift back.

`index.html` (single page, inline CSS, local assets): hero (full-bleed rider,
"Kitesurfing in TARIFA", 366/99%/OLK proof strip) → kite family (10+/7/3 +
Romain pull-quote) → Courses (3-card decision, middle highlighted, mono prices,
includes-strip) → Why Tarifa (blue ocean overlay, 3 facts) → Reviews (score
strip + 3 real TripAdvisor quotes) → Stay (4 items) → Pre-book CTA (over the
orange-kite photo) → dark footer. content.md + design.md filled from scraped
facts with [verified]/[recheck]/[unconfirmed] tags.

## Sources (answered Annabel's question)

- Images: all THEIR OWN, local. Logo/banner/favicon from their site; the 6 page
  photos curated from their Instagram pull (`@addict_kiteschool`, gallery-dl).
- Wording: scraped from their live site (facts, prices, team, reviews are real
  TripAdvisor quotes). No invented taglines.

## Ship Gate run (hook-enforced)

All 9 items pass. Fixed one violation found in the gate: `<title>` had an
em-dash → changed to a middot. Also fixed two responsive bugs caught in-browser
earlier (mobile menu missing base `display:none`; footer 3-col grid + hero h1
overflow on mobile). Verified desktop 1440 + mobile 375, console clean, no
horizontal overflow.

## WhatsApp surfaced (Annabel's request)

Added a recognizable green (#25D366) WhatsApp button with the WA glyph to the
**top nav** (next to Pre-book) and to the mobile menu. Links to
`wa.me/34691288784` (+34 691 288 784). Already present in the Book CTA + footer
too. Verified desktop + mobile.

## Deployed

`vercel --prod --yes` from the project dir. Live, PUBLIC (no login wall, 200):
**https://addict-kiteschool-tarifa.vercel.app**. Added `.vercelignore`
(content.md, design.md, assets/web/photos/instagram) so internal docs + unused
backup don't ship (confirmed they 404). Local preview: `addict-tarifa` server,
port 8857.

## Outreach blurb (drafted, in Annabel's voice, no dashes)

Angle differs from FyM: Addict's site WORKS, so no fabricated bad-booking story.
Honest angle = the MISMATCH (excellent school, 366 reviews/99% 5-star, but a
generic WordPress template site that doesn't show it). Recommended + shorter
versions written; lead with the reviews praise, then "I rebuilt your home page
as an example with your own photos and info in your own orange and blue," then
low-pressure two-path close (build out the full site, or clean up current one).
Link to paste: the Vercel URL above. Told Annabel NOT to claim a personal
booking experience unless true; flagged unconfirmed facts (address, 2026 prices)
are fine for a sample.

## Confirm-before-launch list (from content.md)

Exact studio address; recheck 2026 prices + TripAdvisor count; photo-use
permission; whether Eleveight is an actual sponsor vs just gear shown.
