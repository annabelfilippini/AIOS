#!/usr/bin/env node
// compound-audit.mjs — measures how much the AI-OS is actually compounding.
// Inventories reusable assets (skills, templates), counts how often each is
// reused across memory + checkpoints, flags write-once / cold assets, and
// tracks activity growth over time. Run it whenever you want to check that the
// system is growing as you grow.
//
//   node operations/memory/scripts/compound-audit.mjs            # scorecard
//   node operations/memory/scripts/compound-audit.mjs --json     # machine output
//   node operations/memory/scripts/compound-audit.mjs --coldDays 30
//   node operations/memory/scripts/compound-audit.mjs --full     # list every skill

import fs from "node:fs";
import path from "node:path";
import os from "node:os";
import { fileURLToPath } from "node:url";

const scriptPath = fileURLToPath(import.meta.url);
const memoryRoot = path.resolve(path.dirname(scriptPath), "..");
const root = path.resolve(memoryRoot, "../..");

const args = parseArgs(process.argv.slice(2));
const coldDays = Number(args.coldDays || 21);
const json = Boolean(args.json);
const full = Boolean(args.full);

const SKIP_DIRS = new Set([
  "node_modules", ".git", "_archive", "dist", "build", ".next", "vendor",
]);

const today = new Date();
const todayKey = today.toISOString().slice(0, 10);

// --- collect assets -------------------------------------------------------

const skillFiles = walk(root, (p) => path.basename(p) === "SKILL.md");
const templateFiles = walk(root, (p) =>
  p.includes(`${path.sep}templates${path.sep}`) && p.endsWith(".md"),
);

// memory + checkpoint corpus we measure reuse against
const memoryFiles = walk(memoryRoot, (p) => p.endsWith(".md"));
const corpus = memoryFiles.map((file) => ({
  file,
  base: path.basename(file),
  dateKey: dateFromName(file),
  text: safeRead(file).toLowerCase(),
}));

// unique skills keyed by folder name (collapses agent-scoped dupes / symlinks)
const skillMap = new Map();
for (const f of skillFiles) {
  const name = path.basename(path.dirname(f));
  if (!skillMap.has(name)) skillMap.set(name, { name, copies: [] });
  skillMap.get(name).copies.push(rel(f));
}

// --- measure reuse --------------------------------------------------------

const skills = [...skillMap.values()].map((s) => {
  const needle = s.name.toLowerCase();
  const hits = corpus.filter((c) => c.text.includes(needle));
  const dates = hits.map((h) => h.dateKey).filter(Boolean).sort();
  const lastUsed = dates.length ? dates[dates.length - 1] : null;
  return {
    name: s.name,
    copies: s.copies.length,
    refs: hits.length,
    firstUsed: dates[0] || null,
    lastUsed,
    coldDays: lastUsed ? daysBetween(lastUsed, todayKey) : null,
  };
}).sort((a, b) => b.refs - a.refs || a.name.localeCompare(b.name));

const dead = skills.filter((s) => s.refs === 0);
const cold = skills.filter(
  (s) => s.refs > 0 && s.coldDays !== null && s.coldDays > coldDays,
);
const workhorses = skills.filter((s) => s.refs >= 3);

// --- activity timeline ----------------------------------------------------

const byMonth = {};
for (const c of corpus) {
  if (!c.dateKey) continue;
  const m = c.dateKey.slice(0, 7);
  byMonth[m] = (byMonth[m] || 0) + 1;
}
const months = Object.entries(byMonth).sort((a, b) => a[0].localeCompare(b[0]));

// --- design-layer drift ---------------------------------------------------

const designFiles = walk(root, (p) =>
  /(^|\/)design(-system)?\.md$/i.test(p) || /(^|\/)DESIGN\.md$/.test(p),
).map(rel);
const globalDesign = path.join(os.homedir(), ".claude", "design.md");
const globalDesignLines = fs.existsSync(globalDesign)
  ? safeRead(globalDesign).split("\n").length
  : null;

// --- output ---------------------------------------------------------------

const result = {
  generatedAt: today.toISOString(),
  totals: {
    skillsUnique: skills.length,
    skillFilesIncludingCopies: skillFiles.length,
    templates: templateFiles.length,
    memoryAndCheckpoints: corpus.length,
  },
  reuse: {
    workhorses: workhorses.length,
    reusedAtLeastOnce: skills.filter((s) => s.refs >= 1).length,
    dead: dead.map((s) => s.name),
    cold: cold.map((s) => ({ name: s.name, lastUsed: s.lastUsed, coldDays: s.coldDays })),
  },
  activityByMonth: months,
  design: {
    fileCount: designFiles.length,
    globalTrunkLines: globalDesignLines,
    files: designFiles,
  },
  skills,
};

