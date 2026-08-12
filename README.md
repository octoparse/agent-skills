[![skills.sh](https://skills.sh/b/octoparse/agent-skills)](https://skills.sh/octoparse/agent-skills)

<p align="center">
  <img src="assets/logo.png" alt="Octoparse" width="96" height="96">
</p>

<h1 align="center">Octoparse Agent Skills</h1>

<p align="center">
  <strong>Octoparse web scraping skills for coding agents</strong>
</p>

<p align="center">
  <a href="#skills"><img src="https://img.shields.io/badge/Templates-670%2B-0055FF?style=for-the-badge" alt="670+ templates"></a>
  <a href="https://mcp.octoparse.com"><img src="https://img.shields.io/badge/MCP-Compatible-0055FF?style=for-the-badge" alt="MCP compatible"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-0055FF?style=for-the-badge" alt="MIT"></a>
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

The Octoparse MCP server gives an agent the tools. These skills give it the judgment to use
them well — which of 670+ templates answers a given request, what its inputs are really
called, what the run will cost, and when the honest answer is that nothing covers the site.

- **Routing, not keyword matching** — nine workflow guides map a request to a shortlist
  that fits the market, the budget, and the account tier, then verify the choice against
  the live library.
- **Right inputs on the first call** — the agent reads each template's live schema and its
  dependent option tree before building parameters, instead of carrying a field name over
  from memory or documentation.
- **Cost discipline** — every list-shaped job is sized in rows before it runs, and the
  agent knows which templates already collect detail pages so a second pass is not bought
  twice.
- **Chains that actually connect** — two templates are linked only when the upstream
  output type matches the downstream input, because a failed downstream pass does not
  refund the upstream rows.
- **A straight no** — when no template or dataset covers a site, the agent says so rather
  than bending a nearby template onto it and billing you for the wrong page's data.
- **Your own tasks, in reach** — a task you configured in Octoparse can be found by name,
  run, and exported without opening the app.

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
