# Hop Alley — Website Audit

Prepared for Tommy Lee — April 2026

---

## What you're doing right

Before anything else: Hop Alley is a **three-peat Michelin Bib Gourmand** restaurant (2023, 2024, 2025), a 2025 James Beard semifinalist for Outstanding Wine & Beverage, and a 2025 Michelin Exceptional Cocktails awardee. On top of that you run a six-seat Chef's Counter with Doug Rankin — a concept with a legitimate chef's-table format in a city where that category barely exists.

Reading the site, a few things stood out:

- **Your voice is unmistakably yours.** "WE ACCEPT TAKE OUT ORDERS OVER THE PHONE AT 3:30P, ONLINE ORDERING OPENS AT 5P" is the kind of copy you'd never see on a chain. It reads confident and operational, not marketing-brain. Keep it.
- **Your awards copy is bold and above-the-fold.** Most restaurants bury accolades in an "About" page. You lead with them. Good instinct.
- **Your photography is strong.** The interior and food shots in the image sitemap are editorial quality.
- **Your sitemap and robots.txt are clean.** Every major AI crawler — OpenAI's GPTBot, Anthropic's ClaudeBot, Google's AI crawler — is allowed to read your site. This is a free win most Squarespace sites accidentally turn off.

The site's not broken. It converts the people who find it. The problem is **the people who should be finding it, aren't.**

---

## The big opportunity: your awards are invisible to Google and AI

This is the single most important thing to know from this audit.

You have **seven awards** on your homepage. Google and Perplexity and ChatGPT can't see any of them.

Awards on your site today exist as **bold body text**. Google and modern AI search engines need them as **structured data** — a machine-readable format called schema.org — to surface them in search results, Knowledge Panels, and AI-generated recommendations. Your site has schema, but it's generic (`LocalBusiness`) and doesn't include the `award` property or the `Restaurant` type that would make your Bib Gourmand streak parseable.

We ran a test. We asked Perplexity, **"best sichuan restaurant denver,"** and here is what it said, verbatim:

> *"A strong current pick is **Wok Spicy in Englewood** for the most authentic Sichuan-style cooking near Denver. It explicitly brands itself as authentic Sichuan cuisine…*
>
> *Other good Denver-area options are: Happy Cafe, MAKfam, and **Hop Alley — not strictly Sichuan-only, but it's a Michelin Bib Gourmand restaurant and a top Denver Chinese restaurant overall.***
>
> *If you want the single best bet for traditional Sichuan heat and flavor, **Wok Spicy is the safest recommendation** from the current results."*

A Michelin-recognized restaurant with four years of Sichuan cooking lost the top spot to a suburban restaurant **because Wok Spicy's website says the word "Sichuan" clearly, and yours doesn't.** That's not a kitchen problem. That's a website problem. And it's fixable in a single afternoon.

When we asked Perplexity about the 2025 Denver Bib Gourmand list, Hop Alley appeared — but alphabetized, undifferentiated, and cited as one of ten. The three-peat streak isn't mentioned, because the site has nothing machine-readable to claim it with.

**This is the whole audit in one sentence: your kitchen has earned everything, and your website hasn't been updated to match.**

---

## Urgency: the 2026 Michelin Guide releases this fall

The 2026 Michelin Guide for Colorado is expected to release in September or October. Queries like "michelin restaurants denver 2026" will surge the week it drops. Today, those queries don't find hopalleydenver.com — they find Eater, Westword, 9News, and the Michelin Guide itself. The award schema fix below takes about 30 minutes. If we ship it before September, Hop Alley is positioned to appear in rich results and AI recommendations the moment the 2026 guide lands.

---

## Five things to fix this week

These are all small, all specific, all change the trajectory of your discoverability without touching the menu or the kitchen.

### 1. Replace the three schema blocks with one `Restaurant` block (30 minutes)

Your homepage has three separate JSON-LD schema blocks right now (`WebSite`, `Organization`, `LocalBusiness`). Replace them with a single `Restaurant` block that includes:

