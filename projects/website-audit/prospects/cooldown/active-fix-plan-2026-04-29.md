# Cooldown Active Fix Plan - 2026-04-29

Goal: correct the live shopping confusion as efficiently as possible before spending more time polishing the theme.

## Fastest Order Of Operations

### 1. Fix The Promo Link

Public site currently has a real bundle page:

- `https://cooldownrunning.com/pages/bundle-and-save`

In Shopify theme customizer:

1. Open draft theme `Annabel Design`.
2. Open the `Announcement bar`.
3. Click the nested announcement block, not only the parent section.
4. Change the link from `Run Clubs` / `/pages/run-clubs` to `Bundle and Save` / `/pages/bundle-and-save`.
5. Save.

Flag for Bailey:

- The announcement says `buy 4+ items • get 20% off`.
- If any bundle app text says `3 products / 10%`, Bailey needs to confirm the actual promo rule.

### 2. Fix Katherine Bra Variant Flow First

This is the highest-leverage PDP fix because it addresses Bailey's actual complaint: customers think products are sold out.

In Shopify admin:

1. Go to `Products`.
2. Open `Katherine Bra`.
3. In variants/options, check current option order.
4. If it is `Size, Color`, change it to:
   - `Color`
   - `Size`
5. Save.
6. Preview the product page.
7. Confirm the page now asks shoppers to choose color before size.

QA on Katherine Bra:

- First selected/default variant should be available if possible.
- Selecting a color should update which sizes are unavailable.
- Sold-out sizes can be crossed out, but the whole color set should not look dead.
- Check known problem combo: `maroon` + `XL` should show unavailable without making the whole product feel sold out.
- Check inventory: `XS` previously appeared as `-11`; ask Bailey whether overselling is intentional.

### 3. Check Globo Swatch Settings

Only after Katherine Bra option order is corrected, inspect Globo Swatch.

Settings to look for:

- Auto-select first available variant: turn on if available.
- Hide sold-out variants: keep off.
- Cross out sold-out variants: keep on for unavailable sizes.
- Unavailable combination behavior: show but clearly disable.

Best behavior:

- Customer chooses color first.
- Sizes update for that selected color.
- Unavailable sizes are visibly disabled.
- Colors do not all look sold out because one size was selected.

### 4. Repeat Only On Priority Products

Status: completed by Annabel on 2026-04-29 for the priority color/size products.

If more products are added later, repeat the option-order fix on the products most likely to matter:

1. Molly Short
2. Nicole Bra
3. Meg Tank
4. Elizabeth Short
5. Mikelle Bra / Alkal Short if Bailey still sells them prominently

Do not fix every product yet. Fix the products with meaningful color + size inventory and customer traffic.

### 5. Then Polish Product Page CSS

Use the existing bottom CSS block in `assets/section-main-product.css`, but first check for the accidental typo:

- Bad: `.globo- style--button`
- Good: `.globo-style--button`

PDP CSS is secondary. Product data and swatch behavior decide whether customers understand availability.

## Decision Rule

If option order fixes the confusion, stay on the current draft theme and finish a tight Phase 1.

If the theme/app setup still fights simple edits after option order + Globo settings, recommend a cleaner Shopify theme migration instead of continuing to patch brittle code.
