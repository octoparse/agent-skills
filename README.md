[![skills.sh](https://skills.sh/b/octoparse/agent-skills)](https://skills.sh/octoparse/agent-skills)

<p align="center">
  <strong>Octoparse Agent Skills</strong>
</p>

<p align="center">
  <strong>Web data extraction for AI agents — hundreds of ready-made templates, no scraper to build</strong>
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
  <a href="#coverage">Coverage</a> &bull;
  <a href="#pricing">Pricing</a> &bull;
  <a href="#support">Support</a>
</p>

---

## Overview

Drop these skills into Claude Code, Cursor, VS Code, Gemini CLI, or any MCP-capable agent
and it gains working hands on the Octoparse platform. With one install, your agent can:

- **Extract from hundreds of sites** — Google Maps, Amazon, LinkedIn, Indeed, Yellow
  Pages, Gelbe Seiten, Pagesjaunes, Naver, Suumo, Booking, Trustpilot, Reddit, TikTok,
  YouTube, and many more, across seven languages.
- **Choose the right template itself** — nine workflow guides turn a plain-language
  request into the best-fitting template for your market, account tier, and budget.
- **Run and export** — creates the cloud task, tracks it to completion, and returns
  structured rows ready for CSV, a CRM, or further analysis.
- **Query managed datasets** — Temu and TikTok Shop ship as typed, filterable datasets
  with richer fields than page scraping provides.
- **Chain templates safely** — knows which templates genuinely feed each other, and which
  already collect detail pages internally so you are not billed twice.

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

The skill picks the template, shapes the input, runs the cloud task, and returns the rows.

---

## Example use cases

Describe the outcome in plain language. The agent selects the template, adds a second pass
when one genuinely helps, and reports what it collected.

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
MCP server directly:

```bash
claude mcp add --transport http octoparse https://mcp.octoparse.com
```

### Agent Plugins clients

The repo ships a root `plugin.json` and `mcp.json` conforming to
[Agent Plugins 1.0.0](https://agent-plugins.org). Clients implementing that specification
discover the skills and the MCP server without further configuration.

### Manually

Point your agent at `skills/octoparse-ultimate-scraper/SKILL.md` and register
`https://mcp.octoparse.com` as an MCP server.

---

## Prerequisites

1. **Octoparse account** — sign up at [octoparse.com](https://www.octoparse.com). The free
   tier covers most templates.
2. **Authorization** — run `/mcp` for browser OAuth. For headless or CI use, create an API
   key in the [account console](https://www.octoparse.com/console/account-center/api-keys)
   and set it as an `x-api-key` header in your client configuration.

---

## Coverage

**Sites** — e-commerce marketplaces, business directories, maps, job boards, property
portals, travel and booking sites, social platforms, review platforms, company registries,
and search engines.

**Languages** — English, Japanese, Spanish, French, German, Italian, and Korean.
Coverage is genuinely local rather than translated: German and French lead business
directories and B2B registries, Japan leads jobs and property, Korea leads e-commerce and
social.

When a site is not covered, the agent says so directly instead of substituting something
that looks similar.

---

## Pricing

Templates bill **per output line**, and many are free. The agent confirms scope before
running anything that produces a list, and tells you the expected cost at your result
size.

Some templates require a paid plan; the agent flags this before running.

See [octoparse.com/pricing](https://www.octoparse.com/pricing) for plan details.

---

## Skills

| Skill | What it does |
|---|---|
| **[`octoparse-ultimate-scraper`](skills/octoparse-ultimate-scraper/)** | Routes any extraction request to the right template, runs the cloud task, and exports results. Nine workflow guides covering leads, price monitoring, market research, reviews, supplier vetting, hiring, property and travel, social listening, and search visibility. |
| **[`octoparse-mcp-setup`](skills/octoparse-mcp-setup/)** | Connects and authorizes the MCP server. Only needed when tools are missing or a call returns an authorization error. |

---

## Contributing

Development notes, catalog regeneration, and the validation workflow are in
[CONTRIBUTING.md](CONTRIBUTING.md).

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
