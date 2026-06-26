import { createRequire } from "node:module";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath, pathToFileURL } from "node:url";

const require = createRequire(import.meta.url);

function loadPlaywright() {
  try {
    return require("playwright");
  } catch {
    return require("/Users/annabelfilippini/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright");
  }
}

const { chromium } = loadPlaywright();
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(__dirname, "index.html");

const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({
  viewport: { width: 1180, height: 1450 },
  deviceScaleFactor: 1,
});

await page.goto(pathToFileURL(htmlPath).href, { waitUntil: "networkidle" });

const slide = page.locator("#slide-1");
await slide.screenshot({ path: path.join(__dirname, "we-are-moving.png") });

await browser.close();

const slideCards = `
  <figure>
    <img src="we-are-moving.png" alt="Vital Health is moving announcement">
    <figcaption><strong>Single image announcement</strong><span>Vital Health is moving, with the new West Austin address set as the hero.</span></figcaption>
  </figure>
`;

const review = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Vital Health New Location Post Review</title>
  <style>
    * { box-sizing: border-box; margin: 0; padding: 0; }
    body {
      background: #ede6d7;
      color: #12351e;
      font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    }
    main { max-width: 1500px; margin: 0 auto; padding: 46px 24px 76px; }
    header {
      display: flex;
      align-items: end;
      justify-content: space-between;
      gap: 32px;
      border-bottom: 1px solid rgba(18, 53, 30, 0.16);
      padding-bottom: 24px;
      margin-bottom: 28px;
    }
    h1 {
      max-width: 600px;
      font-family: Georgia, "Times New Roman", serif;
      font-weight: 400;
      font-size: 42px;
      line-height: 1.08;
      color: #12351e;
    }
    p {
      max-width: 650px;
      color: #676359;
      font-size: 15px;
      line-height: 1.58;
    }
    .grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
      gap: 22px;
    }
    figure {
      margin: 0;
      background: #fbf7ec;
      border: 1px solid rgba(18, 53, 30, 0.14);
      padding: 10px;
    }
    img {
      display: block;
      width: 100%;
      aspect-ratio: 4 / 5;
      object-fit: cover;
    }
    figcaption {
      display: grid;
      gap: 6px;
      padding: 12px 4px 4px;
      color: #676359;
      font-size: 13px;
      line-height: 1.45;
    }
    figcaption strong {
      color: #1f4d2a;
      font-size: 12px;
      letter-spacing: 0.1em;
      text-transform: uppercase;
    }
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Vital Health New Location Post</h1>
      <p>Single Instagram announcement for Vital Health's move to 500 N Capital of Texas Hwy, Bldg 6, Suite 125, Austin, TX 78746.</p>
    </header>
    <section class="grid">${slideCards}</section>
  </main>
</body>
</html>`;

fs.writeFileSync(path.join(__dirname, "review.html"), review);
console.log("Rendered we-are-moving.png and review.html");
