#!/usr/bin/env python3
"""
QA script for Black Pearl mockup.
Tests each of 12 pages for:
 - zero 404s in network
 - all <img> src files exist on disk (and bg-image URLs where we can extract them)
 - menu rows have non-empty prices
 - at least one element gets .is-visible (reveal worked)
 - polish checks on menu pages: no "n/a", no "&amp;amp;", no "$undefined",
   no two consecutive identical <h2> headings
 - desktop + mobile screenshots written to qa-screenshots/
Outputs mockups/qa-report.md.
"""
import os, re, subprocess, time, json
from pathlib import Path
from playwright.sync_api import sync_playwright

HERE = Path(__file__).resolve().parent            # /.../mockups
IMG_DIR = HERE / "assets" / "img"
SCREENS = HERE / "qa-screenshots"
SCREENS.mkdir(exist_ok=True)

PAGES = [
    "index.html",
    "menus.html",
    "menu-dinner.html",
    "menu-lunch.html",
    "menu-sushi.html",
    "menu-happy-hour.html",
    "menu-cocktails.html",
    "menu-wine.html",
    "menu-beer.html",
    "about.html",
    "private-events.html",
    "reservations.html",
]

MENU_PAGES = [
    "menu-dinner.html",
    "menu-lunch.html",
    "menu-sushi.html",
    "menu-happy-hour.html",
    "menu-cocktails.html",
    "menu-wine.html",
    "menu-beer.html",
]

# Start a local HTTP server for the mockups dir
def start_server(port=8765):
    proc = subprocess.Popen(
        ["python3", "-m", "http.server", str(port), "--directory", str(HERE)],
        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
    )
    time.sleep(1.5)
    return proc

def extract_bg_image_urls(html_text):
    # pulls URLs from background-image:url('...') in inline styles
    return re.findall(r"background-image:\s*url\(['\"]([^'\")]+)['\"]", html_text)

def check_local_assets(page, file_path):
    """Collect every <img src> and inline background-image URL, assert file exists."""
    problems = []

    # <img> tags
    srcs = page.eval_on_selector_all("img", "els => els.map(e => e.getAttribute('src'))")
    for src in srcs:
        if not src:
            continue
        if src.startswith("http"):
            if "images.squarespace-cdn.com" in src:
                problems.append(f"hotlink: {src}")
        else:
            # relative path
            p = HERE / src
            if not p.exists():
                problems.append(f"missing img: {src}")

    # background-images from inline HTML
    html_text = file_path.read_text()
    for url in extract_bg_image_urls(html_text):
        if url.startswith("http"):
            if "images.squarespace-cdn.com" in url:
                problems.append(f"hotlink bg: {url}")
            continue
        p = HERE / url
        if not p.exists():
            problems.append(f"missing bg-image: {url}")

    return problems

def check_menu_prices(page):
    """For menu pages, every .menu-item (non-banner) should have non-empty .menu-item-price."""
    offenders = page.eval_on_selector_all(
        ".menu-item:not(.menu-item--banner)",
        """els => els.map(el => {
            const title = (el.querySelector('.menu-item-title') || {}).innerText || '(no title)';
            const priceEl = el.querySelector('.menu-item-price');
            const price = priceEl ? priceEl.innerText.trim() : '';
            return { title: title.trim(), price, ok: !!price };
        }).filter(r => !r.ok)"""
    )
    return offenders

