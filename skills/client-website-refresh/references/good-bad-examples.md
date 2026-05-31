# Good And Bad Examples

These come from Vital Health, the older website-audit process, and Annabel's
voice corrections. Use them before creating the next client site.

## Scope And Architecture

Good: "Website Refresh + Patient Store Workflow Coordination." This names both
the public site and the workflow layer without pretending the website replaces
the portal.

Bad: "We will build the new patient portal." Vital Health already used Cerbo.
The right move was to keep the portal and coordinate links, product flow, and
manager discovery.

Good: Webflow for editable public pages, provider bios, services, resources,
announcements, and promotion banners.

Bad: Treating a Vercel/static preview as the real client-manageable site. Vercel
was useful for mockup review, but the client needed editable Webflow pages.

Good: Backend ranges after discovery: manager meeting, map the current tools,
then price coordination work hourly.

Bad: Quoting backend/admin setup as a fixed brochure-site task before knowing
whether the client uses Cerbo, Fullscript, WholeScripts, Xymogen, Shopify, or
another stack.

## Design And Build

Good: Preserve the chosen direction: cream/forest/gold, editorial medical feel,
Fraunces plus Inter, square CTAs, hummingbird/logo lockup.

Bad: Flattening a client into a generic SaaS template or copying a reference
site so hard that the client's own identity disappears.

Good: Choose a specific HTML preview direction before coding, then visually QA
desktop and mobile against that direction.

Bad: A technically complete static preview that still reads as AI generated:
blue/white medical SaaS palette, pill CTAs, generic trust strip, rounded card
grids, right-side hero image card, and internal "preview" labels.

Good: Preserve an original image when it is doing real work, such as showing a
woman in a tech-enabled medical clinic section. Improve the crop, spacing,
caption, or surrounding layout instead of replacing the asset.

Bad: Removing identity-bearing images and swapping in unrelated stock or random
visuals because the new page layout needs an image slot.

Good: Inspect and reuse the original site's font stack when it is part of the
brand read.

Bad: Replacing the site's typography with a generic AI-default font stack. This
can make even decent layout work feel generated.

Good: Check desktop and mobile, real links, nav, portal buttons, contact details,
SEO titles, and console errors before sharing a review link.

Bad: Calling a Webflow canvas "done" without checking the published staging URL.
Some fonts, scripts, current nav states, and animations only appear after publish.

Good: Keep placeholders visible in the handoff: testimonials, headshots, policies,
claim sign-off, founder story.

Bad: Publishing live custom domain while review-only placeholders or sensitive
medical claims are still unresolved.

## Webflow Lessons

Good: Use Webflow Data API for reliable site/page/script/publish operations.
Batch Designer element/style work into short bursts and retry with the Designer
tab foregrounded when it times out.

Bad: Treating Webflow CLI/API like Shopify theme push. It cannot import static
HTML/CSS into editable Designer pages. The practical path is a visual rebuild.

Good: Native Designer elements for text, images, bios, stats, and contact
details. Custom code is acceptable for polish such as reveal animation or mobile
nav only when the editability tradeoff is named.

Bad: Solving everything with injected code and leaving the client unable to edit
the parts they specifically care about.

## Copy And Voice

Good: "continuing Dr. Feste's model and writing its next chapter" when the
founder/advisor is still present.

Bad: "carrying forward Dr. Feste's model" or "legacy" phrasing when the person
is still active. It reads like they have been written out.

Good: Remove redundant prose when a chip or nearby layout already says the fact.

Bad: "no longer seeing patients" in prose when a "Not seeing patients" chip
already appears beside the bio.

Good: No dashes as punctuation in client-facing Annabel copy. Use periods,
commas, colons, or simpler sentences.

Bad: Letting em dashes or en dashes survive because they were in pasted source
text. Annabel has had to strip them repeatedly, so the generator should do it.

## Proposal

Good: Short PDF with phases, rates, hosting/subscription costs, exact next
steps, and honest ranges. Vital Health ended with a clean two-page proposal.

Bad: A giant proposal that hides the real question: what is approved now, what
depends on discovery, what costs extra, and who needs to provide missing inputs.

Good: Keep optional add-ons separate, such as Instagram automation after the
site and backend scope are clear.

Bad: Bundling optional social automation into the core website scope before the
client has approved the site work.

## Health And Claims

Good: Build a claims matrix before writing the mockup. Revero surfaced health
claims, pricing claims, state/lab limitations, and patient outcome testimonials
that need clinical/legal approval before a redesign amplifies them.

Bad: Treating "root cause treatment," "reverse disease," "off medications," or
specific weight-loss/blood-pressure outcomes as normal marketing copy. On a
medical site, those lines are scope and approval blockers, not just copy polish.
