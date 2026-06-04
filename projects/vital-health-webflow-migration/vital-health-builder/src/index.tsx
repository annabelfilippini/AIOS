import React, { useState } from "react";
import ReactDOM from "react-dom/client";

const SITE = {
  portalUrl: "https://vitalhealth.md-hq.com",
  phone: "(512) 559-4350",
  phoneHref: "tel:5125594350",
  email: "info@vitalhealthim.com",
  address: "7000 Bee Cave Road, Suite 310, Austin, TX 78746",
  hero:
    "https://cdn.prod.website-files.com/6a15e6f364922623e13946da/6a15e762c2275bbc9df0cb25_homepage-hero.png",
  logo:
    "https://cdn.prod.website-files.com/6a15e6f364922623e13946da/6a15e761c2275bbc9df0caf7_vh-logo-transparent.png",
};

const homePageWhtml = `
<main class="vh-page" style="background:#F5EFE0;color:#2A2A26;font-family:Inter,Arial,sans-serif;">
  <section class="vh-hero" style="min-height:92vh;display:flex;align-items:center;position:relative;overflow:hidden;background:#F5EFE0;">
    <div class="vh-hero-bg" style="position:absolute;inset:0;background-image:linear-gradient(90deg,#F5EFE0 0%,#F5EFE0 42%,rgba(245,239,224,.82) 58%,rgba(245,239,224,.28) 78%,rgba(245,239,224,.02) 100%),url('${SITE.hero}');background-size:cover;background-position:center;"></div>
    <div class="vh-wrap" style="position:relative;z-index:2;width:100%;max-width:1320px;margin:0 auto;padding:120px 56px 90px;">
      <img src="${SITE.logo}" alt="Vital Health Integrative Medicine" style="width:220px;height:auto;margin-bottom:34px;" />
      <div class="vh-eyebrow" style="font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:#7A776B;margin-bottom:22px;">Austin, Texas · Integrative Medicine · Since 1970</div>
      <h1 style="max-width:720px;margin:0 0 28px;font-family:Fraunces,Georgia,serif;font-weight:300;font-size:78px;line-height:1.04;letter-spacing:-.02em;color:#2A2A26;">Your journey to <span style="color:#1F4D2A;font-weight:400;">optimal vitality.</span></h1>
      <p style="max-width:540px;margin:0 0 40px;font-size:17px;line-height:1.75;color:#3F3F38;">Integrative, regenerative, and preventive medicine — built on fifty years of clinical foundation and the long view of whole-body health. From the inside out.</p>
      <div style="display:flex;gap:22px;align-items:center;flex-wrap:wrap;">
        <a href="/contact" style="display:inline-flex;align-items:center;gap:10px;background:#1F4D2A;color:#F5EFE0;padding:16px 30px;text-decoration:none;font-weight:500;">Schedule a consultation →</a>
        <a href="/services" style="color:#2A2A26;text-decoration:none;border-bottom:1px solid #C9A04A;padding-bottom:6px;font-size:12px;letter-spacing:.22em;text-transform:uppercase;">Explore our services →</a>
      </div>
    </div>
  </section>

  <section class="vh-facts" style="background:#FBF7EC;padding:96px 56px 108px;border-top:1px solid #E0D7BE;">
    <div style="max-width:1320px;margin:0 auto;">
      <div style="font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:#1F4D2A;margin-bottom:14px;">The practice</div>
      <h2 style="max-width:720px;margin:0 0 48px;font-family:Fraunces,Georgia,serif;font-weight:300;font-size:42px;line-height:1.1;">A <span style="color:#1F4D2A;font-weight:400;">different kind</span> of integrative care.</h2>
      <div style="display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:44px;border-top:1px solid #E0D7BE;padding-top:44px;">
        <div><div style="font-family:Fraunces,Georgia,serif;font-size:58px;line-height:1;">50<span style="color:#C9A04A;">+</span></div><p style="color:#7A776B;">Years of clinical foundation, brought by founder Dr. Joseph Feste.</p></div>
        <div><div style="font-family:Fraunces,Georgia,serif;font-size:58px;line-height:1;">4</div><p style="color:#7A776B;">Dedicated practitioners — one MD, two NPs, one founding advisor.</p></div>
        <div><div style="font-family:Fraunces,Georgia,serif;font-size:58px;line-height:1;">90<span style="color:#A6823A;font-family:Inter,Arial,sans-serif;font-size:19px;">min</span></div><p style="color:#7A776B;">Dedicated to your first visit — a full workup, not a triage.</p></div>
        <div><div style="font-family:Fraunces,Georgia,serif;font-size:58px;line-height:1;">$0</div><p style="color:#7A776B;">Complimentary initial consultation. No cost, no commitment.</p></div>
      </div>
    </div>
  </section>

  <section class="vh-services" style="padding:132px 56px;background:#F5EFE0;">
    <div style="max-width:1320px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:80px;align-items:end;margin-bottom:70px;">
      <div>
        <div style="font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:#1F4D2A;margin-bottom:18px;">What we offer</div>
        <h2 style="margin:0;font-family:Fraunces,Georgia,serif;font-size:58px;font-weight:300;line-height:1.02;">Four pillars of <span style="color:#1F4D2A;font-weight:400;">integrative care.</span></h2>
      </div>
      <p style="font-size:16px;line-height:1.75;color:#3F3F38;">Integrative medicine, regenerative therapies, medical weight loss, and hormone optimization — prescribed against your physiology, not a protocol.</p>
    </div>
    <div style="max-width:1320px;margin:0 auto;display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:20px;">
      ${[
        ["Peptide Therapy", "Cellular-level regrowth protocols that target longevity, recovery, cognition, and vitality through targeted peptides.", "/services#peptide"],
        ["Hormone Optimization", "Bio-identical hormone therapy for men and women — micro-dosed against the labs, adjusted quarterly.", "/services#hormone"],
        ["Medical Weight Loss", "Physician-supervised GLP-1 programs — Semaglutide and Tirzepatide — paired with lab-based support.", "/services#weight"],
        ["Wellness & Rejuvenation", "Exosome regenerative therapy, IV infusions, and ozone protocols for tissue repair and restoration.", "/services#wellness"],
      ]
        .map(
          ([title, copy, href]) => `
        <a href="${href}" style="display:flex;flex-direction:column;gap:18px;min-height:310px;background:#FBF7EC;border:1px solid #E0D7BE;border-radius:4px;padding:38px 30px 32px;color:#2A2A26;text-decoration:none;">
          <div style="width:44px;height:44px;border:1px solid #C9A04A;"></div>
          <h3 style="font-family:Fraunces,Georgia,serif;font-size:22px;line-height:1.2;margin:0;">${title}</h3>
          <p style="font-size:14.5px;line-height:1.65;color:#3F3F38;">${copy}</p>
          <span style="margin-top:auto;border-top:1px solid #E0D7BE;padding-top:14px;font-size:11px;letter-spacing:.24em;text-transform:uppercase;color:#1F4D2A;">Learn more →</span>
        </a>`
        )
        .join("")}
    </div>
  </section>

  <section class="vh-philosophy" style="padding:120px 56px;background:#D6DCC9;text-align:center;border-top:1px solid #E0D7BE;border-bottom:1px solid #E0D7BE;">
    <div style="max-width:980px;margin:0 auto;">
      <div style="font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:#1F4D2A;margin-bottom:18px;">The philosophy</div>
      <h2 style="font-family:Fraunces,Georgia,serif;font-size:52px;font-weight:300;line-height:1.08;margin:0 0 34px;">A practice built on <span style="color:#1F4D2A;font-weight:400;">legacy.</span><br />A future built on <span style="color:#1F4D2A;font-weight:400;">you.</span></h2>
      <p style="font-size:17px;line-height:1.8;color:#3F3F38;">Vital Health continues to operate on the strong clinical foundations established by our founder, Dr. Joseph Feste. Care here reads more like a relationship than an appointment — measurement that takes weeks, not minutes, and protocols written against your labs, not assumption.</p>
      <a href="/about" style="display:inline-block;margin-top:32px;color:#2A2A26;text-decoration:none;border-bottom:1px solid #C9A04A;padding-bottom:6px;font-size:12px;letter-spacing:.22em;text-transform:uppercase;">Meet the team →</a>
    </div>
  </section>

  <section class="vh-schedule" style="padding:136px 56px;background:#EFE8D5;text-align:center;">
    <div style="max-width:980px;margin:0 auto;">
      <div style="font-size:11px;letter-spacing:.28em;text-transform:uppercase;color:#1F4D2A;margin-bottom:22px;">Schedule a visit</div>
      <h2 style="font-family:Fraunces,Georgia,serif;font-size:70px;font-weight:300;line-height:1;margin:0 0 28px;">Start with the <span style="color:#1F4D2A;font-weight:400;">complimentary</span> consultation.</h2>
      <p style="font-size:17px;line-height:1.75;color:#3F3F38;margin:0 auto 42px;max-width:590px;">Thirty minutes, no cost. We'll hear what's bringing you in and tell you whether Vital Health is the right fit.</p>
      <div style="display:flex;gap:22px;justify-content:center;flex-wrap:wrap;">
        <a href="${SITE.portalUrl}" style="background:#1F4D2A;color:#F5EFE0;padding:16px 30px;text-decoration:none;font-weight:500;">Book a consultation →</a>
        <a href="${SITE.phoneHref}" style="border:1.5px solid #1F4D2A;color:#1F4D2A;padding:14px 28px;text-decoration:none;font-weight:500;">Call ${SITE.phone}</a>
      </div>
      <div style="display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:44px;text-align:left;margin-top:70px;padding-top:44px;border-top:1px solid #CFC4A6;">
        <div><div style="font-size:10px;letter-spacing:.28em;text-transform:uppercase;color:#A6823A;">Location</div><p>${SITE.address}</p></div>
        <div><div style="font-size:10px;letter-spacing:.28em;text-transform:uppercase;color:#A6823A;">Hours</div><p>Monday–Friday<br />8am–5pm</p></div>
        <div><div style="font-size:10px;letter-spacing:.28em;text-transform:uppercase;color:#A6823A;">Direct</div><p>${SITE.phone}<br />${SITE.email}</p></div>
      </div>
    </div>
  </section>
</main>`;

