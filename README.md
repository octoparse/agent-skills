<p align="center">
  <strong>Octoparse Agent Skills</strong>
</p>

<p align="center">
  <strong>Web data extraction for AI agents — ~670 ready-made templates, no scraper to build</strong>
</p>

<p align="center">
  <a href="https://www.octoparse.com"><img src="https://img.shields.io/badge/Powered%20by-Octoparse-2E6BE6?style=for-the-badge" alt="Powered by Octoparse"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-555555?style=for-the-badge" alt="MIT"></a>
  <a href="#skills"><img src="https://img.shields.io/badge/Templates-670%2B-F86606?style=for-the-badge" alt="670+ templates"></a>
  <a href="https://agent-plugins.org"><img src="https://img.shields.io/badge/Agent%20Plugins-1.0.0-9D97F4?style=for-the-badge" alt="Agent Plugins 1.0.0"></a>
  <a href="https://mcp.octoparse.com"><img src="https://img.shields.io/badge/MCP-Compatible-15C1E6?style=for-the-badge" alt="MCP compatible"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> &bull;
  <a href="#example-use-cases">Use cases</a> &bull;
  <a href="#installation">Installation</a> &bull;
  <a href="#what-it-covers">Coverage</a> &bull;
  <a href="#pricing">Pricing</a> &bull;
  <a href="#how-it-works">How it works</a> &bull;
  <a href="#support">Support</a>
</p>

---

## Overview

Drop these skills into Claude Code, Cursor, VS Code, Gemini CLI, or any MCP-capable agent
and it gains working hands on the Octoparse platform. With one install, your agent can:

- **Extract from hundreds of sites** — Google Maps, Amazon, LinkedIn, Indeed, Yellow
  Pages, Gelbe Seiten, Pagesjaunes, Naver, Suumo, Booking, Trustpilot, Reddit, TikTok,
  YouTube, and hundreds more, in English, Japanese, Spanish, French, German, Italian, and
  Korean.
- **Pick the right template itself** — nine need-shaped workflow guides route a plain
  request to a curated shortlist, filtered by market, account tier, and cost.
- **Run and export** — creates the cloud task, polls it, and returns structured rows.
- **Query managed datasets** — Temu and TikTok Shop ship as typed, filterable datasets
  with fields no scraper exposes.
- **Tell you when it can't** — coverage gaps are documented as carefully as the
  capabilities, so you get an honest "no" instead of a wrong template that still bills.

---

## Quick start

```
/plugin marketplace add octoparse/agent-skills
/plugin install octoparse
```

Run `/mcp` to authorize, then ask for what you want:

> *Find dentists in Chicago with phone numbers and websites, and export them as CSV.*

The skill picks the template, shapes the input, runs the cloud task, and returns the rows.

---

## Example use cases

Describe the outcome in plain language. The agent selects the template, chains a second
pass when one is genuinely needed, and reports what it actually got.

| Use case | Example prompt |
|---|---|
| **Lead generation** | Find plumbers in Munich on Gelbe Seiten, then crawl their websites for emails and social links, and export a CSV for my CRM. |
| **Price monitoring** | Track these 40 ASINs on Amazon Germany weekly and flag anything that drops more than 10%. |
| **Market research** | Show me what's selling in Amazon Best Sellers for wireless earbuds, plus the price band across the top 50 listings. |
| **Reputation analysis** | Pull the last 500 reviews for our hotel from TripAdvisor, Booking, and Google Maps, and summarise the top complaint themes. |
| **Supplier research** | Shortlist industrial suppliers on IPROS and Kompass, then check each one's filings on North Data before I contact them. |
| **Talent market** | Who is hiring backend engineers in Japan right now? Pull Hello Work and Indeed listings with salary ranges. |
| **Social listening** | Collect Reddit and X mentions of our brand from the last month, plus the comment threads, for sentiment analysis. |
| **Search visibility** | Capture Google and Naver results for these 20 keywords and tell me where we rank versus our two competitors. |
| **Property research** | Scrape Suumo used-apartment listings in Setagaya with layout, age, and station distance. |

---

## Installation

### Claude Code

```
/plugin marketplace add octoparse/agent-skills
/plugin install octoparse
```

The MCP server is declared by the plugin — no manual configuration. Run `/mcp` to
authorize.

### Cursor, VS Code, Windsurf

These read the Claude Code plugin format. Add the repo to your workspace, or register the
MCP server directly:

```bash
claude mcp add --transport http octoparse https://mcp.octoparse.com
```

### Agent Plugins clients

