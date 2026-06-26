---
date: 2026-06-21
time: 15:40
project: websites / freeyourmind-tarifa
status: in-progress (site polished + QA'd + mobile nav added; outreach message ready; competitor/site research done. NEXT: Annabel sends the WhatsApp pitch and converts/deploys the sample to a real link)
next-session: Deploy the sample site to a real URL (Vercel or Netlify) so Annabel has a clickable link to paste into the WhatsApp message, then she sends it. Pre-launch content confirms still open (prices, accommodation list, certs, reviewer permission, old email domain).
supersedes: 2026-06-21-1341-freeyourmind-tarifa-inner-pages-built.md
---

# Session: Free your Mind — polish + QA + mobile nav + outreach pitch + 3-site discovery

Two threads this session: (1) a round of polish + QA on the sample site Annabel
built, and (2) prep for Annabel to pitch herself to the real business over
WhatsApp, which turned up a significant finding about the client's actual web
setup.

## 1. Site polish (all on homepage unless noted, verified in browser)

- **Hero "zoom out":** the surfer was cropped to legs only. Added
  `object-position: center 18%` to `.hero-media img` so the whole rider (head,
  bar, body, board, sun) is in frame. Tuned live (30/42% worse, 18% best).
- **Nav floats:** removed the divider line under the top bar
  (`.topbar` `border-bottom` → `transparent`).
- **Kitesurf band de-blurred:** swapped the soft reel-frame `action-1.jpg` for a
  sharp wing-foil photo (`instagram/3821376578803076949.jpg`, 1440×1774).
- **Morocco band reshot:** dropped the weak backpack-walker for
  `raw/tarifa-30.jpg` (mountains + coast + turquoise water + rider), watermark
  cropped, `object-position: center 72%`. Originals backed up in
  `assets/web/photos/_pre-imgfix-backup/`.
- **Offerings cards aligned:** the 4 `.card` numbers/headings/CTAs sat at
  different heights (bottom-anchored blocks, unequal copy). Reserved
  `.card p { min-height: 6em }` (reset to 0 ≤560px) so all four line up; tightened
  the "Kite & yoga" blurb (the long outlier). Verified aligned at 1280 + 1440.
- **"No wind, no pay" demoted:** Annabel found the full-width animated coral
  marquee too prominent. Removed it from all 4 pages it was on; replaced with a
  small static `.promise` pill under the hero/page-hero CTAs. Then she asked to
  **remove the ✦ star** — done (pill now plain "No wind, no pay · full refund,
  every time"). Removed the unused `.promise b` rule.
- **Reviews → scrolling marquee (Freeride-style):** replaced the static 2×2
  `.review-grid` with a full-bleed `.marquee` (track `translateX(0→-50%)` 60s,
  4 real cards duplicated for a seamless loop, hover-pause, `mask-image` edge
  fade, reduced-motion → manual scroll). Cards use `margin-right` not flex gap so
  -50% loops perfectly; `align-items:stretch` keeps equal height. Only the 4
  existing real TripAdvisor quotes are used.
- **Removed "#3 of 27 in Tarifa"** from the reviews badge (now just "350 reviews").

## 2. Mobile navigation added (real bug found in QA)

QA found there was **no mobile nav**: below 860px the links were `display:none`
with no hamburger, so phone/tablet visitors could only reach Home + WhatsApp.
Added a "Menu"/"Close" text toggle (`.nav-toggle`) on all 6 pages → full-width
cream dropdown panel; handler in `site.js` (click, link-click-closes, Escape,
auto-close on widen). Gotcha: the fixed panel collapsed to its grid cell until
`grid-column: 1 / -1; justify-self: stretch` forced it full-viewport. Verified
mobile + tablet + no desktop regression.

## 3. Full QA pass (otherwise clean)

All 6 pages: 0 broken images, 0 console errors, all internal links + same/cross-
page anchors resolve, contact details consistent everywhere, no horizontal
overflow, split/lodge/info-grid/card layouts stack on mobile, contact OSM map
renders. Mobile nav was the only real defect (fixed).

## 4. Outreach prep — Annabel pitching herself to the business

Annabel was in Tarifa, landed on their site, found images/videos down + broken
links, and **booked with someone else**. She wants to WhatsApp them, send her
sample site, and offer to redesign theirs. Drafted the message in her plain
voice (no dashes, no marketing-speak). Final angle reframed after the research
below.

## 5. KEY FINDING — the business runs THREE websites

Investigated `kitesurf-tarifa-spain.com` (their domain, from the email):

| Site | Lang | Platform | State |
|---|---|---|---|
| kitesurf-tarifa-spain.com | EN only | **Jimdo Creator** (legacy, being wound down) + Cloudflare | The broken one Annabel landed on |
| kiteschule-tarifa.de | DE only | **Jimdo Creator** | German-market site |
| **freeyourmindexperience.com** | **EN/ES/DE/FR** | **WordPress** (Elementor + WooCommerce) | Newer, modern, multilingual |

The "second/Spanish site" Annabel half-remembered = freeyourmindexperience.com
(has `/es/`). Reviewed it: **functional but generic Elementor** — disjointed
hero ("Welcome to / Free Your Mind / Experience" scattered), plain type, yellow
pill buttons, ✔️-emoji bullets, cluttered with cookie+chat+WhatsApp overlays,
4–8 JS console errors, ~3 broken images, English homepage has a **Spanish title
tag**. BUT it **does list real prices** (Private 1-on-1 140€, 10h Pack 700€,
wingfoiling…) and is complete.

**Strategic point:** the prices/info DO exist, just on the newer site — Annabel
hit the OLD broken Jimdo site, which is still live and findable and leaking
bookings. So her pitch reframed to: (a) quick win = redirect the old broken
Jimdo sites to the real one so nobody hits a dead page; (b) bigger win = upgrade
the generic main site (her sample demonstrates the craft level) + fix broken
images / console errors / SEO title mess. Final WhatsApp draft names
freeyourmindexperience.com and the old-broken-site problem (honest, shows
homework).

## NEXT

- **Deploy the sample to a real link** (Vercel/Netlify) so the WhatsApp message
  has a clickable URL. Annabel said she'll "send this and convert my site in a
  bit" — she may deploy herself or want help.
- Pre-launch confirms unchanged: camp/Morocco prices kept off (route to
  WhatsApp), accommodation list drift (Casa Arcos), IKO/VDWS currency, reviewer
  permission, contact email still on old `kitesurf-tarifa-spain.com` domain.
- Files touched: index/courses/offers/stay/tarifa/contact.html, styles.css,
  site.js, design.md (project + global, with the new Image Handling + Ship Gate
  + "don't shout fine-print" + scrolling-reviews log entries).