async function findInsertionTarget() {
  const selected = await webflow.getSelectedElement();
  if (selected && "children" in selected && selected.children) return selected;

  const allElements = await webflow.getAllElements();
  return allElements.find((element) => element.type === "Body") ?? selected;
}

const App: React.FC = () => {
  const [status, setStatus] = useState("Ready.");
  const [busy, setBusy] = useState(false);

  const insertHomePage = async () => {
    setBusy(true);
    setStatus("Looking for the page body or selected parent element...");
    try {
      if (!webflow.insertElementFromWHTML) {
        throw new Error("This Webflow Designer version does not expose insertElementFromWHTML.");
      }

      const target = await findInsertionTarget();
      if (!target) {
        throw new Error("Open the Home page in Designer, select the Body or any parent section, then try again.");
      }

      setStatus("Inserting Vital Health home page structure...");
      await webflow.insertElementFromWHTML(homePageWhtml, target, "append");
      setStatus("Inserted the first-pass Home page structure. Review it in Designer, then style/adjust as needed.");
    } catch (error) {
      setStatus(error instanceof Error ? error.message : "Something went wrong while inserting the page.");
    } finally {
      setBusy(false);
    }
  };

  return (
    <main className="app">
      <h1>Vital Health Builder</h1>
      <p>
        Open the Home page in Webflow Designer, select the Body or a top-level wrapper, then insert the
        Vercel-inspired structure.
      </p>
      <button onClick={insertHomePage} disabled={busy}>
        {busy ? "Building..." : "Insert Home Page"}
      </button>
      <p className="status">{status}</p>
      <p className="note">
        This creates the first editable structure. Webflow may still need Designer polish for responsive
        behavior, interactions, and CMS bindings.
      </p>
    </main>
  );
};

const root = ReactDOM.createRoot(document.getElementById("root") as HTMLElement);
root.render(<App />);
