#!/usr/bin/env python3
"""Build a self-contained preview.html for the carousel with PNGs inlined as base64.

Output: preview.html (next to slide-*.png) AND a copy on the Desktop.
"""
import base64
from pathlib import Path

ROOT = Path(__file__).parent
DESKTOP = Path.home() / "Desktop" / "vital-health-when-peptides-considered-preview.html"

slides = []
for i in range(1, 4):
    p = ROOT / f"slide-{i}.png"
    b64 = base64.b64encode(p.read_bytes()).decode("ascii")
    slides.append(f"data:image/png;base64,{b64}")

slide_imgs = "\n".join(
    f'        <img class="slide" data-i="{i}" src="{src}" alt="Slide {i+1}" />'
    for i, src in enumerate(slides)
)
grid_imgs = "\n".join(
    f'        <figure><img src="{src}" alt="Slide {i+1}" /><figcaption>Slide {i+1}</figcaption></figure>'
    for i, src in enumerate(slides)
)

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title>Vital Health — When are peptides considered? (preview)</title>
<style>
  :root {{
    --bg: #ebe5da;
    --paper: #fbf7ec;
    --cream: #f5efe0;
    --ink: #2a2a26;
    --muted: #676359;
    --forest: #1f4d2a;
    --clay: #c77a4a;
  }}
  * {{ box-sizing: border-box; }}
  body {{
    margin: 0;
    background: var(--bg);
    color: var(--ink);
    font-family: "Inter", -apple-system, "Segoe UI", Arial, sans-serif;
    padding: 32px 16px 80px;
  }}
  header {{
    max-width: 980px;
    margin: 0 auto 24px;
    text-align: center;
  }}
  header h1 {{
    font-family: Georgia, serif;
    font-size: 28px;
    font-weight: 400;
    margin: 0 0 6px;
    color: var(--forest);
  }}
  header p {{
    color: var(--muted);
    font-size: 14px;
    letter-spacing: 0.04em;
    margin: 0;
  }}
  .tabs {{
    display: flex;
    justify-content: center;
    gap: 8px;
    margin: 16px 0 24px;
  }}
  .tabs button {{
    background: var(--paper);
    border: 1px solid #d8d2c2;
    color: var(--ink);
    cursor: pointer;
    font-family: inherit;
    font-size: 13px;
    letter-spacing: 0.1em;
    padding: 10px 18px;
    text-transform: uppercase;
  }}
  .tabs button.active {{
    background: var(--forest);
    border-color: var(--forest);
    color: var(--paper);
  }}

  /* ===== Instagram-style carousel ===== */
  .ig-wrap {{
    display: none;
    margin: 0 auto;
    max-width: 540px;
  }}
  .ig-wrap.active {{ display: block; }}
  .ig-card {{
    background: white;
    border: 1px solid #d8d2c2;
    border-radius: 8px;
    overflow: hidden;
  }}
  .ig-header {{
    align-items: center;
    border-bottom: 1px solid #efe9d8;
    display: flex;
    gap: 10px;
    padding: 12px 14px;
  }}
  .ig-avatar {{
    background: var(--forest);
    border-radius: 50%;
    height: 32px;
    width: 32px;
  }}
  .ig-handle {{
    font-size: 14px;
    font-weight: 600;
  }}
  .ig-frame {{
    position: relative;
    width: 100%;
    aspect-ratio: 1 / 1;
    background: var(--cream);
    overflow: hidden;
  }}
  .ig-frame .slide {{
    display: none;
    height: 100%;
    object-fit: cover;
    width: 100%;
  }}
  .ig-frame .slide.active {{ display: block; }}
  .ig-nav {{
    align-items: center;
    background: rgba(255,255,255,0.85);
    border: none;
    border-radius: 50%;
    color: var(--ink);
    cursor: pointer;
    display: flex;
    font-size: 18px;
    height: 36px;
    justify-content: center;
    position: absolute;
    top: 50%;
    transform: translateY(-50%);
    width: 36px;
    z-index: 5;
    box-shadow: 0 1px 3px rgba(0,0,0,0.18);
  }}
  .ig-nav.prev {{ left: 10px; }}
  .ig-nav.next {{ right: 10px; }}
  .ig-nav:disabled {{ opacity: 0.35; cursor: default; }}
  .ig-dots {{
    display: flex;
    gap: 6px;
    justify-content: center;
    padding: 10px 0 12px;
  }}
  .ig-dot {{
    background: #cdc8b6;
    border-radius: 50%;
    height: 6px;
    width: 6px;
    transition: background 0.15s;
  }}
  .ig-dot.active {{ background: var(--forest); }}
  .ig-actions {{
    color: var(--ink);
    display: flex;
    font-size: 18px;
    gap: 14px;
    padding: 6px 14px 4px;
  }}
  .ig-caption {{
    font-size: 13.5px;
    line-height: 1.4;
    padding: 6px 14px 14px;
    color: var(--ink);
  }}
  .ig-caption b {{ font-weight: 600; }}
  .ig-counter {{
    background: rgba(0,0,0,0.55);
    border-radius: 12px;
    color: white;
    font-size: 12px;
    padding: 3px 9px;
    position: absolute;
    right: 12px;
    top: 12px;
    z-index: 5;
  }}

  /* ===== Grid view ===== */
  .grid-wrap {{
    display: none;
    margin: 0 auto;
    max-width: 1200px;
  }}
  .grid-wrap.active {{ display: block; }}
  .grid {{
    display: grid;
    gap: 24px;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  }}
  .grid figure {{
    background: white;
    border: 1px solid #d8d2c2;
    margin: 0;
    padding: 8px;
  }}
  .grid img {{
    display: block;
    width: 100%;
    height: auto;
  }}
  .grid figcaption {{
    color: var(--muted);
    font-size: 12px;
    letter-spacing: 0.12em;
    padding: 10px 4px 4px;
    text-align: center;
    text-transform: uppercase;
  }}