if (json) {
  console.log(JSON.stringify(result, null, 2));
} else {
  render(result);
}

function render(r) {
  const t = r.totals;
  const reusePct = pct(r.reuse.workhorses, t.skillsUnique);
  out("");
  out("# AI-OS compound audit");
  out(`_${r.generatedAt.slice(0, 16).replace("T", " ")} · cold threshold ${coldDays}d_`);
  out("");
  out("## Scorecard");
  out(`- reusable assets:        ${t.skillsUnique} skills (${t.skillFilesIncludingCopies} incl. copies) + ${t.templates} templates`);
  out(`- memory + checkpoints:   ${t.memoryAndCheckpoints}`);
  out(`- workhorse skills (3+):  ${r.reuse.workhorses} / ${t.skillsUnique}  (${reusePct}%)`);
  out(`- reused at least once:   ${r.reuse.reusedAtLeastOnce} / ${t.skillsUnique}`);
  out(`- never reused:           ${r.reuse.dead.length}`);
  out(`- gone cold (>${coldDays}d):     ${r.reuse.cold.length}`);
  out("");

  out("## Activity per month (memory + checkpoint files)");
  const max = Math.max(1, ...r.activityByMonth.map((m) => m[1]));
  for (const [m, n] of r.activityByMonth) {
    out(`  ${m}  ${bar(n, max)} ${n}`);
  }
  out("");

  if (r.reuse.dead.length) {
    out("## Never reused since built  (write-once — fix or delete)");
    for (const name of r.reuse.dead) out(`  - ${name}`);
    out("");
  }
  if (r.reuse.cold.length) {
    out(`## Gone cold  (built, used, then quiet >${coldDays}d)`);
    for (const c of r.reuse.cold) out(`  - ${name(c.name)} last used ${c.lastUsed} (${c.coldDays}d ago)`);
    out("");
  }

  out("## Top reused skills");
  for (const s of r.skills.slice(0, full ? r.skills.length : 8)) {
    out(`  ${String(s.refs).padStart(3)}x  ${name(s.name)}${s.lastUsed ? `  (last ${s.lastUsed})` : ""}`);
  }
  if (!full && r.skills.length > 8) out(`  ... +${r.skills.length - 8} more (use --full)`);
  out("");

  out("## Design layer");
  out(`- design files on disk:   ${r.design.fileCount}  (more files = more drift)`);
  out(`- global trunk:           ${r.design.globalTrunkLines ? r.design.globalTrunkLines + " lines" : "missing"}  (~/.claude/design.md)`);
  out("");
}

// --- helpers --------------------------------------------------------------

function walk(dir, match, acc = []) {
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); }
  catch { return acc; }
  for (const e of entries) {
    if (e.name.startsWith(".") && e.name !== ".claude" && e.name !== ".agents") {
      if (e.isDirectory() && SKIP_DIRS.has(e.name)) continue;
    }
    const p = path.join(dir, e.name);
    if (e.isDirectory()) {
      if (SKIP_DIRS.has(e.name)) continue;
      walk(p, match, acc);
    } else if (match(p)) {
      acc.push(p);
    }
  }
  return acc;
}

function dateFromName(file) {
  const m = path.basename(file).match(/(20\d{2}-\d{2}-\d{2})/);
  return m ? m[1] : null;
}
function daysBetween(a, b) {
  return Math.round((Date.parse(b) - Date.parse(a)) / 86400000);
}
function safeRead(f) { try { return fs.readFileSync(f, "utf8"); } catch { return ""; } }
function rel(p) { return path.relative(root, p); }
function name(s) { return s; }
function pct(a, b) { return b ? Math.round((a / b) * 100) : 0; }
function bar(n, max) { return "█".repeat(Math.max(1, Math.round((n / max) * 24))); }
function out(s) { process.stdout.write(s + "\n"); }

function parseArgs(argv) {
  const a = {};
  for (let i = 0; i < argv.length; i++) {
    const k = argv[i];
    if (k.startsWith("--")) {
      const key = k.slice(2);
      const next = argv[i + 1];
      if (next && !next.startsWith("--")) { a[key] = next; i++; }
      else a[key] = true;
    }
  }
  return a;
}
