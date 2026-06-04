# Cooldown Running - Website Audit
**Prepared by Annabel Filippini | April 2026**
**Site: cooldownrunning.com | Platform: Shopify (Dawn 7.0.1)**

---

## Executive Summary

Cooldown Running has a strong brand identity and genuinely compelling community positioning — the "social club disguised as a run club" concept is excellent and the energy comes through. The site looks polished at first glance and the product photography is high quality. However, there are real gaps in SEO fundamentals (missing meta descriptions, generic image alt text, no blog strategy), accessibility (missing alt text on product images, heading hierarchy issues), and some housekeeping items (duplicate/test pages indexed, URL slugs with "-copy" artifacts) that are leaving growth on the table. The biggest opportunity is content — Cooldown has an incredible story with 15+ city chapters, and the site barely tells it.

---

## Score Card

| Dimension | Grade | Summary |
|-----------|-------|---------|
| Technical Health | B- | Solid Shopify foundation, but test pages indexed, duplicate URLs, announcement bar links to wrong page |
| SEO | C+ | Missing meta descriptions across the site, no alt text on product images, empty blog, no structured product schema beyond Shopify defaults |
| Accessibility | C | Generic/missing image alt text, heading hierarchy skips levels, unclear form labels |
| Content & UX | B | Great brand voice and photography, but product descriptions are inconsistent, no reviews visible, community story undertold |
| AI Opportunities | N/A | Significant upside — detailed below |

---

## Top 5 Quick Wins

These are high-impact fixes that should take under an hour each:

### 1. Fix the Announcement Bar Link
The announcement bar says "buy 4+ items - get 20% off" but links to `/pages/run-clubs` instead of `/pages/bundle-and-save`. Customers clicking the promo land on the run clubs page, not the bundle deal. Swap the href.

### 2. Add Meta Descriptions to All Pages
Not a single page has a custom meta description. Google is auto-generating snippets from page content, which means you're losing control of how you appear in search results. Write a compelling 150-160 character description for at least: homepage, collections pages, about page, and run clubs page. Shopify makes this easy — it's in the SEO section at the bottom of each page/product editor.

### 3. Fix Product Image Alt Text
Every product image across the site uses generic alt text like "Katherine Bra" or "Molly Short" repeated for all 20-30 images per product. Change these to descriptive text: "Katherine Bra in lavender horizon - front view," "Molly Short in midnight green - side pocket detail." This helps both SEO and screen reader users.

### 4. Remove or Noindex the Test Page
`/pages/run-clubs-typeform-test` is a test page that's publicly accessible and indexed in the sitemap. Either delete it, set it to draft in Shopify, or add a noindex tag. Same for duplicate city pages (`/boston` vs `/boston-1`, `/tampa` vs `/tampa-1`) — decide which is canonical and redirect the other.

### 5. Clean Up "-copy" Product URLs
Two products have URL slugs with "-copy" artifacts from being duplicated in Shopify:
- `/products/elizabeth-short-copy` (the Elizabeth Short)
- `/products/molly-short-copy` (the Boulderthon Molly Short)
- `/products/boulderthon-katherine-bra-copy` (the Boulderthon Tank)

These look unprofessional in shared links and hurt SEO. Update the URL handles in Shopify's product editor and set up redirects from the old URLs.

---

## Detailed Findings

### Technical Health (B-)

**What's Working:**
- SSL is active (HTTPS across the site)
- Shopify CDN handles image delivery with width parameters for responsive serving
- Custom fonts use `font-display: swap` for decent loading behavior
- hCaptcha protection on forms
- Payment integrations (Apple Pay, Google Pay, Shop Pay) are properly configured
- Responsive breakpoints at 750px and 990px

**Issues Found:**

**Announcement Bar Mismatch**
The promo "buy 4+ items - get 20% off" links to `/pages/run-clubs` — completely wrong destination. Should link to `/pages/bundle-and-save` where the actual bundle builder lives. This is actively costing conversions.

