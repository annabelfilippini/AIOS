# CLAUDE

Claude-specific runtime adapter for this AI-OS.

Claude is an execution surface, not an identity boundary. Annie, Garry, and
Business Partner are AI-OS modes/personas that can be used from any capable LLM
runtime. Skills and standards are global unless a tool is physically unavailable
in the current runtime.

## Read Only What Applies

- Read `AGENTS.md` for universal AI-OS rules.
- Read project-specific `CLAUDE.md` or `AGENTS.md` before broad searches.
- Read `agents/agent.md` when coordinating Annie, Garry, and Business Partner.
- Read `agents/garry/README.md` when Annabel explicitly wants Garry or
  strategy/planning work.
- Read `agents/annie/README.md` when the request involves orchestration,
  inbox/calendar/docs, follow-through, or personal/business operations.
- Read `SOUL.md` or `USER.md` only when voice, preference, or personal context
  matters.

## Claude Runtime Role

Claude is a strong planning and drafting runtime. Garry is not Claude-specific;
Garry is the strategy/challenge mode that Claude may run when Annabel or Annie
chooses it. Annie is the default AI-OS front door and orchestrator.

If Annabel has not explicitly chosen Garry, assume Annie should triage and
coordinate the request. Garry remains the specialist Annie can route to for:

- idea intake and critique
- stress-testing
- scope and decision memos
- product judgment
- implementation-ready handoffs

Garry should not pretend repository assumptions are implementation truth. If
code will change, write the handoff so Business Partner can verify it
against the repo.

## Builder Lane

- Keep scope tied to Annabel's stated goal and active project instructions.
- Make implementation choices from repository reality, not assumptions.
- Run relevant verification before claiming done.
- For QA, provide branch/diff/PR, what changed, verification run, and
  known risks.
- For substantial cross-agent work, use `agents/shared/handoffs/active/`.

## Source Of Truth

- Agent coordination: `agents/agent.md`
- Garry identity and commands: `agents/garry/`
- Annie identity and SOPs: `agents/annie/`
- Business Partner identity and SOPs: `agents/business-partner/`
- Global skills for Claude and Codex: `skills/`
- Global CLI/tool connections: `cli-connections/`
- Cross-agent handoffs, QA, and templates: `agents/shared/`
- Durable memory/checkpoints: `operations/memory/`
- Knowledge vault: `knowledge/`
- Active project work: `projects/<project>/`

Runtime folders like `~/.claude/skills` and `~/.codex/skills` should point to
top-level `skills/`. They are adapters, not source-of-truth copies.

## Workspace Rules

- This root is an index, not a working project.
- Work inside `projects/<project>/` for project work.
- Project-specific instructions override root guidance.
- On session start or project switch, run
  `node operations/memory/scripts/recall.mjs --cwd "$PWD" --query "<task>"`
  and use the surfaced checkpoints/candidates before reading memory broadly.
- `wiki` is a compatibility symlink to `knowledge`.
- Large generated outputs belong in `scratch/` during active work and
  `_archive/generated/` after handoff.

Before reading broadly, identify the target project and open only that
project's instructions.

## Stack

This is the stack reality at the AI-OS root level. Do NOT assume anything
beyond what is listed here. Project folders should carry their own `## Stack`
section overriding/extending this one.

**Configured at the AI-OS / system level:**

- Claude Code CLI (`~/.claude/`) as one runtime adapter.
- Codex CLI (`~/.codex/`) as a peer runtime adapter.
- Git for all version control.
- AI-OS memory and checkpoint system under `operations/memory/`.
- Shared AI-OS skills, standards, and CLI connections should be available to all
  capable runtimes, not owned by Claude or Codex.
- MCP servers available in-session: Telegram, Playwright, Stitch, Firecrawl,
  Google (Gmail/Calendar/Drive).

**Skool content scraping:** use `skool-curl`, not generic web scraping.

**Explicitly NOT configured at the root level** (do not assume; ask before
introducing):

- Dropbox, Supabase, Cloudflare, Claude Teams.
- Any deploy/hosting target (Vercel, Netlify, etc.) — declared per-project.
- Any analytics, billing, or CRM tool.

**For project folders:** add a `## Stack` section to that project's
`CLAUDE.md` listing the tools that ARE configured for that project, the
deploy target if any, and an explicit "not assumed" line for tools that
adjacent projects use but this one does not.
