# Vital Health Builder Setup

This is a local Webflow Designer Extension that inserts a first-pass Vital Health Home page structure into the Webflow Designer canvas.

## Why This Exists

Codex can authenticate Webflow CLI, upload assets, and create CMS structure, but the in-app Codex browser cannot reuse Annabel's normal web browser login. Webflow Designer layout changes need either browser access to the signed-in Designer or a Designer Extension that runs inside the signed-in Designer.

This extension is the second path.

## Build Status

Last verified:

```bash
npm run build
```

Result: `bundle.zip` created successfully.

## Local Development

From this folder:

```bash
npm run dev
```

The command serves the extension locally and watches `src/index.tsx`.

Use the displayed development URL in Webflow Designer's Apps panel if Webflow prompts for one.

## Current Extension Behavior

Button: `Insert Home Page`

What it does:

- Finds the selected element if it can contain children.
- Otherwise tries to find the page `Body`.
- Inserts a first-pass Home page structure using Webflow's `insertElementFromWHTML` API.
- Uses uploaded Webflow asset URLs for the Vital Health logo and homepage hero image.

Important:

- Open the Home page in Webflow Designer first.
- Select the page Body or a top-level wrapper if possible.
- Run the extension.
- Review the inserted page in Designer and polish responsive styles/CMS bindings.

## Known Limits

- This is not a full Shopify-style theme push.
- Webflow may normalize or strip some inline styles during insertion.
- The first pass focuses on structure and content. Designer polish may still be needed.
- Services/About/Contact can be added with additional extension actions after Home is validated.