**Duplicate/Orphan Pages in Sitemap**
The sitemap includes 35 pages. Several are problematic:
- `/pages/run-clubs-typeform-test` — test page, publicly indexed
- `/pages/boston` AND `/pages/boston-1` — two Boston pages with different leader lists
- `/pages/tampa` AND `/pages/tampa-1` — two Tampa pages with different schedules (Sundays vs Thursdays)
- `/pages/chicago-1` — why the "-1" suffix?

If Tampa and Boston genuinely have two chapters each, the pages need to be named clearly (e.g., `/pages/tampa-south`, `/pages/tampa-downtown`). If they're duplicates, consolidate and redirect.

**Product URL Slugs with "-copy"**
Three products have copy artifacts in their URLs:
- `elizabeth-short-copy`
- `molly-short-copy` (this is actually the Boulderthon Molly Short)
- `boulderthon-katherine-bra-copy` (this is actually the Boulderthon Tank)

These happen when you duplicate a product in Shopify and forget to update the handle. Fix in the Shopify admin under product SEO settings.

**Heavy Third-Party Script Load**
The site loads a significant number of third-party scripts:
- Google Tag Manager + Google Ads conversion tracking
- Facebook Pixel
- Mailchimp integration
- Loox (reviews app — but no reviews are displayed anywhere)
- Pop Convert (popup app)
- Instafeed
- Globo Swatch
- Easy Bundles by GiftBox
- TikTok pixel
- Shopify's own analytics stack

That's 10+ third-party scripts. Each one adds load time. If Loox isn't actively displaying reviews, consider removing it. Same for any other apps not actively used.

**San Diego Page Says "Paused for Winter"**
It's April. If the club is still paused, update the messaging. If it's back, update the status. Stale content erodes trust.

---

### SEO (C+)

**What's Working:**
- Clean URL structure for products (`/products/katherine-bra`) and collections (`/collections/womens-collection`)
- Organization schema (JSON-LD) with social profiles
- SearchAction schema for site search
- Sitemap is properly structured and submitted
- robots.txt is well-configured (standard Shopify)

**Issues Found:**

**No Meta Descriptions — Anywhere**
Checked homepage, collections, product pages, about page, contact page — none have custom meta descriptions. This is the single biggest SEO gap. Google will auto-generate snippets, but they're often pulled from random page content and rarely compelling. Every key page should have a hand-written meta description.

**Page Titles Are Bare**
- Homepage: "Cooldown" — should be something like "Cooldown Running | Colorful Running Apparel & Social Run Clubs"
- Collections: "All - Cooldown" — should include keywords like "running apparel," "women's running clothes"
- Products: "Katherine Bra - Cooldown" — decent but could include "running bra" or "athletic bra"

**No Blog Content**
The blog section exists (`/blogs/news`) but has zero published posts. The blog index page shows section headers ("Movement Together," "Desk Job Wellness") but no actual articles. A running apparel brand with 15+ city chapters has unlimited content to write about — race recaps, runner spotlights, training tips, city guides. This is a massive missed opportunity for organic traffic.

**Product Image Alt Text is Generic**
Every product image uses just the product name as alt text. With 20-30 images per product, that means "Katherine Bra" appears 30 times. Google can't distinguish between a front view, a side view, a detail shot, or a lifestyle photo. Descriptive alt text helps image search rankings and accessibility.

**No Product-Level Structured Data Beyond Defaults**
Shopify provides basic product schema, but there's no:
- Review/rating schema (because there are no reviews)
- FAQ schema on product pages
- BreadcrumbList schema
- Aggregate rating data

**Inconsistent Product Descriptions**
Some products (Kenny Short, Meg Tank) have detailed descriptions with materials, features, and comparisons. Others (Molly Short, Katherine Bra based on the crawl) appear to have minimal or no description content. Consistency matters for both SEO and conversion.

**City Pages Are Thin Content**
Each city page has maybe 50 words of unique content (day, time, leaders). For 15+ cities, these could be rich pages with local SEO value — "best run clubs in Denver," etc. Currently they're too thin to rank for anything.

---

### Accessibility (C)

**What's Working:**
- Skip-to-content links present ("Skip to content," "Skip to product information")
- Form elements have associated labels on the contact page
- Responsive design supports various screen sizes
- ARIA hidden attributes used on modals

