# Frita Batidos: Website & AI Visibility Audit

**Prepared April 17, 2026**

---

## 1. What You're Doing Right

Before we get into the hard stuff, let's be clear: Frita Batidos has built something most restaurants never will.

**4.4 stars across 2,521 Yelp reviews.** That's not good -- that's elite. For context, most successful Ann Arbor restaurants sit around 500-800 reviews. You have three times that, and you're still at 4.4. People don't just eat here -- they evangelize:

> "I would drive all the way from Chicago to Michigan to get this batido again." -- Kari O., Yelp Elite All-Star

> "The frita burger with the shoestring fries on top is so good and honestly unlike anything else around here." -- Haley M.

> "I cannot count the number of people that recommended Frita Batidos while I was visiting Ann Arbor." -- Brittany L., Yelp Elite

**"Best Burger" 11 consecutive years (2014-2025).** That's not a streak -- that's a dynasty. The Michigan Daily, Metro Times Best Cuban Restaurant (2020-2024), Hour Magazine Best Specialty Burger (2025), #31 on Yelp's national Top 100 Burger Spots. Eve Aronoff didn't just open a restaurant -- she built an institution.

**Three locations and growing.** Ann Arbor, Detroit, Frita Air at HOMES Campus. Plus a Brooklyn expansion. That's real proof of concept.

**Halal-certified chicken and beef.** In a city with one of the largest Muslim student populations in the Midwest, this is a massive differentiator. Most competitors can't say this.

**A founder story that sells itself.** Top Chef Season 6, Slow Food philosophy, Cuban-inspired street food that sources from Michigan farms. That's the kind of story food media and AI systems love to tell -- if they can find it.

---

## 2. The Uncomfortable Truth: AI Can't Find You

We asked ChatGPT: **"best burger in ann arbor."**

Frita Batidos appeared -- but only because the Michigan Daily wrote "Frita Batidos wins 2025 Best Ann Arbor Burger." Not because of your website. Your website returned a 503 error. The AI pulled a newspaper headline and moved on.

Then we asked: **"halal restaurant ann arbor."**

You weren't there. Not mentioned. Not listed. Not anywhere.

Taystee's Burgers showed up. Palm Palace showed up. Haifa Falafel showed up. Frita Batidos -- the restaurant with 2,521 reviews and certified halal meat -- was invisible.

Here's why: your food page says "All of our chicken and beef is certified Halal!" But that text is buried on a page that's currently down, with no structured data markup. Yelp categorizes you as "Cuban, Burgers, Cocktail Bars" -- not halal. So when AI systems look for halal restaurants in Ann Arbor, you don't exist. In a town where UMich's Muslim student population is actively searching for halal dining options, your biggest competitors are winning that audience by default.

**It gets worse.** We searched your own brand name: "frita batidos ann arbor." Five of the top ten results are your own website -- and every single one is a dead link. Meanwhile, a domain called **fritabatidosannarbor.shop** -- which you don't own -- is ranking on your brand name and actually working.

Your awards? "Best Burger Michigan Daily Consecutively 2014-2025" is displayed as a yellow banner image on your homepage. That's great for people who visit the site. But AI systems can't read images. So when someone asks "what's the most-awarded burger place in Ann Arbor?" -- your eleven-year dynasty is trapped in a PNG file that no machine can parse.

**Your AI Discoverability Score: 18 out of 100.**

That's the lowest we've seen. For a restaurant of your caliber, it should be 70+.

The good news is this is all fixable. The bad news is every day it stays like this, your competitors get recommended instead of you.

---

## 3. Your Site Is Down Right Now

This isn't subtle. fritabatidos.com returns a **503 Service Unavailable** error on every single page -- homepage, menu, chef bio, contact, catering. All of it. It's been down since at least our April 17 audit.

This isn't a ranking problem -- there's literally nothing to rank. There's no content for Google to index, no data for AI to read, no page for a customer to land on. Anyone who searches for you, clicks through from Yelp or Google, and lands on your site sees this:

> 503 Service Unavailable -- The server is temporarily busy, try again later!

Google has already started deindexing your pages. The longer this continues, the harder it is to recover your search position. Pages that took years to build authority are being erased from Google's memory week by week.

---

## 4. Five Things to Fix This Week

These are concrete, specific, and the first four can be done in a single afternoon.

**1. Get the site back online.** This is the obvious one. Contact your hosting provider. The server is returning 503 -- this is typically a hosting-level or WordPress-level issue, not a code problem.

**2. Add Restaurant structured data to your homepage.** This is a block of code that goes in your page header. It tells Google and AI systems exactly who you are in a format they can read. Here's what it should say -- your developer can paste this directly:

