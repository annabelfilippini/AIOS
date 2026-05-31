#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptPath = fileURLToPath(import.meta.url);
const memoryRoot = path.resolve(path.dirname(scriptPath), "..");
const root = path.resolve(memoryRoot, "../..");

const args = parseArgs(process.argv.slice(2));
const cwd = path.resolve(args.cwd || process.cwd());
const query = String(args.query || args.q || "").trim();
const limit = Number(args.limit || 5);
const includeArchive = Boolean(args.includeArchive);
const json = Boolean(args.json);
const weakTokens = new Set(["active", "current", "memory", "next", "recent", "startup", "system"]);
const stopTokens = new Set(["the", "and", "for", "with", "from", "that", "this", "into", "about", "session", "project"]);

const detectedProject = args.project || detectProject(cwd);
const entries = collectEntries({ includeArchive });
const queryTokens = tokenize(query);
const ranked = entries
  .map((entry) => scoreEntry(entry, { query, detectedProject }))
  .filter((entry) => shouldKeepEntry(entry, { queryTokens, detectedProject }))
  .sort((a, b) => b.score - a.score || String(b.dateKey).localeCompare(String(a.dateKey)))
  .slice(0, limit);

const result = {
  generatedAt: new Date().toISOString(),
  cwd,
  query,
  detectedProject,
  includeArchive,
  entries: ranked.map(publicEntry),
};

if (json) {
  console.log(JSON.stringify(result, null, 2));
} else {
  renderMarkdown(result);
}

function parseArgs(rawArgs) {
  const out = {};
  for (let i = 0; i < rawArgs.length; i += 1) {
    const arg = rawArgs[i];
    if (!arg.startsWith("--")) continue;
    const key = arg.slice(2);
    if (["json", "includeArchive"].includes(key)) {
      out[key] = true;
      continue;
    }
    out[key] = rawArgs[i + 1] || "";
    i += 1;
  }
  return out;
}

function detectProject(currentDir) {
  const rel = path.relative(root, currentDir);
  const parts = rel.split(path.sep).filter(Boolean);
  const projectsIndex = parts.indexOf("projects");
  if (projectsIndex !== -1 && parts[projectsIndex + 1]) return parts[projectsIndex + 1];
  if (parts[0] === "operations" && parts[1]) return `operations/${parts[1]}`;
  if (parts[0] === "agents" && parts[1]) return `agents/${parts[1]}`;
  return "";
}

function collectEntries({ includeArchive: includeOld }) {
  const dirs = [
    { type: "checkpoint", dir: path.join(memoryRoot, "checkpoints") },
    { type: "refinement", dir: path.join(memoryRoot, "refinement-candidates") },
  ];
  if (includeOld) dirs.push({ type: "archive", dir: path.join(memoryRoot, "archive") });

  return dirs.flatMap(({ type, dir }) =>
    listMarkdown(dir).map((filePath) => {
      const text = fs.readFileSync(filePath, "utf8");
      const { frontmatter, body } = parseFrontmatter(text);
      return {
        type,
        path: filePath,
        relativePath: path.relative(root, filePath),
        filename: path.basename(filePath),
        frontmatter,
        inferredProject: inferProject(body),
        body,
        title: firstHeading(body) || titleFromFilename(filePath),
        dateKey: frontmatter.date || dateFromFilename(filePath) || "",
      };
    }),
  );
}

function listMarkdown(dir) {
  if (!fs.existsSync(dir)) return [];
  return fs
    .readdirSync(dir, { withFileTypes: true })
    .flatMap((entry) => {
      const filePath = path.join(dir, entry.name);
      if (entry.isDirectory()) return listMarkdown(filePath);
      if (entry.isFile() && entry.name.endsWith(".md")) return [filePath];
      return [];
    })
    .sort((a, b) => a.localeCompare(b));
}

function parseFrontmatter(text) {
  if (!text.startsWith("---\n")) return { frontmatter: {}, body: text.trim() };
  const end = text.indexOf("\n---", 4);
  if (end === -1) return { frontmatter: {}, body: text.trim() };
  return {
    frontmatter: parseSimpleYaml(text.slice(4, end).trim()),
    body: text.slice(end + 4).trim(),
  };
}