**Issues Found:**

**Image Alt Text**
This is the biggest accessibility issue. Product images use generic alt text (just the product name repeated). Many page images (hero banners, city photos, lifestyle images on the about/join pages) have no alt text at all. Screen reader users get almost no useful information from images across the site.

Examples of missing/poor alt text:
- Join Our Crew page hero images: no alt text
- City page cover images: no alt text
- Product images: "Katherine Bra" x30 instead of descriptive text

**Heading Hierarchy Issues**
The site jumps from H2 to H5 in many places, skipping H3 and H4 entirely. H5 is used extensively for stylistic purposes (applying the SpeziaMono-Bold font) rather than semantic meaning. This confuses screen readers that navigate by heading level.

Example from homepage:
- H2: "uniting the world through running"
- H5: (used for styled text that should be a span or p with a class)
- H2: "running apparel that's just as functional as it is colorful"

The fix: use CSS classes for styling instead of heading tags. Reserve headings for document structure.

**Color Contrast Considerations**
The brand uses light lavender backgrounds (rgb 207, 214, 240) with purple accents (rgb 178, 146, 231). Text on these backgrounds should be verified against WCAG AA standards (4.5:1 ratio for normal text). The light purple on light blue-grey could be problematic.

**Form Accessibility**
The contact form has labels, but the newsletter signup form in the footer ("join the email list") should be checked for proper label association. The email input should have a visible label or proper aria-label, not just placeholder text.

**Final Sale Modal**
The modal that warns about final sale items uses `aria-hidden` toggling, which is good. But keyboard focus management should be verified — when the modal opens, does focus move to it? Can users close it with Escape? Can they tab through it without getting trapped?

---

### Content & UX (B)

**What's Working Well:**
- **Brand voice is strong.** "A social club disguised as a run club" is a great tagline. The copy is casual, warm, and authentic throughout. Lowercase styling feels intentional and on-brand.
- **Product photography is excellent.** Clean, colorful, well-lit product shots with multiple angles and lifestyle images.
- **Community positioning is compelling.** The run club network across 15+ cities is a genuine differentiator. Products named after real people (Katherine, Molly, Meg, Nicole) adds a personal touch.
- **Color palette is distinctive.** The lavender/purple/navy brand colors stand out in the running apparel space and reinforce the "colorful" positioning.
- **Hero video on homepage** creates energy and movement.

**Issues Found:**

**No Reviews Visible Anywhere**
Loox (a reviews app) is installed and loading scripts, but no reviews appear on any product page. Customer reviews are one of the highest-impact conversion drivers for e-commerce. Either:
- Reviews haven't been collected yet (set up post-purchase email flows to request them)
- Loox isn't configured to display (fix the widget placement)
- There are reviews but the display is broken (debug the app)

If you're paying for Loox and not showing reviews, you're wasting money. If you don't have reviews yet, that's priority #1 for conversion optimization.

**Inconsistent Product Descriptions**
- **Good:** Kenny Short has "Why We Made This" section, features list, materials, care instructions, size guide, and even a comparison to similar products.
- **Good:** Meg Tank has feature sections ("Speed Meets Function," "Pocket for the Long Haul")
- **Weak:** Katherine Bra and Molly Short appear to have minimal description content despite being featured products.

Every product should have the same level of detail as the Kenny Short. Materials, features, what makes it different, who it's for.

**Run Clubs Page Doesn't List All Cities**
The main run clubs page shows interactive cards for about 15 cities, but the sitemap reveals additional city pages (Charlotte, San Diego, Boston) that may not all be linked. Charlotte and San Diego are in the sitemap but need verification that they're reachable from the run clubs hub. Some cities show "coming soon" or "paused" — these should be visually distinguished from active clubs.

