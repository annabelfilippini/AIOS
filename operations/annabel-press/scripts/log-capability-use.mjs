#!/usr/bin/env node
import fs from "node:fs";
import path from "node:path";
import { fileURLToPath } from "node:url";

const scriptPath = fileURLToPath(import.meta.url);
const root = path.resolve(path.dirname(scriptPath), "../../..");
const usagePath = path.join(root, "operations/annabel-press/usage/events.jsonl");

const args = process.argv.slice(2);
const [type, id] = args;

if (!["skill", "cli"].includes(type) || !id) {
  usage();
}

const options = parseOptions(args.slice(2));
const event = {
  timestamp: new Date().toISOString(),
  type,
  id,
  agent: options.agent || "unknown",
  note: options.note || "",
  source: options.source || "manual",
};

fs.mkdirSync(path.dirname(usagePath), { recursive: true });
fs.appendFileSync(usagePath, `${JSON.stringify(event)}\n`);
console.log(`Logged ${type}:${id}`);

function parseOptions(parts) {
  const parsed = {};
  for (let index = 0; index < parts.length; index += 1) {
    const part = parts[index];
    if (part === "--agent") {
      parsed.agent = parts[index + 1] || "";
      index += 1;
    } else if (part === "--note") {
      parsed.note = parts[index + 1] || "";
      index += 1;
    } else if (part === "--source") {
      parsed.source = parts[index + 1] || "";
      index += 1;
    }
  }
  return parsed;
}

function usage() {
  console.error("Usage: log-capability-use.mjs <skill|cli> <id> [--agent name] [--note text] [--source text]");
  process.exit(1);
}
