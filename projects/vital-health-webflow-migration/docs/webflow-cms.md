# Webflow CMS

Webflow site:

- Name: Vital Health
- Site ID: `6a15e6f364922623e13946da`

Collections created on 2026-05-26.

## Services

- Collection ID: `6a15e7c7d027bc3276dff734`
- Slug: `services`
- Fields:
  - Name: `name` / PlainText / required
  - Slug: `slug` / PlainText / required
  - Short Summary: `short-summary` / PlainText
  - Long Description: `long-description` / RichText
  - Display Order: `display-order` / Number
  - CTA URL: `cta-url` / Link

## Providers

- Collection ID: `6a15e7c7d027bc3276dff7c5`
- Slug: `providers`
- Fields:
  - Name: `name` / PlainText / required
  - Slug: `slug` / PlainText / required
  - Credentials: `credentials` / PlainText
  - Bio: `bio` / RichText
  - Photo: `photo` / Image
  - Display Order: `display-order` / Number

## Promotions

- Collection ID: `6a15e7c7f03a463f6555d87c`
- Slug: `promotions`
- Fields:
  - Name: `name` / PlainText / required
  - Slug: `slug` / PlainText / required
  - Summary: `summary` / PlainText
  - Start Date: `start-date` / DateTime
  - End Date: `end-date` / DateTime
  - Active Status: `active-status` / PlainText
  - CTA URL: `cta-url` / Link
  - Disclaimer Text: `disclaimer-text` / PlainText

Note: Webflow CLI help listed `Bool`, but the site rejected `Bool` as an invalid field type. Use `Active Status` for now unless the toggle is added manually in Designer/CMS settings.

## Patient Resources

- Collection ID: `6a15e7c81454dc5ab0fdb3bb`
- Slug: `patient-resources`
- Fields:
  - Name: `name` / PlainText / required
  - Slug: `slug` / PlainText / required
  - Category: `category` / PlainText
  - Summary: `summary` / PlainText
  - Body: `body` / RichText
  - Resource URL: `resource-url` / Link
  - Display Order: `display-order` / Number

