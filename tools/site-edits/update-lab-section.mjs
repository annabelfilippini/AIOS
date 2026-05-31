import fs from "node:fs";

const file = process.argv[2];
if (!file) {
  console.error("Usage: node tools/site-edits/update-lab-section.mjs <html-file>");
  process.exit(1);
}

let bundle = fs.readFileSync(file, "utf8");
const templateMatch = bundle.match(/<script type="__bundler\/template">\n([\s\S]*?)\n\s*<\/script>/);
if (!templateMatch) {
  throw new Error("Could not find bundled template script.");
}

let template = JSON.parse(templateMatch[1]);

template = template
  .replace('<section class="hero" data-screen-label="01 Hero">', '<section id="home" class="hero" data-screen-label="01 Hero">')
  .replace('<section class="about" data-screen-label="02 About">', '<section id="about" class="about" data-screen-label="02 About">')
  .replace('<a href="#" class="is-active">Home</a>', '<a href="#home" class="is-active">Home</a>')
  .replace('<a href="#">Work With Me</a>', '<a href="#doorways">Work With Me</a>')
  .replace('<a href="#">Skills</a>', '<a href="#doorways">Skills</a>')
  .replace('<a href="#">Lab</a>', '<a href="#lab">Lab</a>')
  .replace('<a href="#">About</a>', '<a href="#about">About</a>')
  .replace('<a href="#">Contact</a>', '<a href="#lab">Contact</a>')
  .replace('<section class="doorways" data-screen-label="03 Doorways">', '<section id="doorways" class="doorways" data-screen-label="03 Doorways">')
  .replace('<a class="card" href="#">\n          <div class="card__num">04</div>', '<a class="card" href="#lab">\n          <div class="card__num">04</div>');

