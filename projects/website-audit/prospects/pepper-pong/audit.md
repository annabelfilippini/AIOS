# Pepper Pong — Internal Audit Reference
**Site:** pepperpong.com | **Platform:** Shopify (custom Horizon-based) | **Date:** 2026-04-13
**Inputs:** scrape-data.md (8 pages, 24 screenshots), seo-research.md (10 keywords)

Core insight: Discovery, not conversion. Branded search locked down. Invisible for 6/10 non-branded keywords. Vocabulary mismatch ("portable paddle sport" vs. what people search) is the root cause. Shark Tank interest decaying (100 → 8-20) with no content sustaining it.

---

## Technical Health (B)

### Working
- SSL active, Shopify CDN with responsive image widths
- Fonts: Gotham (headings, 400-900), Inter (body, 400/500/700) — proper weight ranges
- hCaptcha on forms, Shop Pay / Apple Pay / Google Pay configured
- robots.txt well-configured, responsive breakpoints functional
- Patent #11,786,792 displayed, contact info visible

### Issues

| Finding | Severity | Effort |
|---------|----------|--------|
| Draft/internal pages indexed: `/pages/pdp-draft`, `/pages/email-confirmation`, `/pages/lp1` | Medium | Low |
| 6 PDF curriculum pages indexed (pdf-standards, pdf-rubric, pdf-rally, pdf-2week, pdf-4week, pdf-skill-cards) — should be noindexed or gated behind Schools flow | Low | Low |
| OG image uses HTTP not HTTPS (`http://pepperpong.com/cdn/shop/files/Pepper_Pong_logo.png`) | Low | Low |
| Twitter card image tag missing entirely on homepage | Low | Low |
| Homepage HTML 377KB — 21 VideoObject schemas inline, 30+ theme JS files, inline CSS/JS | Low | Medium |
| No Organization schema (JSON-LD) — brand has enough press presence for Knowledge Panel | Medium | Low |
| No BreadcrumbList schema on product/content pages | Low | Low |
| No Google Analytics/GTM, no Facebook Pixel, no TikTok Pixel — zero marketing attribution | High | Medium |
| 7 third-party services: Judge.me, Klaviyo (ID: Ydxv4T), Microsoft Clarity, Triple Pixel, hCaptcha, Automizely Returns, Shop Pay | Info | — |
| `/pages/llms-txt` exists — Pepper Pong has an AI/LLM page. Interesting signal for AI opportunities pitch. | Info | — |

---

## SEO (C)

### Working
- Homepage + all 12 products have meta descriptions
- Clean URL structure (`/products/pepper-pong-full-set`, `/pages/how-to-play`)
- Sitemap structured and submitted, robots.txt clean
- #1 for "portable ping pong game" and all branded terms
- 21 VideoObject schemas on homepage (heavy but gives video rich results)

### Keyword Visibility

| Keyword | Position | Root Cause |
|---------|----------|------------|
| pepper pong game | #1 | — |
| pepper pong shark tank | #1 | — |
| portable ping pong game | #1 | — |
| pickleball ping pong tabletop buy | #1-2 | — |
| tabletop paddle game | Invisible | Site never uses this language |
| mini pickleball tabletop game | Invisible | Never uses "mini pickleball" — HIGH volume category (10 autocomplete suggestions) |
| best family games 2025/2026 | Invisible | No blog content, no PR outreach for roundup lists |
| PE games for schools indoor | Invisible | Schools page has no meta desc, not in nav, wrong vocabulary |
| office break room games | Invisible | Zero content targeting corporate use case |
| best shark tank products games | Absent | Not on "best of" compilations |

**Root cause:** Vocabulary mismatch. Site uses "portable paddle sport." Searchers use "mini pickleball set," "tabletop game," "indoor ping pong."

### Google Trends
- Peak: Feb 2026 (score 100) — Shark Tank replay bump
- Holiday spike: Nov-Dec 2025 (85-86)
- Current: Mar-Apr 2026 at 8-20 — decaying
- Pattern: Event-driven, not sustained. Content marketing is the only long-term fix.
- Top states: Colorado (100), Oklahoma (84), Connecticut (76), South Carolina (74). Absent: CA, NY, TX, FL.

