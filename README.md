# Octoparse Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Scenario-oriented Octoparse agent skills, template knowledge packs, and evaluation assets for MCP-enabled assistants. The repository now focuses on higher-level workflows such as lead generation, social media competitor monitoring, template-chain design, and MCP bootstrap instead of low-level task CRUD skills alone.

## Overview

This repository currently contains:

- **4 skills** under `skills/`
- **2 template knowledge packs** under `templates/`
- curated reference files for routing, shortlisting, and chain validation
- eval assets for scenario skills
- planning and validation documents under `docs/plans/`

## Skill Catalog

| Skill | Type | What it does | Key assets |
|---|---|---|---|
| `octoparse-mcp-setup` | setup / utility | Configures the Octoparse MCP server and guides OAuth 2.1 or API key authentication | client-specific reference docs for Claude Code, Cursor, Gemini CLI, Qwen Code, VS Code, TRAE, and OpenClaw |
| `octoparse-lead-generation` | scenario skill | Recommends and runs lead-generation workflows for local-business and B2B prospecting requests | request classifier, split shortlists, track guidance, evals |
| `octoparse-social-media-competitor-monitoring` | scenario skill | Recommends workflows for competitor account tracking, brand mention discovery, and comment collection for downstream analysis | request classifier, shortlist files, scenario guidance, evals |
| `octoparse-link-template` | workflow design skill | Designs and validates multi-template chains, including field mapping and downstream enrichment logic | linking rules, output inference rules, stable template catalog |

## Template Knowledge Packs

The `templates/` directory stores reusable template documentation that scenario skills can cite when recommending or validating workflows.

Current template family:

| Template | Output level | Primary use | Included docs |
|---|---|---|---|
| `google-maps-scraper` | business / detail | local business discovery, lead generation, competitor discovery | `TEMPLATE.md`, `INPUT.md`, `OUTPUT.md`, `LIMITATIONS.md`, `TIPS.md`, `FAQ.md` |
| `google-maps-reviews-scraper` | review | review analysis, reputation monitoring, downstream sentiment workflows | `TEMPLATE.md`, `INPUT.md`, `OUTPUT.md`, `LIMITATIONS.md`, `TIPS.md`, `FAQ.md` |

These docs are designed to make template behavior explicit:

- `TEMPLATE.md` explains the use case and fit
- `INPUT.md` documents required parameters and common mistakes
- `OUTPUT.md` documents high-value fields and linking value
- `LIMITATIONS.md`, `TIPS.md`, and `FAQ.md` capture guardrails and operator guidance

## How The Repository Is Organized

```text
AgentSkills/
├── docs/
│   └── plans/                               # Design notes, validation reports, and planning docs
├── skills/
│   ├── octoparse-lead-generation/
│   │   ├── SKILL.md
│   │   ├── evals/
│   │   └── references/
│   ├── octoparse-link-template/
│   │   ├── SKILL.md
│   │   └── references/
│   ├── octoparse-mcp-setup/
│   │   ├── SKILL.md
│   │   └── references/
│   └── octoparse-social-media-competitor-monitoring/
│       ├── SKILL.md
│       ├── evals/
│       └── references/
├── templates/
│   └── google-maps/
│       ├── google-maps-scraper/
│       └── google-maps-reviews-scraper/
├── CLAUDE.md                               # Project-level guidance and AI-native evaluation standard
├── LICENSE
└── README.md
```

## Typical Usage

Install one or more skill folders from `skills/` into your assistant's skill directory, then use natural-language prompts to trigger them.

Example requests:

- "Set up Octoparse MCP in Cursor"
- "Find the best Octoparse workflow for plumber leads in Berlin"
- "I need a Google Maps workflow that finds cafes and then pulls reviews"
- "Help me monitor competitor mentions on TikTok and Reddit"
- "Can this template feed a downstream contact-enrichment template?"

Recommended usage flow:

1. Use `octoparse-mcp-setup` to connect Octoparse MCP in your client.
2. Use a scenario skill such as `octoparse-lead-generation` or `octoparse-social-media-competitor-monitoring` to narrow the workflow.
3. Use `octoparse-link-template` when the request needs a multi-template chain or downstream enrichment.
4. Use the local docs in `templates/` when you need concrete input/output expectations for a specific template.

## Supported MCP Client References

The repository includes setup references for these clients inside `skills/octoparse-mcp-setup/references/`:

- Claude Code
- Cursor
- Gemini CLI
- Qwen Code
- VS Code
- TRAE
- OpenClaw

These references focus on Octoparse MCP configuration differences per client rather than duplicating the main skill logic.

## Reference and Evaluation Assets

This repository is more than a collection of `SKILL.md` files. It also includes:

- request classifiers that route ambiguous user requests into explicit internal tracks
- curated shortlist JSON files that keep recommendations narrow and consistent
- guidance files that encode recommendation rules and scenario boundaries
- eval datasets in `evals/` for scenario-skill regression checks
- design and validation material in `docs/plans/`

## Development Notes

If you modify a skill in this repository:

- keep the `SKILL.md` instructions aligned with any supporting files in `references/`
- update eval assets when scenario behavior changes
- update template docs when a skill depends on their input/output guarantees
- review the AI Native Evaluation Standard in [CLAUDE.md](CLAUDE.md)

## License

MIT License. See [LICENSE](LICENSE) for details.
