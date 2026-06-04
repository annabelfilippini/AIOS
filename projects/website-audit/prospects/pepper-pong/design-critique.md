# Pepper Pong — Design Critique & Redesign Plan
**Date:** 2026-04-13 | **Reference site:** glossier.com | **Step 5 of BUILD-PLAN.md

## Design Critique Summary

Pepper Pong's current site feels like a Shark Tank product still in launch mode — every page screams "BUY THIS!" with heavy red, ALL CAPS, and high information density. The product and brand story are genuinely great. The design undersells them.

**Reference comparison:** Glossier trusts its product. Big lifestyle photography, generous whitespace, restrained color, editorial typography. Visitors feel like they're discovering something worth wanting, not being sold to. Pepper Pong has equally strong bones (brand voice, social proof, founder story) — the design just doesn't let them breathe.

---

## Page-by-Page Visual Critique

### Homepage — Grade: C+
**The core problem:** Too many things competing for attention. Hero video, press marquee, product callout, "100K+ sold" badge, "SEE WHY" section, "WHAT THE @%$& IS", "EVERYONE GOES FROM SKEPTIC TO OBSESSED", video wall, "WHERE WILL YOU RALLY?" — all fighting for the same eyeballs on a single scroll.

| Issue | Severity | Glossier Contrast |
|-------|----------|-------------------|
| ALL CAPS headings throughout — no typographic hierarchy | High | Glossier uses bold display type for ONE headline per section, body text is calm |
| No whitespace between sections — everything is edge-to-edge | High | Glossier has 80-120px padding between sections minimum |
| Video wall (21 thumbnails) with no context or curation | Medium | Glossier never shows a grid of 21 things. 3-4 items max per visual section |
| Press marquee bar is loud (red background, animated scroll) | Medium | Glossier's brand partner displays are subtle — logo strip on white |
| Red (#ED1846) used for everything: backgrounds, text, buttons, bars | High | Glossier uses one accent color sparingly. Background is mostly white/cream |
| No clear visual hierarchy — what should I look at first? | High | Glossier's homepage has a clear reading order: hero → product → story → shop |
| Hero video auto-plays behind text — distracting, hurts load time | Medium | Glossier's hero is a static editorial photo with bold type overlay |
| Mobile: hero cuts at marquee bar, may not entice scroll | Medium | Glossier mobile: full-bleed hero photo with one clear CTA visible |

**What's working:** Brand voice ("skeptic to obsessed"), social proof numbers, the energy is there. The conversion narrative is smart — it just needs visual breathing room.

### Product Page (Full Set) — Grade: B
**The core problem:** Standard Shopify template. Functional but not elevated.

| Issue | Severity | Glossier Contrast |
|-------|----------|-------------------|
| Product images are small and catalog-style | Medium | Glossier: hero product shot takes up 50%+ of viewport |
| "SOLD OUT 3X IN 3 MONTHS" is body text, not a design element | Medium | Glossier makes social proof visual — "2M+ sold" as a styled badge |
| Price presentation differs mobile vs. desktop (strikethrough vs. not) | Low | Consistent pricing treatment across breakpoints |
| "What's Inside" icons are effective but small | Low | — (Pepper Pong does this well) |
| FAQ accordion at bottom is good but visually plain | Low | — |

**What's working:** "What's Inside" breakdown, "QUESTIONS YOUR MOM WOULD ASK" FAQ section, comparison grid, trust badges. This page converts — the audit said conversion isn't the problem.

### Our Story — Grade: D+
**The core problem:** The most compelling story on the site gets the laziest design treatment.

| Issue | Severity | Glossier Contrast |
|-------|----------|-------------------|
| Pink diagonal stripes background — dated, clip-art feel | High | Glossier about: intimate close-up photography, editorial layout |
| Page is very short (~400px of content) | High | Story pages should be the longest, richest pages on a brand site |
| No photos of Tom playing, building, or on Shark Tank | High | Glossier about: photography IS the page |
| "GET IN ON THE SPICY GAME" CTA disconnects from emotional recovery story | Medium | CTAs should match the emotional tone of the content above them |
| Rally 4 Recovery section feels tacked on, not integrated | Medium | — |
| No growth milestones, no team, no journey arc | High | — |

**What's working:** The recovery narrative is genuinely moving. "MORE THAN A GAME" headline is strong. The Rally 4 Recovery program is a real differentiator.

### Press — Grade: B+
**The core problem:** Strongest visual page but article cards are too small.

| Issue | Severity |
|-------|----------|
| Article cards cramped, hard to read | Medium |
| No direct links to external coverage visible | Medium |
| Shark Tank hero image is the right move | — (working) |

### Schools — Grade: B+
**The core problem:** Best-structured page on the site but invisible (NOT IN MAIN NAV).

| Issue | Severity |
|-------|----------|
| Not in navigation — $599 product invisible to educators | High (audit #2 priority) |
| SEL research and educator messaging is strong | — (working) |
| Volume pricing widget is clear | — (working) |

### Reviews — Grade: D
Raw Judge.me embed. No brand wrapper, no curated highlights, no filtering. Looks like a default theme page.

### FAQ — Grade: B-
Clean accordion, great brand voice. No category grouping, no search, no FAQ schema (audit finding).

### How to Play — Grade: B
Lifestyle photo is good, video tutorial is smart. "A LEVEL PLAYING FIELD" philosophy section adds depth. Hero text overlaps image on some viewports.

---

## Redesign Strategy

### Highest-Impact Pages to Mock Up

**1. Homepage** — Every visitor sees it. Currently the weakest design relative to the strength of the underlying brand. The gap between what Pepper Pong IS (fun, energetic, social, Shark Tank-validated) and how the homepage FEELS (infomercial, cluttered, loud) is the biggest design opportunity.

**2. Our Story** — The most under-invested page given the most compelling content. Tom's recovery story + Shark Tank + Rally 4 Recovery = a brand narrative most companies would kill for. Currently wasted on pink stripes and 400px of text.

### Design Principles (Extracted from Glossier, Applied to Pepper Pong)

These are NOT about making Pepper Pong look like Glossier. Glossier is beauty/skincare. Pepper Pong is an energetic game. But the principles translate:

1. **One thing per section.** Each scroll-stop has ONE message, ONE visual, ONE action. Not three headlines competing.
2. **Photography does the selling.** Big lifestyle shots of people playing, laughing, rallying. Let the joy sell itself.
3. **Whitespace = confidence.** A brand that gives its content room to breathe says "we trust our product." Cramming says "please buy before you leave."
4. **Color restraint.** Use Pepper Pong Red (#ED1846) for ONE purpose: the primary CTA button. Everything else: white, charcoal (#1a1a1a), warm gray. The red pops when it's rare.
5. **Typography hierarchy.** Gotham Black for the ONE headline per section. Inter Regular for body. Not every line needs to shout.
6. **Progressive disclosure.** Don't show 21 videos — show 3 with a "See all" link. Don't list every feature — show the hero benefit and let them explore.
7. **Audit findings drive priorities.** The redesign isn't just visual — it addresses: vocabulary mismatch (add "tabletop game" / "mini pickleball" language), missing Schools nav link, buried social links, unclear CTA hierarchy.

### Brand Assets

| Asset | Value |
|-------|-------|
| Primary Red | #ED1846 |
| Orange | #FF571A |
| Navy | #2C5184 |
| Sky Blue | #5AC4F2 |
| Headings | Gotham (400-900) |
| Body | Inter (400/500/700) |
| Voice | Spicy, playful, irreverent — "Rally," "Peppers," "QUESTIONS YOUR MOM WOULD ASK" |
| Social proof | 4.95 stars / 211+ reviews / 100K+ sold / Shark Tank S16 |
| Key imagery | People playing at tables, Shark Tank footage, Tom/founder, classroom settings |

---

## Next: Build Mockups

1. Homepage redesign (HTML, using brand assets, Glossier principles, audit-informed)
2. Our Story redesign (HTML, photography-led, full journey narrative)
