#!/usr/bin/env node
import { spawnSync } from "node:child_process";
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptPath = fileURLToPath(import.meta.url);
const root = path.resolve(path.dirname(scriptPath), "../../..");
const appDataPath = path.join(root, "operations/annabel-press/app/data/capabilities.js");
const usagePath = path.join(root, "operations/annabel-press/usage/events.jsonl");
const usageEvents = readUsageEvents();

function readText(filePath) {
  return fs.readFileSync(filePath, "utf8");
}

function listDirs(dirPath) {
  if (!fs.existsSync(dirPath)) return [];
  return fs
    .readdirSync(dirPath, { withFileTypes: true })
    .filter((entry) => entry.isDirectory() || entry.isSymbolicLink())
    .map((entry) => path.join(dirPath, entry.name))
    .filter((entryPath) => fs.existsSync(entryPath) && fs.statSync(entryPath).isDirectory())
    .sort((a, b) => path.basename(a).localeCompare(path.basename(b)));
}

function listFiles(dirPath) {
  if (!fs.existsSync(dirPath)) return [];
  return fs
    .readdirSync(dirPath, { withFileTypes: true })
    .filter((entry) => entry.isFile())
    .map((entry) => entry.name)
    .sort((a, b) => a.localeCompare(b));
}

function parseFrontmatterAndBody(text) {
  if (!text.startsWith("---\n")) return { frontmatter: {}, body: text.trim() };

  const end = text.indexOf("\n---", 4);
  if (end === -1) return { frontmatter: {}, body: text.trim() };

  const raw = text.slice(4, end).trim();
  const body = text.slice(end + 4).trim();
  return { frontmatter: parseSimpleYaml(raw), body };
}

function parseSimpleYaml(raw) {
  const result = {};
  const lines = raw.split(/\r?\n/);
  let currentKey = null;

  for (const line of lines) {
    if (!line.trim() || line.trim().startsWith("#")) continue;

    const listMatch = line.match(/^\s*-\s+(.*)$/);
    if (listMatch && currentKey) {
      if (!Array.isArray(result[currentKey])) result[currentKey] = [];
      result[currentKey].push(cleanValue(listMatch[1]));
      continue;
    }

    const splitAt = line.indexOf(":");
    if (splitAt === -1) continue;

    const key = line.slice(0, splitAt).trim();
    const value = line.slice(splitAt + 1).trim();
    currentKey = key;

    if (!value) {
      result[key] = [];
    } else if (value.startsWith("[") && value.endsWith("]")) {
      result[key] = value
        .slice(1, -1)
        .split(",")
        .map((item) => cleanValue(item))
        .filter(Boolean);
    } else {
      result[key] = cleanValue(value);
    }
  }

  return result;
}

