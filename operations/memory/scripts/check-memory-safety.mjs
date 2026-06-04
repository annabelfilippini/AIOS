#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptPath = fileURLToPath(import.meta.url);
const memoryRoot = path.resolve(path.dirname(scriptPath), "..");

const activeDirs = ["checkpoints", "refinement-candidates"].map((dir) => path.join(memoryRoot, dir));
const secretPatterns = [
  { name: "Tally API token", pattern: /\btly-[A-Za-z0-9_-]{12,}\b/g },
  { name: "Telegram bot token", pattern: /\b\d{8,12}:[A-Za-z0-9_-]{25,}\b/g },
  { name: "OpenAI/Anthropic-style API key", pattern: /\b(?:sk-ant-[A-Za-z0-9_-]{20,}|sk-proj-[A-Za-z0-9_-]{20,}|sk-[A-Za-z0-9_-]{20,})\b/g },
  { name: "GitHub token", pattern: /\b(?:ghp_[A-Za-z0-9_]{20,}|github_pat_[A-Za-z0-9_]{20,})\b/g },
  { name: "Google API key", pattern: /\bAIza[0-9A-Za-z_-]{25,}\b/g },
  { name: "JWT", pattern: /\beyJ[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{20,}\.[A-Za-z0-9_-]{10,}\b/g },
  { name: "auth/cookie assignment", pattern: /\b(?:auth_token|authorization|cookie|set-cookie)\s*[:=]\s*["']?[A-Za-z0-9%._~+/=-]{20,}/gi },
];

const warnings = [];
const failures = [];
const strict = process.env.MEMORY_STRICT === "1";

for (const filePath of activeDirs.flatMap(listMarkdown)) {
  const text = fs.readFileSync(filePath, "utf8");
  const relativePath = path.relative(memoryRoot, filePath);
  const lines = text.replace(/(?:\r?\n)+$/, "").split(/\r?\n/);

  if (!text.startsWith("---\n")) {
    warnings.push(`${relativePath}: missing frontmatter`);
  }

  if (relativePath.startsWith("checkpoints/") && lines.length > 100) {
    warnings.push(`${relativePath}: ${lines.length} lines; checkpoint target is under 100`);
  }

  for (const { name, pattern } of secretPatterns) {
    pattern.lastIndex = 0;
    for (const match of text.matchAll(pattern)) {
      failures.push(`${relativePath}:${lineNumberFor(text, match.index)} likely ${name}`);
    }
  }
}

if (warnings.length) {
  console.log("Memory safety warnings:");
  for (const warning of warnings) console.log(`- ${warning}`);
}

if (strict && warnings.length) {
  console.error("Memory safety strict mode enabled (MEMORY_STRICT=1). Treating warnings as failures.");
  process.exit(1);
}

if (failures.length) {
  console.error("Memory safety failures:");
  for (const failure of failures) console.error(`- ${failure}`);
  process.exit(1);
}

console.log("Memory safety check passed.");

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

function lineNumberFor(text, index) {
  return text.slice(0, index).split(/\r?\n/).length;
}
