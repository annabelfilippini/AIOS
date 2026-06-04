# Webflow Fonts Setup — Vital Health

The site styles declare two typefaces as design tokens:

- **Fraunces** — display/headings (`font-display` variable)
- **Inter** — body/UI (`font-body` variable)

Webflow needs both added to **Site Settings → Fonts** before they will actually load on the published site. Variables only tell Webflow *what to ask for*; the Site Settings tell Webflow *where to get it*.

## Step-by-step (Webflow Designer UI)

1. In the Designer, click the **gear icon** (Site Settings) in the top-left, or open `https://vital-health-9bf311.design.webflow.com/dashboard/sites/vital-health/fonts`
2. Open the **Fonts** tab.
3. Scroll to **Add Google fonts**.
4. **Fraunces:**
   - Type `Fraunces` in the search box and select it.
   - Variants to include: `300 (Light)`, `400 (Regular)`, `500 (Medium)`.
   - Click **Add font**.
5. **Inter:**
   - Type `Inter` in the search box and select it.
   - Variants to include: `300 (Light)`, `400 (Regular)`, `500 (Medium)`, `600 (Semi-bold)`.
   - Click **Add font**.
6. Close Site Settings. Return to the Designer canvas.
7. **Publish** the site (top-right). The next published preview / live site will render with Fraunces + Inter loaded.

## Why the Designer canvas may still look "off" until publish

The Designer canvas previews fonts as soon as they're added to Site Settings — but **only if you reload the Designer tab** after adding them. If headings still look like a system serif (Times New Roman or similar):

1. Save your work.
2. Refresh the Designer tab.
3. Headings should now render in Fraunces.

## What the snapshots showed before fonts were added

In every snapshot taken during this build, the Designer was falling back to macOS system fonts (San Francisco / Times) for both serif and sans-serif. That's why:

- The hero lede looked like `"Integrative regenerative and preventivemedicine—built"` — system-font word-spacing artifacts.
- The reviews quotes and other Inter copy felt cramped.

Once Fraunces + Inter are loaded, every section will render with proper Webflow typography.

## Verification

After publishing or refreshing the Designer:

- Open the Home page.
- The hero `"Your journey to / optimal vitality."` should be in **Fraunces** — geometric, refined serif with the gentle curves visible.
- The Austin/Integrative Medicine/Since 1970 ticker and Patient Portal button should be in **Inter** — clean, neutral sans.