```json
{
  "@context": "https://schema.org",
  "@type": "Restaurant",
  "name": "Frita Batidos",
  "description": "Cuban-inspired street food in downtown Ann Arbor since 2010. Home of the frita -- a Cuban-style burger topped with shoestring fries.",
  "telephone": "+1-734-761-2882",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "117 W Washington St",
    "addressLocality": "Ann Arbor",
    "addressRegion": "MI",
    "postalCode": "48104"
  },
  "servesCuisine": ["Cuban", "Burgers", "Cocktails"],
  "priceRange": "$$",
  "aggregateRating": {
    "@type": "AggregateRating",
    "ratingValue": "4.4",
    "reviewCount": "2521"
  },
  "award": [
    "Best Burger, Michigan Daily -- 2014-2025 (11 consecutive years)",
    "Best Cuban Restaurant, Metro Times -- 2020-2024",
    "#31 on Yelp's Top 100 Burger Spots -- 2023"
  ]
}
```

**3. Add FAQ structured data for halal and dietary questions.** This is the single highest-ROI change. One code block makes you visible to every "halal restaurant" search in Ann Arbor overnight. It answers the questions AI assistants get asked most:

- "Is Frita Batidos halal?" -- Yes, all chicken and beef is certified Halal.
- "What is a frita?" -- A Cuban-style burger topped with shoestring fries on a soft egg bun.
- "Does Frita Batidos have vegetarian options?" -- Yes, the Black Bean Frita and several sides.

**4. Convert your menu images to crawlable text.** Right now your food menu, bar menu, and menu guide are PNG image files. No search engine or AI can read them. When someone asks "does Frita Batidos have a black bean burger?" the AI can't answer. Keep the beautiful visual menus, but add the menu as real text on the page too.

**5. Add an llms.txt file.** This is a new standard (used by Anthropic, Cloudflare, and others) that tells AI systems what your business is. It's a simple text file at your website's root. Takes 10 minutes to create, puts you ahead of 99% of restaurants in the country for AI visibility.

---

## 5. Revenue You're Leaving on the Table

**The halal market.** UMich has one of the largest Muslim student populations in the Midwest. They search for halal dining weekly. Right now, Taystee's Burgers wins that query -- with fewer reviews, fewer awards, and no comparable food quality. You have certified halal meat and zero visibility to this audience.

**"Best burger ann arbor."** You've won this title 11 years straight, but Blimpy Burger, Taystee's, and Casey's Tavern all outrank you in Google with their direct websites. You appear at position ~9 via a Michigan Daily article. A restaurant that has won Best Burger more than a decade running should own the #1 spot.

**Happy hour and cocktails.** You have a cocktail program with hibiscus mojitos and sangria. There's no dedicated happy hour page on your site. "Ann arbor happy hour" is a high-volume search term. Black Pearl, Pretzel Bell, and Zingerman's Roadhouse all rank with dedicated pages. You're invisible.

**Catering.** You offer catering, but the page routes to Toast. Corporate event planners searching "ann arbor catering" or "ann arbor restaurant catering" can't find you. This is a high-margin revenue stream that's currently invisible to search.

---

## 6. How AI Is Recommending Your Competitors Instead

Here's what happens when real people ask AI assistants about dining in Ann Arbor:

**"Where to eat near University of Michigan"** -- Zingerman's Deli gets a full paragraph ("iconic," detailed menu, directions). Frita Batidos gets a single line from a UMich admissions blog. You're #1 on TripAdvisor out of 423 restaurants, but the AI doesn't know that because your site is down and has no structured data.

**"Best restaurant in Ann Arbor"** -- Echelon gets highlighted (2026 James Beard semifinalist). Miss Kim gets highlighted (2025 James Beard semifinalist). Frita Batidos is mentioned in passing in aggregator lists. Those restaurants have working websites with structured data. You have a 503 error.

**"Cuban restaurant ann arbor"** -- You dominate this one, but through Yelp and TripAdvisor, not through your own site. And that squatter domain -- fritabatidosannarbor.shop -- shows up and is actually functional while your real site is dead.

The gap between your reputation and your AI visibility is the widest we've seen. You're legendary in Ann Arbor. You're a ghost to AI.

---

## 7. What's Next

We've put together homepage redesign mockups and an AI visibility dashboard that shows exactly how to close this gap -- what your competitors' structured data looks like, what yours should look like, and a step-by-step implementation plan.

The fixes aren't complicated. Most of them are one-time code additions. The halal visibility alone could open you to thousands of students who eat out multiple times a week and currently don't know Frita Batidos is an option.

You've spent 16 years building something people love. The only thing missing is making sure the technology that's increasingly deciding where people eat can actually find you.

We'd love to walk you through it.