</style>
</head>
<body>
  <header>
    <h1>Vital Health — Peptides (informational)</h1>
    <p>3-slide carousel preview · 2026-06-08</p>
  </header>
  <div class="tabs">
    <button class="tab-btn active" data-view="ig">Instagram view</button>
    <button class="tab-btn" data-view="grid">Side-by-side grid</button>
  </div>

  <!-- Instagram-style carousel -->
  <section class="ig-wrap active" id="ig">
    <div class="ig-card">
      <div class="ig-header">
        <div class="ig-avatar"></div>
        <div class="ig-handle">vitalhealthatx</div>
      </div>
      <div class="ig-frame" id="frame">
        <span class="ig-counter"><span id="counter">1</span>/3</span>
        <button class="ig-nav prev" id="prev" aria-label="Previous slide">&#10094;</button>
{slide_imgs}
        <button class="ig-nav next" id="next" aria-label="Next slide">&#10095;</button>
      </div>
      <div class="ig-dots" id="dots"></div>
      <div class="ig-actions">♡  💬  ↗  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;🔖</div>
      <div class="ig-caption">
        <b>vitalhealthatx</b> Peptides. A category of clinical options, not a single decision. They may be considered for tissue repair, growth hormone axis support, immune support, and recovery, guided by your labs, history, and full clinical picture. Educational only, not medical advice…
      </div>
    </div>
  </section>

  <!-- Side-by-side grid -->
  <section class="grid-wrap" id="grid">
    <div class="grid">
{grid_imgs}
    </div>
  </section>

<script>
  const slides = document.querySelectorAll('.ig-frame .slide');
  const dotsHost = document.getElementById('dots');
  const counter = document.getElementById('counter');
  const prev = document.getElementById('prev');
  const next = document.getElementById('next');
  let idx = 0;

  slides.forEach((_, i) => {{
    const d = document.createElement('div');
    d.className = 'ig-dot' + (i === 0 ? ' active' : '');
    dotsHost.appendChild(d);
  }});
  const dots = document.querySelectorAll('.ig-dot');
  slides[0].classList.add('active');

  function go(n) {{
    idx = Math.max(0, Math.min(slides.length - 1, n));
    slides.forEach((s, i) => s.classList.toggle('active', i === idx));
    dots.forEach((d, i) => d.classList.toggle('active', i === idx));
    counter.textContent = idx + 1;
    prev.disabled = idx === 0;
    next.disabled = idx === slides.length - 1;
  }}
  prev.addEventListener('click', () => go(idx - 1));
  next.addEventListener('click', () => go(idx + 1));
  document.addEventListener('keydown', (e) => {{
    if (e.key === 'ArrowLeft') go(idx - 1);
    if (e.key === 'ArrowRight') go(idx + 1);
  }});
  go(0);

  // Tabs
  document.querySelectorAll('.tab-btn').forEach(btn => {{
    btn.addEventListener('click', () => {{
      document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      const view = btn.dataset.view;
      document.getElementById('ig').classList.toggle('active', view === 'ig');
      document.getElementById('grid').classList.toggle('active', view === 'grid');
    }});
  }});
</script>
</body>
</html>
"""

out = ROOT / "preview.html"
out.write_text(HTML, encoding="utf-8")
DESKTOP.parent.mkdir(parents=True, exist_ok=True)
DESKTOP.write_text(HTML, encoding="utf-8")
print(f"wrote {out}")
print(f"wrote {DESKTOP}")
print(f"size: {out.stat().st_size / 1024:.0f} KB")
