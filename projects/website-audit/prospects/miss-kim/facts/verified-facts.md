# Verified Facts — Miss Kim Ann Arbor
Scraped 2026-04-19. Every fact cites a source file in this directory (or a sibling `scrape/` file).

## Sources
- ✓ Yelp — facts/yelp.md (4.0 / 373 reviews, 676 photos, strong review quotes + menu pricing)
- ✗ OpenTable — facts/opentable.md (scrape returned a 404 / bot-walled; no reservation page content recovered)
- ✓ Google knowledge panel + web results — facts/google-search.md (4.4 / 838 Google reviews, GBP hours, Zingerman's blog excerpt)
- ✓ Zingerman's profile — facts/zingermans-profile.md (NYT Eric Kim + Matt Rodbard Apr 2024 press, Cacio e Pepe Tteokbokki Jan 2025 blog reference)
- ✓ Own site homepage — scrape/homepage.md (hours, address, phone, parking copy, sister-concept positioning)
- ⚠ Own site /about, /menu, /contact, /private-events, /reservations — scrape/*.md (reCAPTCHA-walled or 404; only hero/links recovered)

## Identity
- Legal name: Miss Kim Korean Restaurant [source: scrape/homepage.md; images.logoAlt in scrape/branding.json]
- Tagline (own site hero): "Really Great Korean Food" [source: scrape/homepage.md]
- Sister-brand tagline (Zingerman's nav): "Really great Korean food and drink" [source: facts/zingermans-profile.md]
- Google descriptor: "Trendy spot for traditional Korean fare with a modern, seasonal twist in contemporary surrounds." [source: facts/google-search.md]
- Google category + price: Korean restaurant, $20–30 per person (reported by 27 people) [source: facts/google-search.md]
- Yelp category: Korean, Tapas/Small Plates, $$$ [source: facts/yelp.md]
- Address: 415 N. Fifth Ave, Ann Arbor, MI 48104 [sources: scrape/homepage.md, facts/yelp.md, facts/google-search.md]
- Neighborhood: Kerrytown Ann Arbor / located in Kerrytown Market & Shops [sources: facts/yelp.md, facts/google-search.md]
- Phone: (734) 275-0099 [sources: scrape/homepage.md, facts/yelp.md, facts/google-search.md]
- Email: misskim@zingermans.com [sources: scrape/homepage.md, facts/google-search.md (Facebook panel)]
- Website: misskimannarbor.com [source: scrape/homepage.md]
- Opened: 2016 [source: facts/google-search.md — "From Miss Kim" blurb: "opened in 2016"]

## Hours (exactly as published on own site)
- Monday — 11:30 am – 9:00 pm [source: scrape/homepage.md]
- Tuesday — Closed [source: scrape/homepage.md]
- Wednesday — 11:30 am – 9:00 pm [source: scrape/homepage.md]
- Thursday — 11:30 am – 9:00 pm [source: scrape/homepage.md]
- Friday — 11:30 am – 9:30 pm [source: scrape/homepage.md]
- Saturday — 11:00 am – 9:30 pm [source: scrape/homepage.md]
- Sunday — 11:30 am – 9:00 pm [source: scrape/homepage.md]
- Cross-confirm: Google GBP hours match own-site exactly [source: facts/google-search.md]
- Holiday hours (own-site): "12/23 through 12/25: Closed" and "12/30 through 1/1: Closed" [source: scrape/homepage.md]
- Annual winter break: "We're closed for our annual winter break from January 1-January 10" [source: facts/yelp.md — Winter Break 2023 update]

## Reservations / Ordering
- OpenTable reservation link: https://www.opentable.com/r/miss-kim-korean-restaurant-reservations-ann-arbor?restref=1210180 [source: scrape/homepage.md, scrape/reservations.md]
- Toast online ordering: https://misskimannarbor.com/order (Toast-powered — inferred from Toast CDN on images + "Order Now > reCAPTCHA" on own pages) [source: scrape/homepage.md, scrape/branding.json]
- Third-party delivery: GrubHub, SnackPass, Chowbus [source: facts/yelp.md — "About the Business" copy]
- Reservation CTA copy (verbatim): "Reservations are highly encouraged. Check out our reservation page or give us a call at 734.275.0099 for more info!" [source: scrape/homepage.md]
- Takes reservations: yes [source: facts/yelp.md]
- Walk-ins (historically, 2016 soft-open note): "Walk-ins are welcome Tues-Sun" [source: facts/google-search.md — People-also-ask citing Instagram post]

## Team
- Chef Ji Hye Kim — founder / chef-owner (confirmed by both Google knowledge panel and homepage image alt "Chef Ji Hye") [sources: facts/google-search.md, scrape/homepage.md]
- Background: "Chef Ji Hye Kim grew up in Seoul, South Korea and is obsessed with ancient Korean culinary texts and the finer points of fermentation." [source: facts/google-search.md — "From Miss Kim" blurb]
- Connection to Zingerman's: Miss Kim is "a proud part of the Zingerman's Community of Businesses" (ZCoB), listed alongside Zingerman's Deli, Roadhouse, Bakehouse, Coffee Company, Creamery, Cornman Farms, Candy Manufactory, Mail Order, Press, Catering, Food Tours, Greyline, BAKE!, and ZingTrain [sources: facts/google-search.md, facts/zingermans-profile.md]
- Opening year: 2016 [source: facts/google-search.md]
- James Beard connection: the homepage hero photo file is titled `jamesbeard.jpg` (alt: "Chef Ji Hye") [source: scrape/homepage.md line 114] — filename implies a James Beard honor, but NO scrape source (Yelp, Google, Zingerman's) explicitly states "semifinalist" or "nominee." Treat as visual/photo credit only — (nomination status not verified in this scrape set).

## Menu (signature + anchor dishes)

**Review-walled menu page.** scrape/menu.md is a reCAPTCHA stub. Items below come from the Yelp "Popular Dishes" grid (with prices), Yelp review quotes, Google knowledge panel "Products," and the Zingerman's blog reference.

**Popular dishes with prices** [all from facts/yelp.md — "Popular Dishes" grid]:
- Street Style Tteokbokki — $19 (13 photos, 15 reviews) [source: facts/yelp.md]
- Cacio e Pepe Tteokbokki — $18 (6 photos, 4 reviews) [source: facts/yelp.md]
- Kimchi Pork Fried Rice — $24 (10 photos, 12 reviews) [source: facts/yelp.md]
- Kids Soy Butter Rice w/ Egg — $8 (20 photos, 30 reviews — highest-review menu item on Yelp) [source: facts/yelp.md]
- Moo Radish Kimchi — $5 (6 photos, 7 reviews) [source: facts/yelp.md]

**Frequently-mentioned dishes (no direct Yelp grid price — pulled from review quotes and Yelp photo categories):**
- Korean Fried Chicken — soy glaze option; 42 reviews, 29 photos [source: facts/yelp.md]
- Pork Belly — 50 reviews, 27 photos [source: facts/yelp.md]
- Fried Tofu / Korean Fried Tofu Sandwich (on challah bun, w/ jalapeño and spicy mayo, ~$15) [source: facts/yelp.md — photo caption]
- Beet + Avocado Salad — ~$14 — "Roasted local beets, avocado, pickled red onions, toasted walnuts, garlic dressing" [source: facts/yelp.md — photo caption]
- Crispy Broccolini / Fish Caramel Broccolini [source: facts/yelp.md — review quotes]
- Buddhist Lotus Roots [source: facts/yelp.md]
- Mushroom / Steamed / Pork / Bao Buns [source: facts/yelp.md]
- Braised Short Ribs / Baby Back Ribs [source: facts/yelp.md]
- Bibimbap [source: facts/yelp.md — Emmit P. review, Dec 12 2025]
- Mushroom Japchae [source: facts/yelp.md — Linda I. review]
- Smoked Tofu & Mushroom Bibimbap / Vegetarian & GF Royale Style Tteokbokki / Kimchi Rice Balls [source: facts/yelp.md — Alina S. review]

**Daily / weekly specials** [source: facts/google-search.md — "Products" panel]:
- Wednesday Chicken Dinner Special — $20
- Tuesday Banh Mi Special — $13
- Ssam Plates (new to dinner menu) — $22–$29

**Signature dish featured on Zingerman's blog Jan 2025**:
- Cacio e Pepe Tteokbokki [source: facts/zingermans-profile.md — "Cacio e Pepe Tteokbokki at Miss Kim… A Southern Italian Twist on a Korean Classic"]

**Most-popular per Zingerman's (Oct 2025 blog, quoted in Google People-Also-Ask)**:
- "As in Korea, one of the most popular dishes at Miss Kim has been the spicy, pork-scented, gochujang-laced Street Style Tteokbokki." [source: facts/google-search.md — People-also-ask referencing zingermanscommunity.com 2025/10 "Royale Style Tteokbokki at Miss Kim"]

**Sourcing / philosophy**:
- "Korean-inspired food made with local Michigan ingredients!" [source: facts/yelp.md — "About the Business"]

**Beverage**:
- Makku (Korean rice beer) [source: facts/yelp.md — Sergio R. review]
- "Kpop demon hunters themed 'gonna be golden' hot toddy with apricot brandy" [source: facts/yelp.md — Kirsten F. Dec 4 2025 review — drink programming cue]
- "Many unique alcoholic and non-alcoholic beverages" [source: facts/yelp.md — Linda I. review]

## Verified Review Quotes

All quotes verbatim from facts/yelp.md. Attribution + date preserved.

1. "An absolute gem of a restaurant in Ann Arbor. The food is so tasteful and delicious. The staff is so friendly and kind. I love the coziness and vibe and always have the best time when I eat there!" — Alina S., Elite 26, Ann Arbor MI, Dec 17 2025 (updated review) [source: facts/yelp.md]

2. "The food here is so fresh and classic Korean with a little twist sometimes. It's the perfect balance of salty, spicy, umami in every bite." — Kirsten F., Elite 26, Troy MI, Dec 4 2025 [source: facts/yelp.md]

3. "Outstanding! Love the food, the care and intention that goes into the food, the friendly service, and the whole dining experience at Miss Kim. Be aware that this is a nice, leisurely meal! And budget time accordingly :)." — Linda I., Elite 26 / All-Star, MI, Oct 25 2025 [source: facts/yelp.md]

4. "The soy butter rice was a stand out. My wife says 'that is the best rice I've ever had.' I enjoyed a Makku with my meal. It's a tasty Korean rice beer." — Sergio R., Elite 26, Jan 30 2026 [source: facts/yelp.md]

5. "Service is always exceptional here, being as it's associated with Zingermans so the staff are well trained, attentive and knowledgeable, and food comes out perfect. We will be going here as many times as we can squeeze in a trip over to A2." — Kirsten F., Elite 26, Dec 4 2025 [source: facts/yelp.md]

6. "Tteokbokki (street style is my favorite but I bet they're all great). The TEXTURE and flavor of this is the best." — Linda I., Elite 26, Oct 25 2025 [source: facts/yelp.md]

7. "Broccolini!! Not sure how they get these both so tender and soo crispy at the same time. The flavor combinations with the fish sauce and sweetness is phenomenal." — Linda I., Elite 26, Oct 25 2025 [source: facts/yelp.md]

**Google knowledge-panel review snippets** [source: facts/google-search.md]:
- "Fresh food, great people and place, tips are included in the price." — Jenny V.
- "Went for a work party and we were thrilled with the quality and service." — Jef Saunders
- "Highly recommend the smashed potatoes, KFC, and the street style tteokbokki" — Peter Ng

## Press
- NYT writer Eric Kim visit, April 2024 [source: facts/zingermans-profile.md — "April 30 in Ann Arbor: Three Cooks, Two Dinners, One… NYT writer Eric Kim and award-winning author Matt Rodbard come…"]
- Matt Rodbard (Koreaworld author) — same April 2024 event [source: facts/zingermans-profile.md]
- Zingerman's blog feature: "Cacio e Pepe Tteokbokki at Miss Kim — A Southern Italian Twist on a Korean Classic," posted Jan 2025 (blog-date listed as Nov 15 2024 on Zingerman's profile banner; image filepath `2025/02/cacio-e-pepe.jpg`) [source: facts/zingermans-profile.md]
- Zingerman's blog feature: "Royale Style Tteokbokki at Miss Kim," Oct 2025 [source: facts/google-search.md — People-also-ask citation]
- Ann Arbor Restaurant Week, January 21–26 2024 — "Miss Kim and the Roadhouse offer up delicious deals" [source: facts/zingermans-profile.md]
- Travel Muse Magazine, March 17 2026 — "Where Tteokbokki Meets Memories: Dining at Miss Kim"; quote: "Booths and communal tables create an inviting, shared atmosphere. Miss Kim is known for its family dining style." [source: facts/google-search.md]
- James Beard — (not verified in this scrape set; only the `jamesbeard.jpg` filename on the homepage hints at it)

## Sister properties
- Little Kim (vegetarian) — littlekimannarbor.com — tagline "Really great vegetarian food" [source: facts/zingermans-profile.md — ZCoB nav]
- Wider Zingerman's Community of Businesses family: Zingerman's Delicatessen, Roadhouse, Bakehouse, Coffee Company, Creamery (Cornman Farms), Candy Manufactory, Mail Order, Press, Catering & Events, Food Tours, Greyline, BAKE!, ZingTrain [source: facts/zingermans-profile.md]

## Social
- Instagram: @misskimannarbor [sources: scrape/homepage.md, facts/google-search.md]
- Facebook: facebook.com/misskimannarbor (3.1K+ followers; 4.9 / 60 votes) [source: facts/google-search.md]
- TikTok: @misskimannarbor [source: facts/google-search.md]
- LinkedIn: linkedin.com/company/misskimannarbor [source: facts/google-search.md]

## Ratings (live)
- Google: 4.4 / 838 reviews [source: facts/google-search.md]
- Yelp: 4.0 / 373 reviews (676 photos) [source: facts/yelp.md]
- Facebook: 4.9 / 60 votes [source: facts/google-search.md]

## Signature moments / Programming
- Monthly chef pop-ups — verbatim: "Each month we're inviting some incredible local Chefs to pop-up in the Miss Kim kitchen and share their incredible food with you!" [source: scrape/homepage.md]
- Cacio e Pepe Tteokbokki as Italian-Korean crossover signature [source: facts/zingermans-profile.md]
- Monthly Zingerman's blog rhythm — Miss Kim dishes covered Jan 2025 and Oct 2025 [sources: facts/zingermans-profile.md, facts/google-search.md]
- Large-party / catering inquiry form (Google Forms) [source: scrape/homepage.md]

## Parking / access (verbatim from homepage)
> "Our street address is on Fifth Avenue but our entrance is closer to Kingsley and directly off of the one way parking lot located at Kingsley (entrance) and Fourth Ave (exit). We suggest that you park in this small lot when you come to pick up your food." [source: scrape/homepage.md]
>
> "If you've already parked on Fifth, you can still find us by walking all the way through the courtyard between Sweetwaters and Found to the small parking lot on the other side." [source: scrape/homepage.md]

## Amenities (Yelp attributes)
- Trendy, Casual, Moderate noise, Good for kids, Outdoor seating, Good for groups [source: facts/yelp.md]
- Takes reservations, Offers delivery, Offers take-out [source: facts/yelp.md]
- Service options (Google): Outdoor seating, Great cocktails, Vegan options [source: facts/google-search.md]

## Atmosphere
- "Booths and communal tables create an inviting, shared atmosphere. Miss Kim is known for its family dining style." — Travel Muse Magazine Mar 17 2026 [source: facts/google-search.md]
- Homepage copy: "Nestled in the heart of Ann Arbor, MI, Miss Kim Korean Restaurant exudes warmth and welcomes guests with open arms. With its cozy atmosphere, friendly staff, and a menu bursting with mouthwatering dishes, it's the perfect place to unwind and savor a delightful meal." [source: scrape/homepage.md]

## Known gaps (flagged for Phase B)
- James Beard status: image filename `jamesbeard.jpg` on homepage, but no scraped source confirms semifinalist / nominee / award — do NOT write "James Beard nominee" into mockup without external verification.
- OpenTable detail (seat counts, menu PDFs): bot-walled (facts/opentable.md is a 404).
- Full menu text: reCAPTCHA-walled on own site; only dishes mentioned in reviews / Yelp grid / Google products are verified.
- Little Kim positioning: confirmed as vegetarian sister concept, but no product detail was scraped.
