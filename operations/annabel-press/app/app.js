const data = window.ANNABEL_PRESS_DATA || {
  skills: [],
  cliConnections: [],
  profiles: [],
};

const state = {
  mode: "skills",
  query: "",
  profile: "all",
  selectedId: null,
};

const els = {
  skillCount: document.querySelector("#skillCount"),
  cliCount: document.querySelector("#cliCount"),
  profileCount: document.querySelector("#profileCount"),
  tabs: document.querySelectorAll(".tab"),
  search: document.querySelector("#searchInput"),
  profileFilter: document.querySelector("#profileFilter"),
  listTitle: document.querySelector("#listTitle"),
  resultCount: document.querySelector("#resultCount"),
  list: document.querySelector("#capabilityList"),
  detail: document.querySelector("#detailPanel"),
};

function init() {
  els.skillCount.textContent = data.skills.length;
  els.cliCount.textContent = data.cliConnections.length;
  els.profileCount.textContent = data.profiles.length;

  for (const profile of data.profiles) {
    const option = document.createElement("option");
    option.value = profile.agent;
    option.textContent = profile.agent;
    els.profileFilter.append(option);
  }

  els.tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      state.mode = tab.dataset.mode;
      state.selectedId = null;
      render();
    });
  });

  els.search.addEventListener("input", (event) => {
    state.query = event.target.value.trim().toLowerCase();
    render();
  });

  els.profileFilter.addEventListener("change", (event) => {
    state.profile = event.target.value;
    state.selectedId = null;
    render();
  });

  render();
}

function render() {
  els.tabs.forEach((tab) => tab.classList.toggle("active", tab.dataset.mode === state.mode));
  els.listTitle.textContent = modeTitle();

  const items = filteredItems();
  if (!state.selectedId && items.length) state.selectedId = keyFor(items[0]);
  if (state.selectedId && !items.some((item) => keyFor(item) === state.selectedId)) {
    state.selectedId = items[0] ? keyFor(items[0]) : null;
  }

  els.resultCount.textContent = items.length;
  renderList(items);
  renderDetail(items.find((item) => keyFor(item) === state.selectedId));
}

function filteredItems() {
  const source = state.mode === "skills" ? data.skills : data.cliConnections;
  const profile = data.profiles.find((item) => item.agent === state.profile);

  return source
    .filter((item) => {
      if (!profile || state.profile === "all") return true;
      const ids = capabilityIdsForProfile(profile, state.mode);
      return ids.includes(item.id) || ids.includes(item.name);
    })
    .filter((item) => {
      if (!state.query) return true;
      const haystack = [
        item.id,
        item.name,
        item.displayName,
        item.description,
        item.summary,
        item.binary,
        item.path,
        ...(item.relatedSkills || []),
        ...(item.relatedCliConnections || []),
      ]
        .filter(Boolean)
        .join(" ")
        .toLowerCase();
      return haystack.includes(state.query);
    });
}

function renderList(items) {
  els.list.innerHTML = "";
  if (!items.length) {
    els.list.innerHTML = `<div class="empty-state"><p>No matching capabilities.</p></div>`;
    return;
  }

  for (const item of items) {
    const button = document.createElement("button");
    button.type = "button";
    button.className = `capability-card ${item.id === state.selectedId ? "active" : ""}`;
    button.innerHTML = `
      <div class="mini-row">
        <span class="pill">${state.mode === "skills" ? "Skill" : "CLI"}</span>
        ${profilePillsFor(item)}
      </div>
      <strong>${escapeHtml(titleFor(item))}</strong>
      <p>${escapeHtml(item.description || item.summary || item.path)}</p>
      <div class="mini-row">
        ${usagePill(item)}
        ${state.mode === "cli" ? statusPill(item.installed, "Installed", "Missing") : runtimePills(item)}
      </div>
    `;
    button.addEventListener("click", () => {
      state.selectedId = item.id;
      render();
    });
    els.list.append(button);
  }
}

function renderDetail(item) {
  if (!item) {
    els.detail.innerHTML = `
      <div class="empty-state">
        <h2>Select a capability</h2>
        <p>Choose a skill or CLI connection to inspect its source, profile access, references, scripts, and safety model.</p>
      </div>
    `;
    return;
  }

  els.detail.innerHTML = state.mode === "skills" ? skillDetail(item) : cliDetail(item);
}

function modeTitle() {
  if (state.mode === "skills") return "Skills";
  return "CLI Connections";
}

function skillDetail(item) {
  return `
    <div class="detail-inner">
      ${header(item, "Skill")}
      <div class="detail-grid">
        <section class="section">
          <h3>Profile Access</h3>
          <div class="mini-row">${profilePillsFor(item) || `<span class="pill warn">No profile</span>`}</div>
        </section>
        <section class="section">
          <h3>Runtime Links</h3>
          <div class="mini-row">${runtimePills(item)}</div>
        </section>
        ${usageSection(item)}
        <section class="section full">
          <h3>Source</h3>
          <p class="path">${escapeHtml(item.entrypoint)}</p>
          <p class="path">${escapeHtml(item.realPath)}</p>
        </section>
        ${fileSection("References", item.references)}
        ${fileSection("Scripts", item.scripts)}
        ${fileSection("Assets", item.assets)}
        <section class="section">
          <h3>Related CLI Connections</h3>
          <div class="mini-row">${pills(item.relatedCliConnections, "warn") || `<span class="muted">None declared yet.</span>`}</div>
        </section>
      </div>
    </div>
  `;
}

