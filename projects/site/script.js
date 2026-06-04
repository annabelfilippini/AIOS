const toggle = document.querySelector(".nav-toggle");
const nav = document.querySelector(".site-nav");

toggle?.addEventListener("click", () => {
  const isOpen = nav.classList.toggle("open");
  toggle.setAttribute("aria-expanded", String(isOpen));
});

nav?.addEventListener("click", (event) => {
  if (event.target.matches("a")) {
    nav.classList.remove("open");
    toggle?.setAttribute("aria-expanded", "false");
  }
});

const draftButton = document.querySelector("#draft-inquiry");
const contactForm = document.querySelector(".contact-form");

draftButton?.addEventListener("click", () => {
  const data = new FormData(contactForm);
  const name = data.get("name") || "";
  const email = data.get("email") || "";
  const website = data.get("website") || "";
  const path = data.get("path") || "";
  const message = data.get("message") || "";
  const body = [
    "Hi Annabel,",
    "",
    "I would love your thoughts on where to start.",
    "",
    `Name: ${name}`,
    `Email: ${email}`,
    `Business or website: ${website}`,
    `Path: ${path}`,
    "",
    "What feels frustrating right now:",
    String(message),
  ].join("\n");

  window.location.href = `mailto:?subject=${encodeURIComponent(
    "Website / AI inquiry"
  )}&body=${encodeURIComponent(body)}`;
});

const frictionLabels = {
  time: "Time sink",
  handoff: "Wait / handoff loop",
  quality: "Quality or rework risk",
  data: "Scattered data or stale context",
  customer: "Customer-visible friction",
  risk: "Compliance, privacy, or reputation risk",
};

function getAuditData(auditForm) {
  if (!auditForm) return null;
  const data = new FormData(auditForm);
  return {
    business: String(data.get("business") || "").trim(),
    size: String(data.get("size") || "").trim(),
    area: String(data.get("area") || "").trim(),
    workflow: String(data.get("workflow") || "").trim(),
    friction: String(data.get("friction") || "").trim(),
    frequency: String(data.get("frequency") || "").trim(),
    roles: String(data.get("roles") || "").trim(),
    tools: String(data.get("tools") || "").trim(),
    goal: String(data.get("goal") || "").trim(),
  };
}

function getReadinessNote(values) {
  if (values.friction === "risk") {
    return "Human approval and clear rules should come before automation.";
  }
  if (values.friction === "data") {
    return "This may need cleanup before automation can be reliable.";
  }
  if (values.friction === "handoff") {
    return "The first win is likely clearer ownership and closed-loop handoffs.";
  }
  if (values.frequency === "Daily" || values.frequency === "Weekly") {
    return "This sounds frequent enough to justify a deeper paid audit.";
  }
  return "This may be worth scoping if the cost or customer impact is meaningful.";
}

function buildAuditSummary(values) {
  return [
    "Free AI audit preview",
    "",
    `Business: ${values.business || "-"}`,
    `Industry / size: ${values.size || "-"}`,
    `Likely audit area: ${values.area || "-"}`,
    `Workflow: ${values.workflow || "-"}`,
    `Friction: ${frictionLabels[values.friction] || "-"}`,
    `Frequency: ${values.frequency || "-"}`,
    `People involved: ${values.roles || "-"}`,
    `Tools involved: ${values.tools || "-"}`,
    `90-day goal: ${values.goal || "-"}`,
    `Readiness note: ${getReadinessNote(values)}`,
  ].join("\n");
}

function setScopedText(container, selector, value) {
  const target = container?.querySelector(selector);
  if (target) target.textContent = value;
}

function renderAuditResult(auditForm) {
  if (!auditForm?.reportValidity()) return;
  const values = getAuditData(auditForm);
  if (!values) return;
  const container = auditForm.closest(".audit-preview-layout") || document;
  const auditResult = container.querySelector(".audit-result-card");

  setScopedText(container, "#result-area, [data-result-field='area']", values.area);
  setScopedText(container, "#result-friction, [data-result-field='friction']", frictionLabels[values.friction] || "Workflow friction");
  setScopedText(container, "#result-readiness, [data-result-field='readiness']", getReadinessNote(values));

  const note = values.workflow
    ? `Your first useful read is probably ${values.area.toLowerCase()}: "${values.workflow}". The paid audit would turn this into Step Cards, cleanup priorities, ROI + cost of inaction, success criteria, and an agency-ready brief.`
    : `Your first useful read is probably ${values.area.toLowerCase()}. The paid audit would turn this into Step Cards, cleanup priorities, ROI + cost of inaction, success criteria, and an agency-ready brief.`;

  setScopedText(container, "#result-note, [data-result-field='note']", note);
  auditResult?.querySelector(".result-breakdown")?.removeAttribute("hidden");
  auditResult?.classList.add("has-result");
}

document.querySelectorAll("#show-audit-result, [data-audit-action='show-result']").forEach((auditButton) => {
  auditButton.addEventListener("click", () => {
    const auditForm = auditButton.closest("form") || auditButton.closest(".audit-preview-layout")?.querySelector(".audit-preview-form");
    renderAuditResult(auditForm);
  });
});

document.querySelectorAll("#send-audit-preview, [data-audit-action='send-preview']").forEach((sendAuditPreview) => {
  sendAuditPreview.addEventListener("click", () => {
    const auditForm = sendAuditPreview.closest(".audit-preview-layout")?.querySelector(".audit-preview-form") || document.querySelector("#free-audit-form");
    const values = getAuditData(auditForm);
    if (!values) return;
    const body = [
      "Hi Annabel,",
      "",
      "I filled out the free AI audit preview and would love your read on where to start.",
      "",
      buildAuditSummary(values),
    ].join("\n");

    window.location.href = `mailto:?subject=${encodeURIComponent(
      "Free AI audit preview"
    )}&body=${encodeURIComponent(body)}`;
  });
});
