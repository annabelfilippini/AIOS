# Pepper Pong — Site Scrape & Data Collection
**URL:** pepperpong.com | **Platform:** Shopify | **Date:** 2026-04-13
**Step 2 of BUILD-PLAN.md — raw data for AI analysis in Step 3**

## Data Sources
- **Firecrawl** (v4.22.1): 8 pages x 3 screenshots each (desktop full, desktop viewport, mobile) + rendered markdown + metadata. Files in `pepper-pong-scrape/`.
- **curl + Python**: Raw HTML parsing for meta tags, structured data, heading hierarchy, image alt audit, third-party script detection.
- **Sitemap crawl**: All 4 child sitemaps (products, pages, collections, blogs).

## Screenshots Index
All at `pepper-pong-scrape/screenshots/`:
| Page | Desktop Full | Desktop Viewport | Mobile |
|------|-------------|-----------------|--------|
| Homepage | homepage-desktop-full.png | homepage-desktop-viewport.png | homepage-mobile.png |
| Product (Full Set) | product-full-set-desktop-full.png | product-full-set-desktop-viewport.png | product-full-set-mobile.png |
| Our Story | our-story-desktop-full.png | our-story-desktop-viewport.png | our-story-mobile.png |
| How to Play | how-to-play-desktop-full.png | how-to-play-desktop-viewport.png | how-to-play-mobile.png |
| Schools | schools-desktop-full.png | schools-desktop-viewport.png | schools-mobile.png |
| Press | press-desktop-full.png | press-desktop-viewport.png | press-mobile.png |
| Reviews | reviews-desktop-full.png | reviews-desktop-viewport.png | reviews-mobile.png |
| FAQ | faq-desktop-full.png | faq-desktop-viewport.png | faq-mobile.png |

---

## Site Overview

- **Company:** Play Everywhere Sports LLC
- **Patent:** #11,786,792
- **Contact:** play@pepperpong.com | (720) 706-8897
- **Product:** Portable tabletop paddle sport ("Pepper Pong")
- **Key claim:** "Shark Tank sensation 2025" / "100,000+ sets sold"
- **Review stats:** 4.95 stars / 211 reviews on homepage (223 on product page) — via Judge.me
- **Shop ID:** 74122068247

---

## 1. Homepage Metadata

| Field | Value |
|-------|-------|
| Title | `Pepper Pong®` |
| Meta Description | "Pepper Pong® — The Shark Tank sensation 2025 portable paddle sport that turns any table into an arena. 100,000+ sold. Whisper quiet. Addictively fun. Sets up in 60 seconds. Free shipping on all bundles." |
| OG Title | `Pepper Pong®` |
| OG Description | Same as meta description |
| OG Image | `http://pepperpong.com/cdn/shop/files/Pepper_Pong_logo.png?v=1732216451` |
| OG Type | website |
| OG URL | `https://pepperpong.com/` |
| Twitter Card | summary_large_image |
| Twitter Image | **MISSING** |
| Canonical | `https://pepperpong.com/` |
| Viewport | `width=device-width,initial-scale=1` |

**Issues:**
- OG image uses HTTP, not HTTPS
- Twitter image tag missing entirely
- Homepage meta description is solid — one of the few pages that has one

---

## 2. Homepage Content Structure

### Heading Hierarchy
```
H1: WORLD'S HOTTEST 🔥 NEW GAME
H2: PEPPER PONG FULL SET
H2: SEE WHY 100,000+ CAN'T SHUT UP ABOUT IT.
H2: EPIC FUN FOR EVERYONE, ANYWHERE
H2: EVERYONE GOES FROM SKEPTIC TO OBSESSED IN ONE RALLY
  H3: "This looks dumb."
  H3: "Ok, one game."
  H3: "1 more best of 7?"
  H3: "I am giving this to every single person i know."
H2: WHERE WILL YOU RALLY?
(Footer)
  H3: Quick Links
  H3: Spicy Newsletter Signup
  H3: Need Help?
H2: Search
  H4: Products
H2: Your Cart
```

