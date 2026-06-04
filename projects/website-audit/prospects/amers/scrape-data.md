# Scrape Data — Amer's Deli

**Scraped:** 2026-04-20
**Mode:** `AUDIT_REDESIGN_ONLY=1` (redesign path — skipped SEO/analyze; just collected the redesign prereqs)
**URL:** https://www.amersdeli.com/
**CMS:** PopMenu (confirmed via `popmenucloud.com` asset domain throughout homepage)

## Prospect — pages scraped

| Page | Status | Markdown chars | Desktop shot | Mobile shot |
|---|---|---|---|---|
| homepage | ok | 6,185 | ✓ | ✓ |

Sibling pages (Menu, About, Directions) skipped per redesign-only policy — PopMenu sibling pages typically return reCAPTCHA stubs (Miss Kim Apr 19 pattern). All load-bearing facts sourced from homepage + third-party verified-facts sources below.

## Branding — from `branding.json`

- **Colors (current, PopMenu defaults):** primary `#0A4F8A` (blue), secondary `#3C763D` (green), accent `#F04649` (red), background `#333333` (charcoal). Flag-like palette, generic — **do not preserve in redesign.**
- **Fonts (current):** Open Sans (body), Futura PT (heading), Proxima Nova. Also generic PopMenu defaults.
- **Logo asset captured:** `popmenucloud.com/.../31b4fbc1-2b9c-4232-8a79-14b99a50ee31.png` (labeled "Amer's Deli home")
- **Welcome-frog illustration:** `popmenucloud.com/.../42bd4465-06ba-4a54-888c-1d09a21dc9de.png` — hand-drawn frog with "welcome" text. Signature quirk — elevate, don't erase.
- **Personality tag (Firecrawl):** tone=professional, energy=medium, audience=local Ann Arbor.

**Redesign palette direction** (drawn from Landini + deli-heritage references):
- Deep espresso `#2A1D15`, warm ivory `#F3ECDE`, brick-red `#A23A2A` accent, brass `#B08B4F` accent.
- Serif display (Playfair/Canela-family) + grotesque body (Inter / GT America).

## Reference sites scraped

| Brand | Pages | Why |
|---|---|---|
| Landini Brothers (landinibrothers.com) | homepage (menu page weak — 405 chars, skipped) | heritage anchor, dark-band editorial, owner-named block |
| High Street Deli (highstdeli.com) | homepage + menu | counter-service deli voice, named items with prices, illustrated badge system |

Detailed takeaways: `reference/reference-summary.md`.

## Verified-facts sources

| Source | Status | File |
|---|---|---|
| Yelp biz page | ok (42k chars) | facts/yelp-biz.md |
| Yelp search | ok | facts/yelp-search.md |
| Google search (hours/phone) | ok | facts/google-search.md |
| Google locations (AI overview flagged inaccurate) | ok | facts/google-locations.md |
| TripAdvisor reviews | ok (58k chars) | facts/tripadvisor.md |
| The Michigan Daily (Dec 2022 feature) | ok | facts/mich-daily.md |

Canonical facts file: **`facts/verified-facts.md`** — this is what `/audit-redesign` reads.

Key verified identity: 312 S. State St. (also written 314), (734) 761-6000, 8am–10pm daily, owner-on-the-floor, across from the Diag, opened 1988 (Flint) / 1990 (Ann Arbor), "over 30 years in A2" per Michigan Daily.

## Top findings (for redesign, not an audit)

1. **Current site is a PopMenu template with generic colors/fonts.** Zero brand identity in typography or palette. Food photography is strong; everything else is off-the-shelf.
2. **Home page buries the heritage story.** "Since 1988" is in a paragraph four scrolls down, not the hero.
3. **Menu tiles are thumbnail icons** (sandwich, eggwich, frozen yogurt icons) — no actual menu content or prices on the homepage.
4. **The welcome frog is a quirky asset** that the current template treats as a weird decorative blob. Promote it to a mascot/badge role instead.
5. **Mediterranean identity is hidden.** The about copy calls it "Amer's Mediterranean Deli" but the homepage visual says generic American deli. Falafel + tabbouleh + bagels with lox + reuben is an unusually specific cross-menu that deserves editorial treatment.
6. **Owner-and-staff story is the strongest differentiator** per the Michigan Daily feature, but absent from the site.
7. **Sub-brands (Chicago Reds, Yogurt Rush) are under-developed visually** — they could each be a callout block with the right typography.
8. **Ratings mismatch**: Google 4.2 / 443 vs Yelp 3.4 / 212. Lead with Google-side social proof + Michigan Daily press, de-emphasize Yelp.
9. **No Mediterranean photography on the homepage.** Current food shots are Reuben, Chicago dog, yogurt, pastry. No falafel / tabbouleh / bagel-lox — the "Mediterranean Deli" tagline isn't visually supported.
10. **Ordering flow is via PopMenu / Snackpass**, not on-site. External Order CTA is fine, but it should be the hero's secondary CTA.

## Completion gate check

- [x] `branding.json` exists with non-empty colors + fonts (native Firecrawl branding + rawHtml fallback)
- [x] `facts/verified-facts.md` exists with Identity + Hours + ≥3 review quotes + [source:] citations
- [x] `facts/` contains raw source dumps (yelp-biz, yelp-search, google-search, google-locations, tripadvisor, mich-daily)
- [x] `reference/` has 2 subdirectories (landini-brothers, high-street-deli) with scraped content
- [x] `reference/reference-summary.md` written with a block per ref + takeaways + do-not-copy
- [x] `scrape/screenshots/` contains homepage desktop-full + mobile PNGs
- [x] `scrape-data.md` written
- [x] Leakage audit — all assets under `prospects/amers/`; none at project root

**Ready for `/audit-redesign`.**
