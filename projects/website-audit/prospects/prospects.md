# Prospects

> **Source of truth** for the website-audit pipeline. Claude reads and writes this file. Annabel edits freely — if a row changes, tell Claude so it stays in sync with any per-prospect folders.
>
> **Last updated:** 2026-04-14

---

## Pipeline summary

- **Total prospects:** 13
- **Sent:** 1 (Pepper Pong)
- **Queued:** 12
  - High confidence: 4
  - Medium confidence: 5
  - Low confidence: 3

---

## ✅ Sent

| Company | Website | City | Vertical | Contact | Sent Date | Video | Portal |
|---|---|---|---|---|---|---|---|
| Pepper Pong | [pepperpong.com](https://pepperpong.com) | Ann Arbor | Athletic | Tom Filippini (Founder) — *family, via Drive share* | 2026-04-14 | [Drive](https://drive.google.com/file/d/1xPsyZOuOcYMSiu0qxKSqQ-Sr6riLfwSn/view) | [Portal](https://pepper-pong-audit.vercel.app) |

---

## 🟢 Queued — High Confidence

*Verified contact info. Ready to send after audit.*

### Adelitas Cocina y Cantina ⭐ *Top pick for prospect #2*
- **Website:** https://adelitasco.com/
- **City / Vertical:** Denver / Restaurant
- **Contact:** Silvia Andaya, Owner/Executive Chef
- **Email:** info@adelitasco.com
- **Audit hook:** Broken **Reserve Now** button, lingering COVID-era content, malformed gift-card URL params, no mobile menu, dated layout
- **Bonus:** Silvia also owns **La Doña Mezcaleria** — natural two-fer pitch
- **Source:** [ShoutoutColorado interview](https://shoutoutcolorado.com/meet-silvia-andaya-owner-and-executive-chef-adelitas-cocina-y-cantina-la-dona-mezcaleria/)

### Frita Batidos (Ann Arbor)
- **Website:** https://fritabatidos.com/ann-arbor/
- **City / Vertical:** Ann Arbor / Restaurant
- **Contact:** Eve Aronoff Fernandez, Chef/Owner
- **Email:** eve@evefrita.com
- **Audit hook:** Homepage hides hours, address, and phone. "Best Burger 2014–2025" banner is prominent but has **no schema markup** so Google doesn't surface it.
- **Source:** [wanderingglutton interview](https://fritabatidos.com/ann-arbor/chef/)

### Hop Alley
- **Website:** https://hopalleydenver.com/
- **City / Vertical:** Denver / Restaurant
- **Contact:** Tommy Lee, Chef/Owner
- **Email:** info@hopalleydenver.com *(generic inbox — high confidence)*
- **Audit hook:** Michelin + James Beard awards front-and-center but **zero schema markup** → Google doesn't surface them. Reservations bounce to external Tock. No chef-story / concept page.
- **Source:** [Denver Office of Storytelling, 303 Magazine](https://hopalleydenver.com/)

### Wolverine Pickleball
- **Website:** https://wolverinepickleball.com/
- **City / Vertical:** Ann Arbor / Athletic
- **Contact:** Christy Howden & Leslie White, Co-Founders
- **Email:** hello@wolverinepickleball.com
- **Audit hook:** UX fragmentation — reservations bounce users off-site to CourtReserve and PickleballClubs.com. Minimal meta/structured data. No unified mobile booking flow.
- **Source:** [A2 Observer feature](https://wolverinepickleball.com/)

---

## 🟡 Queued — Medium Confidence

*Mix of verified generic inboxes and plausible personal emails. Send with a quick deliverability check.*

### Miss Kim
- **Website:** https://misskimannarbor.com/
- **City / Vertical:** Ann Arbor / Restaurant
- **Contact:** Ji Hye Kim, Chef/Owner
- **Email:** hello@misskimannarbor.com
- **Audit hook:** JBF-nominated chef; new sister concept **Little Kim** not linked from homepage; press page is text-heavy with no logos; no reservation integration above the fold.
- **Note:** Part of Zingerman's ZCoB — ask who owns the website.

### Cayman Sports
- **Website:** https://www.caymansports.com/pickleball/
- **City / Vertical:** Ann Arbor / Athletic
- **Contact:** Bridget He, Owner
- **Email:** info@caymansports.com *(generic fallback — no personal email published)*
- **Audit hook:** Opened Dec 2025 — many "Out of stock" product cards, truncated product descriptions, no founder/about content yet.

### Pactimo
- **Website:** https://www.pactimo.com/
- **City / Vertical:** Denver / Athletic
- **Contact:** Clint Bolton, Founder/CEO
- **Email:** hello@pactimo.com *(verified)* — personal pattern guess: clint@pactimo.com
- **Audit hook:** Cycling apparel veteran (est. 2003). Heavy/slow site, large hero carousels, complex custom-kit config flow confuses first-time buyers. Solid checkout-funnel audit target.

### REEB Cycles
- **Website:** https://reebcycles.com/
- **City / Vertical:** Longmont / Denver metro / Athletic
- **Contact:** Adam Protextor, Co-Founder
- **Email:** info@reebcycles.com *(generic inbox)*
- **Audit hook:** Handcrafted bikes. Product pages read as spec sheets — no size-fit calculator, no video embeds. Gravel category (Sam's Pants) buried in main nav.

### Pacific Rim by Kana
- **Website:** https://pacificrimbykana.com/
- **City / Vertical:** Ann Arbor / Restaurant
- **Contact:** Duc Tang, Owner/Executive Chef
- **Email:** ❌ **none published — phone only**
- **Audit hook:** Phone-only contact. Menu one click away from homepage. Image-heavy slider with no lazy loading. Tock integrated but no online ordering.
- **Note:** If reaching out, may need DM / walk-in / phone instead of email.

---

## 🔴 Queued — Low Confidence

*Pattern-guessed emails or no named founder. Verify before sending.*

### Ann Arbor Running Company
- **Website:** https://www.annarborrunningcompany.com/
- **City / Vertical:** Ann Arbor / Athletic
- **Contact:** Nick Stanko & Ian Forgings, Co-Founders
- **Email:** ⚠️ `nick@annarborrunningcompany.com` — *pattern-guess only, not verified*
- **Audit hook:** Three locations, no email anywhere on site. "Shoe School" is a huge brand story buried on the about page. No run-club event schema / local SEO for "running store near me."

### Spencer (Ann Arbor)
- **Website:** https://spencerannarbor.com/
- **City / Vertical:** Ann Arbor / Restaurant
- **Contact:** Abby Olitzky & Steve Hall, Chef/Owner & FOH Owner
- **Email:** ⚠️ `hello@spencerannarbor.com` — *pattern-guess only, not verified*
- **Audit hook:** Counter-serve + communal seating concept is hard to explain. Landing page fails to set expectations → 1-star "confused about how this works" reviews. Low SEO for "Ann Arbor wine bar."

### Pickle for the People
- **Website:** https://pickleforthepeople.co/
- **City / Vertical:** Denver / Athletic
- **Contact:** ❌ **no named founder** — contact form only
- **Email:** none published
- **Audit hook:** Brand-first site with no founder name, no contact email, unoptimized 1024px hero images, story page links to `/collections/all` with minimal product-detail depth.
- **Note:** Route through contact form only if we commit to this one.

---

## Do-not-contact / Removed

*Ruled out during research.*

- **Vander Jacket** (Denver) — closing May 31, 2026, fire-sale banner everywhere
- **ACE Pickleball** — polished global ecommerce op with 150+ country localization, out of scope
- **Great Lakes Cycling** (Ann Arbor) — closed
- **Two Wheel Tango** (Ann Arbor) — closed
- **Safta** — part of Pomegranate Hospitality multi-city group
- **Cooldown Running** — already a prospect (separate warm lead from Apr 9)

---

## Dry subverticals (noted)

- **Ann Arbor cycling shops** — both major shops closed; don't chase locally.