- `servesCuisine: ["Chinese", "Sichuan", "Regional Chinese"]`
- `priceRange: "$$$"`
- `acceptsReservations: true`
- `award[]` — all seven accolades, one per line
- `menu: "https://hopalleydenver.com/menus"` (pointing to a real HTML menu — see #4 below)
- `employee` — a `Person` block naming Tommy Lee as Chef and Owner
- `sameAs` — Facebook (update from the broken `?fref=ts` URL), Instagram (`@hopalleydenver`), Michelin Guide URL, and Tock

The full copy-pasteable block lives in the technical appendix of this audit. One paste into Squarespace → Settings → Advanced → Code Injection → Header. That's the fix.

**What this unlocks:** Knowledge Panel accolade rows in Google search. Rich-result eligibility for "michelin restaurants denver" and "bib gourmand denver." First-party claim on Sichuan positioning, which is what's currently being handed to Wok Spicy.

### 2. Add a meta description to the homepage (5 minutes)

Your homepage has no meta description. Google's SERP preview is guessing from scraped text. Draft:

> Michelin Bib Gourmand Chinese restaurant in Denver's RiNo — three-time Bib Gourmand (2023, 2024, 2025), 2025 James Beard semifinalist for Outstanding Wine & Beverage. Regional Sichuan cuisine, six-seat Chef's Counter, reservations via Tock.

### 3. Fix the Tock / Resy contradiction (10 minutes)

Your homepage CTA says "RESERVATIONS VIA TOCK." Your large-party page says "Reservations are available 14 days in advance through Resy.com." One of these is wrong. For a Michelin property, a customer hitting a dead Resy link after reading about your large-party policies is a trust-killer that costs a booking. Pick Tock, update the large-party page, done.

### 4. Fix the broken delivery link and drop Postmates (15 minutes)

Your homepage copy reads `[delivery available through Ubereats, postmates & doordash]` — and the link points to hopalleydenver.com itself (a self-loop). Postmates was absorbed by Uber Eats in 2020; listing it separately is dated. Replace with three live links to your actual Uber Eats, DoorDash, and (if applicable) Grubhub storefronts.

### 5. Uncle Ramen: two-minute emergency fixes (yes, both of them)

We audited Uncle Ramen as part of this — Tommy's sister concept. Two things need immediate attention:

- **Your H1 tag on the homepage literally reads `Copy of HOME`.** This is a Squarespace template placeholder that was never replaced. Customers don't see it, but Google does. It's the first thing crawlers read.
- **Your phone number link is broken.** The `tel:` anchor dials a 10-digit number missing the last digit — anyone clicking the phone link from a phone dials nothing.

Both are two-minute fixes. Listed here because if nothing else lands from this audit, these land today.

---

## Revenue channels you're leaving on the table

### Chef's Counter — a zero-competition page

Your six-seat tasting counter with Doug Rankin is, to our knowledge, the only Chinese tasting-menu concept in Denver. We checked: **you rank #1 for "chinese tasting menu denver"** — and that query has effectively zero competition because the category barely exists.

But right now there's no landing page to cement the rank, no Doug Rankin bio, no Person schema, no photos of the counter or the food, no booking-CTA above the fold. You're ranking #1 on a category you could own uncontested, with nothing on the site built to capitalize.

Recommended: `/chefs-counter` — Rankin's bio (Bar Chelou / José Andrés / Ludo Lefebvre lineage), a photo of the counter, menu format explanation, Tock deep-link, and press pull-quotes from New Denizen and Westword who have already written about it.

### HTML menus (five of them)

All five menus (main, vegan, pescatarian, vegetarian, gluten-free) live as Canva PDF links. **Google can't index Canva content.** Every query for "mapo tofu denver," "vegan chinese denver," "gluten free chinese denver," "dan dan noodles denver" bypasses your site — even though you serve every single one of those dishes. Converting to HTML menus (you already have the content) unlocks discovery for every dish name and every dietary variant on your menu.

This is a half-day of work for a web person. It pays back every time someone searches for a dish by name.

### The "Sichuan (Szechuan)" spelling fix

Searcher behavior is split between "Sichuan" (the transliteration Hop Alley uses) and "Szechuan" (the older spelling still dominant in Denver autocomplete). Writing "Sichuan (Szechuan)" once in your hero copy, once in schema, once in the meta description captures both variants without compromising your brand voice.

---

## How AI is recommending your competitors

Perplexity is where a growing share of restaurant discovery is happening — people asking "best X in Y" and taking the answer at face value. The "best sichuan restaurant denver" quote we opened with is the headline. Here's what it actually means for a restaurant owner:

The restaurant Perplexity recommends first — Wok Spicy — has no Michelin recognition, no James Beard recognition, no Bib Gourmand, no national press. It wins because it **says what it is, clearly, on its homepage**: *"authentic Sichuan cuisine."* That's all it took.

Hop Alley says, at the top of the homepage: *"Hop Alley is a new restaurant concept from Tommy Lee and the Uncle team that serves traditional, regional Chinese cuisine served family-style as well as dishes with a unique spin on other Asian ideas."*

Rewritten:

> Hop Alley is a regional Chinese restaurant in Denver's RiNo district, specializing in Sichuan (Szechuan) cooking, with three consecutive Michelin Bib Gourmands (2023–2025) and 2025 James Beard Foundation recognition for our wine program. Chef Doug Rankin leads our six-seat Chef's Counter tasting menu.

Three sentences. Every keyword a Sichuan or Michelin searcher would use is in there. Every credential is in there. Nothing about the food or the service has changed — only the way the site makes itself legible to the people and machines deciding who to recommend.

---

## Where AI fits in (not just marketing-speak)

A few small, specific ways to put AI to work on the site itself — not a chatbot, not a gimmick:

- **An FAQ page** — five questions you already get asked (Michelin star? tasting menu? dietary? hours? Tock or Resy?) in a schema-marked FAQPage. Perplexity and Claude quote FAQ answers verbatim. It's the highest-ROI AI-discoverability move for restaurants.
- **An `llms.txt` file** — one markdown file at hopalleydenver.com/llms.txt that tells AI crawlers, in plain language, what Hop Alley is and what pages matter. It's an emerging standard that few restaurants have yet, and it pays off more as AI search matures.
- **`AggregateRating` schema** — you have 4.5+ stars on OpenTable, Yelp, and Google. Declaring those ratings first-party enables star snippets directly in Google search results.

All three are in the technical appendix as copy-paste templates.

---

## The housekeeping list

Small things, in order of how much they matter:

- **Two H1 tags per page** (`Hop Alley` + `FOLLOW US`) — rewrite to one H1 per page, demote `FOLLOW US` to a section heading.
- **`openingHours` trailing comma** breaks schema parsing after Saturday.
- **4 of 12 homepage images have empty alt text** — both an SEO leak and an accessibility fail on a visually-led restaurant.
- **Typos**: "RESERVATIONS VIA TOCk" (lowercase k), inconsistent "Bar Chelou" / "Petit Chelou" capitalization.
- **Instagram embed shows four posts from May 2022.** Either pull a live feed or remove the embed.
- **`/home-3` in the sitemap** looks like an unpublished draft leaking to crawlers.
- **No analytics installed** — no GA4, no Meta Pixel, no Squarespace Analytics surfaced. You're flying blind on website conversion for a property that books six nights a week.
- **Chef's Counter gets two paragraphs mid-page.** For the highest-margin product on your menu, it should have its own page (already covered above).
- **No press/reviews section.** Your Michelin, JBF, and 5280 mentions are plain text. A proper press wall with logos + outbound links + pull-quotes takes an afternoon and reads like a Michelin-tier site should.

---

## What's next

This audit is part one of a three-part package. What comes next:

- **Redesign mockups** — homepage + a Chef's Counter page, using your actual brand assets and photography, with every fix above wired into the design.
- **Intelligence dashboard** — a preview of what ongoing tracking would look like for Hop Alley: keyword position, Perplexity visibility, schema coverage, Michelin Guide outbound link clicks, and the metrics that actually correlate with reservations.

Both are coming in the next few days. If anything in this document raises a question or there's a fix you want prioritized, text or email back — we'll adjust.

---

*All findings in this audit are sourced from your live website as of April 15, 2026. Technical appendix with copy-pasteable schema blocks, `llms.txt` template, FAQ schema, and source artifacts available on request.*
