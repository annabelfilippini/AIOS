import { createRequire } from "node:module";
import path from "node:path";
import { fileURLToPath } from "node:url";

const require = createRequire(import.meta.url);
const { chromium } = require("playwright");
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const htmlPath = path.join(__dirname, "index.html");
const browser = await chromium.launch({ headless: true });
const page = await browser.newPage({ viewport: { width: 1400, height: 1300 }, deviceScaleFactor: 1 });

await page.goto(`file://${htmlPath}`, { waitUntil: "networkidle" });

for (let i = 1; i <= 5; i += 1) {
  const slide = page.locator(`#slide-${i}`);
  await slide.screenshot({ path: path.join(__dirname, `slide-${i}.png`) });
}

await browser.close();
