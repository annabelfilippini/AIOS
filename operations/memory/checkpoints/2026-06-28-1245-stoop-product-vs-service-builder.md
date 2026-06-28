---
date: 2026-06-28 12:45
project: stoop
status: in-progress
type: checkpoint
slug: stoop-product-vs-service-builder
---

# Stoop — builder branches by offer type (service vs product), product gallery + description

Follows `2026-06-28-1200-stoop-batch2-account-front-door.md`. All work in the single
file `projects/stoop/index.html`. Tracker: `projects/stoop/in-progress.md`.

## Why
A honey/bracelet seller staring at a "when are you free" calendar is confusing.
Annabel asked to branch the builder so a product seller gets product-shaped fields
and a service seller (Delaney) keeps scheduling. Then: let products add more images
than the profile pic, and add a product description.

## What shipped this session
**1. Offer-type branch.** New first builder question "What are you offering?" →
`service` | `product` (`obKind`, `setKind()`, `.kind` picker reusing the role-card look).
- `.svc-only` (how-long / where / what-to-bring / availability calendar) shows for
  services only. `.prod-only` (description, gallery) shows for products only.
  `setKind` toggles both via inline `display`; missing `profile.kind` = service (back-compat).
- **Service profile** (Delaney): calendar + "Pick a time" + "Request a lesson", facts =
  dur/loc/bring.
- **Product profile**: no calendar, "Get one" + price + "Local pickup" fact +
  always-enabled "Request this"; pickup sub copy.
- Request modal / SMS body / done screen adapt by kind. Confirmation made
  gender-neutral ("They'll reach out"); dropped lacrosse-only "See you on the field".
- DEFAULT (Delaney) seeded `kind:'service'`.

**2. Product gallery + description** (product-only):
- **Description** textarea `f-desc` in "What you offer" → `profile.desc`, rendered
  `#p-desc` in the book section.
- **Gallery**: "Photos of what you're selling" card, multi-file, reuses `downscale()`
  at 720px, capped at 6 (localStorage quota; comment names the upgrade path). Thumb
  strip with per-image remove → `profile.photos[]`, rendered `#p-gallery` grid between
  hero and book. Both render only when a product has content; service shows neither.
- Saved in ob-go (`desc`/`photos` cleared for services), loaded in fillOnboard.

## Verified (preview port 8762)
- Product builder hides svc fields, adapts unit label ("Each") + placeholder ("jar").
- Product profile: no calendar, request enabled, desc + 2 gallery imgs render, send
  uses pickup copy + 🧺. Thumb remove works (2→1).
- Service path (Delaney): calendar intact, no gallery/desc, "Request a lesson".
- Front door (Batch 2) still works end to end. No console errors throughout.

## Open / deferred
- **"Where" for products** is currently hidden (pickup implied by neighborhood +
  "Local pickup" tag). Revisit if a product should name a pickup spot.
- Product reqbar: lone "Request this" sits in the wide dark bar (leftover from the
  service layout's "no time picked" hint). Functional; could center/tighten.
- Gallery has no backend → 6-image cap + localStorage only.
- **Batch 3 (next):** tag stands with neighborhood id, filter feed to `account.hoods`,
  wire top-bar `.place` to account hoods (still hardcoded "Country Club"), reseed
  Delaney in Country Club, role-aware home (buyer shouldn't see Delaney's demo as
  "your page").
- Older deferred: real SMS/backend confirmations; per-week "copy to next 4 weeks";
  single profile slot → multi-kid; "too quiet" empty-neighborhood valve.