The repo ships a root `plugin.json` and `mcp.json` conforming to
[Agent Plugins 1.0.0](https://agent-plugins.org). Clients implementing that specification
discover the skills and the MCP server without further configuration.

### Any agent that reads Markdown

Point it at `skills/octoparse-ultimate-scraper/SKILL.md` and register
`https://mcp.octoparse.com` as an MCP server.

---

## Prerequisites

1. **Octoparse account** — sign up at [octoparse.com](https://www.octoparse.com); a free
   tier is available and covers 479 of the templates.
2. **Authorization** — run `/mcp` for browser OAuth. For headless or CI use, create an API
   key in the [account console](https://www.octoparse.com/console/account-center/api-keys)
   and set it as an `x-api-key` header on your own client config.

Some templates require a **STANDARD** account regardless of their per-line price. The
skill flags this before running anything.

---

## What it covers

**Markets:** English/global, Japanese, Spanish, French, German, Italian, Korean.
Non-English templates are the majority — German and French lead B2B and directories,
Japan leads jobs and property, Korea leads e-commerce and social.

**Known gaps**, stated up front so the agent never substitutes a near-miss:

- No Instagram or Facebook templates
- No SEO metrics — no backlinks, domain authority, keyword volume, or traffic estimates
- No US Amazon review template (Germany, Italy, France, UK, Japan have one)
- No Korean lead-generation templates
- Glassdoor is Germany only; no job templates for Italy or Korea
- Almost no German property coverage; flights are Check24 Germany only

---

## Pricing

Templates bill **per output line**. 479 are free; the rest range from $0.05 to $3 per
1,000 lines, set per template. There is no scheduler — recurring monitoring means
re-running, which bills again.

The skill confirms scope before running anything that produces a list, and states the
per-run cost at your result size.

---

## Skills

| Skill | What it does |
|---|---|
| **[`octoparse-ultimate-scraper`](skills/octoparse-ultimate-scraper/)** | Routes any extraction request to the right template, runs the cloud task, and exports results. Nine workflow guides covering leads, price monitoring, market research, reviews, supplier vetting, hiring, property and travel, social listening, and search visibility. |
| **[`octoparse-mcp-setup`](skills/octoparse-mcp-setup/)** | Connects and authorizes the MCP server. Only needed when tools are missing or a call returns 401/403. |

---

## How it works

### Routing follows need, not category

The template library's own tags describe *where data comes from*. `Directories`, `Maps`
and `Search Engine` are source types nobody asks for by name — and 60 of the 103
`Directories` templates are also tagged `Lead Generation`. Meanwhile one real need is
scattered across tags: 44 templates collect review text, but the `Reviews` tag covers only
20 of them.

So the guides are shaped by intent instead, each with a curated shortlist by market, the
account and pricing gates, verified chains, and an explicit **Do not** section.
Misrecommending costs real money, so failure modes get as much space as the happy path.

### Three capabilities, one router

| Capability | Covers | Status |
|---|---|---|
| **Template** | ~670 preset templates | available |
| **Dataset** | typed, filterable datasets — Temu, TikTok Shop | available, expanding |
| **Agent-generated task** | long-tail sites the preset library misses | planned |

The routing slot for the third exists already, marked unavailable. Its tool names are
deliberately unwritten — an agent trusts these files and would call an API that does not
exist yet.

### The execution contract is verified, not inferred

Every rule in `SKILL.md` and `references/gotchas.md` was checked against the live service.
Seven documented behaviours turned out to be wrong, including: local-only templates are
*not* filtered from search results, `templateName` is the slug rather than the display
name, input field names are normalised and match no offline source, and `outputSchema`
under-reports (one template declares 4 fields and returns 18). Written from the API docs
alone, every `execute_task` call would have failed.

---

## Repository layout

```
├── plugin.json / mcp.json              Agent Plugins 1.0.0 manifests
├── .claude-plugin/ + .mcp.json         Claude Code manifests
├── skills/
│   ├── octoparse-ultimate-scraper/
│   │   ├── SKILL.md                    routing + verified execution contract
│   │   ├── references/
│   │   │   ├── gotchas.md              traps, verified against the live service
│   │   │   ├── chaining.md             when one template can feed another
│   │   │   ├── dataset-capability.md   typed datasets (not templates)
│   │   │   └── workflows/              9 need-shaped guides
│   │   └── evals/                      22 behavioural + 27 trigger cases
│   └── octoparse-mcp-setup/
├── data/catalog.json                   routing projection, generated
├── scripts/build_catalog.py            build · validate · candidates
└── templates/                          per-template knowledge packs
```

---

## Contributing

`data/catalog.json` is a **generated** routing projection — id, name, category, language,
execution mode, price. Schemas are deliberately absent: the MCP service is authoritative
for those, and a committed copy would be a stale mirror. Never hand-edit it.

```bash
python3 scripts/build_catalog.py build --snapshot <dir>   # regenerate from upstream
python3 scripts/build_catalog.py validate                 # check curated ids still resolve
python3 scripts/build_catalog.py candidates --need lead-generation --all-languages
```

Curated recommendations carry `<!-- id:NNNN -->` markers keyed on `template_id`.
`validate` re-checks all 313 against a fresh catalog, so a template that is removed, put
into maintenance, or switched to local-only fails the build instead of silently producing
a dead recommendation. Run it after any catalog rebuild or workflow edit.

Every skill change is evaluated against the AI Native standard in [CLAUDE.md](CLAUDE.md).

---

## Support

- [Octoparse documentation](https://www.octoparse.com/docs/en/mcp)
- [Help center](https://helpcenter.octoparse.com)
- [Issues](https://github.com/octoparse/agent-skills/issues) on this repo
- support@octoparse.com

---

## License

[MIT](LICENSE)

<p align="center">
  <sub>Built by the <a href="https://www.octoparse.com">Octoparse</a> team for AI agents everywhere.</sub>
</p>
