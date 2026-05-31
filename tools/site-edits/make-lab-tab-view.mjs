import fs from "node:fs";

const file = process.argv[2];
if (!file) {
  console.error("Usage: node tools/site-edits/make-lab-tab-view.mjs <html-file>");
  process.exit(1);
}

let bundle = fs.readFileSync(file, "utf8");
const templateMatch = bundle.match(/<script type="__bundler\/template">\n([\s\S]*?)\n\s*<\/script>/);
if (!templateMatch) {
  throw new Error("Could not find bundled template script.");
}

let template = JSON.parse(templateMatch[1]);

if (!template.includes(".lab {")) {
  throw new Error("Lab styles not found.");
}

if (!template.includes(".site-view--lab")) {
  template = template.replace(
    "  .lab {\n    background: var(--forest);",
    "  .lab {\n    display: none;\n    background: var(--forest);"
  );

  const tabCss = String.raw`

  /* ============ TAB VIEWS ============ */
  body.site-view--lab { background: var(--forest); }
  body.site-view--lab .hero {
    min-height: 96px;
    height: 96px;
    background: var(--forest);
    overflow: visible;
  }
  body.site-view--lab .hero__wordmark,
  body.site-view--lab .hero__photo,
  body.site-view--lab .about,
  body.site-view--lab .doorways {
    display: none;
  }
  body.site-view--lab .nav {
    position: fixed;
    background: rgba(31, 63, 47, 0.96);
    box-shadow: 0 10px 28px rgba(12, 27, 20, 0.18);
  }
  body.site-view--lab .lab {
    display: block;
    min-height: calc(100vh - 96px);
    padding-top: 156px;
  }
  body:not(.site-view--lab) .lab { display: none; }
`;

  template = template.replace("\n  /* ============ RESPONSIVE ============ */", tabCss + "\n  /* ============ RESPONSIVE ============ */");
}

const oldScript = String.raw`
</body></html>`;

const newScript = String.raw`
<script>
  const setSiteView = () => {
    const isLab = window.location.hash === '#lab';
    document.body.classList.toggle('site-view--lab', isLab);
    document.querySelectorAll('.nav__links a').forEach((link) => {
      const href = link.getAttribute('href');
      link.classList.toggle('is-active', isLab ? href === '#lab' : href === '#home');
    });
    if (!isLab && window.location.hash === '#home') {
      document.getElementById('home')?.scrollIntoView();
    }
  };
  window.addEventListener('hashchange', setSiteView);
  setSiteView();
</script>
</body></html>`;

if (!template.includes("const setSiteView = () =>")) {
  template = template.replace(oldScript, newScript);
}

const safeTemplateJson = JSON.stringify(template).split("</script>").join("<\\/script>");
const nextTemplateScript = `<script type="__bundler/template">\n${safeTemplateJson}\n  </script>`;
bundle = bundle.replace(templateMatch[0], nextTemplateScript);
fs.writeFileSync(file, bundle);