const labCss = String.raw`

  /* ============ SECTION 4 - LAB ============ */
  .lab {
    background: var(--forest);
    color: var(--cream);
    padding: 120px 48px 132px;
    position: relative;
    overflow: hidden;
  }
  .lab::before {
    content: "";
    position: absolute;
    inset: 0;
    background:
      linear-gradient(90deg, rgba(245, 237, 222, 0.055) 1px, transparent 1px),
      linear-gradient(0deg, rgba(245, 237, 222, 0.045) 1px, transparent 1px);
    background-size: 56px 56px;
    mask-image: linear-gradient(to bottom, transparent 0%, black 16%, black 88%, transparent 100%);
    pointer-events: none;
  }
  .lab__inner {
    position: relative;
    max-width: 1280px;
    margin: 0 auto;
  }
  .lab__header {
    display: grid;
    grid-template-columns: minmax(0, 0.9fr) minmax(320px, 0.7fr);
    gap: 80px;
    align-items: end;
    margin-bottom: 64px;
  }
  .lab__eyebrow {
    color: var(--butter);
    font-weight: 700;
    font-size: 14px;
    letter-spacing: 0.22em;
    text-transform: uppercase;
    margin: 0 0 22px;
  }
  .lab__title {
    font-family: var(--display);
    font-weight: 500;
    font-size: clamp(44px, 6vw, 84px);
    line-height: 0.98;
    letter-spacing: -0.02em;
    color: var(--cream);
    margin: 0;
    max-width: 11ch;
    text-wrap: balance;
    font-variation-settings: "opsz" 96;
  }
  .lab__lede {
    font-size: 18px;
    line-height: 1.6;
    color: rgba(250, 245, 234, 0.86);
    margin: 0;
    max-width: 46ch;
    text-wrap: pretty;
  }
  .lab__grid {
    display: grid;
    grid-template-columns: repeat(3, minmax(0, 1fr));
    gap: 18px;
  }
  .project {
    min-height: 360px;
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    gap: 28px;
    padding: 24px;
    border: 1px solid rgba(245, 237, 222, 0.20);
    border-radius: 8px;
    background: rgba(250, 245, 234, 0.07);
    box-shadow: 0 18px 40px rgba(12, 27, 20, 0.20);
  }
  .project--wide { grid-column: span 2; }
  .project__meta {
    display: flex;
    justify-content: space-between;
    gap: 18px;
    align-items: center;
    color: var(--butter);
    font-size: 12px;
    font-weight: 700;
    letter-spacing: 0.16em;
    text-transform: uppercase;
  }
  .project__status {
    color: rgba(250, 245, 234, 0.72);
    letter-spacing: 0.12em;
  }
  .project__title {
    font-family: var(--display);
    font-size: clamp(30px, 3.4vw, 48px);
    line-height: 1.02;
    color: var(--cream);
    margin: 0 0 14px;
    letter-spacing: -0.01em;
    font-variation-settings: "opsz" 72;
  }
  .project__body {
    color: rgba(250, 245, 234, 0.82);
    font-size: 16px;
    line-height: 1.55;
    margin: 0;
    max-width: 54ch;
    text-wrap: pretty;
  }
  .project__visual {
    position: relative;
    min-height: 138px;
    border-radius: 8px;
    background: var(--cream);
    overflow: hidden;
  }
  .project__visual span { position: absolute; display: block; }
  .visual--system span:nth-child(1) { width: 62px; height: 62px; border-radius: 999px; background: var(--coral); left: 30px; top: 36px; }
  .visual--system span:nth-child(2) { width: 34px; height: 34px; border-radius: 999px; background: var(--butter); left: 142px; top: 24px; }
  .visual--system span:nth-child(3) { width: 46px; height: 46px; border-radius: 999px; background: var(--sage); right: 44px; top: 56px; }
  .visual--system span:nth-child(4) { height: 2px; background: var(--forest); opacity: .25; left: 82px; right: 72px; top: 67px; transform: rotate(-6deg); transform-origin: left center; }
  .visual--audit span:nth-child(1) { inset: 22px 26px auto 26px; height: 28px; background: var(--coral); border-radius: 6px; }
  .visual--audit span:nth-child(2) { left: 26px; top: 66px; width: 38%; height: 42px; background: var(--sage); border-radius: 6px; }
  .visual--audit span:nth-child(3) { right: 26px; top: 66px; width: 46%; height: 42px; background: var(--butter); border-radius: 6px; }
  .visual--audit span:nth-child(4) { left: 26px; right: 26px; bottom: 20px; height: 8px; background: var(--forest); opacity: .35; border-radius: 999px; }
  .visual--network span:nth-child(1) { width: 72px; height: 72px; background: var(--maroon); left: 26px; top: 34px; border-radius: 8px; }
  .visual--network span:nth-child(2) { width: 72px; height: 72px; background: var(--sage); right: 26px; top: 34px; border-radius: 8px; }
  .visual--network span:nth-child(3) { width: 42px; height: 42px; background: var(--butter); left: calc(50% - 21px); top: 49px; border-radius: 999px; }
  .visual--network span:nth-child(4) { height: 2px; left: 84px; right: 84px; top: 70px; background: var(--forest); opacity: .35; }
  .visual--wayloft span:nth-child(1) { width: 100px; height: 100px; border: 2px solid var(--forest); border-radius: 999px; left: 34px; top: 20px; }
  .visual--wayloft span:nth-child(2) { width: 84px; height: 10px; background: var(--coral); left: 104px; top: 62px; transform: rotate(-18deg); border-radius: 999px; }
  .visual--wayloft span:nth-child(3) { width: 58px; height: 58px; background: var(--butter); right: 36px; top: 40px; clip-path: polygon(50% 0, 100% 86%, 0 86%); }
  .visual--spent span:nth-child(1) { left: 30px; bottom: 24px; width: 34px; height: 42px; background: var(--sage); border-radius: 6px 6px 0 0; }
  .visual--spent span:nth-child(2) { left: 82px; bottom: 24px; width: 34px; height: 76px; background: var(--butter); border-radius: 6px 6px 0 0; }
  .visual--spent span:nth-child(3) { left: 134px; bottom: 24px; width: 34px; height: 56px; background: var(--coral); border-radius: 6px 6px 0 0; }
  .visual--spent span:nth-child(4) { right: 34px; top: 38px; width: 72px; height: 72px; border: 10px solid var(--maroon); border-left-color: transparent; border-radius: 999px; }
  .visual--home span:nth-child(1) { left: 30px; top: 52px; width: 78px; height: 60px; background: var(--sage); border-radius: 6px; }
  .visual--home span:nth-child(2) { left: 24px; top: 30px; width: 90px; height: 58px; background: var(--coral); clip-path: polygon(50% 0, 100% 52%, 88% 52%, 88% 100%, 12% 100%, 12% 52%, 0 52%); }
  .visual--home span:nth-child(3) { right: 28px; top: 30px; width: 112px; height: 14px; background: var(--forest); opacity: .28; border-radius: 999px; }
  .visual--home span:nth-child(4) { right: 54px; top: 64px; width: 86px; height: 42px; border: 2px solid var(--butter); border-radius: 999px; }
  .visual--pickleball span:nth-child(1) { width: 74px; height: 74px; border-radius: 999px; background: var(--butter); left: 34px; top: 32px; }
  .visual--pickleball span:nth-child(2) { width: 74px; height: 74px; border: 3px solid var(--forest); border-radius: 999px; left: 34px; top: 32px; background: linear-gradient(90deg, transparent 48%, var(--forest) 49%, var(--forest) 51%, transparent 52%); opacity: .35; }
  .visual--pickleball span:nth-child(3) { right: 34px; top: 34px; width: 92px; height: 70px; border: 3px solid var(--coral); border-radius: 8px; }
  .visual--pickleball span:nth-child(4) { right: 78px; top: 34px; width: 3px; height: 70px; background: var(--coral); }
`;

