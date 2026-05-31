window.ANNABEL_PRESS_DATA = {
  "generatedAt": "2026-05-31T08:22:37.290Z",
  "root": "/Users/annabelfilippini/Documents/AI-OS",
  "skills": [
    {
      "id": "adversarial-review-lite",
      "name": "adversarial-review-lite",
      "description": "Adversarial code or plan review. Use when Annabel asks for the harshest useful critique, when a change is risky, or before shipping user-facing behavior.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/adversarial-review-lite",
      "realPath": "skills/adversarial-review-lite",
      "entrypoint": "skills/adversarial-review-lite/SKILL.md",
      "summary": "This skill borrows the useful parts of gstack `/review` without importing the full workflow.",
      "references": [
        "gstack-distillation.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/adversarial-review-lite",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/adversarial-review-lite",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 1,
        "lastUsedAt": "2026-05-25T16:08:36.182Z",
        "agents": [
          "codex"
        ],
        "recent": [
          {
            "timestamp": "2026-05-25T16:08:36.182Z",
            "agent": "codex",
            "note": "QA review of Creative Business Refresh founder-letter HTML before sending to potential clients.",
            "source": "manual"
          }
        ]
      }
    },
    {
      "id": "ceo-review-lite",
      "name": "ceo-review-lite",
      "description": "Founder/CEO review for business idea scope. Use when Annabel wants to think bigger, reduce scope, choose ambition level, or challenge a plan before handoff.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/ceo-review-lite",
      "realPath": "skills/ceo-review-lite",
      "entrypoint": "skills/ceo-review-lite/SKILL.md",
      "summary": "This skill borrows the useful parts of gstack `/plan-ceo-review` without importing the full workflow.",
      "references": [
        "gstack-distillation.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/ceo-review-lite",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/ceo-review-lite",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "checkpoint",
      "name": "checkpoint",
      "description": "Save Garry/Claude strategy session state for continuity. Captures decisions, reasoning, open questions, and next steps.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/checkpoint",
      "realPath": "skills/checkpoint",
      "entrypoint": "skills/checkpoint/SKILL.md",
      "summary": "Save working state so the next Claude/Garry session can pick up without re-explaining context.",
      "references": [
        "README.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/checkpoint",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/checkpoint",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 6,
        "lastUsedAt": "2026-05-26T18:39:39.456Z",
        "agents": [
          "codex"
        ],
        "recent": [
          {
            "timestamp": "2026-05-26T18:39:39.456Z",
            "agent": "codex",
            "note": "Saved Vital Health Webflow CLI connection checkpoint",
            "source": "Vital Health Webflow CLI session"
          },
          {
            "timestamp": "2026-05-26T18:24:43.105Z",
            "agent": "codex",
            "note": "Saved paused checkpoint for Creative Business Refresh founder-letter hook decision.",
            "source": "manual"
          },
          {
            "timestamp": "2026-05-26T18:17:33.005Z",
            "agent": "codex",
            "note": "Saved Vital Health proposal questions and Webflow transfer checkpoint",
            "source": "Vital Health proposal session"
          },
          {
            "timestamp": "2026-05-25T16:40:29.332Z",
            "agent": "codex",
            "note": "Saved session checkpoint for Creative Business Refresh founder-letter/sendable PDF work.",
            "source": "manual"
          },
          {
            "timestamp": "2026-05-22T12:33:03.444Z",
            "agent": "codex",
            "note": "Saved free audit Tally preview checkpoint",
            "source": "manual"
          }
        ]
      }
    },
    {
      "id": "client-opportunity-map",
      "name": "client-opportunity-map",
      "description": "Annie-led workflow for auditing a client or business folder, mapping tools and recurring work, identifying practical AI opportunities, and producing a plain-English opportunity map that can route strategy to Garry and build feasibility to Business Partner.",
      "audience": [
        "annie",
        "garry",
        "business-partner"
      ],
      "runtime": [
        "codex",
        "claude"
      ],
      "visibility": "private",
      "relatedCliConnections": [
        "github"
      ],
      "path": "skills/client-opportunity-map",
      "realPath": "skills/client-opportunity-map",
      "entrypoint": "skills/client-opportunity-map/SKILL.md",
      "summary": "Use when Annabel wants to turn messy client or business context into a practical\nAI opportunity map.",
      "references": [
        "artifact-template.md",
        "opportunity-patterns.md",
        "question-bank.md",
        "workflow.md"
      ],
      "scripts": [
        "audit-existing-folder.py"
      ],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/client-opportunity-map",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/client-opportunity-map",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "client-proposal-pdf",
      "name": "client-proposal-pdf",
      "description": "Build concise branded client proposal PDFs from markdown for Annabel's website refresh and consulting work, using the Vital Health proposal pattern for phases, rates, honest ranges, hosting costs, next steps, approval blockers, no-dash copy mechanics, and markdown-to-HTML-to-Chrome PDF generation.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/client-proposal-pdf",
      "realPath": "skills/client-proposal-pdf",
      "entrypoint": "skills/client-proposal-pdf/SKILL.md",
      "summary": "Use when Annabel needs a polished client proposal PDF, especially after a\nwebsite refresh, Webflow rebuild, backend workflow mapping, or follow-up scope.",
      "references": [
        "good-bad-examples.md",
        "proposal-structure.md"
      ],
      "scripts": [
        "build_proposal_pdf.py"
      ],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/client-proposal-pdf",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/client-proposal-pdf",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "client-website-refresh",
      "name": "client-website-refresh",
      "description": "End-to-end Annabel website refresh harness for client sites. Use when auditing an existing business website, capturing what the client dislikes, planning a higher-standard redesign with Garry and Business Partner, creating or iterating an HTML preview, rebuilding into an editable platform such as Webflow, and preparing a client proposal with next steps and rates.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/client-website-refresh",
      "realPath": "skills/client-website-refresh",
      "entrypoint": "skills/client-website-refresh/SKILL.md",
      "summary": "Use this when Annabel wants to repeat the Vital Health style website process for\nanother client: diagnose the existing site, capture the client's dislikes,\ndesign a better version, iterate with Claude Code and Codex, rebuild it so the\nclient can edit it, and produce a clear proposal.",
      "references": [
        "client-question-bank.md",
        "good-bad-examples.md",
        "workflow.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/client-website-refresh",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/client-website-refresh",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "decision-pipeline",
      "name": "decision-pipeline",
      "description": "Turn a business or product idea into a clear decision and Codex-ready handoff. Use after Garry has clarified the customer, pain, scope, and next move.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/decision-pipeline",
      "realPath": "skills/decision-pipeline",
      "entrypoint": "skills/decision-pipeline/SKILL.md",
      "summary": "Garry owns intent, judgment, scope, and the decision record.",
      "references": [
        "README.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/decision-pipeline",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/decision-pipeline",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "guardrails-lite",
      "name": "guardrails-lite",
      "description": "Scope and safety guardrails for Codex implementation. Use when work risks drifting outside the approved plan or touching sensitive/reversible boundaries.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/guardrails-lite",
      "realPath": "skills/guardrails-lite",
      "entrypoint": "skills/guardrails-lite/SKILL.md",
      "summary": "This skill borrows useful concepts from gstack guard/freeze/careful workflows without importing the full stack.",
      "references": [
        "gstack-distillation.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/guardrails-lite",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/guardrails-lite",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "implement-approved-plan",
      "name": "implement-approved-plan",
      "description": "Implement a Claude/Garry handoff only after Business Partner/Codex has reviewed it against the repo. Use when given an approved or amended handoff and asked to make code changes, run verification, and write implementation notes.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/implement-approved-plan",
      "realPath": "skills/implement-approved-plan",
      "entrypoint": "skills/implement-approved-plan/SKILL.md",
      "summary": "Use this skill after `review-claude-plan`.",
      "references": [
        "README.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/implement-approved-plan",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/implement-approved-plan",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "investigate-lite",
      "name": "investigate-lite",
      "description": "Root-cause investigation for bugs or confusing repo behavior. Use before fixing when the cause is not yet proven.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/investigate-lite",
      "realPath": "skills/investigate-lite",
      "entrypoint": "skills/investigate-lite/SKILL.md",
      "summary": "This skill borrows the useful parts of gstack `/investigate` without importing the full workflow.",
      "references": [
        "gstack-distillation.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/investigate-lite",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/investigate-lite",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "markdown-lint-operating-docs",
      "name": "markdown-lint-operating-docs",
      "description": "Run practical Markdown linting for AI-OS operating docs without noisy generated/reference files.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/markdown-lint-operating-docs",
      "realPath": "skills/markdown-lint-operating-docs",
      "entrypoint": "skills/markdown-lint-operating-docs/SKILL.md",
      "summary": "Use this skill to make Markdown linting repeatable without burning context on\ngenerated or reference-heavy files.",
      "references": [],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/markdown-lint-operating-docs",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/markdown-lint-operating-docs",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "office-hours-lite",
      "name": "office-hours-lite",
      "description": "YC-style business idea office hours for Garry. Use when Annabel wants to brainstorm, validate, troubleshoot, or decide whether a business/product idea is worth pursuing.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/office-hours-lite",
      "realPath": "skills/office-hours-lite",
      "entrypoint": "skills/office-hours-lite/SKILL.md",
      "summary": "This skill borrows the useful parts of gstack `/office-hours` without importing the full workflow.",
      "references": [
        "gstack-distillation.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/office-hours-lite",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/office-hours-lite",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 1,
        "lastUsedAt": "2026-05-24T18:56:12.211Z",
        "agents": [
          "codex"
        ],
        "recent": [
          {
            "timestamp": "2026-05-24T18:56:12.211Z",
            "agent": "codex",
            "note": "Used to shape authentic small-business AI refresh one-pager positioning from Annabel's Cooldown/Marta/dad examples.",
            "source": "manual"
          }
        ]
      }
    },
    {
      "id": "plan-eng-review-lite",
      "name": "plan-eng-review-lite",
      "description": "Engineering review for implementation plans. Use when a Claude/Garry handoff may be technically risky, overbuilt, under-specified, or mismatched with the repo.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/plan-eng-review-lite",
      "realPath": "skills/plan-eng-review-lite",
      "entrypoint": "skills/plan-eng-review-lite/SKILL.md",
      "summary": "This skill borrows the useful parts of gstack `/plan-eng-review` without importing the full workflow.",
      "references": [
        "gstack-distillation.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/plan-eng-review-lite",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/plan-eng-review-lite",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "review-claude-plan",
      "name": "review-claude-plan",
      "description": "Review a Claude/Garry handoff against the actual repository before implementation. Use when given a handoff file and asked to assess feasibility, risks, scope, or implementation fit. Do not edit product code.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/review-claude-plan",
      "realPath": "skills/review-claude-plan",
      "entrypoint": "skills/review-claude-plan/SKILL.md",
      "summary": "Use this skill before implementing a Claude/Garry handoff.",
      "references": [
        "README.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/review-claude-plan",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/review-claude-plan",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "site-scraper-cli-builder",
      "name": "site-scraper-cli-builder",
      "description": "Build or review a site-specific, read-only scraper CLI and matching AI-OS skill/CLI connection, modeled after skool-pp-cli, for sites Annabel can legitimately access. Use when creating reusable tools that mirror account/community/course/member/content data into a local searchable store with auth safety, doctor checks, agent-context, sync, search, digest, and citation workflows.",
      "audience": [
        "annie",
        "business-partner"
      ],
      "runtime": [
        "codex"
      ],
      "visibility": "private",
      "relatedCliConnections": [],
      "path": "skills/site-scraper-cli-builder",
      "realPath": "skills/site-scraper-cli-builder",
      "entrypoint": "skills/site-scraper-cli-builder/SKILL.md",
      "summary": "Use this skill when Annabel wants a reusable CLI-backed scraper for a specific\nsite, not a one-off script. The target shape is:",
      "references": [
        "skool-pp-cli-pattern.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": false,
          "path": "/Users/annabelfilippini/.claude/skills/site-scraper-cli-builder",
          "pointsToCanonical": false
        },
        {
          "name": "Codex",
          "installed": false,
          "path": "/Users/annabelfilippini/.codex/skills/site-scraper-cli-builder",
          "pointsToCanonical": false
        }
      ],
      "usage": {
        "count": 1,
        "lastUsedAt": "2026-05-22T07:57:39.195Z",
        "agents": [
          "business-partner"
        ],
        "recent": [
          {
            "timestamp": "2026-05-22T07:57:39.195Z",
            "agent": "business-partner",
            "note": "Created reusable builder skill for site-specific scraper CLI pattern.",
            "source": "codex-session"
          }
        ]
      }
    },
    {
      "id": "skool-intelligence-digest",
      "name": "skool-intelligence-digest",
      "description": "Collect and summarize Skool community signals for Annabel Press, including account status, pricing, member counts, visible posts, useful links, and attention-worthy updates.",
      "audience": [
        "annie",
        "business-partner"
      ],
      "runtime": [
        "codex"
      ],
      "visibility": "private",
      "relatedCliConnections": [
        "skool-pp-cli"
      ],
      "path": "skills/skool-intelligence-digest",
      "realPath": "skills/skool-intelligence-digest",
      "entrypoint": "skills/skool-intelligence-digest/SKILL.md",
      "summary": "Use this skill when Annabel wants to scrape, search, or summarize Skool\ncommunities she legitimately owns or pays for, using the authenticated\n`skool-pp-cli` local knowledge-base workflow.",
      "references": [
        "digest-fields.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/skool-intelligence-digest",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/skool-intelligence-digest",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 3,
        "lastUsedAt": "2026-05-22T08:32:08.364Z",
        "agents": [
          "codex",
          "business-partner"
        ],
        "recent": [
          {
            "timestamp": "2026-05-22T08:32:08.364Z",
            "agent": "codex",
            "note": "Used Skool CLI local mirror and Mansel captured audit materials to assess Tally audit form section necessity.",
            "source": "user request 2026-05-22"
          },
          {
            "timestamp": "2026-05-21T15:05:33.106Z",
            "agent": "business-partner",
            "note": "Checked Skool scraper status and ran public-only digest refresh.",
            "source": "manual"
          },
          {
            "timestamp": "2026-05-12T21:44:43.036Z",
            "agent": "business-partner",
            "note": "Planned Skool agency partner sourcing workflow for Agency Audit Network.",
            "source": "manual"
          }
        ]
      }
    },
    {
      "id": "small-business-shopify-redesign",
      "name": "small-business-shopify-redesign",
      "description": "Draft-only Shopify redesign workflow for small business sites. Use when Codex is asked to improve, redesign, QA, simplify, push, or document a Shopify theme for a small business, especially when there are multiple draft/live themes, app-generated code, owner-editability goals, product/page templates, metafields, theme previews, or requests to replicate lessons from the Cooldown redesign.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/small-business-shopify-redesign",
      "realPath": "skills/small-business-shopify-redesign",
      "entrypoint": "skills/small-business-shopify-redesign/SKILL.md",
      "summary": "Use this skill to redesign or clean up a Shopify site without creating live-site risk, while making the result easier for a non-developer owner to maintain.",
      "references": [
        "good-bad-examples.md",
        "shopify-guardrails.md",
        "workflow.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/small-business-shopify-redesign",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/small-business-shopify-redesign",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 3,
        "lastUsedAt": "2026-05-12T15:13:36.531Z",
        "agents": [
          "business-partner",
          "codex"
        ],
        "recent": [
          {
            "timestamp": "2026-05-12T15:13:36.531Z",
            "agent": "business-partner",
            "note": "Used for Cooldown Annabel v3 Shopify PDP add-to-cart fix.",
            "source": "codex"
          },
          {
            "timestamp": "2026-05-12T14:26:39.613Z",
            "agent": "codex",
            "note": "Created Annabel v3 unpublished Shopify draft",
            "source": "codex-session"
          },
          {
            "timestamp": "2026-05-12T14:14:40.570Z",
            "agent": "codex",
            "note": "Cooldown cart/PDP QA re-review",
            "source": "codex-session"
          }
        ]
      }
    },
    {
      "id": "webflow-rebuild-qa",
      "name": "webflow-rebuild-qa",
      "description": "Webflow rebuild and QA workflow for turning a static HTML or Vercel preview into a client-editable Webflow site, using Vital Health lessons about Designer limits, Data API reliability, staging-only publish, CMS/editability, mobile QA, link checks, placeholder blockers, and client review readiness.",
      "audience": [],
      "runtime": [],
      "visibility": "unspecified",
      "relatedCliConnections": [],
      "path": "skills/webflow-rebuild-qa",
      "realPath": "skills/webflow-rebuild-qa",
      "entrypoint": "skills/webflow-rebuild-qa/SKILL.md",
      "summary": "Use this when a client site preview, static HTML mockup, or Vercel build needs to\nbe rebuilt, checked, or prepared inside Webflow so the client can edit it.",
      "references": [
        "good-bad-examples.md",
        "qa-checklist.md",
        "webflow-gotchas.md"
      ],
      "scripts": [],
      "assets": [],
      "runtimeStatus": [
        {
          "name": "Claude",
          "installed": true,
          "path": "/Users/annabelfilippini/.claude/skills/webflow-rebuild-qa",
          "pointsToCanonical": true
        },
        {
          "name": "Codex",
          "installed": true,
          "path": "/Users/annabelfilippini/.codex/skills/webflow-rebuild-qa",
          "pointsToCanonical": true
        }
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    }
  ],
  "cliConnections": [
    {
      "id": "flights",
      "name": "flights",
      "displayName": "Flightscope (flight routes + prices CLI)",
      "binary": "tools/flightscope/bin/flightscope",
      "installed": true,
      "audience": [
        "annie",
        "business-partner"
      ],
      "runtime": [
        "claude",
        "codex"
      ],
      "visibility": "private",
      "relatedSkills": [],
      "safeCommands": [
        "tools/flightscope/bin/flightscope --version",
        "tools/flightscope/bin/flightscope doctor --json",
        "tools/flightscope/bin/flightscope airports \"<place>\" --json",
        "tools/flightscope/bin/flightscope spots --wind --json",
        "tools/flightscope/bin/flightscope routes \"<IATA>\" --json",
        "tools/flightscope/bin/flightscope routes \"<IATA>\" --kiteable --json",
        "tools/flightscope/bin/flightscope routes \"<IATA>\" --to \"<A,B,C>\" --json",
        "tools/flightscope/bin/flightscope price \"<FROM>\" \"<TO>\" --depart \"<YYYY-MM-DD>\" --json",
        "tools/flightscope/bin/flightscope plan \"<FROM,FROM2>\" --depart \"<YYYY-MM-DD>\" --json",
        "tools/flightscope/bin/flightscope plan \"<FROM,FROM2>\" --depart \"<YYYY-MM-DD>\" --min-wind 15 --json",
        "tools/flightscope/bin/flightscope plan \"<FROM,FROM2>\" --depart \"<YYYY-MM-DD>\" --no-wind --json"
      ],
      "approvalRequired": [
        "pip install fast-flights   # already installed 2026-05-24; listed for re-provisioning"
      ],
      "path": "cli-connections/flights",
      "entrypoint": "cli-connections/flights/CONNECTION.md",
      "summary": "A reusable CLI scraper for flight **routes** (flightconnections.com) and flight\n**prices** (Google Flights), in the `skool-pp-cli` mold. Built as Annabel's\npersonal travel-decision tool — customer #1 is a solo kitesurfer deciding where\nto go next based on where flights actually reach, what they cost, and where the\nwind is.",
      "references": [
        "commands.md",
        "safety.md"
      ],
      "scripts": [
        "check-auth.sh",
        "check-installed.sh"
      ],
      "usage": {
        "count": 1,
        "lastUsedAt": "2026-05-29T17:13:27.685Z",
        "agents": [
          "codex"
        ],
        "recent": [
          {
            "timestamp": "2026-05-29T17:13:27.685Z",
            "agent": "codex",
            "note": "Used Flightscope route and price checks for Annabel's Europe trip planning from Tarifa",
            "source": "manual"
          }
        ]
      }
    },
    {
      "id": "github",
      "name": "github",
      "displayName": "GitHub CLI",
      "binary": "gh",
      "installed": true,
      "audience": [
        "garry",
        "business-partner"
      ],
      "runtime": [
        "claude",
        "codex"
      ],
      "visibility": "private",
      "relatedSkills": [
        "review-claude-plan",
        "implement-approved-plan"
      ],
      "safeCommands": [
        "gh auth status",
        "gh repo view",
        "gh pr view",
        "gh pr checks"
      ],
      "approvalRequired": [
        "gh pr merge",
        "gh repo delete",
        "gh release create"
      ],
      "path": "cli-connections/github",
      "entrypoint": "cli-connections/github/CONNECTION.md",
      "summary": "Use this connection for repository inspection, PR review, issue lookup, and\nshipping support when a project already uses GitHub.",
      "references": [
        "commands.md",
        "safety.md"
      ],
      "scripts": [
        "check-auth.sh",
        "check-installed.sh"
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "shopify",
      "name": "shopify",
      "displayName": "Shopify CLI",
      "binary": "shopify",
      "installed": true,
      "audience": [
        "business-partner"
      ],
      "runtime": [
        "codex"
      ],
      "visibility": "private",
      "relatedSkills": [
        "small-business-shopify-redesign"
      ],
      "safeCommands": [
        "shopify theme list",
        "shopify theme dev",
        "shopify theme check"
      ],
      "approvalRequired": [
        "shopify theme push",
        "shopify app deploy"
      ],
      "path": "cli-connections/shopify",
      "entrypoint": "cli-connections/shopify/CONNECTION.md",
      "summary": "Use this connection for Annabel's Shopify theme and small-business redesign\nworkflows.",
      "references": [
        "commands.md",
        "safety.md"
      ],
      "scripts": [
        "check-auth.sh",
        "check-installed.sh"
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "skills-sh",
      "name": "skills-sh",
      "displayName": "skills.sh CLI",
      "binary": "npx skills",
      "installed": true,
      "audience": [
        "garry",
        "business-partner"
      ],
      "runtime": [
        "claude",
        "codex"
      ],
      "visibility": "private",
      "relatedSkills": [],
      "safeCommands": [
        "npx skills list",
        "npx skills show"
      ],
      "approvalRequired": [
        "npx skills add",
        "npx skills remove",
        "npx skills update"
      ],
      "path": "cli-connections/skills-sh",
      "entrypoint": "cli-connections/skills-sh/CONNECTION.md",
      "summary": "Use this connection when inspecting, installing, or packaging skills through the\n`skills.sh` ecosystem.",
      "references": [
        "commands.md",
        "safety.md"
      ],
      "scripts": [
        "check-auth.sh",
        "check-installed.sh"
      ],
      "usage": {
        "count": 0,
        "lastUsedAt": null,
        "agents": [],
        "recent": []
      }
    },
    {
      "id": "skool-pp-cli",
      "name": "skool-pp-cli",
      "displayName": "Skool Personal Knowledge Base CLI",
      "binary": "tools/skool-pp-cli/bin/skool-pp-cli",
      "installed": true,
      "audience": [
        "annie",
        "business-partner"
      ],
      "runtime": [
        "codex"
      ],
      "visibility": "private",
      "relatedSkills": [
        "skool-intelligence-digest"
      ],
      "safeCommands": [
        "tools/skool-pp-cli/bin/skool-pp-cli --version",
        "tools/skool-pp-cli/bin/skool-pp-cli doctor --json --no-input --no-color",
        "tools/skool-pp-cli/bin/skool-pp-cli agent-context --pretty",
        "tools/skool-pp-cli/bin/skool-pp-cli communities list --agent",
        "tools/skool-pp-cli/bin/skool-pp-cli kb stats --json",
        "tools/skool-pp-cli/bin/skool-pp-cli find \"<query>\" --prefer-recent 0.5 --agent",
        "tools/skool-pp-cli/bin/skool-pp-cli guide \"<topic>\" --markdown"
      ],
      "approvalRequired": [
        "tools/skool-pp-cli/bin/skool-pp-cli auth set-token",
        "tools/skool-pp-cli/bin/skool-pp-cli kb sync-all",
        "tools/skool-pp-cli/bin/skool-pp-cli kb sync",
        "tools/skool-pp-cli/bin/skool-pp-cli transcribe-refs"
      ],
      "path": "cli-connections/skool-pp-cli",
      "entrypoint": "cli-connections/skool-pp-cli/CONNECTION.md",
      "summary": "Use this connection when Annabel wants to mirror her own Skool communities into\na local SQLite knowledge base for search, citations, guides, digests, and agent\nqueries.",
      "references": [],
      "scripts": [],
      "usage": {
        "count": 7,
        "lastUsedAt": "2026-05-22T08:32:08.370Z",
        "agents": [
          "codex",
          "business-partner"
        ],
        "recent": [
          {
            "timestamp": "2026-05-22T08:32:08.370Z",
            "agent": "codex",
            "note": "Ran doctor, communities/list attempt, kb stats, and kb sql against local ainative mirror for Mansel audit review.",
            "source": "user request 2026-05-22"
          },
          {
            "timestamp": "2026-05-22T07:57:39.225Z",
            "agent": "business-partner",
            "note": "Inspected Skool CLI agent-context, help, and source pattern to generalize scraper CLI skill.",
            "source": "codex-session"
          },
          {
            "timestamp": "2026-05-21T15:15:51.676Z",
            "agent": "business-partner",
            "note": "Removed Skool Press wrapper references and attempted authenticated private sync for earlyaidopters and ainative.",
            "source": "manual"
          },
          {
            "timestamp": "2026-05-21T15:05:33.112Z",
            "agent": "business-partner",
            "note": "Ran Skool CLI doctor to verify auth and connectivity.",
            "source": "manual"
          },
          {
            "timestamp": "2026-05-15T21:50:20.871Z",
            "agent": "business-partner",
            "note": "Queried local Skool KB for Mansel Scheffel posts/comments from 2026-05-15.",
            "source": "user request"
          }
        ]
      }
    },
    {
      "id": "windguru",
      "name": "windguru",
      "displayName": "Windguru (live GFS wind forecast)",
      "binary": "tools/flightscope/bin/flightscope",
      "installed": true,
      "audience": [
        "annie",
        "business-partner"
      ],
      "runtime": [
        "claude",
        "codex"
      ],
      "visibility": "private",
      "relatedSkills": [],
      "safeCommands": [
        "tools/flightscope/bin/flightscope doctor --json",
        "tools/flightscope/bin/flightscope wind \"<spot>\" --json",
        "tools/flightscope/bin/flightscope wind \"<spot>\" --when \"<YYYY-MM-DD>\" --json",
        "tools/flightscope/bin/flightscope wind \"<spot>\" --when \"<YYYY-MM-DD>\" --days 5 --min-wind 15 --json",
        "tools/flightscope/bin/flightscope wind --id <windguru_id> --json"
      ],
      "approvalRequired": [
        "[]   # stdlib-only (urllib); no install, no key, no browser"
      ],
      "path": "cli-connections/windguru",
      "entrypoint": "cli-connections/windguru/CONNECTION.md",
      "summary": "Live wind forecast for kite spots, read from Windguru's public GFS model. This\nis the **wind** half of flightscope: it answers \"will it actually be windy at\nthis spot during my travel window?\" while the [flights](../flights/CONNECTION.md)\nconnector answers \"can I get there and what does it cost?\". The two share one\nbinary — `tools/flightscope/bin/flightscope` — and Windguru data also drives the\n`plan` command's wind ranking.",
      "references": [
        "commands.md",
        "safety.md"
      ],
      "scripts": [
        "check-auth.sh",
        "check-installed.sh"
      ],
      "usage": {
        "count": 2,
        "lastUsedAt": "2026-05-29T17:43:28.323Z",
        "agents": [
          "codex"
        ],
        "recent": [
          {
            "timestamp": "2026-05-29T17:43:28.323Z",
            "agent": "codex",
            "note": "Compared European Windguru forecasts for Annabel's June 5 kitesurf travel planning",
            "source": "manual"
          },
          {
            "timestamp": "2026-05-29T17:13:27.683Z",
            "agent": "codex",
            "note": "Used live Windguru forecast via Flightscope to assess Leucate kite conditions for Europe trip planning",
            "source": "manual"
          }
        ]
      }
    }
  ],
  "profiles": [
    {
      "agent": "annie",
      "role": "global-orchestrator",
      "path": "agents/annie/profile.yaml",
      "skills": [
        "client-opportunity-map",
        "client-website-refresh",
        "client-proposal-pdf",
        "skool-intelligence-digest"
      ],
      "cliConnections": [
        "skool-pp-cli"
      ],
      "delegates": [
        "garry",
        "business-partner"
      ]
    },
    {
      "agent": "business-partner",
      "role": "specialist",
      "path": "agents/business-partner/profile.yaml",
      "skills": [
        "adversarial-review-lite",
        "client-website-refresh",
        "client-proposal-pdf",
        "guardrails-lite",
        "implement-approved-plan",
        "investigate-lite",
        "markdown-lint-operating-docs",
        "plan-eng-review-lite",
        "review-claude-plan",
        "site-scraper-cli-builder",
        "small-business-shopify-redesign",
        "webflow-rebuild-qa"
      ],
      "cliConnections": [
        "github",
        "skool-pp-cli",
        "shopify",
        "skills-sh"
      ],
      "delegates": []
    },
    {
      "agent": "garry",
      "role": "specialist",
      "path": "agents/garry/profile.yaml",
      "skills": [
        "checkpoint",
        "client-website-refresh",
        "client-proposal-pdf",
        "decision-pipeline",
        "office-hours-lite",
        "ceo-review-lite"
      ],
      "cliConnections": [
        "github",
        "skills-sh"
      ],
      "delegates": []
    }
  ]
};