function parseSimpleYaml(raw) {
  const out = {};
  for (const line of raw.split(/\r?\n/)) {
    const splitAt = line.indexOf(":");
    if (splitAt === -1) continue;
    const key = line.slice(0, splitAt).trim();
    const value = line.slice(splitAt + 1).trim();
    out[key] = value.replace(/^["']|["']$/g, "");
  }
  return out;
}

function scoreEntry(entry, { query: rawQuery, detectedProject: project }) {
  const entryProject = entry.frontmatter.project || entry.inferredProject;
  const haystackText = [
    entry.filename,
    entry.title,
    entryProject,
    entry.frontmatter.status,
    entry.frontmatter["next-session"],
    entry.body,
  ]
    .filter(Boolean)
    .join(" ");

  const queryTokens = tokenize(rawQuery);
  const projectTokens = tokenize(project);
  const haystackTokens = new Set(tokenize(haystackText));
  const matchedQueryTokens = queryTokens.filter((token) => haystackTokens.has(token));
  const matchedProjectTokens = projectTokens.filter((token) => haystackTokens.has(token));
  const compactQuery = queryTokens.join(" ");
  const compactIdentity = normalizeForPhrase(`${entry.filename} ${entry.title} ${entryProject || ""}`);
  const projectMatch = Boolean(project && (entryProject === project || entry.relativePath.includes(project)));
  const relevanceMatched = Boolean(matchedQueryTokens.length || matchedProjectTokens.length || projectMatch);
  const strongQueryTokens = queryTokens.filter((token) => !weakTokens.has(token));
  const matchedStrongQueryTokens = matchedQueryTokens.filter((token) => !weakTokens.has(token));

  let score = 0;
  if (entry.frontmatter.status === "in-progress") score += 35;
  if (entry.frontmatter.status === "paused") score += 30;
  if (entry.frontmatter["next-session"]) score += 8;
  if (project && entryProject === project) score += 55;
  if (project && entry.relativePath.includes(project)) score += 20;
  score += matchedProjectTokens.length * 12;
  score += matchedQueryTokens.reduce((sum, token) => sum + tokenWeight(token), 0);
  if (queryTokens.length >= 2 && matchedQueryTokens.length) {
    score += Math.round((matchedQueryTokens.length / queryTokens.length) * 30);
  }
  if (strongQueryTokens.length >= 2 && matchedStrongQueryTokens.length) {
    score += Math.round((matchedStrongQueryTokens.length / strongQueryTokens.length) * 25);
  }
  if (compactQuery && compactIdentity.includes(compactQuery)) score += 35;
  score += recencyScore(entry.dateKey);
  if (entry.type === "refinement") score -= 5;
  if (entry.type === "archive") score -= 20;
  if (queryTokens.length && !relevanceMatched) score -= 50;
  if (queryTokens.length >= 2 && matchedQueryTokens.length === 1 && !projectMatch) score -= 35;
  if (strongQueryTokens.length && !matchedStrongQueryTokens.length && !projectMatch) score -= 45;
  if (queryTokens.length >= 3 && matchedQueryTokens.length < 2 && !projectMatch) score -= 35;

  return {
    ...entry,
    entryProject,
    score,
    projectMatch,
    matchedTokens: [...new Set([...matchedQueryTokens, ...matchedProjectTokens])],
    startHint: startHintFor(entry),
    sections: {
      decisions: sectionBullets(entry.body, "Decisions made", 3),
      openQuestions: sectionBullets(entry.body, "Open questions", 3),
      nextSteps: sectionBullets(entry.body, "Next steps", 4),
      context: sectionBullets(entry.body, "Context to preserve", 3),
    },
  };
}

function shouldKeepEntry(entry, { queryTokens, detectedProject }) {
  if (!queryTokens.length) {
    return entry.score > 0 || entry.projectMatch || isContinuable(entry);
  }

  if (isProjectOnlyQuery(queryTokens, detectedProject) && !entry.projectMatch) return false;

  const matchedQueryTokens = entry.matchedTokens.filter((token) => queryTokens.includes(token));
  const matchedStrongQueryTokens = matchedQueryTokens.filter((token) => !weakTokens.has(token));
  const strongQueryTokens = queryTokens.filter((token) => !weakTokens.has(token));

  if (entry.projectMatch && entry.score > 0) return true;
  if (strongQueryTokens.length && !matchedStrongQueryTokens.length) return false;
  if (queryTokens.length >= 3 && matchedQueryTokens.length < 2) return false;
  return entry.score > 0;
}

function isProjectOnlyQuery(queryTokens, detectedProject) {
  const projectTokens = tokenize(detectedProject);
  if (!projectTokens.length) return false;
  return queryTokens.length > 0 && queryTokens.every((token) => projectTokens.includes(token));
}

function isContinuable(entry) {
  return ["in-progress", "paused"].includes(entry.frontmatter.status);
}

function tokenWeight(token) {
  return weakTokens.has(token) ? 4 : 14;
}

function tokenize(text) {
  return String(text || "")
    .toLowerCase()
    .split(/[^a-z0-9]+/)
    .filter((token) => token.length > 2 && !stopTokens.has(token));
}

function normalizeForPhrase(text) {
  return tokenize(text).join(" ");
}

function recencyScore(dateKey) {
  const date = new Date(dateKey);
  if (Number.isNaN(date.getTime())) return 0;
  const ageDays = (Date.now() - date.getTime()) / 86400000;
  if (ageDays < 2) return 25;
  if (ageDays < 7) return 18;
  if (ageDays < 21) return 10;
  if (ageDays < 60) return 5;
  return 0;
}

function sectionBullets(body, heading, maxItems) {
  const pattern = new RegExp(`^##\\s+${escapeRegExp(heading)}\\s*$`, "im");
  const match = body.match(pattern);
  if (!match) return [];
  const start = match.index + match[0].length;
  const rest = body.slice(start);
  const nextHeading = rest.search(/^##\s+/m);
  const section = (nextHeading === -1 ? rest : rest.slice(0, nextHeading)).trim();
  const bullets = [];
  let current = "";
  for (const rawLine of section.split(/\r?\n/)) {
    const line = rawLine.trim();
    if (!line) continue;
    if (/^[-*]\s+|\d+\.\s+/.test(line)) {
      if (current) bullets.push(current);
      current = line.replace(/^[-*]\s*/, "").replace(/^\d+\.\s*/, "").trim();
      continue;
    }
    if (current && !/^#{1,6}\s+/.test(line)) current = `${current} ${line}`;
  }
  if (current) bullets.push(current);
  return bullets.slice(0, maxItems);
}

function firstHeading(body) {
  return body.match(/^#\s+(.+)$/m)?.[1]?.trim() || "";
}

function titleFromFilename(filePath) {
  return path
    .basename(filePath, ".md")
    .replace(/^\d{4}-\d{2}-\d{2}-\d{4,6}-?/, "")
    .replace(/-/g, " ");
}

function dateFromFilename(filePath) {
  return path.basename(filePath).match(/^(\d{4}-\d{2}-\d{2})/)?.[1] || "";
}

function publicEntry(entry) {
  return {
    score: entry.score,
    type: entry.type,
    path: entry.relativePath,
    title: entry.title,
    project: entry.entryProject || "",
    status: entry.frontmatter.status || "",
    date: entry.frontmatter.date || dateFromFilename(entry.path),
    nextSession: entry.frontmatter["next-session"] || "",
    startHint: entry.startHint,
    matchedTokens: entry.matchedTokens,
    sections: entry.sections,
  };
}

function renderMarkdown(data) {
  console.log("# Memory Recall");
  console.log("");
  console.log(`- CWD: \`${path.relative(root, data.cwd) || "."}\``);
  if (data.detectedProject) console.log(`- Detected project: \`${data.detectedProject}\``);
  if (data.query) console.log(`- Query: ${data.query}`);
  console.log(`- Scope: checkpoints + refinement candidates${data.includeArchive ? " + archive" : ""}`);
  console.log("");

  if (!data.entries.length) {
    console.log("No relevant memory surfaced. Read project docs next, then search manually if needed.");
    return;
  }

  const topEntry = data.entries[0];
  if (topEntry.startHint) {
    console.log("## Where To Start");
    console.log(`- ${topEntry.startHint}`);
    console.log(`- Source: \`${topEntry.path}\``);
    console.log("");
  }

  console.log("## Top Matches");
  for (const entry of data.entries) {
    console.log("");
    console.log(`### ${entry.title}`);
    console.log(`- Score: ${entry.score}`);
    console.log(`- Source: \`${entry.path}\``);
    console.log(`- Type/status/project: ${entry.type} / ${entry.status || "n/a"} / ${entry.project || "n/a"}`);
    if (entry.date) console.log(`- Date: ${entry.date}`);
    if (entry.matchedTokens.length) console.log(`- Matched: ${entry.matchedTokens.join(", ")}`);
    if (entry.nextSession) console.log(`- Next: ${entry.nextSession}`);
    if (!entry.nextSession && entry.startHint) console.log(`- Start hint: ${entry.startHint}`);
    printSection("Decisions", entry.sections.decisions);
    printSection("Open Questions", entry.sections.openQuestions);
    printSection("Next Steps", entry.sections.nextSteps);
  }

  console.log("");
  console.log("Read only the source files above if the brief is not enough. Search archive/raw stores only on demand.");
}

function startHintFor(entry) {
  if (entry.frontmatter["next-session"]) return entry.frontmatter["next-session"];

  const nextSteps = sectionBullets(entry.body, "Next steps", 1);
  if (nextSteps.length) return nextSteps[0];

  const recommended = recommendedNextMove(entry.body);
  if (recommended) return recommended;

  const startSections = ["Recommended Next Move", "Next Session Start", "Start Here"];
  for (const heading of startSections) {
    const section = sectionText(entry.body, heading);
    const hint = firstUsefulLine(section);
    if (hint) return hint;
  }

  return "";
}

function recommendedNextMove(body) {
  const lines = String(body || "").split(/\r?\n/);
  const labelIndex = lines.findIndex((line) => /Recommended next implementation move(?: remains)?:/i.test(line));
  if (labelIndex === -1) return "";

  const collected = [];
  for (const rawLine of lines.slice(labelIndex + 1)) {
    const line = rawLine.replace(/^[-*\d.\s>`]+/, "").trim();
    if (!line) {
      if (collected.length) break;
      continue;
    }
    if (/^#{1,6}\s+/.test(line)) break;
    collected.push(line);
    if (collected.join(" ").length > 180) break;
  }

  return collected.join(" ").trim();
}

function inferProject(body) {
  const frontmatterStyle = body.match(/^project:\s*([^\n]+)/im)?.[1];
  if (frontmatterStyle) return cleanProjectName(frontmatterStyle);

  const boldLabelStyle = body.match(/^\*\*Project:\*\*\s*`?([^`\n]+)`?/im)?.[1];
  if (boldLabelStyle) return cleanProjectName(boldLabelStyle);

  const projectPath = body.match(/\/projects\/([^/\s`)]+)/i)?.[1];
  if (projectPath) return cleanProjectName(projectPath);

  return "";
}

function cleanProjectName(value) {
  return String(value || "")
    .trim()
    .replace(/^["']|["']$/g, "")
    .replace(/^.*\/projects\//, "")
    .split(/[\/\s`]/)[0]
    .trim();
}

function sectionText(body, heading) {
  const pattern = new RegExp(`^##\\s+${escapeRegExp(heading)}\\s*$`, "im");
  const match = body.match(pattern);
  if (!match) return "";
  const start = match.index + match[0].length;
  const rest = body.slice(start);
  const nextHeading = rest.search(/^##\s+/m);
  return (nextHeading === -1 ? rest : rest.slice(0, nextHeading)).trim();
}

function firstUsefulLine(text) {
  for (const rawLine of String(text || "").split(/\r?\n/)) {
    const line = rawLine.replace(/^[-*\d.\s>`]+/, "").trim();
    if (!line || line.startsWith("```")) continue;
    return line;
  }
  return "";
}

function printSection(title, items) {
  if (!items?.length) return;
  console.log(`- ${title}:`);
  for (const item of items) console.log(`  - ${item}`);
}

function escapeRegExp(value) {
  return String(value).replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}