def check_polish(page, file_path):
    """Menu-page polish checks. Any hit here is a loud failure because these
    are the exact artifacts that have bitten us before (n/a leakage from
    parse, double-escape in hero eyebrow, undefined price, duplicate tab
    heading). Checks run against rendered DOM text AND raw HTML source so we
    catch issues regardless of whether they're in content or attributes.
    """
    offenders = []
    raw = file_path.read_text()
    # rendered text as the user sees it
    body_text = page.evaluate("document.body.innerText")

    # 1. literal "n/a" in menu-item *titles* only. Descriptions legitimately
    #    contain "N/A Dhos Orange" (non-alcoholic brand names for the
    #    spirit-free section), so we scope the check to <h3> title text.
    title_texts = page.eval_on_selector_all(
        ".menu-item-title", "els => els.map(e => e.innerText.trim())"
    )
    for t in title_texts:
        if re.search(r'\bn/a\b', t, flags=re.IGNORECASE):
            offenders.append(f'menu-item title contains "n/a": "{t}"')
            break

    # 2. double-escape: &amp;amp; or &amp;# in the HTML source
    if '&amp;amp;' in raw:
        offenders.append('HTML contains double-escape "&amp;amp;"')
    if '&amp;#' in raw:
        offenders.append('HTML contains double-escape "&amp;#"')

    # 3. $undefined anywhere (broken template substitution)
    if '$undefined' in raw or '$undefined' in body_text:
        offenders.append('contains literal "$undefined"')

    # 4. two consecutive identical <h2> headings (the Bottled Wine duplicate bug)
    h2_texts = page.eval_on_selector_all(
        "h2", "els => els.map(e => e.innerText.trim())"
    )
    for i in range(len(h2_texts) - 1):
        a, b = h2_texts[i], h2_texts[i + 1]
        if a and b and a.lower() == b.lower():
            offenders.append(f'two consecutive identical <h2>: "{a}"')
            break

    return offenders

def check_reveal(page):
    """Scroll through page, check at least one [data-reveal] got .is-visible."""
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    page.wait_for_timeout(900)
    page.evaluate("window.scrollTo(0, 0)")
    page.wait_for_timeout(400)
    count = page.evaluate("document.querySelectorAll('[data-reveal].is-visible').length")
    return count

