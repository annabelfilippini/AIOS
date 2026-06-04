#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptPath = fileURLToPath(import.meta.url);
const memoryRoot = path.resolve(path.dirname(scriptPath), "..");

const targetDirs = ["checkpoints", "refinement-candidates"].map((dir) => path.join(memoryRoot, dir));
const dryRun = process.argv.includes("--dry-run");

const changed = [];

for (const filePath of targetDirs.flatMap(listMarkdown)) {
  const text = fs.readFileSync(filePath, "utf8");
  if (text.startsWith("---\n")) continue;

  const relativePath = path.relative(memoryRoot, filePath);
  const base = path.basename(filePath, ".md");
  const { date, time } = parseDateTimeFromFilename(base);

  const frontmatter =
    `---\n` +
    `date: ${date}\n` +
    `time: ${time}\n` +
    `project: unknown\n` +
    `status: draft\n` +
    `next-session: \"\"\n` +
    `---\n\n`;

  if (!dryRun) fs.writeFileSync(filePath, frontmatter + text, "utf8");
  changed.push(relativePath);
}

if (changed.length === 0) {
  console.log("No files needed frontmatter.");
  process.exit(0);
}

console.log(dryRun ? "Would add frontmatter to:" : "Added frontmatter to:");
for (const rel of changed) console.log(`- ${rel}`);

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

function parseDateTimeFromFilename(name) {
  // Expected patterns:
  // - YYYY-MM-DD-....
  // - YYYY-MM-DD-HHMM-....
  const date = /^\d{4}-\d{2}-\d{2}/.test(name) ? name.slice(0, 10) : "1970-01-01";
  const remainder = name.slice(10);
  const timeMatch = remainder.match(/^-(\d{4})(?:\D|$)/);
  const time = timeMatch ? `${timeMatch[1].slice(0, 2)}:${timeMatch[1].slice(2, 4)}` : "00:00";
  return { date, time };
}