### Autocomplete Insights
- "pepper pong" — 10 suggestions, all bottom-of-funnel (amazon, reviews, discount code, shark tank)
- "mini pickleball" — 10 suggestions, active category (courts, sets, paddles, nets). Pepper Pong absent.
- "portable ping pong" — 10 suggestions, #10 is "portable ping pong shark tank." Already connected.
- "indoor game for office" — 10 suggestions (employees, teams, party, Fun Friday). Untapped.
- "PE equipment for schools" — 10 suggestions including UK, Ireland, Australia, NZ. International demand.

### AnswerThePublic (Trust/Validation Queries)
- "why is pepper pong so expensive" — price objection
- "is pepper pong worth it" — purchase validation
- "is pepper pong legit" — trust barrier
- "is pepper pong sold in stores" — wants retail
- "is pepper pong still in business" — doubt signal
- "where to buy pepper pong nearby" — strong local intent

### Other SEO Issues

| Finding | Severity | Effort |
|---------|----------|--------|
| 18/20 content pages missing meta descriptions | High | Low |
| Blog dead: 5 posts (4 from June 2023, 1 from Jan 2025). Titles unprofessional ("Blog 1:", "Tom's New Blog Post") | High | Medium |
| No FAQ schema on FAQ page (15+ Q&As matching real autocomplete queries) | Medium | Low |
| NIRSA discount codes exposed on indexed page: `1SAMPLENIRSA26` (61% off), `8PACKNIRSA26` (62% off), expires Apr 30 | High | Low |
| Product title inconsistencies: `spicy-solo` slug as display title, mixed "Extra" prefix casing | Low | Low |
| Collection naming: "core-products" titled "Extra Peppers", "frontpage" titled "Home page", extremely long replacements slug | Low | Low |
| Blog post titles have "Blog 1:" numbering format | Low | Low |
| Product titles don't include category keywords | Medium | Low |

---

## Accessibility (B-)

### Working
- Heading hierarchy clean on homepage (H1 → H2 → H3)
- H2 for Search/Cart drawers — common Shopify pattern, minor
- Responsive design across breakpoints
- hCaptcha accessible alternative
- Skip-to-content link present

### Issues

| Finding | Severity | Effort |
|---------|----------|--------|
| 5 images with empty alt text on homepage | Medium | Low |
| 8 images use generic "Press logo" — should name the publication | Low | Low |
| 6 images use "Thumbnail 1-6" — should describe content | Low | Low |
| 2 images use "AS SEEN ON SHARK TANK" / "100,000+ SETS SOLD" as alt text (promo text, not image description) | Low | Low |
| 4 images use section headings as alt text ("This looks dumb.", etc.) | Low | Low |
| Product image alt text likely repeats product name across all angles (needs verification across all 12 products) | Medium | Low |
| Footer newsletter signup — verify label association (placeholder vs. proper label/aria-label) | Low | Low |
| Verify `lang="en"` on `<html>` tag (custom theme) | Low | Low |

---

## Content & UX (B+)

### Working
- Brand voice exceptional: "Spicy," "Rally," "Peppers," "QUESTIONS YOUR MOM WOULD ASK" — consistent throughout
- Social proof strong: 211+ reviews at 4.95 (Judge.me), 100K+ sold badge, Shark Tank, 21 UGC videos, press from major outlets
- Founder story emotionally compelling: sobriety narrative, Rally 4 Recovery program
- Schools page best-structured on site: value props, SEL research, educator messaging, volume pricing
- Product page (Full Set) comprehensive: What's Inside, comparison, FAQ accordion, trust badges, bundle upsell
- Homepage conversion narrative ("skeptic to obsessed") is smart storytelling
- FAQ content thorough, written in brand voice

### Issues

| Finding | Severity | Effort |
|---------|----------|--------|
| Schools/education not in main nav — $599 product invisible to educators | High | Low |
| Social media links buried in sub-footer copyright bar (tiny Facebook, Instagram, TikTok icons) | Medium | Low |
| Footer "SHOP" links to single product not `/collections/all-products` | Low | Low |
| Footer grammar: "Read our FAQ's" → "Read our FAQs" | Low | Low |
| Our Story page undertells the story — no Shark Tank, no growth milestones, no team, no Tom photos in main content | Medium | Medium |
| Reviews page is raw Judge.me embed — no brand wrapper, no curated highlights, no filtering by buyer type | Medium | Medium |
| No announcement bar for active promotions (NIRSA deal, bundle discounts, free shipping) | Medium | Low |
| Product description consistency unknown — Full Set is thorough, catalog may vary | Medium | Medium |
| Blog dead — massive content opportunity untapped (Shark Tank, schools, use cases, comparisons) | High | High |
| San Diego equivalent check: any seasonal/paused messaging that's now stale? | Low | Low |