def main():
    proc = start_server()
    results = []
    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)

            for pagename in PAGES:
                print(f"\n--- {pagename} ---")
                failed_reqs = []
                file_path = HERE / pagename
                url = f"http://127.0.0.1:8765/{pagename}"

                ctx = browser.new_context(viewport={"width": 1440, "height": 900})
                page = ctx.new_page()
                page.on("requestfailed", lambda req: failed_reqs.append(req.url))
                page.on("response", lambda r: failed_reqs.append(f"{r.status} {r.url}") if r.status >= 400 else None)

                page.goto(url, wait_until="networkidle", timeout=15000)
                page.wait_for_timeout(600)

                # image/asset check
                asset_problems = check_local_assets(page, file_path)

                # menu prices check (only menu pages)
                price_offenders = []
                polish_offenders = []
                if pagename in MENU_PAGES:
                    price_offenders = check_menu_prices(page)
                    polish_offenders = check_polish(page, file_path)

                # reveal check
                reveal_count = check_reveal(page)

                # Scroll down in steps to trigger reveals across the page,
                # then scroll back to top before full-page screenshot
                total_h = page.evaluate("document.body.scrollHeight")
                step = 600
                y = 0
                while y < total_h:
                    page.evaluate(f"window.scrollTo(0, {y})")
                    page.wait_for_timeout(120)
                    y += step
                page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
                page.wait_for_timeout(400)
                page.evaluate("window.scrollTo(0, 0)")
                page.wait_for_timeout(300)

                # Force all reveal elements to visible state for screenshots
                # (otherwise full-page screenshot captures off-viewport as opacity:0)
                page.evaluate("""
                  document.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('is-visible'));
                """)
                page.wait_for_timeout(300)

                # desktop screenshot
                desktop_shot = SCREENS / f"{pagename.replace('.html','')}.png"
                page.screenshot(path=str(desktop_shot), full_page=True)

                # mobile
                page.set_viewport_size({"width": 390, "height": 844})
                page.wait_for_timeout(400)
                page.evaluate("""
                  document.querySelectorAll('[data-reveal]').forEach(el => el.classList.add('is-visible'));
                """)
                page.wait_for_timeout(200)
                mobile_shot = SCREENS / f"{pagename.replace('.html','')}-mobile.png"
                page.screenshot(path=str(mobile_shot), full_page=True)

                # filter failed reqs — ignore favicon & fonts CDN check (fonts OK)
                real_fails = [r for r in failed_reqs if "favicon.ico" not in r]
                # Keep only genuine 4xx/5xx for LOCAL resources (same origin)
                local_fails = [r for r in real_fails if ("127.0.0.1" in r or r.startswith("http://localhost")) ]
                # reduce to only 4xx/5xx
                local_4xx = [r for r in local_fails if re.match(r"^[45]\d\d ", r)]

                results.append({
                    "page": pagename,
                    "assets_ok": len(asset_problems) == 0,
                    "asset_problems": asset_problems,
                    "local_404s": local_4xx,
                    "price_offenders": price_offenders,
                    "polish_offenders": polish_offenders,
                    "reveal_count": reveal_count,
                    "desktop_screenshot": str(desktop_shot.relative_to(HERE)),
                    "mobile_screenshot": str(mobile_shot.relative_to(HERE)),
                })

                print(f"  assets ok: {len(asset_problems) == 0} (problems: {len(asset_problems)})")
                print(f"  local 404s: {len(local_4xx)}")
                print(f"  menu price offenders: {len(price_offenders)}")
                if pagename in MENU_PAGES:
                    if polish_offenders:
                        print(f"  POLISH FAIL: {polish_offenders}")
                    else:
                        print(f"  polish: OK")
                print(f"  reveal elements visible: {reveal_count}")

                ctx.close()

            browser.close()
    finally:
        proc.terminate()
        proc.wait(timeout=5)

    # Write report
    lines = []
    lines.append("# Black Pearl Mockup QA Report\n")
    lines.append(f"Tested {len(results)} pages at desktop (1440x900) and mobile (390x844).\n")
    lines.append("## Summary Table\n")
    lines.append("| Page | Assets OK | 404s | Menu Prices OK | Polish OK | Reveals Visible | Desktop Shot | Mobile Shot |")
    lines.append("|------|-----------|------|----------------|-----------|-----------------|--------------|-------------|")

    all_green = True
    for r in results:
        is_menu = r["page"] in MENU_PAGES
        prices_ok = "—" if not is_menu else ("OK" if not r["price_offenders"] else f"FAIL ({len(r['price_offenders'])})")
        polish_ok = "—" if not is_menu else ("OK" if not r.get("polish_offenders") else f"FAIL ({len(r['polish_offenders'])})")
        assets_ok = "OK" if r["assets_ok"] else f"FAIL ({len(r['asset_problems'])})"
        errors = "0" if not r["local_404s"] else str(len(r["local_404s"]))
        reveals = "OK" if r["reveal_count"] > 0 else "FAIL"
        if (not r["assets_ok"] or r["local_404s"]
            or (is_menu and r["price_offenders"])
            or (is_menu and r.get("polish_offenders"))
            or r["reveal_count"] == 0):
            all_green = False
        lines.append(f"| {r['page']} | {assets_ok} | {errors} | {prices_ok} | {polish_ok} | {reveals} | [desktop]({r['desktop_screenshot']}) | [mobile]({r['mobile_screenshot']}) |")

    lines.append("")
    lines.append(f"**Overall: {'ALL GREEN' if all_green else 'ISSUES FOUND'}**\n")

    # Detail section for any failures
    for r in results:
        is_menu = r["page"] in MENU_PAGES
        has_issue = (
            r["asset_problems"] or r["local_404s"]
            or (is_menu and r["price_offenders"])
            or (is_menu and r.get("polish_offenders"))
            or r["reveal_count"] == 0
        )
        if has_issue:
            lines.append(f"## Issues — {r['page']}\n")
            if r["asset_problems"]:
                lines.append("**Asset problems:**")
                for a in r["asset_problems"]:
                    lines.append(f"- {a}")
                lines.append("")
            if r["local_404s"]:
                lines.append("**Local 404s:**")
                for e in r["local_404s"]:
                    lines.append(f"- {e}")
                lines.append("")
            if r["price_offenders"]:
                lines.append("**Menu rows missing prices:**")
                for o in r["price_offenders"]:
                    lines.append(f"- {o['title']}")
                lines.append("")
            if is_menu and r.get("polish_offenders"):
                lines.append("**Polish failures:**")
                for p in r["polish_offenders"]:
                    lines.append(f"- {p}")
                lines.append("")
            if r["reveal_count"] == 0:
                lines.append("**No reveal elements became visible after scroll.**\n")

    (HERE / "qa-report.md").write_text("\n".join(lines))
    print("\n\nWrote mockups/qa-report.md")
    print(f"Overall: {'ALL GREEN' if all_green else 'ISSUES FOUND'}")
    return all_green

if __name__ == "__main__":
    main()