**No About Page (It's a Franchise Page)**
The navigation says "About" and links to `/pages/about-us`, but this page is actually titled "franchise a cooldown" and is focused on recruiting chapter leaders. There's no page that tells the Cooldown origin story, introduces the founders, or explains the brand mission. For a community-driven brand, this is a significant gap. Visitors want to know: who started this? Why? What's the vision?

**Bundle Promotion is Buried**
The "buy 4+ items, get 20% off" offer is mentioned in the announcement bar but links to the wrong page (run clubs instead of bundle-and-save). Even with the correct link, the bundle-and-save page loads a third-party app (Easy Bundles) which may be slow. The promotion should be more prominently featured — maybe a dedicated section on the homepage or a banner on collection pages.

**Navigation Missing Key Links**
- No direct link to the bundle/save promotion in the main nav
- "Start a Cooldown" nav item goes to `/pages/join-our-crew-1` — the URL has a "-1" suffix (another Shopify duplicate artifact)
- No men's collection highlighted as prominently as women's in the featured products on homepage

**Size Guide Pages**
There are four separate size guide pages (women's, men's, unisex tops, t-shirt). The women's size guide at `/pages/size-guide` appears to have no actual content — just a page shell with no measurements or charts visible. If the size guide content is loading via JavaScript/an embedded app, it may not be accessible to all users. Individual product pages (like Kenny Short) do have inline size guides, which is good — but the standalone pages should also work.

---

### AI Opportunities

This is where it gets exciting. Cooldown is at a perfect stage to leverage AI tools — small team, growing fast, lots of repetitive content needs.

**1. AI-Powered Product Descriptions (Quick Win)**
Use AI to generate consistent, high-quality product descriptions for every item. Feed it the product name, materials, features, and brand voice guidelines, and it can produce descriptions matching the quality of the Kenny Short page — but for every product in minutes instead of hours. This directly improves SEO and conversions.

**2. AI Customer Service Chatbot**
A chatbot on the site could handle the most common questions instantly:
- "What size should I get?" (pulling from size guides)
- "What's your return policy?" (15-day returns, final sale items excluded)
- "When does the [city] run club meet?" (pulling from city pages)
- "How do I start a Cooldown chapter?" (directing to the franchise page)
This reduces the load on whoever monitors the contact form and provides instant answers 24/7.

**3. AI-Generated Blog Content**
Cooldown has unlimited content to work with but zero published blog posts. AI can help produce:
- City-specific run guides ("Best running routes in Denver for your Cooldown meetup")
- Race recaps and event coverage
- Training tips and running advice
- Runner spotlight interviews (AI helps draft, human adds the personal touch)
- "What to wear" seasonal guides

Even 2-4 posts per month would dramatically improve organic search traffic. Each city page could link to related blog content, creating an internal linking web that boosts the entire site.

**4. Email Marketing Automation**
The site has Mailchimp integrated and a newsletter signup, but there's an opportunity for AI-driven email flows:
- **Post-purchase sequences:** "How to care for your new [product]" + "Leave a review" + "Here's what pairs with what you bought"
- **City-specific emails:** "This week's Denver meetup is at [location]" — personalized by the user's city
- **Re-engagement:** "We miss you at Cooldown [city]" for lapsed run club attendees
- **Product launch announcements** with AI-written copy tailored to different segments (new customers vs. repeat buyers)

**5. Inventory and Demand Forecasting**
With 21 products across multiple colors and sizes, AI can help predict:
- Which variants will sell out (the Katherine Bra already has many sold-out variants)
- When to reorder based on sales velocity
- Which cities drive the most product sales (informing where to expand)

---

## Closing Notes

Cooldown has something most brands would kill for — a genuine community. 15+ city chapters, real people leading real meetups, products named after real humans. The brand voice is authentic and the visual identity is strong. The bones are great.

Most of the gaps identified in this audit are foundational — meta descriptions, alt text, consistent product copy, page consolidation. Individually they're small, but collectively they determine whether Cooldown appears when someone in Denver searches "fun run clubs near me" or when a potential customer discovers your products through Google Images.

The AI opportunities represent a significant advantage for a team of your size. The right tools for content generation, customer service, and email automation can dramatically reduce the time spent on repetitive work — and Cooldown is well-positioned to adopt them, given how strong and consistent the brand voice already is.

---

*Audit conducted April 2026 by Annabel Filippini using AI-powered site analysis tools.*
