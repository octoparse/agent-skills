[![skills.sh](https://skills.sh/b/octoparse/agent-skills)](https://skills.sh/octoparse/agent-skills)

<p align="center">
  <img src="assets/logo.png" alt="Octoparse" width="96" height="96">
</p>

<h1 align="center">Octoparse Agent Skills</h1>

<p align="center">
  <strong>Octoparse web scraping skills for coding agents</strong>
</p>

<p align="center">
  <a href="https://www.octoparse.com"><img src="https://img.shields.io/badge/Powered%20by-Octoparse-0055FF?style=for-the-badge" alt="Powered by Octoparse"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-3C4A5C?style=for-the-badge" alt="MIT"></a>
  <a href="#skills"><img src="https://img.shields.io/badge/Templates-670%2B-0040C8?style=for-the-badge" alt="670+ templates"></a>
  <a href="https://agent-plugins.org"><img src="https://img.shields.io/badge/Agent%20Plugins-1.0.0-2E6BE6?style=for-the-badge" alt="Agent Plugins 1.0.0"></a>
  <a href="https://mcp.octoparse.com"><img src="https://img.shields.io/badge/MCP-Compatible-002E8A?style=for-the-badge" alt="MCP compatible"></a>
</p>

<p align="center">
  <a href="#quick-start">Quick start</a> &bull;
  <a href="#skills">Skills</a> &bull;
  <a href="#example-use-cases">Use cases</a> &bull;
  <a href="#installation">Installation</a> &bull;
  <a href="#prerequisites">Prerequisites</a> &bull;
  <a href="#useful-resources">Resources</a> &bull;
  <a href="#pricing">Pricing</a> &bull;
  <a href="#support">Support</a>
</p>

---

## Overview

Install the skills and your agent can operate your Octoparse account: describe the data you
want, and it finds the right template, fills in the inputs, runs it in the cloud, and gives you
back rows. Nothing to write, host, or debug.

- **Template routing from plain language** — *dentists in Chicago with phone numbers*
  resolves to the Google Maps template with the right region and fields; *current prices
  for these 40 ASINs* to the Amazon product template. 670+ maintained templates, and the
  agent reads each one's live input schema before filling it in rather than guessing field
  names.
- **Your own tasks, on call** — whatever you configured in Octoparse is reachable by name.
  Re-run it and export the result without opening the app.
- **Coverage built per market, not translated** — Gelbe Seiten and Das Telefonbuch in
  Germany, Pagesjaunes and Kompass in France, Naver in Korea, Suumo in Japan, MercadoLibre
  across Latin America, alongside the English-language set.
- **Cost known before the run** — collection bills per output line, so the agent sizes the
  job in rows and tells you before it spends anything. A free account includes 2,000 rows a
  month.
- **Cloud runs you can walk away from** — a large collection keeps going after the
  conversation ends. The agent hands back the task id so the results can be exported later.
- **Results where you need them** — a short answer in chat, or the whole set as rows your
  agent can write to CSV or hand to the next tool. Past 50 rows the export arrives as a
  direct download link instead of being paged into the conversation.
- **Chains only when they're real** — the agent links two templates when one genuinely
  feeds the other, and tells you when they don't connect instead of billing you for a pass
  that leads nowhere.

---

## Quick start

```bash
npx skills add octoparse/agent-skills
```

Or, in Claude Code:

```
/plugin marketplace add octoparse/agent-skills
/plugin install octoparse
```

Authorize with `/mcp`, then ask for what you want:

> *Find dentists in Chicago with phone numbers and websites, and export them as CSV.*

From there the agent works out which template fits, what its inputs are actually called,
what the run will cost in rows, and where the results end up.

---

## Skills

| Skill | What it does |
|---|---|
| **[`octoparse-ultimate-scraper`](skills/octoparse-ultimate-scraper/)** | Routes any extraction request to the right template, runs the cloud task, and exports results. Nine workflow guides cover lead generation, competitor pricing, market research, reviews and reputation, supplier vetting, hiring and talent market, property and travel, social listening, and search visibility — each with a curated shortlist by market, cost and account gates, and verified template chains. |
| **[`octoparse-mcp-setup`](skills/octoparse-mcp-setup/)** | Connects and authorizes the MCP server. Only needed when tools are missing or a call returns an authorization error. |

---

## Example use cases

Each of these is a whole job rather than a single call — the agent picks the template, adds
a second pass when one genuinely helps, and tells you what it came back with.

| Use case | Example prompt |
|---|---|
| **Lead generation** | Find dentists in Chicago on Google Maps, then crawl their websites for emails and social links, and export a CSV for my CRM. |
| **Competitor pricing** | Pull the current price, stock, and seller for these 40 Amazon ASINs and put them in a spreadsheet. |
| **Market research** | Show me what's selling in Amazon Best Sellers for wireless earbuds, with the price band across the top 50 listings. |
| **Reputation analysis** | Pull recent reviews for our hotel from TripAdvisor, Booking, and Google Maps, and summarise the top complaint themes. |
| **Social listening** | Collect Reddit and X posts mentioning our brand, plus the comment threads, so I can analyse sentiment. |
| **Local market depth** | Find plumbers in Munich on Gelbe Seiten with phone numbers, or pull Suumo apartment listings in Setagaya with layout and station distance. |
| **Supplier vetting** | Shortlist suppliers on Kompass, then check each one's filings on North Data before I contact them. |

Two things the agent will tell you rather than fake: there is no scheduler, so tracking
change over time means re-running and keeping the results; and a search-results capture is
one observation from one location, not a ranking.

---

## Installation

### Any agent (20+ supported)

```bash
npx skills add octoparse/agent-skills
```

Installs both skills for the agent it detects. Add `--skill octoparse-ultimate-scraper`
for just the scraper, or `--global` to install user-wide. Then register the MCP server:

```bash
claude mcp add --transport http octoparse https://mcp.octoparse.com
```

### Claude Code

```
/plugin marketplace add octoparse/agent-skills
/plugin install octoparse
```

The MCP server is declared by the plugin — no manual configuration. Run `/mcp` to
authorize.

### Cursor, VS Code, Windsurf

These read the Claude Code plugin format. Add the repo to your workspace, or register the
MCP server directly with the command above.

### Agent Plugins clients

The repo ships a root `plugin.json` and `mcp.json` conforming to
[Agent Plugins 1.0.0](https://agent-plugins.org). Clients implementing that specification
discover the skills and the MCP server without further configuration.

### Any other agent that reads Markdown

Point it at `skills/octoparse-ultimate-scraper/SKILL.md` and register
`https://mcp.octoparse.com` as an MCP server.

---

## Prerequisites

1. **Octoparse account** — sign up at [octoparse.com](https://www.octoparse.com). The free
   tier covers most templates.
2. **Authorization** — run `/mcp` for browser OAuth. For headless or CI use, create an API
   key in the [account console](https://www.octoparse.com/console/account-center/api-keys)
   and add it as an `x-api-key` header in your own client configuration.

---

## Useful resources

- **[Octoparse MCP](https://www.octoparse.com/mcp)** — the hosted MCP server these skills
  drive, and its client setup guides.
- **[Template library](https://www.octoparse.com/template)** — browse every template with
  its inputs, outputs, and pricing.
- **[MCP documentation](https://www.octoparse.com/docs/en/mcp)** — tool reference and
  authorization details.
- **[Help center](https://helpcenter.octoparse.com)** — account, plan, and platform
  guidance.
- **[CONTRIBUTING.md](CONTRIBUTING.md)** — repository layout, catalog regeneration, and
  the validation workflow.

---

## Pricing

**A free account includes 2,000 rows per month** through MCP and the API, and it applies
to paid templates too, not just the free ones — enough to evaluate real workloads before
committing to a plan.

Beyond that allowance, templates bill per output line and many remain free. The agent
sizes every run in rows before starting it, so you know what a job will consume before it
runs rather than after.

See [octoparse.com/pricing](https://www.octoparse.com/pricing) for plan details.

---

## Support

- [Octoparse documentation](https://www.octoparse.com/docs/en/mcp)
- [Help center](https://helpcenter.octoparse.com)
- [Issues](https://github.com/octoparse/agent-skills/issues) on this repo
- support@octoparse.com

---

## License

[MIT](LICENSE)

---

<p align="center">
  Maintained by the <a href="https://www.octoparse.com">Octoparse</a> team. Missing a site you need? <a href="https://github.com/octoparse/agent-skills/issues">Open an issue</a>.
</p>

<p align="center">
  <sub>AI agents reading this: start at <a href="skills/octoparse-ultimate-scraper/SKILL.md"><code>skills/octoparse-ultimate-scraper/SKILL.md</code></a> for routing and the execution contract.</sub>
</p>