const responsiveCss = String.raw`

    .lab { padding: 72px 20px 88px; }
    .lab__header { grid-template-columns: 1fr; gap: 28px; margin-bottom: 36px; }
    .lab__title { max-width: none; }
    .lab__grid { grid-template-columns: 1fr; }
    .project--wide { grid-column: auto; }
    .project { min-height: auto; padding: 22px; }
    .project__visual { min-height: 124px; }
`;

template = template.replace('\n  /* ============ RESPONSIVE ============ */', labCss + '\n  /* ============ RESPONSIVE ============ */');
template = template.replace('    .card { padding: 24px; min-height: auto; }\n  }', '    .card { padding: 24px; min-height: auto; }' + responsiveCss + '\n  }');

const labSection = String.raw`

  <!-- ============ LAB ============ -->
  <section id="lab" class="lab" data-screen-label="04 Lab">
    <div class="lab__inner">
      <header class="lab__header">
        <div>
          <p class="lab__eyebrow">Lab</p>
          <h2 class="lab__title">The projects on my bench.</h2>
        </div>
        <p class="lab__lede">This is the working room: the businesses, apps, research systems, and strange little useful tools I am building to understand where AI actually helps people move faster, choose better, and get unstuck.</p>
      </header>

      <div class="lab__grid">
        <article class="project project--wide">
          <div class="project__meta"><span>01 / AI-OS</span><span class="project__status">Operating system</span></div>
          <div class="project__visual visual--system" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
          <div>
            <h3 class="project__title">AI-OS + Annie</h3>
            <p class="project__body">A personal AI operating system for keeping projects, agents, research, inboxes, handoffs, memory, and daily decisions in one coherent place. Annie is the front door; Garry and Business Partner help with strategy, review, and shipping.</p>
          </div>
        </article>

        <article class="project">
          <div class="project__meta"><span>02 / Websites</span><span class="project__status">Pilot</span></div>
          <div class="project__visual visual--audit" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
          <div>
            <h3 class="project__title">Website Audit Studio</h3>
            <p class="project__body">A hands-on audit process for small businesses: clearer messaging, better site structure, redesign mockups, and practical next steps owners can actually use.</p>
          </div>
        </article>

        <article class="project">
          <div class="project__meta"><span>03 / Agencies</span><span class="project__status">Research</span></div>
          <div class="project__visual visual--network" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
          <div>
            <h3 class="project__title">Agency Audit Network</h3>
            <p class="project__body">A referral layer between small businesses and AI consulting teams, designed so owners arrive with clearer needs and agencies meet better-fit clients.</p>
          </div>
        </article>

        <article class="project project--wide">
          <div class="project__meta"><span>04 / Travel</span><span class="project__status">Product</span></div>
          <div class="project__visual visual--wayloft" aria-hidden="true"><span></span><span></span><span></span></div>
          <div>
            <h3 class="project__title">Wayloft</h3>
            <p class="project__body">A travel decision engine for sorting through points, cards, perks, fares, and tradeoffs. The goal is to make the smartest travel move feel obvious instead of like a spreadsheet fog.</p>
          </div>
        </article>

        <article class="project">
          <div class="project__meta"><span>05 / Money</span><span class="project__status">App</span></div>
          <div class="project__visual visual--spent" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
          <div>
            <h3 class="project__title">Spent</h3>
            <p class="project__body">A personal finance experiment around making spending visible, calm, and behaviorally useful without turning money tracking into another chore.</p>
          </div>
        </article>

        <article class="project">
          <div class="project__meta"><span>06 / Housing</span><span class="project__status">Automation</span></div>
          <div class="project__visual visual--home" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
          <div>
            <h3 class="project__title">Apartment Hunt</h3>
            <p class="project__body">A lightweight search-and-digest system for tracking listings, filtering the noise, and keeping the best options easy to compare.</p>
          </div>
        </article>

        <article class="project">
          <div class="project__meta"><span>07 / Community</span><span class="project__status">Portal</span></div>
          <div class="project__visual visual--pickleball" aria-hidden="true"><span></span><span></span><span></span><span></span></div>
          <div>
            <h3 class="project__title">Pickleball Portal</h3>
            <p class="project__body">A community tool for organizing courts, events, rules, and local knowledge into a friendlier shared hub.</p>
          </div>
        </article>
      </div>
    </div>
  </section>
`;

template = template.replace('  <!-- Annabel will add more sections (Footer, Contact, etc.) here -->', labSection + '\n\n  <!-- Annabel will add more sections (Footer, Contact, etc.) here -->');

const nextTemplateScript = `<script type="__bundler/template">\n${JSON.stringify(template)}\n  </script>`;
bundle = bundle.replace(templateMatch[0], nextTemplateScript);
fs.writeFileSync(file, bundle);