**Issues:**
- Heading hierarchy is clean in main content (H1 → H2 → H3) — good
- H2 "Search" and H2 "Your Cart" are used for UI elements (search drawer, cart drawer) — not ideal semantically but common on Shopify

### Sections (top to bottom)
1. **Marquee bar** — red (#ED1846) scrolling banner (press logos: FOX, Yahoo, USA Today, "AS SEEN ON SHARK TANK", "100,000+ SETS SOLD")
2. **Hero** — "WORLD'S HOTTEST 🔥 NEW GAME" + "SHARK-TANK RECORD BREAKER 🥇" + "Any Surface Is Your Center Court."
3. **Product spotlight** — Pepper Pong Full Set with thumbnails (6 images), volume pricing (BOGO 50% off extras)
4. **Social proof** — "SEE WHY 100,000+ CAN'T SHUT UP ABOUT IT." (video testimonials — 21 VideoObject schemas)
5. **Value props** — "EPIC FUN FOR EVERYONE, ANYWHERE" — Spark Joy Build Bonds / Easy to learn / All ages
6. **Conversion journey** — "EVERYONE GOES FROM SKEPTIC TO OBSESSED IN ONE RALLY" — 4-step progression story
7. **UGC/Reviews** — "WHERE WILL YOU RALLY?" — Real people, real tables, real obsession + customer quotes

### Navigation
| Text | URL |
|------|-----|
| HOW TO PLAY | /pages/how-to-play |
| Full Set | /products/pepper-pong-full-set |
| Peppers | /products/pepper-pong-ball-replacements |
| Mullet | /products/mullet-paddle |
| Fence | /products/fence-net |
| OUR STORY | /pages/our-story |
| REVIEWS | /pages/reviews |
| IN THE NEWS | /pages/press |
| FAQ | /pages/frequently-asked-questions |

**Note:** Nav links appear duplicated in HTML (desktop + mobile versions). No "Schools" or "NIRSA" link in main nav — those are only accessible via direct URL.

### Footer
| Section | Links |
|---------|-------|
| Quick Links | HOW TO PLAY, SHOP (→ full set product), OUR STORY, REVIEWS, IN THE NEWS, FAQ |
| Need Help? | Contact us, Read our FAQ's, play@pepperpong.com, (720) 706-8897, Terms of Service, Privacy Policy |
| Newsletter | "Spicy Newsletter Signup" |
| Copyright | © 2026 Play Everywhere Sports LLC · Patent #11,786,792 |

**Issues:**
- No social media links in footer (Instagram, TikTok, YouTube, Facebook — none visible)
- Footer "SHOP" only links to the Full Set, not to /collections/all-products
- "Read our FAQ's" — apostrophe error (should be "FAQs")

---

## 3. Image Audit (Homepage)

**Total images in main:** 38
**Empty alt text:** 5 images
**Missing alt entirely:** 0

| Alt Text | Count | Issue |
|----------|-------|-------|
| "Press logo" | 8 | Generic — should be specific: "FOX News logo", "Yahoo News logo" |
| "FOX" | 2 | OK |
| "Yahoo" | 2 | OK |
| "USA Today" | 2 | OK |
| "AS SEEN ON SHARK TANK" | 2 | Promotional text as alt — should describe the image |
| "100,000+ SETS SOLD" | 2 | Same issue — promotional text, not image description |
| "PEPPER PONG FULL SET" | 1 | OK for product image |
| "Thumbnail 1" through "Thumbnail 6" | 6 | Totally generic — should describe what each thumbnail shows |
| "This looks dumb." / "Ok, one game." etc. | 4 | These are section headings used as alt text for section images |
| (empty alt) | 5 | Decorative images? Or missing alt text? |

---

## 4. Product Catalog (12 products)

| Product | Price | Meta Desc |
|---------|-------|-----------|
| Pepper Pong Full Set | $89.99 | YES |
| Extra Peppers (balls) | $19.95 | YES |
| Extra Mullet (paddle) | $19.95 | YES |
| Extra Fence (net) | $24.95 | YES |
| Extra Spice Sack | $19.99 | YES |
| Extra Sweat Kit "OG Edition" | $19.95 | YES |
| Spicy Solo | $94.99 | YES |
| Double Down (2 sets) | $159.99 | YES |
| Triple Trouble (3 sets) | $229.99 | YES |
| Quad Squad (4 sets) | $277.99 | YES |
| School 8-Pack PLUS (SHAPE) | $599.00 | YES |
| 8-Pack PLUS (NIRSA) | $599.00 | YES |

**Positive:** Every product has a meta description.

### Product Page (Full Set) — Detailed
- **Title:** "Pepper Pong Full Set" (no brand suffix inconsistency — some products add " – Pepper Pong", some don't)
- **Price:** $89.99 (no compare-at price)
- **Meta desc:** Solid, 200+ char description mentioning Shark Tank, setup time, surfaces
- **Reviews:** 4.94 / 5, 223 reviews (Judge.me)
- **Trust badges:** 100,000+ Sets Sold, 60-Day Guarantee, FAST Shipping, Secure Checkout
- **Sections:** What's Inside, The Game That Brings People Together, Quick & Easy Setup, How We Compare, Raving Reviews, QUESTIONS YOUR MOM WOULD ASK (FAQ)
- **Bundle upsell:** "Get 50% OFF Extras" — volume pricing for 2+ units ($36 discount/unit)
- **Structured data:** 21 VideoObject items in ItemList schema

### Product Title Inconsistencies
- `spicy-solo` → title is lowercase "spicy-solo" (slug as title)
- Some titles include "extra" prefix, some don't
- "Extra Sweat Kit - 'OG Edition'" vs "extra Peppers (balls)" — casing inconsistent

---

## 5. Pages Audit (26 pages in sitemap)

### Meta Description Coverage
| Page | Meta Desc? | Notes |
|------|-----------|-------|
| /pages/how-to-play | NO | Key page, needs description |
| /pages/our-story | NO | Key page, needs description |
| /pages/reviews | NO | Key page, needs description |
| /pages/press | NO | Key page, needs description |
| /pages/frequently-asked-questions | NO | Key page, needs description |
| /pages/schools | YES | Good — "Educator Pricing..." |
| /pages/nirsa | NO | Active promo page, needs description |
| /pages/returns | NO | |
| /pages/contact-us | NO | |
| /pages/join | YES | Post-signup confirmation |
| /pages/get-spicy | NO | |
| /pages/pe-playbook | NO | |
| /pages/campus-rec-programming-guide | NO | |
| /pages/reading-reviews | NO | |
| /pages/llms-txt | YES | AI/LLM page — interesting |
| /pages/pdp-draft | NO | **DRAFT page publicly indexed** |
| /pages/lp1 | NO | Landing page, recently updated (Apr 12) |
| /pages/og | YES | First-edition owners page |
| /pages/you | NO | |
| /pages/email-confirmation | NO | **Should NOT be publicly indexed** |
| /pages/pdf-standards | NO | PDF download pages |
| /pages/pdf-rubric | NO | " |
| /pages/pdf-rally | NO | " |
| /pages/pdf-2week | NO | " |
| /pages/pdf-4week | NO | " |
| /pages/pdf-skill-cards | NO | " |

**Summary:** Only 3/26 pages have meta descriptions. 18 of 20 key pages are missing them.

### Suspicious/Problem Pages
1. **`/pages/pdp-draft`** — "PDP Draft" — literally a draft page, publicly accessible and indexed
2. **`/pages/email-confirmation`** — internal confirmation page, should not be indexed
3. **`/pages/lp1`** — "8 Reasons why" — unnamed landing page with a slug that reveals it's a test
4. **`/pages/og`** — "OG" — first-edition owners page, fine to exist but the slug is opaque
5. **`/pages/you`** — "You" — unclear purpose
6. **6 PDF pages** — pdf-standards, pdf-rubric, pdf-rally, pdf-2week, pdf-4week, pdf-skill-cards — all indexed, likely should be noindexed or gated behind the schools flow

---

## 6. Collections Audit (6 collections)

| Collection | Title | Meta Desc? |
|-----------|-------|-----------|
| /collections/frontpage | "Home page" | NO |
| /collections/core-products | "Extra Peppers" | YES |
| /collections/all-products | "All Products" | NO |
| /collections/the-full-set | "The Full Set" | YES |
| /collections/the-bundles | "The Bundles" | YES |
| /collections/keep-the-rally-rolling-replacements-a-la-carte | "Replacements" | YES |

**Issues:**
- "frontpage" collection titled "Home page" — that's confusing (Shopify auto-generates this)
- "core-products" collection titled "Extra Peppers" — misleading title for the collection
- Slug `keep-the-rally-rolling-replacements-a-la-carte` is extremely long

---

## 7. Blog Audit (5 posts + index)

| Post | Title | Date |
|------|-------|------|
| /blogs/news/the-story | Blog 1: Backstory - Tom Announcement (Official) | June 9, 2023 |
| /blogs/news/the-launch | Blog 2: Launch at Pickleball Tournament of the Pros | June 15, 2023 |
| /blogs/news/first-shipments | First Shipments | June 22, 2023 |
| /blogs/news/reviews-and-player-gallery | Reviews and Player Gallery | June 25, 2023 |
| /blogs/news/toms-new-blog-post | Tom's New Blog Post | Jan 9, 2025 |

**Issues:**
- Blog is essentially dead — 4 posts from launch week (June 2023), 1 post 18 months later
- "Tom's New Blog Post" is a terrible title for SEO — generic, not descriptive
- Blog numbering ("Blog 1:", "Blog 2:") in titles is unprofessional for SEO
- No blog content since Jan 2025 — massive missed opportunity given Shark Tank appearance, schools program, 100K+ sales
- The blog index `/blogs/news` hasn't been updated since Jan 2025

---

## 8. Technical Stack & Third-Party Scripts

### Theme
- **Theme:** Custom Shopify theme (Horizon-based)
- **Fonts:** Gotham (headings, 400-900), Inter (body, 400/500/700)
- **Color palette:** Pepper Pong Red (#ED1846), Orange (#FF571A), Navy (#2C5184), Sky Blue (#5AC4F2)
- **Design features:** Glassmorphic cards, liquid gradient buttons, fence grid overlay decorative elements

### Third-Party Integrations
| Service | Purpose | Status |
|---------|---------|--------|
| Judge.me | Product reviews | Active — 4.95 stars, 211+ reviews |
| Klaviyo (ID: Ydxv4T) | Email marketing | Active — newsletter signup in footer |
| Microsoft Clarity | Heatmaps/session recording | Active |
| Triple Pixel | Analytics/attribution | Active |
| hCaptcha | Spam protection | Active |
| Automizely Returns | Returns management | Active |
| Shop Pay / Apple Pay / Google Pay | Payment | Active |

**No Facebook Pixel, Google Analytics/GTM, or TikTok Pixel detected** (unlike Cooldown which had all of these).

### Performance
- Homepage HTML: 377KB (heavy — lots of inline CSS/JS)
- 21 video objects on homepage (heavy media load)
- 30+ theme JavaScript files loaded

### Structured Data
- ItemList schema with 21 VideoObject entries on homepage
- No Organization schema detected
- No BreadcrumbList schema
- No Product schema on homepage (only on PDP via Shopify defaults)
- No FAQ schema on FAQ page

### Security
- SSL: Active (HTTPS)
- hCaptcha: Protecting forms
- robots.txt: Well-configured with explicit anti-bot-checkout statement

---

## 9. Content Deep Dives

### Our Story (/pages/our-story)
**Title:** "Our Story – Pepper Pong" | **Meta Desc:** NONE

Content is powerful — Tom's sobriety story, Pepper Pong born from recovery. Three sections:
1. Personal story of addiction/recovery
2. How the game was born from clarity found in sobriety
3. **Rally 4 Recovery** — donation program for addiction recovery facilities

This is the emotional core of the brand. Missing meta description is a real loss — this page could rank for searches like "Pepper Pong story" or "Pepper Pong founder."

### How to Play (/pages/how-to-play)
**Title:** "Play – Pepper Pong" | **Meta Desc:** NONE

Sections:
- "A LEVEL PLAYING FIELD" — game philosophy (strategic, long rallies, underdogs shine)
- "VIDEO QUICK START GUIDE"
- "Get Latest Rulebook" — downloadable rules
- Detailed game description: "Purposefully engineered to slow the pace, lengthen rallies...highly strategic!"

### Schools (/pages/schools) — Best page on the site
**Title:** "Schools & Educators — Volume Pricing – Pepper Pong" | **Meta Desc:** YES (only content page with one)

Value props: 60-Second Setup, Every Kid Plays, Indoor-Friendly, SEL Built In, Adapted PE Ready
References research on games in PE and social-emotional learning.
Links to PE Playbook, curriculum PDFs, standards alignment.

### NIRSA (/pages/nirsa) — Active promo
**Title:** "NIRSA 2026 — Pepper Pong for Campus Rec" | **Meta Desc:** NONE

Active promotion with discount codes (expires April 30, 2026):
- Sample: $34.99 (normally $89.99) — code 1SAMPLENIRSA26
- 8-Pack: $399 (normally $1,049.80) — code 8PACKNIRSA26
Free Programming Guide included.

**Issue:** Discount codes are publicly visible on an indexed page. Anyone can use them.

### Press (/pages/press)
**Title:** "Press – Pepper Pong" | **Meta Desc:** NONE

Features:
- Shark Tank Season 16 Episode 6 (Nov 22, 2024)
- National/local TV features
- Print coverage
- "PEPPER PONG IS THE 'NEXT PICKLEBALL'" headline
- Firehouse video content
- Live studio appearances

### FAQ (/pages/frequently-asked-questions)
**Title:** "FAQ – Pepper Pong" | **Meta Desc:** NONE

15+ questions covering: game vs ping pong, origin story, name meaning, fence/net, three ball types (Ghost/red=aggressive, Jalapeno/green=casual, middle), mullet paddles, what's in the set, extra gear ordering, table requirements, official rules, pickleball comparison, shipping, returns.

**Issue:** No FAQ schema markup — these Q&As could appear as rich results in Google.

---

## 10. Visual Audit (from Firecrawl screenshots)

### Homepage — Desktop
**What works:**
- Hero is high-energy — Shark Tank footage background with bold "WORLD'S HOTTEST NEW GAME" headline. Immediately establishes credibility.
- Red marquee bar with press logos (ABC, HuffPost, NatGeo, Boston Globe, GQ, FOX, NBC, USA Today) is impressive social proof.
- "AS SEEN ON SHARK TANK" + "4.93 (100,000+ SOLD)" badges directly under hero — strong trust signals above the fold.
- Product showcase section with gallery thumbnails and "SHOP NOW" CTA is clear.
- Video testimonial section with 18+ video thumbnails shows massive UGC content.
- "Skeptic to Obsessed" journey section is clever storytelling — relatable conversion narrative.

**What needs work:**
- **Hero text readability** — "WORLD'S HOTTEST NEW GAME" overlays busy Shark Tank video footage. White/pink text on busy background can be hard to read in some frames.
- **No clear price visible above the fold** — the $89.99 price point is a selling point but requires scrolling to the product section.
- **Video section is just a wall of thumbnails** — no context, no names, no "play" affordance immediately obvious. It's visually dense but not inviting.
- **No announcement bar / promo banner** — missed opportunity for active promotions (NIRSA deal, bundle discounts, free shipping).
- **"Where Will You Rally?" UGC section** has small images that don't showcase the action well on desktop. The testimonial quotes are small and easy to miss.
- **Footer is dense and dark** — the dark footer with social icons (Facebook, Instagram, TikTok) at the very bottom is easy to miss. Wait — the footer DOES have social icons! They're buried in the copyright bar below the main footer, tiny and not prominent.

### Homepage — Mobile
**What works:**
- Hero scales well — headline is large and readable on mobile.
- "GET THE SET" CTA button is prominent and thumb-friendly.
- Press logo marquee adapts to scrolling ticker.

**What needs work:**
- Only see hero + press logos above the fold on mobile — product, price, and trust badges are all below the fold.
- The fold cuts right at the marquee bar — a user might not scroll further.

### Product Page (Full Set) — Desktop
**What works:**
- Clean, professional product layout — Shopify doing its job.
- Image gallery with 6+ thumbnails including lifestyle shots.
- "What's Inside" section with icon-based breakdown of set contents is clear.
- "The Game That Brings People Together" lifestyle photo grid.
- "Quick & Easy Setup" section.
- "How We Compare" section (comparison positioning).
- "Raving Reviews" section with Judge.me integration.
- "QUESTIONS YOUR MOM WOULD ASK" FAQ accordion — great brand voice.
- Trust badges visible: 100,000+ Sets Sold, 60-Day Guarantee, FAST Shipping, Secure Checkout.

**What needs work:**
- **Product title "Pepper Pong Full Set" is plain** — no benefit-driven subtitle ("The complete portable paddle sport set" or similar).
- **Mobile shows $134.99 crossed out → $89.99 with "+FREE shipping"** — but desktop doesn't clearly show compare-at pricing in the same way. Pricing presentation inconsistency.
- **"SOLD OUT 3X IN 3 MONTHS" copy** is great urgency, but it appears as body text rather than a prominent badge/banner.
- **"How We Compare" section** — can't read the details in the screenshot but the concept is solid for a category-creating product.

### Our Story — Desktop
**What works:**
- Clean, focused layout — hero with group photo on pink diagonal background looks vibrant and fun.
- "MORE THAN A GAME" headline is strong.
- Tom's recovery story is front and center — emotionally powerful.
- "Rally 4 Recovery" giving program has its own section with CTA ("DONATION REQUEST").

**What needs work:**
- **Very short page** — the story deserves more depth. No timeline, no Shark Tank mention, no growth milestones, no team photos beyond the hero.
- **The recovery narrative is the only content** — there's no "how we got here" entrepreneurial journey, no mention of 100K+ sets, no Shark Tank chapter.
- **CTA "GET IN ON THE SPICY GAME"** in the middle of the page feels generic and disconnects from the emotional story just told.
- **No images of Tom personally** in the main content — just the group hero shot. For a founder story page, this is a miss.

### Schools — Desktop
**What works:**
- Best-structured page on the site. Clear value prop hierarchy.
- Hero shows real classroom/gym context.
- "THE PE GAME THAT BUILDS SOCIAL-EMOTIONAL SKILLS WHILE EVERY KID PLAYS" — excellent SEL-focused headline.
- Volume pricing widget is clean and functional.
- Multiple CTAs for different buyer paths (sample vs 8-pack).

**What needs work:**
- **Navigation doesn't link here** — this page is a hidden gem. Schools/PE is clearly a major revenue channel but you'd never find it from the main site.
- **The bottom half of the page gets dark/dense** — transitions from white content area to dark footer without a clear closing CTA.

### Reviews — Desktop
**What works:**
- Judge.me widget is rendering with star ratings and customer photos.
- 4.9 average visible at top.
- "Write a review" CTA is prominent (yellow button).

**What needs work:**
- **Page is visually plain** — just a Judge.me embed with no brand wrapper. Compared to the rest of the site, this feels like a raw plugin dump.
- **No featured/curated reviews** — all reviews look the same. Could highlight a few standout testimonials with photos.
- **No filtering or category views** — "reviews from educators", "reviews from families", etc. would help different buyer personas find relevant social proof.

### Press — Desktop
**What works:**
- Visually the strongest content page — Shark Tank hero footage, publication logos, video embeds, article cards.
- Good use of media — multiple video embeds and image cards.
- "IN THE SPICY SPOTLIGHT" headline maintains brand voice.

**What needs work:**
- **Article cards have publication logos but are small and hard to read** at the card level.
- **No direct links to external articles visible** — visitors want to read the actual press coverage.

### FAQ — Desktop
**What works:**
- Clean accordion layout — professional and easy to scan.
- Hero image adds visual interest.
- Questions are written in brand voice and are comprehensive.

**What needs work:**
- **Accordion items are close together** — could use more vertical spacing for scannability.
- **No search function** — with 13+ questions, search would help.
- **No category grouping** — "About the Game", "Ordering", "Shipping & Returns" headers would help users find what they need.

### How to Play — Desktop
**What works:**
- Hero video/image shows actual gameplay in a real home kitchen setting — relatable.
- "A LEVEL PLAYING FIELD" philosophy section is well-written.
- Video Quick Start Guide with expandable sections (How It Plays, The Gear, Setup, Rules, etc.) is good progressive disclosure.
- Rulebook CTA section at the bottom is clean.

**What needs work:**
- **Video tutorial is a single embedded video** — could benefit from shorter chapter-based clips for each topic.
- **Hero text "ACTION FOR EVERYONE, EVERYWHERE!"** overlaps with the image in a way that reduces readability.

---

## 11. Key Findings Summary (for Step 3 analysis)

### What's Working Well
1. **Meta description on homepage and all products** — solid keyword coverage
2. **Judge.me reviews active** with 200+ reviews at 4.95 — social proof is strong
3. **Heading hierarchy** is clean on homepage (H1 → H2 → H3)
4. **Strong brand voice** — "spicy" language is fun, consistent, memorable
5. **Schools page** is the best-executed content page with meta desc, value props, SEL research
6. **Video content** is abundant (21 videos on homepage)
7. **Shark Tank credibility** used throughout — strong trust signal
8. **Our Story** is emotionally compelling — sobriety narrative is authentic and powerful
9. **FAQ content is comprehensive** and written in brand voice
10. **Product pricing** is clear with bundle discounts visible

### What Needs Fixing
1. **18/20 content pages missing meta descriptions** — massive SEO gap
2. **Draft/internal pages indexed** — pdp-draft, email-confirmation, lp1 are all in sitemap
3. **Blog is dead** — 5 posts, last one 15 months ago, titles are unprofessional
4. **Social media links buried** — tiny icons in sub-footer copyright bar, not in main footer or anywhere else on site
5. **NIRSA discount codes exposed** on publicly indexed page
6. **No FAQ schema** on FAQ page — missing rich snippet opportunity
7. **No Organization schema** — missing brand knowledge panel opportunity
8. **Image alt text issues** — 8 "Press logo" generics, 6 "Thumbnail N" generics, 5 empty alts
9. **Product title inconsistencies** — "spicy-solo" slug used as title, mixed casing
10. **Schools/education vertical not in main nav** — hidden gem buried
11. **Social media links barely visible** — Facebook, Instagram, TikTok icons exist but are tiny in the sub-footer copyright bar, not in the main footer Quick Links section
12. **"Read our FAQ's"** — grammar error in footer
13. **OG image uses HTTP** instead of HTTPS
14. **Twitter image tag missing** on homepage
15. **Collection "core-products" titled "Extra Peppers"** — misleading
16. **Blog post titles** include "Blog 1:" numbering — bad for SEO
17. **6 PDF curriculum pages** indexed but probably should be gated/noindexed
18. **No Google Analytics, Facebook Pixel, or TikTok Pixel** — limited marketing attribution
19. **Rally 4 Recovery** program barely visible — could be major PR/brand story
20. **377KB homepage HTML** — heavy, lots of inline CSS/JS
