import fs from "node:fs";
import path from "node:path";
import { pathToFileURL } from "node:url";
import { createRequire } from "node:module";

const require = createRequire(import.meta.url);

function loadPlaywright() {
  try {
    return require("playwright");
  } catch {
    return require("/Users/annabelfilippini/.cache/codex-runtimes/codex-primary-runtime/dependencies/node/node_modules/playwright");
  }
}

const { chromium } = loadPlaywright();

const dir = path.dirname(new URL(import.meta.url).pathname);
const slidesDir = path.join(dir, "slides");
const logoPath = path.join(dir, "vh-bird-logo.png");
const generatedDir = path.join(dir, "generated");
const art = {
  abstract: pathToFileURL(path.join(generatedDir, "cellular-abstract.png")).href,
  labs: pathToFileURL(path.join(generatedDir, "labs-tabletop.png")).href,
  vials: pathToFileURL(path.join(generatedDir, "still-life-vials.png")).href,
};

const brand = {
  name: "Vital Health",
  service: "Peptide Therapy",
  location: "Austin, Texas",
  url: "vitalhealth.md-hq.com",
};

const slides = [
  {
    eyebrow: "Peptide Therapy",
    klass: "s1",
    html: `
      <img class="cover-photo" src="${art.abstract}" alt="">
      <div class="cover-veil"></div>
      <div class="corner left">Vital Health</div>
      <div class="corner right">Educational Note</div>
      <div class="hero-orbit orbit-a"></div>
      <div class="hero-orbit orbit-b"></div>
      <div class="copy bottom-left">
        <span class="rule"></span>
        <h1>Peptide therapy:<br><em>what to know.</em></h1>
        <p>A simple guide to how Vital Health thinks about peptides.</p>
      </div>`,
  },
  {
    eyebrow: "What They Are",
    klass: "s2",
    html: `
      <div class="split">
        <section>
          <span class="rule"></span>
          <h2>What are<br><em>peptides?</em></h2>
          <p>Peptides are short chains of amino acids. In the body, some act as messengers that help cells and tissues communicate.</p>
        </section>
        <aside class="molecule-field" aria-hidden="true">
          <img class="panel-photo" src="${art.vials}" alt="">
          <div class="panel-wash"></div>
          <span></span><span></span><span></span><span></span><span></span>
          <i class="l1"></i><i class="l2"></i><i class="l3"></i><i class="l4"></i>
        </aside>
      </div>`,
  },
  {
    eyebrow: "Why Personal",
    klass: "s3",
    html: `
      <div class="grid-bg"></div>
      <div class="copy top-wide">
        <h2>Why are peptides<br><em>personal?</em></h2>
        <p>The same peptide conversation can mean something different depending on the person in front of us.</p>
      </div>
      <figure class="s3-photo-card">
        <img src="${art.labs}" alt="">
      </figure>
      <div class="context-panel">
        <span>What changes the plan?</span>
        <p>Your provider looks at patterns across hormones, inflammation, recovery, sleep, medications, and metabolic markers before deciding whether peptides belong in the conversation.</p>
      </div>
      <div class="card-row">
        <div><strong>Age and stage</strong><span>What season of health are we supporting?</span></div>
        <div><strong>Hormones</strong><span>What is changing in the broader endocrine picture?</span></div>
        <div><strong>Sleep and recovery</strong><span>How well is the body restoring itself?</span></div>
        <div><strong>Immune history</strong><span>What patterns show up over time?</span></div>
        <div><strong>Medications</strong><span>What could interact or change risk?</span></div>
        <div><strong>Metabolic markers</strong><span>What do labs say about energy and resilience?</span></div>
      </div>
      <p class="footnote">That is why Vital Health starts with the full clinical picture, not a trend.</p>`,
  },
  {
    eyebrow: "When Appropriate",
    klass: "s4",
    html: `
      <img class="s4-photo" src="${art.vials}" alt="">
      <div class="s4-photo-wash"></div>
      <div class="copy">
        <span class="rule"></span>
        <h2>When are peptides considered?</h2>
        <p>They may be reviewed when your history, labs, and goals point toward a specific clinical question.</p>
      </div>
      <div class="s4-note">
        <strong>Not every goal needs a peptide.</strong>
        <span>The first step is deciding what question the care plan is trying to answer, and whether the safer path is testing, nutrition, hormones, recovery support, or medication review.</span>
      </div>
      <div class="topic-grid">
        <div><strong>Recovery</strong><span>Tissue support, joint comfort, training stress, and how progress would be measured.</span></div>
        <div><strong>Metabolic health</strong><span>Body composition, glucose patterns, energy, and whether labs show a clear target.</span></div>
        <div><strong>Immune support</strong><span>Resilience, inflammation patterns, immune history, and current risk factors.</span></div>
        <div><strong>Sleep and cognition</strong><span>Restorative sleep, focus, stress response, and what else may be driving symptoms.</span></div>
        <div><strong>Sexual wellness</strong><span>Libido, function, hormone context, medications, and relationship to the broader plan.</span></div>
      </div>`,
  },
  {
    eyebrow: "Labs And History",
    klass: "s5",
    html: `
      <img class="labs-photo" src="${art.labs}" alt="">
      <div class="labs-wash"></div>
      <div class="copy">
        <span class="rule"></span>
        <h2>Why do<br><em>labs matter?</em></h2>
        <p>At Vital Health, a protocol is shaped by more than the symptom that brought you in.</p>
      </div>
      <div class="timeline">
        <div><span>01</span>History</div>
        <div><span>02</span>Labs</div>
        <div><span>03</span>Goals</div>
        <div><span>04</span>Risk factors</div>
        <div><span>05</span>Monitoring</div>
      </div>
      <p class="bottom-line">A careful plan asks what fits, what does not, and what should be measured next.</p>`,
  },
  {
    eyebrow: "Examples",
    klass: "s6",
    html: `
      <img class="examples-photo" src="${art.abstract}" alt="">
      <div class="examples-photo-wash"></div>
      <div class="copy">
        <span class="rule"></span>
        <h2>Which peptides<br><em>might come up?</em></h2>
        <p>Names are examples, not recommendations. Your provider walks through what is clinically appropriate for you.</p>
      </div>
      <div class="examples">
        <div><strong>Growth hormone signaling</strong><span>Sermorelin, Ipamorelin, CJC-1295</span></div>
        <div><strong>Recovery and tissue support</strong><span>BPC-157, Thymosin beta-4</span></div>
        <div><strong>Immune conversations</strong><span>Thymosin alpha-1, LL-37</span></div>
        <div><strong>Metabolic and mitochondrial</strong><span>MOTS-c</span></div>
        <div><strong>Sexual wellness</strong><span>PT-141</span></div>
        <div><strong>Cognition and stress response</strong><span>Semax, Selank, Cerebrolysin</span></div>
      </div>`,
  },
  {
    eyebrow: "Vital Health Approach",
    klass: "s7",
    html: `
      <div class="quote-mark">"</div>
      <img class="s7-photo" src="${art.labs}" alt="">
      <div class="s7-photo-wash"></div>
      <div class="quote">
        <h2>How does<br><em>Vital Health decide?</em></h2>
        <p>Good peptide care asks about indication, source, route, dose, timing, interactions, and how progress will be measured.</p>
      </div>
      <div class="decision-grid">
        <div><strong>Indication</strong><span>What are we trying to support?</span></div>
        <div><strong>Source</strong><span>Where does it come from, and is it appropriate?</span></div>
        <div><strong>Route</strong><span>How would it be taken or administered?</span></div>
        <div><strong>Dose</strong><span>What level fits the clinical picture?</span></div>
        <div><strong>Timing</strong><span>What else should happen first?</span></div>
        <div><strong>Monitoring</strong><span>How will we know whether to continue?</span></div>
      </div>
      <div class="quiet-list">
        <span>What are we trying to support?</span>
        <span>What do labs and history rule in or out?</span>
        <span>What should we monitor, change, or stop?</span>
      </div>`,
  },
  {
    eyebrow: "How To Ask",
    klass: "s8",
    logo: true,
    html: `
      <img class="final-photo" src="${art.vials}" alt="">
      <div class="final-wash"></div>
      <img class="bird" src="${logoPath}" alt="Vital Health hummingbird">
      <div class="copy">
        <span class="rule"></span>
        <h2>How do I ask<br><em>about peptides?</em></h2>
        <p>Ask which options fit your goals, what labs should come first, what risks matter for you, and how Vital Health would measure progress.</p>
      </div>
      <div class="cta-band">
        <span>Complimentary 60 minute consultation</span>
        <span>No cost. No commitment.</span>
      </div>`,
  },
];