function cliDetail(item) {
  return `
    <div class="detail-inner">
      ${header(item, "CLI Connection")}
      <div class="detail-grid">
        <section class="section">
          <h3>Install State</h3>
          <div class="mini-row">${statusPill(item.installed, "Binary found", "Binary missing")}</div>
          <p class="path">${escapeHtml(item.binary || "No binary declared")}</p>
        </section>
        <section class="section">
          <h3>Profile Access</h3>
          <div class="mini-row">${profilePillsFor(item) || `<span class="pill warn">No profile</span>`}</div>
        </section>
        ${usageSection(item)}
        <section class="section full">
          <h3>Source</h3>
          <p class="path">${escapeHtml(item.entrypoint)}</p>
        </section>
        <section class="section">
          <h3>Safe Commands</h3>
          ${commandList(item.safeCommands)}
        </section>
        <section class="section">
          <h3>Approval Required</h3>
          ${commandList(item.approvalRequired)}
        </section>
        ${fileSection("References", item.references)}
        ${fileSection("Scripts", item.scripts)}
        <section class="section">
          <h3>Related Skills</h3>
          <div class="mini-row">${pills(item.relatedSkills, "warn") || `<span class="muted">None declared yet.</span>`}</div>
        </section>
      </div>
    </div>
  `;
}

function header(item, type) {
  return `
    <div class="detail-header">
      <div>
        <div class="mini-row"><span class="pill">${escapeHtml(type)}</span><span class="pill">${escapeHtml(item.visibility || "unspecified")}</span></div>
        <h2>${escapeHtml(titleFor(item))}</h2>
        <p>${escapeHtml(item.description || item.summary || "No description yet.")}</p>
      </div>
    </div>
  `;
}

function fileSection(title, files) {
  return `
    <section class="section">
      <h3>${escapeHtml(title)}</h3>
      ${
        files?.length
          ? `<ul class="file-list">${files.map((file) => `<li><code>${escapeHtml(file)}</code></li>`).join("")}</ul>`
          : `<span class="muted">None</span>`
      }
    </section>
  `;
}

function commandList(commands) {
  if (!commands?.length) return `<span class="muted">None declared.</span>`;
  return `<ul class="command-list">${commands.map((command) => `<li><code>${escapeHtml(command)}</code></li>`).join("")}</ul>`;
}

function usageSection(item) {
  const usage = item.usage || { count: 0, recent: [] };
  return `
    <section class="section">
      <h3>Usage</h3>
      <dl class="kv">
        <div><dt>Uses logged</dt><dd>${usage.count || 0}</dd></div>
        <div><dt>Last used</dt><dd>${escapeHtml(formatDate(usage.lastUsedAt))}</dd></div>
      </dl>
      ${usage.recent?.length ? recentUsageList(usage.recent) : `<p class="muted compact">No usage logged yet.</p>`}
    </section>
  `;
}

function recentUsageList(events) {
  return `
    <ul class="usage-list">
      ${events
        .map(
          (event) => `
            <li>
              <span>${escapeHtml(formatDate(event.timestamp))}</span>
              <strong>${escapeHtml(event.agent || "unknown")}</strong>
              ${event.note ? `<p>${escapeHtml(event.note)}</p>` : ""}
            </li>
          `,
        )
        .join("")}
    </ul>
  `;
}

function titleFor(item) {
  return item.displayName || item.name || item.id;
}

function keyFor(item) {
  return item.id;
}

function profilesFor(item) {
  return data.profiles.filter((profile) => {
    const ids = capabilityIdsForProfile(profile, state.mode);
    return ids.includes(item.id) || ids.includes(item.name);
  });
}

function profilePillsFor(item) {
  return profilesFor(item)
    .map((profile) => {
      const label = profile.role === "global-orchestrator" ? `${profile.agent}: routes` : profile.agent;
      return `<span class="pill">${escapeHtml(label)}</span>`;
    })
    .join("");
}

function capabilityIdsForProfile(profile, mode) {
  const direct = mode === "skills" ? profile.skills || [] : profile.cliConnections || [];
  const delegated = (profile.delegates || []).flatMap((delegateName) => {
    const delegate = data.profiles.find((item) => item.agent === delegateName);
    if (!delegate) return [];
    return mode === "skills" ? delegate.skills || [] : delegate.cliConnections || [];
  });
  return [...new Set([...direct, ...delegated])];
}

function runtimePills(item) {
  if (!item.runtimeStatus?.length) return `<span class="pill warn">Runtime unknown</span>`;
  return item.runtimeStatus
    .map((runtime) => {
      const kind = runtime.pointsToCanonical ? "ok" : runtime.installed ? "warn" : "bad";
      const label = runtime.pointsToCanonical
        ? `${runtime.name}: canonical`
        : runtime.installed
          ? `${runtime.name}: installed`
          : `${runtime.name}: missing`;
      return `<span class="pill ${kind}">${escapeHtml(label)}</span>`;
    })
    .join("");
}

function statusPill(condition, yes, no) {
  return `<span class="pill ${condition ? "ok" : "bad"}">${escapeHtml(condition ? yes : no)}</span>`;
}

function usagePill(item) {
  const count = item.usage?.count || 0;
  return `<span class="pill ${count > 0 ? "ok" : "warn"}">Used ${count}</span>`;
}

function formatDate(value) {
  if (!value) return "Never";
  const date = new Date(value);
  if (Number.isNaN(date.getTime())) return value;
  return date.toLocaleDateString(undefined, {
    month: "short",
    day: "numeric",
    year: "numeric",
  });
}

function pills(items, kind = "") {
  return (items || []).map((item) => `<span class="pill ${kind}">${escapeHtml(item)}</span>`).join("");
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#039;");
}

init();
