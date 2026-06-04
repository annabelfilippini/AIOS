# Cooldown Running Redesign Brief

## Context

Cooldown wants a cleaner, easier-to-manage Shopify site. The current site has strong brand assets and community positioning, but the theme appears overbuilt: simple edits are hard, product merchandising is not clear enough, and several quick fixes from the prior audit are still unresolved.

The redesign should prioritize maintainability as much as visual polish. Bailey is interested in a fresh Shopify template approach rather than continuing to patch complex agency-built code.

## Meeting Notes

- Current Shopify site problems:
  - Product page photos are too small.
  - Color and size selection is confusing.
  - Customers think variants are sold out when they may simply have selected an unavailable color/size combination.
  - Agency-built complex code makes simple edits difficult.
- Bailey is interested in a fresh Shopify template approach.
- Annabel will access the Shopify backend to create a draft redesign.
  - Shopify login email: `bailey@cooldownrunning.com`
  - Claude Code will support website improvements.
- Announcement bar promo link still directs to the wrong page and needs a quick fix.

## Redesign Objective

Create a Shopify storefront that feels like Cooldown: colorful, social, running-first, and community-led, while being simple enough for Bailey and Anya to update without developer help.

The design should not become generic minimalist activewear. Cooldown's edge is the overlap of apparel, city chapters, social energy, and colorful product drops.

## Priority Fixes

### 1. Product Page Clarity

Problem: Product photos are too small and variant selection is confusing.

Recommended changes:
- Make product imagery the dominant element on desktop, with large images or a sticky gallery.
- Use clear color swatches with color names visible.
- Separate color availability from size availability.
- Show sold-out states only after a customer understands which color/size combination is unavailable.
- Add a short helper line near variants, such as: "choose a color first, then select your size."
- Make the selected color name explicit.
- Keep the add-to-cart area sticky or highly visible on mobile.

Product page sections to include:
- Large image gallery
- Product name, price, color selector, size selector, add to cart
- Fit note
- Fabric/features
- "Why we made this"
- Size guide
- Reviews
- Related pieces or "complete the kit"

### 2. Shopify Maintainability

Problem: Complex agency-built code makes simple edits hard.

Recommended changes:
- Test a fresh Shopify theme or a minimally customized Online Store 2.0 theme.
- Use native Shopify sections wherever possible.
- Avoid custom code for basic merchandising blocks.
- Create reusable sections for:
  - Product drop banner
  - City/run club carousel
  - UGC gallery
  - Bundle promo
  - Founder/community story
  - Blog/content feature
- Keep homepage and product templates editable through the Shopify customizer.

Decision filter:
If Bailey or Anya cannot edit the section copy, image, CTA, or product collection in Shopify without code, the section is too brittle.

### 3. Announcement Bar Fix

Problem: The announcement bar says "buy 4+ items - get 20% off" but still links to the run club page.

Fix:
- Update the announcement bar destination to the correct bundle/save page.
- If the bundle page is slow or confusing, create a simpler landing section or collection route for the promo.

Suggested CTA copy:
- `buy 4+ items, get 20% off`
- `build your cooldown kit`
- `shop the bundle`

### 4. Homepage Story

Problem: Apparel and run club community are both present, but the page should make their relationship clearer.

Recommended homepage flow:
1. Hero: colorful apparel + community movement
   - Headline: `running apparel for the miles and the meetup after`
   - CTAs: `shop apparel` and `find your city`
2. Featured product drop
3. "A social club disguised as a run club"
4. City finder / chapter grid
5. Bestsellers or complete-the-kit product row
6. UGC/community section
7. Founder or mission story
8. Email signup

## Template Direction

Look for a Shopify template that supports:
- Large product media on PDPs
- Strong variant swatches
- Native metafields
- Flexible section blocks
- Fast mobile performance
- Editable homepage sections
- Clean collection filtering
- Product recommendations
- Reviews integration

Avoid themes that rely on:
- Heavy animation
- Overly custom product forms
- Hard-coded homepage layouts
- Complex app dependencies for basic merchandising

## Shopify Backend First Steps

1. Duplicate the live theme before editing anything.
2. Fix the announcement bar link in the duplicated theme or live theme, depending on Bailey's preference.
3. Audit product template settings:
   - gallery size
   - thumbnail placement
   - variant picker behavior
   - sold-out display rules
   - mobile sticky add-to-cart
4. Check apps affecting product pages:
   - swatches / Globo Swatch
   - bundles / Easy Bundles by GiftBox
   - reviews / Loox
5. Create one draft product page redesign using a high-priority product such as Katherine Bra or Molly Short.
6. Create a homepage draft with native sections only.
7. Test mobile first before showing Bailey.

## Success Criteria

- A customer can understand color and size availability without guessing.
- Product photos feel large enough to inspect fit, fabric, and color.
- Bailey or Anya can update homepage sections without touching code.
- The announcement promo sends shoppers to the correct offer.
- The new site keeps Cooldown's personality instead of flattening it into a generic activewear store.

## Open Questions For Bailey

- Which products most often cause size/color confusion?
- Are customers reporting the confusion through DMs, email, or support tickets?
- Is the goal to start from a new theme immediately or first test improvements in a duplicate of the current theme?
- Which theme sections do Bailey and Anya need to update most often?
- Is Loox collecting reviews but not displaying them, or are reviews not being collected yet?
- What page does the 4+ items promo currently need to land on?
