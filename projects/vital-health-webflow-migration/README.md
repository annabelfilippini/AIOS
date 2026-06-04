# Vital Health Webflow Migration

Purpose: recreate the approved Vercel preview in Webflow, using Webflow CLI where it helps and Webflow Designer where Webflow requires visual structure.

## Source Preview

- Current preview: `https://vital-health-deploy.vercel.app/`
- Local snapshot: `snapshot/`
- Patient portal: `https://vitalhealth.md-hq.com`

## Important Constraint

Webflow CLI is not equivalent to Shopify CLI theme editing. Shopify themes are file-based and can be pulled/pushed as Liquid/theme files. Webflow page layout lives in the Webflow Designer model, so the CLI cannot directly import the Vercel HTML/CSS into editable Webflow page elements.

Use the CLI for:

- Authentication and site lookup
- Asset upload
- CMS collection and item work
- Publishing
- Code components / DevLink if a specific custom component is justified

Use Webflow Designer for:

- Rebuilding the core page sections
- Creating responsive layout structure
- Styling classes and interactions
- Connecting CMS collections to visible sections

## Recommended Build Path

1. Create or open the Vital Health site in Webflow.
2. Authenticate Webflow CLI in this folder.
3. Use CLI to list the site and capture the site ID.
4. Upload logo and image assets from `snapshot/`.
5. Create CMS collections for editable areas:
   - Services
   - Providers
   - Promotions / announcements
   - Patient resources
6. Rebuild pages in Designer using the Vercel snapshot as the reference:
   - Home
   - Services
   - About
   - Contact
7. Wire all patient portal and booking buttons to Cerbo.
8. QA mobile/desktop and publish.

## CLI Commands

Run from this folder:

```bash
npx --cache /private/tmp/npm-cache -y @webflow/webflow-cli auth login
npx --cache /private/tmp/npm-cache -y @webflow/webflow-cli auth status
npx --cache /private/tmp/npm-cache -y @webflow/webflow-cli sites list
```

After the site ID is known:

```bash
npx --cache /private/tmp/npm-cache -y @webflow/webflow-cli assets upload snapshot/vh-logo-transparent.png --site SITE_ID
npx --cache /private/tmp/npm-cache -y @webflow/webflow-cli assets upload snapshot/homepage-hero.png --site SITE_ID
npx --cache /private/tmp/npm-cache -y @webflow/webflow-cli assets upload snapshot/vital-health-hummingbird.png --site SITE_ID
npx --cache /private/tmp/npm-cache -y @webflow/webflow-cli assets upload snapshot/portrait-feste.jpg --site SITE_ID
```

## Proposal Language

"We will use the current Vercel preview as the approved visual direction, then recreate it in Webflow so Vital Health can manage day-to-day website content after launch. Webflow CLI/API will be used for supporting migration tasks such as asset upload, CMS setup, and publishing support, while the final page structure will be rebuilt in Webflow Designer to ensure it is editable and maintainable."