### Page-by-Page Notes

**Homepage:** Hero is high-energy (Shark Tank footage background). Red marquee bar with press logos is strong. No price visible above the fold. Video section is a wall of thumbnails with no context. Mobile cuts at marquee bar — might not scroll.

**Product (Full Set):** Clean Shopify layout. "What's Inside" icon breakdown is clear. Mobile shows $134.99 crossed out → $89.99 (desktop doesn't match this presentation). "SOLD OUT 3X IN 3 MONTHS" appears as body text, not a badge.

**Our Story:** "MORE THAN A GAME" headline. Recovery story front and center. Rally 4 Recovery with donation CTA. Very short — no entrepreneurial journey, no Shark Tank chapter. Generic CTA "GET IN ON THE SPICY GAME" disconnects from emotional story.

**Schools:** Best page. Hero shows classroom context. SEL-focused headline. Volume pricing widget. Multiple CTAs. But NOT IN NAV.

**Reviews:** Just a Judge.me embed. 4.9 average, "Write a review" CTA. No featured reviews, no filtering, no brand wrapper.

**Press:** Visually strongest content page. Shark Tank hero, publication logos, video embeds. Article cards are small/hard to read. No direct links to external coverage visible.

**FAQ:** Clean accordion. 13+ questions in brand voice. No category grouping, no search, tight vertical spacing. No FAQ schema.

**How to Play:** Hero video in kitchen setting. "A LEVEL PLAYING FIELD" philosophy section. Video Quick Start Guide with progressive disclosure. Hero text overlaps image.

---

## AI Opportunities

| Opportunity | Impact | Effort | Connection to Audit Findings |
|-------------|--------|--------|------------------------------|
| Content for non-branded discovery (blog posts targeting invisible keywords) | High | Medium | Directly addresses 6/10 keyword invisibility |
| SEO meta descriptions via AI (18 pages, 5 min each) | Medium | Low | Fixes biggest quick-win gap |
| Consistent product descriptions | Medium | Low | Product catalog consistency issue |
| FAQ chatbot addressing trust queries ("worth it?", "legit?", "sold in stores?") | Medium | Medium | Autocomplete shows trust barrier queries dominate |
| Klaviyo email sequences (post-purchase, abandoned cart, education nurture) | Medium | Medium | Klaviyo already installed |
| Social proof curation (reviews by persona, social posts from UGC) | Medium | Medium | 211 reviews + 21 videos = untapped content |
| PR outreach for "best of" lists | Medium | Medium | Absent from every family game / Shark Tank roundup |

**Notable:** Site has `/pages/llms-txt` — they're already thinking about AI. This is a conversation opener.

---

## Priority Action List (Deduplicated)

### This Week (< 1 hour each)
1. Write meta descriptions for 5 priority pages (Our Story, How to Play, FAQ, Press, Reviews)
2. Add Schools to main navigation
3. Noindex or delete pdp-draft, email-confirmation, lp1
4. Secure NIRSA discount codes (noindex page or gate access)
5. Add FAQ schema markup
6. Fix OG image HTTP → HTTPS
7. Add twitter:image meta tag
8. Fix footer: "FAQ's" → "FAQs", SHOP → /collections/all-products

### This Month
9. Write meta descriptions for remaining 13 content pages
10. Add Organization schema (JSON-LD)
11. Fix product title inconsistencies and add category keywords
12. Fix image alt text (press logos, thumbnails, empty alts)
13. Add announcement bar for active promotions
14. Install Google Analytics and Facebook Pixel (if running ads)
15. Surface social media links in main footer
16. Noindex 6 PDF curriculum pages (or gate behind Schools flow)

### This Quarter
17. Expand Our Story page with full journey (Shark Tank, growth, team)
18. Start blog: 1 post/week targeting non-branded keywords
19. Create corporate/office landing page
20. Optimize Schools page for education search terms
21. Build email sequences in Klaviyo
22. Add "mini pickleball" and "tabletop game" vocabulary to product pages + homepage
23. Curate reviews by buyer type on Reviews page
24. Clean up collection names and blog post titles
25. PR outreach to "best of" list publishers
