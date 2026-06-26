---
date: 2026-06-21
time: 13:41
project: websites / freeyourmind-tarifa
status: in-progress (full site built — homepage + all 5 inner pages, verified; pre-launch fact/permission confirms still pending)
next-session: Pre-launch confirms with the client before going live (see "Open / pre-launch"). Optional polish: muted reel as a hero background loop (25 reels in assets/web/photos/instagram/); per-accommodation photos once the real current list is confirmed. Then the rebuild-into-platform / proposal step if Annabel wants it.
supersedes: 2026-06-20-1521-freeyourmind-tarifa-instagram-pull-real-copy.md
---

# Session: Free your Mind — all inner pages built (Courses, Offers, Stay, Tarifa, Contact)

## What this session resolved

Picked up from the homepage-only state. The whole site now exists: homepage plus
the 5 inner pages, all in the warm-cinematic lane, all using the client's REAL
copy (pulled fresh from their live site), all verified in the browser.

## 1. Shared CSS/JS refactor (so pages can't drift)

- Extracted the homepage's inline `<style>` into `assets/web/styles.css` and the
  inline script into `assets/web/site.js`. Every page (incl. index.html) now
  links both. Tokens are byte-for-byte the same as the approved homepage.
- Rewired the homepage: nav + footer + offering cards now point at the new
  internal pages (no more links to the old Jimdo `kitesurf-tarifa-spain.com`).
- Homepage re-verified: renders pixel-identical after the refactor, 0 console
  errors. Nav IA now real: Home · Courses · Offers · Stay · Tarifa · Contact.
- Inner pages use `body.solid-nav` (solid top bar from the top) + `.page-hero`
  (compact ~62svh hero). New reusable components in styles.css: `.split`
  (alternating image/text rows), `.lodge` (accommodation list), `.chips`
  (activity tags), `.info-grid` + `.map` (contact).

## 2. The 5 inner pages (real copy, scraped via Firecrawl 2026-06-21)

- **courses.html** — "Small groups, real progress" intro (taught EN/DE/FR/ES,
  instructors IKO·VDWS·FAV, 2–4 per group, equipment/insurance/safety boats
  included) + 7 alternating `.split` rows: Beginner, Advanced, Private, Girls,
  Camps, Rental & equipment, Supervision. Prices route to WhatsApp.
- **offers.html** — 5 `.split` offers: Kite & Yoga (3 days kite + 3 days yoga +
  pranayama), Kite camps Tarifa, Morocco camps, Surf courses, Kite & Spanish
  (with Pamela Schulz, IH-certified) + tailor-made/group note.
- **stay.html** — `.lodge` list of the 5 accommodations with real descriptions
  (La Vega, La Residencia Puerto SPA, La Residencia Apartments have full real
  copy; Kite Villa + Valdevaqueros use short factual lines).
- **tarifa.html** — destination page: "why Tarifa" intro, "Costa de la Luz"
  chapter band, "When there is no wind" activity chips (yoga, surf, wakeboard,
  SUP, horse riding, BBQ, old town/chiringuitos, Andalucía trips).
- **contact.html** — `.info-grid` (WhatsApp +34 669 261 678, email, address,
  open all year, IG @free_your_mind_experience, FB fym.experience) + keyless
  OpenStreetMap embed centred on Tarifa.

Held the no-invented-headings rule throughout: headings are their words or plain
labels. No fabricated taglines.

## 3. Verification

- Preview server `fym-tarifa` on :8849 (launch.json). The Claude preview
  screenshot tool IGNORES live scroll and fires before images decode → blank
  shots. Working recipe: set a tall viewport (e.g. 1280x2000), force reveals
  visible (`.reveal.add('in')`), `await img.decode()`, optionally
  `display:none` the sections above the part you want, then screenshot.
  (`img.decode()` can hang when the OSM iframe is loading — drop the await then.)
- All pages: correct active nav, shared CSS applied, 0 broken images. Visually
  confirmed courses (hero + split rows), contact (team-photo hero + info grid),
  stay (lodge list), tarifa (intro + foil chapter band). Homepage unchanged.

## Open / pre-launch (confirm with client before live) — logged in content.md

- **Prices:** live site shows camps "from €890", Morocco "from €990" but it's the
  old Jimdo site (2018–2022). Kept OFF the new pages (route to WhatsApp). Confirm
  current prices before adding any.
- **Accommodation drift:** homepage + stay.html list the 5 from the live nav, but
  the live accommodation page BODY now shows **Casa Arcos Tarifa** instead of the
  Kite Villa + Valdevaqueros. Confirm the real current list.
- **Certs / reviewer permission (still open from prior checkpoint):** confirm
  IKO/VDWS current; get reviewer permission before quoting TripAdvisor reviews.
- **Team roles:** Tanja Rosenkranz is founder (8+ yrs, competitive background);
  recheck Max + Carole roles.

## Files

- New: courses.html, offers.html, stay.html, tarifa.html, contact.html,
  assets/web/styles.css, assets/web/site.js.
- Edited: index.html (links shared CSS/JS, internal links), content.md (inner-page
  facts + pre-launch confirms), design.md (page architecture + 2026-06-21 log).
- Kept: instagram-picksheet.html, build_picksheet.py, photos as before.