function pagination(index) {
  return `<div class="pagination">${slides.map((_, i) => `<span class="${i === index ? "active" : ""}"></span>`).join("")}</div>`;
}

function slidePage(slide, index) {
  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>${brand.name} Peptide Carousel ${index + 1}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@1,400;1,500&family=Fraunces:opsz,wght@9..144,300..650&family=Inter:wght@300;400;500;600&display=swap" rel="stylesheet">
  <style>${css()}</style>
</head>
<body>
  <article class="slide ${slide.klass}" data-slide="${index + 1}">
    <div class="tiny-num">${String(index + 1).padStart(2, "0")}</div>
    <div class="eyebrow">${slide.eyebrow}</div>
    ${slide.html}
    ${pagination(index)}
  </article>
</body>
</html>`;
}

function reviewPage() {
  const imgs = slides.map((slide, i) => `
    <figure>
      <img src="slide-${i + 1}.png" alt="Slide ${i + 1}: ${slide.eyebrow}">
      <figcaption>${String(i + 1).padStart(2, "0")} ${slide.eyebrow}</figcaption>
    </figure>`).join("");

  return `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Vital Health Peptide Therapy Carousel Review</title>
  <style>
    body { margin: 0; background: #ede6d7; color: #12351e; font-family: Inter, Arial, sans-serif; }
    main { max-width: 1500px; margin: 0 auto; padding: 44px 24px 72px; }
    header { display: flex; align-items: end; justify-content: space-between; gap: 32px; border-bottom: 1px solid rgba(18,53,30,.16); padding-bottom: 24px; margin-bottom: 28px; }
    h1 { margin: 0; font-family: Georgia, serif; font-weight: 400; font-size: 36px; }
    p { margin: 0; max-width: 660px; color: #676359; line-height: 1.55; }
    .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(280px, 1fr)); gap: 22px; }
    figure { margin: 0; background: #ded3b8; border: 1px solid rgba(18,53,30,.14); padding: 10px; }
    img { width: 100%; display: block; aspect-ratio: 4 / 5; object-fit: cover; }
    figcaption { padding-top: 10px; font-size: 12px; letter-spacing: .08em; text-transform: uppercase; color: #676359; }
  </style>
</head>
<body>
  <main>
    <header>
      <h1>Vital Health Peptide Therapy Carousel</h1>
      <p>Eight-slide educational carousel. Built to explain peptides carefully without turning the post into a treatment menu.</p>
    </header>
    <section class="grid">${imgs}</section>
  </main>
</body>
</html>`;
}

function postMarkdown() {
  return `# Vital Health Peptide Therapy Carousel

Draft date: 2026-06-07
Format: Instagram carousel, 8 slides, 1080 x 1350
Status: Detailed educational draft for client review

## Direction

Educational peptide post for Vital Health. The tone is calm, clinical, and careful. The post explains what peptides are, why they are personal, when they may be considered, why labs and history matter, examples patients may hear about, and how to ask Vital Health about peptide therapy.

Guardrail: this is not a peptide menu and not medical advice. Examples are framed as names patients may hear about, not recommendations.

## Slide Copy

1. Peptide therapy: what to know.
   A simple guide to how Vital Health thinks about peptides.

2. What are peptides?
   Peptides are short chains of amino acids. In the body, some act as messengers that help cells and tissues communicate.

3. Why are peptides personal?
   The same peptide conversation can mean something different depending on the person in front of us.
   Age and stage. Hormones. Sleep and recovery. Immune history. Medications. Metabolic markers.
   That is why Vital Health starts with the full clinical picture, not a trend.

4. When are peptides considered?
   They may be reviewed when your history, labs, and goals point toward a specific clinical question.
   Not every goal needs a peptide. The first step is deciding what question the care plan is trying to answer.
   Recovery. Metabolic health. Immune support. Sleep and cognition. Sexual wellness.

5. Why do labs matter?
   At Vital Health, a protocol is shaped by more than the symptom that brought you in.
   History. Labs. Goals. Risk factors. Monitoring.

6. Which peptides might come up?
   Names are examples, not recommendations. Your provider walks through what is clinically appropriate for you.
   Sermorelin, Ipamorelin, CJC-1295, BPC-157, Thymosin beta-4, Thymosin alpha-1, LL-37, MOTS-c, PT-141, Semax, Selank, Cerebrolysin.

7. How does Vital Health decide?
   Good peptide care asks about indication, source, route, dose, timing, interactions, and how progress will be measured.
   Indication. Source. Route. Dose. Timing. Interactions. Monitoring.

8. How do I ask about peptides?
   Ask which options fit your goals, what labs should come first, what risks matter for you, and how Vital Health would measure progress.
   Complimentary 60 minute consultation. No cost. No commitment.

## Caption Draft

Peptides are short chains of amino acids. In the body, some peptides act like messengers, helping cells and tissues communicate.

At Vital Health, peptide therapy is not treated like a menu. It is considered through your health history, labs, goals, medications, risk factors, and full clinical picture.

Depending on the patient, peptides may come up in conversations around recovery, tissue support, metabolic health, immune support, sexual wellness, cognition, sleep, or stress response. The important question is not "which peptide is popular?" It is "what is clinically appropriate for me, and how would we monitor it?"

Start with a complimentary 60 minute consultation. No cost. No commitment. Bring your questions, your goals, and your health history.

Educational only. Not medical advice. Peptide therapy should be discussed with a licensed clinician.

## Hashtags

#peptidetherapy
#integrativemedicine
#preventivemedicine
#functionalmedicine
#austinhealth
#austintx
#vitalhealth

## Sources Used

- Vital Health local review site: \`home-review.html\`, \`services-review.html\`, \`about-review.html\`.
- Vital Health meeting notes: \`meeting-2026-06-05/services-change-notes.md\`.
- NIH Genome glossary, peptide definition: https://www.genome.gov/genetics-glossary/Peptide
- NCBI Bookshelf, Biochemistry, Peptide: https://www.ncbi.nlm.nih.gov/books/NBK562260/
- FDA, Human Drug Compounding: https://www.fda.gov/drugs/guidance-compliance-regulatory-information/human-drug-compounding
- FDA, Certain Bulk Drug Substances for Use in Compounding that May Present Significant Safety Risks: https://www.fda.gov/drugs/human-drug-compounding/certain-bulk-drug-substances-use-compounding-may-present-significant-safety-risks

## Review Files

- \`review.html\`
- \`slide-1.png\` through \`slide-8.png\`
- \`slides/slide-1.html\` through \`slides/slide-8.html\`
`;
}

function css() {
  return `
    :root {
      --cream: #f5efe0;
      --paper: #fbf7ec;
      --forest: #1f4d2a;
      --deep: #12351e;
      --sage: #dce5d5;
      --mint: #e8f2df;
      --gold: #c9a04a;
      --terracotta: #c77a4a;
      --rose: #e9c8aa;
      --ink: #2a2a26;
      --muted: #676359;
      --line: #ded3b8;
    }
    * { box-sizing: border-box; }
    html, body { width: 1080px; height: 1350px; margin: 0; overflow: hidden; }
    body { font-family: Inter, Arial, sans-serif; background: var(--paper); }
    .slide {
      width: 1080px;
      height: 1350px;
      position: relative;
      overflow: hidden;
      background: var(--paper);
      color: var(--deep);
      isolation: isolate;
    }
    h1, h2 {
      margin: 0;
      font-family: Fraunces, Georgia, serif;
      font-weight: 400;
      letter-spacing: 0;
      line-height: .98;
    }
    em {
      font-family: "Cormorant Garamond", Fraunces, Georgia, serif;
      font-style: italic;
      font-weight: 400;
    }
    p { margin: 0; color: var(--muted); font-size: 27px; line-height: 1.48; }
    .rule { display: block; width: 54px; height: 2px; background: var(--gold); margin-bottom: 28px; }
    .tiny-num, .eyebrow, .corner {
      position: absolute;
      top: 34px;
      z-index: 10;
      font-size: 11px;
      letter-spacing: .38em;
      text-transform: uppercase;
      color: rgba(42,42,38,.66);
    }
    .tiny-num { left: 38px; }
    .eyebrow { right: 38px; text-align: right; }
    .corner.left { left: 38px; }
    .corner.right { right: 38px; }
    .s1 .tiny-num, .s1 .eyebrow { display: none; }
    .s7 .tiny-num, .s7 .eyebrow { color: rgba(245,239,224,.78); }
    .pagination {
      position: absolute;
      left: 0;
      right: 0;
      bottom: 30px;
      display: flex;
      justify-content: center;
      gap: 8px;
      z-index: 20;
    }
    .pagination span {
      width: 6px;
      height: 6px;
      border-radius: 999px;
      background: rgba(42,42,38,.24);
    }
    .pagination .active { width: 18px; background: var(--gold); }
    .s1, .s7 {
      background:
        radial-gradient(circle at 68% 18%, rgba(245,239,224,.22), transparent 28%),
        radial-gradient(circle at 24% 78%, rgba(201,160,74,.14), transparent 30%),
        linear-gradient(150deg, #12351e 0%, #58755d 100%);
      color: var(--cream);
    }
    .cover-photo, .labs-photo, .examples-photo, .final-photo {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: 0;
    }
    .cover-veil {
      position: absolute;
      inset: 0;
      z-index: 1;
      background:
        linear-gradient(180deg, rgba(18,53,30,.52), rgba(18,53,30,.08) 36%, rgba(18,53,30,.82) 100%),
        radial-gradient(circle at 28% 26%, rgba(199,122,74,.24), transparent 24%);
    }
    .s1 h1 { font-size: 92px; color: var(--cream); max-width: 820px; text-shadow: 0 2px 22px rgba(18,53,30,.22); }
    .s1 p { color: rgba(245,239,224,.88); margin-top: 24px; max-width: 620px; }
    .s1 .copy { position: absolute; left: 46px; right: 46px; bottom: 92px; z-index: 4; }
    .s1 .corner { color: rgba(245,239,224,.82); }
    .s1 .pagination span, .s7 .pagination span { background: rgba(245,239,224,.36); }
    .s1 .pagination .active, .s7 .pagination .active { background: var(--gold); }
    .hero-orbit {
      position: absolute;
      border: 1px solid rgba(245,239,224,.28);
      border-radius: 52% 48% 60% 40%;
      z-index: 2;
    }
    .orbit-a { width: 280px; height: 410px; right: -58px; top: 86px; transform: rotate(42deg); }
    .orbit-b { width: 210px; height: 330px; left: -80px; bottom: 70px; transform: rotate(62deg); }
    .s2 { background: linear-gradient(180deg, var(--paper), #fff7e8); }
    .s2 .split { display: grid; grid-template-columns: 51% 49%; height: 100%; }
    .s2 section { padding: 312px 62px 120px 56px; }
    .s2 h2 { font-size: 76px; }
    .s2 p { margin-top: 24px; max-width: 450px; }
    .molecule-field {
      position: relative;
      background: linear-gradient(180deg, #eef4e8, #fbf7ec);
      border-left: 1px solid rgba(31,77,42,.08);
      overflow: hidden;
    }
    .panel-photo {
      position: absolute;
      inset: 0;
      width: 100%;
      height: 100%;
      object-fit: cover;
      z-index: 0;
    }
    .panel-wash {
      position: absolute;
      inset: 0;
      z-index: 1;
      background:
        linear-gradient(180deg, rgba(245,239,224,.06), rgba(245,239,224,.48)),
        radial-gradient(circle at 66% 28%, rgba(199,122,74,.20), transparent 26%);
    }
    .molecule-field span {
      position: absolute;
      z-index: 2;
      width: 46px;
      height: 46px;
      border: 1px solid rgba(251,247,236,.78);
      border-radius: 50%;
      background: rgba(251,247,236,.18);
      backdrop-filter: blur(3px);
    }
    .molecule-field span:nth-child(1) { left: 150px; top: 300px; }
    .molecule-field span:nth-child(2) { right: 116px; top: 420px; }
    .molecule-field span:nth-child(3) { left: 260px; top: 610px; }
    .molecule-field span:nth-child(4) { left: 170px; bottom: 322px; }
    .molecule-field span:nth-child(5) { right: 70px; bottom: 230px; }
    .molecule-field i {
      position: absolute;
      z-index: 2;
      height: 1px;
      background: rgba(201,160,74,.92);
      transform-origin: left center;
      opacity: .9;
    }
    .l1 { width: 150px; left: 238px; top: 445px; transform: rotate(31deg); }
    .l2 { width: 165px; left: 340px; top: 600px; transform: rotate(-44deg); }
    .l3 { width: 154px; left: 170px; top: 810px; transform: rotate(-58deg); }
    .l4 { width: 170px; right: 112px; bottom: 312px; transform: rotate(28deg); }
    .s3 {
      background:
        linear-gradient(rgba(31,77,42,.035) 1px, transparent 1px),
        linear-gradient(90deg, rgba(31,77,42,.035) 1px, transparent 1px),
        linear-gradient(135deg, var(--cream), #f7ead6 54%, #eef4e8);
      background-size: 78px 78px;
    }
    .s3 .top-wide { position: absolute; left: 58px; right: 430px; top: 118px; }
    .s3 h2 { font-size: 76px; max-width: 650px; }
    .s3 .top-wide p { margin-top: 24px; max-width: 590px; font-size: 25px; }
    .s3-photo-card {
      position: absolute;
      right: 58px;
      top: 136px;
      width: 302px;
      height: 392px;
      margin: 0;
      border: 1px solid rgba(201,160,74,.78);
      background: var(--paper);
      overflow: hidden;
      z-index: 2;
    }
    .s3-photo-card img {
      width: 100%;
      height: 100%;
      object-fit: cover;
      object-position: 56% 50%;
      display: block;
      filter: saturate(.9) contrast(.96);
    }
    .context-panel {
      position: absolute;
      left: 58px;
      right: 58px;
      top: 582px;
      display: grid;
      grid-template-columns: 245px 1fr;
      gap: 30px;
      align-items: start;
      padding: 28px 32px;
      border-top: 1px solid var(--gold);
      border-bottom: 1px solid var(--gold);
      background: rgba(251,247,236,.58);
    }
    .context-panel span {
      font-family: Fraunces, Georgia, serif;
      font-size: 33px;
      line-height: 1.05;
      color: var(--deep);
    }
    .context-panel p {
      font-size: 22px;
      line-height: 1.42;
    }
    .card-row {
      position: absolute;
      left: 54px;
      right: 54px;
      bottom: 116px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border-top: 1px solid var(--gold);
      border-left: 1px solid var(--gold);
    }
    .card-row div {
      min-height: 122px;
      padding: 22px 22px 18px;
      border-right: 1px solid var(--gold);
      border-bottom: 1px solid var(--gold);
      color: var(--deep);
    }
    .card-row strong {
      display: block;
      font-size: 22px;
      font-weight: 500;
      margin-bottom: 10px;
    }
    .card-row span {
      display: block;
      color: var(--muted);
      font-size: 17px;
      line-height: 1.32;
    }
    .card-row div:nth-child(2) { background: rgba(220,229,213,.52); }
    .card-row div:nth-child(3) { background: rgba(233,200,170,.36); }
    .card-row div:nth-child(5) { background: rgba(201,160,74,.16); }
    .footnote { position: absolute; left: 54px; right: 54px; bottom: 62px; font-size: 21px; }
    .s4 {
      background:
        radial-gradient(circle at 86% 18%, rgba(199,122,74,.18), transparent 24%),
        linear-gradient(180deg, var(--paper), #f8ead8);
    }
    .s4-photo {
      position: absolute;
      right: 56px;
      top: 112px;
      width: 300px;
      height: 360px;
      object-fit: cover;
      object-position: 50% 55%;
      z-index: 1;
      border: 1px solid rgba(201,160,74,.74);
    }
    .s4-photo-wash {
      position: absolute;
      right: 56px;
      top: 112px;
      width: 300px;
      height: 360px;
      z-index: 2;
      background: linear-gradient(180deg, rgba(245,239,224,.08), rgba(245,239,224,.28));
      pointer-events: none;
    }
    .s4 .copy { position: absolute; left: 56px; top: 118px; width: 610px; z-index: 3; }
    .s4 h2 { font-size: 64px; }
    .s4 p { margin-top: 26px; }
    .s4-note {
      position: absolute;
      left: 56px;
      right: 56px;
      top: 548px;
      display: grid;
      grid-template-columns: 290px 1fr;
      gap: 32px;
      padding: 26px 30px;
      background: rgba(251,247,236,.72);
      border-top: 1px solid var(--gold);
      border-bottom: 1px solid var(--gold);
      z-index: 3;
    }
    .s4-note strong {
      font-family: Fraunces, Georgia, serif;
      font-size: 31px;
      font-weight: 400;
      line-height: 1.08;
      color: var(--deep);
    }
    .s4-note span {
      color: var(--muted);
      font-size: 22px;
      line-height: 1.42;
    }
    .topic-grid {
      position: absolute;
      left: 56px;
      right: 56px;
      bottom: 86px;
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 1px;
      background: var(--gold);
      border: 1px solid var(--gold);
    }
    .topic-grid div {
      min-height: 312px;
      background: #eef4e8;
      padding: 24px 20px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }
    .topic-grid div:nth-child(2) { background: #f4e5ce; }
    .topic-grid div:nth-child(3) { background: #e8f2df; }
    .topic-grid div:nth-child(4) { background: #efe8d2; }
    .topic-grid div:nth-child(5) { background: #efd7c0; }
    .topic-grid strong { font-family: Fraunces, Georgia, serif; font-size: 27px; font-weight: 400; line-height: 1.05; }
    .topic-grid span { color: var(--muted); font-size: 17px; line-height: 1.42; }
    .s5 {
      background:
        radial-gradient(circle at 78% 24%, rgba(201,160,74,.12), transparent 25%),
        linear-gradient(180deg, var(--sage), var(--paper));
    }
    .s5 .labs-photo {
      left: auto;
      width: 47%;
      object-position: 56% 50%;
    }
    .labs-wash {
      position: absolute;
      inset: 0;
      z-index: 1;
      background:
        linear-gradient(90deg, rgba(245,239,224,.98) 0%, rgba(245,239,224,.94) 52%, rgba(245,239,224,.28) 72%, rgba(245,239,224,.10) 100%),
        radial-gradient(circle at 14% 18%, rgba(232,200,170,.30), transparent 28%);
    }
    .s5 .copy { position: absolute; left: 58px; top: 118px; width: 510px; z-index: 2; }
    .s5 h2 { font-size: 88px; }
    .s5 p { margin-top: 28px; }
    .timeline {
      position: absolute;
      right: 64px;
      top: 220px;
      width: 330px;
      border-top: 1px solid var(--gold);
      z-index: 2;
      background: rgba(251,247,236,.74);
      padding: 0 22px;
      backdrop-filter: blur(8px);
    }
    .timeline div {
      border-bottom: 1px solid var(--gold);
      padding: 32px 0;
      font-size: 31px;
      font-family: Fraunces, Georgia, serif;
      color: var(--deep);
    }
    .timeline span {
      display: block;
      margin-bottom: 10px;
      font-family: Inter, Arial, sans-serif;
      color: var(--muted);
      font-size: 11px;
      letter-spacing: .34em;
    }
    .bottom-line {
      position: absolute;
      left: 58px;
      bottom: 78px;
      width: 720px;
      border-top: 1px solid var(--gold);
      padding-top: 24px;
      font-size: 24px;
      z-index: 2;
    }
    .s6 { background: var(--cream); }
    .examples-photo {
      height: 330px;
      bottom: auto;
      object-position: 50% 46%;
    }
    .examples-photo-wash {
      position: absolute;
      left: 0;
      right: 0;
      top: 0;
      height: 330px;
      z-index: 1;
      background: linear-gradient(180deg, rgba(18,53,30,.18), rgba(245,239,224,.24));
    }
    .s6 .copy { position: absolute; left: 50px; right: 50px; top: 372px; z-index: 2; }
    .s6 h2 { font-size: 66px; max-width: 850px; }
    .s6 p { margin-top: 20px; max-width: 790px; font-size: 24px; }
    .examples {
      position: absolute;
      left: 50px;
      right: 50px;
      bottom: 82px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      border-top: 1px solid var(--gold);
      border-left: 1px solid var(--gold);
      z-index: 2;
    }
    .examples div {
      min-height: 108px;
      padding: 19px 22px 17px;
      border-right: 1px solid var(--gold);
      border-bottom: 1px solid var(--gold);
      background: rgba(251,247,236,.70);
    }
    .examples div:nth-child(2), .examples div:nth-child(5) { background: rgba(232,200,170,.28); }
    .examples div:nth-child(3), .examples div:nth-child(6) { background: rgba(220,229,213,.42); }
    .examples strong {
      display: block;
      color: var(--deep);
      font-size: 19px;
      margin-bottom: 11px;
      font-weight: 500;
    }
    .examples span { color: var(--muted); font-size: 20px; line-height: 1.35; }
    .s7 .quote-mark {
      position: absolute;
      left: 64px;
      top: 118px;
      font-family: "Cormorant Garamond", Georgia, serif;
      font-style: italic;
      color: var(--gold);
      font-size: 160px;
      line-height: .5;
    }
    .s7 .quote {
      position: absolute;
      left: 80px;
      right: 330px;
      top: 240px;
      z-index: 3;
    }
    .s7 h2 { color: var(--cream); font-size: 78px; max-width: 660px; }
    .s7 p { color: rgba(245,239,224,.86); margin-top: 28px; max-width: 620px; }
    .s7-photo {
      position: absolute;
      right: 70px;
      top: 178px;
      width: 238px;
      height: 320px;
      object-fit: cover;
      object-position: 55% 50%;
      border: 1px solid rgba(201,160,74,.70);
      z-index: 2;
    }
    .s7-photo-wash {
      position: absolute;
      right: 70px;
      top: 178px;
      width: 238px;
      height: 320px;
      z-index: 3;
      background: linear-gradient(180deg, rgba(18,53,30,.16), rgba(18,53,30,.34));
      pointer-events: none;
    }
    .decision-grid {
      position: absolute;
      left: 80px;
      right: 80px;
      top: 632px;
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      border-top: 1px solid var(--gold);
      border-left: 1px solid var(--gold);
      z-index: 3;
    }
    .decision-grid div {
      min-height: 120px;
      padding: 18px 20px;
      border-right: 1px solid rgba(201,160,74,.74);
      border-bottom: 1px solid rgba(201,160,74,.74);
      background: rgba(245,239,224,.08);
    }
    .decision-grid strong {
      display: block;
      color: var(--cream);
      font-size: 20px;
      font-weight: 500;
      margin-bottom: 10px;
    }
    .decision-grid span {
      display: block;
      color: rgba(245,239,224,.78);
      font-size: 16px;
      line-height: 1.34;
    }
    .quiet-list {
      position: absolute;
      left: 80px;
      right: 80px;
      bottom: 92px;
      border-top: 1px solid var(--gold);
    }
    .quiet-list span {
      display: block;
      padding: 19px 0;
      border-bottom: 1px solid rgba(201,160,74,.72);
      color: rgba(245,239,224,.92);
      font-size: 22px;
    }
    .s8 {
      background:
        radial-gradient(circle at 50% 68%, rgba(220,229,213,.92), transparent 30%),
        linear-gradient(180deg, var(--paper), #eef4e8);
      text-align: center;
    }
    .final-photo {
      top: auto;
      height: 420px;
      object-position: 50% 64%;
    }
    .final-wash {
      position: absolute;
      inset: auto 0 0 0;
      height: 420px;
      z-index: 1;
      background: linear-gradient(180deg, rgba(245,239,224,.05), rgba(245,239,224,.35));
    }
    .bird {
      position: absolute;
      width: 96px;
      top: 82px;
      left: 50%;
      transform: translateX(-50%);
      opacity: .86;
      z-index: 3;
    }
    .s8 .copy { position: absolute; left: 110px; right: 110px; top: 214px; z-index: 3; }
    .s8 .rule { margin-left: auto; margin-right: auto; }
    .s8 h2 { font-size: 78px; }
    .s8 p { margin: 30px auto 0; max-width: 760px; }
    .cta-band {
      position: absolute;
      left: 54px;
      right: 54px;
      bottom: 86px;
      display: grid;
      grid-template-columns: 1fr 1fr;
      border-top: 1px solid var(--gold);
      border-bottom: 1px solid var(--gold);
      background: rgba(251,247,236,.82);
      z-index: 3;
      backdrop-filter: blur(8px);
    }
    .cta-band span {
      padding: 28px 18px;
      font-size: 15px;
      letter-spacing: .24em;
      text-transform: uppercase;
      color: var(--deep);
    }
    .cta-band span + span { border-left: 1px solid var(--gold); }
  `;
}

async function render() {
  fs.mkdirSync(slidesDir, { recursive: true });

  for (const file of fs.readdirSync(dir)) {
    if (/^slide-\d+\.png$/.test(file)) {
      fs.unlinkSync(path.join(dir, file));
    }
  }

  slides.forEach((slide, index) => {
    fs.writeFileSync(path.join(slidesDir, `slide-${index + 1}.html`), slidePage(slide, index));
  });

  const browser = await chromium.launch({ headless: true });
  const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
  for (let i = 0; i < slides.length; i += 1) {
    const fileUrl = `file://${path.join(slidesDir, `slide-${i + 1}.html`)}`;
    await page.goto(fileUrl, { waitUntil: "networkidle" });
    await page.screenshot({ path: path.join(dir, `slide-${i + 1}.png`), fullPage: false });
  }
  await browser.close();

  fs.writeFileSync(path.join(dir, "review.html"), reviewPage());
  fs.writeFileSync(path.join(dir, "post.md"), postMarkdown());
  console.log(`Rendered ${slides.length} slides into ${dir}`);
}

render().catch((error) => {
  console.error(error);
  process.exit(1);
});