function cleanValue(value) {
  return value.trim().replace(/^["']|["']$/g, "");
}

function firstParagraph(body) {
  return body
    .split(/\n\s*\n/)
    .map((chunk) => chunk.replace(/^#.*\n?/, "").trim())
    .find((chunk) => chunk && !chunk.startsWith("```")) || "";
}

function relativeFromRoot(filePath) {
  return path.relative(root, filePath);
}

function runtimeStatus(skillDir) {
  const runtimes = [
    { name: "Claude", dir: path.join(process.env.HOME || "", ".claude/skills") },
    { name: "Codex", dir: path.join(process.env.HOME || "", ".codex/skills") },
  ];
  const realSkillDir = safeRealpath(skillDir);

  return runtimes.map((runtime) => {
    const runtimePath = path.join(runtime.dir, path.basename(skillDir));
    const installed = fs.existsSync(runtimePath);
    const realRuntimePath = safeRealpath(runtimePath);
    return {
      name: runtime.name,
      installed,
      path: runtimePath,
      pointsToCanonical: Boolean(installed && realRuntimePath && realRuntimePath === realSkillDir),
    };
  });
}

function safeRealpath(filePath) {
  try {
    return fs.realpathSync(filePath);
  } catch {
    return null;
  }
}

function commandAvailable(binary) {
  const executable = String(binary || "").split(/\s+/)[0];
  if (!executable) return false;
  const result = spawnSync("zsh", ["-lc", `command -v ${shellQuote(executable)}`], {
    cwd: root,
    encoding: "utf8",
  });
  return result.status === 0;
}

function shellQuote(value) {
  return `'${String(value).replace(/'/g, "'\\''")}'`;
}

function collectSkills() {
  return listDirs(path.join(root, "skills")).flatMap((dir) => {
    const file = path.join(dir, "SKILL.md");
    if (!fs.existsSync(file)) return [];

    const { frontmatter, body } = parseFrontmatterAndBody(readText(file));
    const id = path.basename(dir);
    const realPath = safeRealpath(dir);

    return {
      id,
      name: frontmatter.name || id,
      description: frontmatter.description || "",
      audience: asArray(frontmatter.audience),
      runtime: asArray(frontmatter.runtime),
      visibility: frontmatter.visibility || "unspecified",
      relatedCliConnections: asArray(frontmatter.related_cli_connections),
      path: relativeFromRoot(dir),
      realPath: realPath ? relativeFromRoot(realPath) : relativeFromRoot(dir),
      entrypoint: relativeFromRoot(file),
      summary: firstParagraph(body),
      references: listFiles(path.join(dir, "references")),
      scripts: listFiles(path.join(dir, "scripts")),
      assets: listFiles(path.join(dir, "assets")),
      runtimeStatus: runtimeStatus(dir),
      usage: usageSummary("skill", id),
    };
  });
}

function collectConnections() {
  return listDirs(path.join(root, "cli-connections")).flatMap((dir) => {
    const file = path.join(dir, "CONNECTION.md");
    if (!fs.existsSync(file)) return [];

    const { frontmatter, body } = parseFrontmatterAndBody(readText(file));
    const id = path.basename(dir);
    const binary = frontmatter.binary || "";

    return {
      id,
      name: frontmatter.name || id,
      displayName: frontmatter.display_name || frontmatter.name || id,
      binary,
      installed: commandAvailable(binary),
      audience: asArray(frontmatter.audience),
      runtime: asArray(frontmatter.runtime),
      visibility: frontmatter.visibility || "unspecified",
      relatedSkills: asArray(frontmatter.related_skills),
      safeCommands: asArray(frontmatter.safe_commands),
      approvalRequired: asArray(frontmatter.approval_required),
      path: relativeFromRoot(dir),
      entrypoint: relativeFromRoot(file),
      summary: firstParagraph(body),
      references: listFiles(path.join(dir, "references")),
      scripts: listFiles(path.join(dir, "scripts")),
      usage: usageSummary("cli", id),
    };
  });
}

function collectProfiles() {
  return listDirs(path.join(root, "agents")).flatMap((agentDir) => {
    const file = path.join(agentDir, "profile.yaml");
    if (!fs.existsSync(file)) return [];
    const profile = parseSimpleYaml(readText(file));
    return {
      agent: profile.agent || path.basename(agentDir),
      role: profile.role || "specialist",
      path: relativeFromRoot(file),
      skills: asArray(profile.skills),
      cliConnections: asArray(profile.cli_connections),
      delegates: asArray(profile.delegates),
    };
  });
}

function asArray(value) {
  if (Array.isArray(value)) return value;
  if (!value) return [];
  return [value];
}

function readUsageEvents() {
  if (!fs.existsSync(usagePath)) return [];
  return fs
    .readFileSync(usagePath, "utf8")
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .flatMap((line) => {
      try {
        return [JSON.parse(line)];
      } catch {
        return [];
      }
    })
    .filter((event) => event && event.type && event.id && event.timestamp);
}

function usageSummary(type, id) {
  const events = usageEvents
    .filter((event) => event.type === type && event.id === id)
    .sort((a, b) => String(b.timestamp).localeCompare(String(a.timestamp)));
  const agents = [...new Set(events.map((event) => event.agent).filter(Boolean))];
  return {
    count: events.length,
    lastUsedAt: events[0]?.timestamp || null,
    agents,
    recent: events.slice(0, 5).map((event) => ({
      timestamp: event.timestamp,
      agent: event.agent || "unknown",
      note: event.note || "",
      source: event.source || "",
    })),
  };
}

const data = {
  generatedAt: new Date().toISOString(),
  root,
  skills: collectSkills(),
  cliConnections: collectConnections(),
  profiles: collectProfiles(),
};

fs.mkdirSync(path.dirname(appDataPath), { recursive: true });
fs.writeFileSync(
  appDataPath,
  `window.ANNABEL_PRESS_DATA = ${JSON.stringify(data, null, 2)};\n`,
);

console.log(`Wrote ${relativeFromRoot(appDataPath)}`);
console.log(`Indexed ${data.skills.length} skills, ${data.cliConnections.length} CLI connections, ${data.profiles.length} profiles.`);
