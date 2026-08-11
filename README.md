# Octoparse Agent Skills

[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

Agent skills for driving Octoparse's ~670 cloud templates through the Octoparse MCP
server. An agent picks the right template for what the user actually wants, runs it, and
reports honestly on what came back — including what the library cannot do.

## Install

**As a plugin** (recommended — the MCP server is declared for you):

```
/plugin marketplace add octoparse/agent-skills
/plugin install octoparse
```

The repository ships manifests for both the [Agent Plugins](https://agent-plugins.org)
specification (`plugin.json`, `mcp.json`) and Claude Code
(`.claude-plugin/plugin.json`, `.mcp.json`). `skills/` is shared between them.

**Manually** — copy `skills/` into your assistant's skill directory and register the MCP
server:

```
claude mcp add --transport http octoparse https://mcp.octoparse.com
```

Then run `/mcp` to authorize. An Octoparse account is required.

## Skills

| Skill | Purpose |
|---|---|
| `octoparse-ultimate-scraper` | Routes any extraction request to a template, runs it, exports results |
| `octoparse-mcp-setup` | Connects and authorizes the MCP server |

## How routing works

Workflow guides are organised by **what the user is trying to accomplish**, not by the
library's own category tags. Those tags describe where data comes from — `Directories`,
`Maps` and `Search Engine` are source types nobody asks for by name, and a single need is
often scattered across several of them.

| Need | Guide |
|---|---|
| Leads, contacts, local business lists | `lead-generation.md` |
| Price and stock tracking for known products | `competitor-price-monitoring.md` |
| What exists and what sells in a category | `product-market-research.md` |
| Reviews, ratings, reputation | `review-reputation-analysis.md` |
| Company vetting, suppliers, registries | `company-supplier-research.md` |
| Hiring, job postings, talent market | `talent-recruitment.md` |
| Property, rentals, hotels, flights | `property-travel-market.md` |
| Social conversation, brand mentions, news | `social-listening.md` |
| Search engine results for keywords | `serp-visibility.md` |

Each guide carries a curated shortlist by market, the account and pricing gates, real
template chains, and an explicit "Do not" section — misrecommending costs the user money,
so the failure modes are documented at least as carefully as the happy path.

## Capabilities

Three capabilities sit side by side and share no tools. The skill routes between them in
Step 1 before doing anything else.

| Capability | What it covers | Status |
|---|---|---|
| **Template** | ~670 preset templates across hundreds of sites | available |
| **Dataset** | pre-collected typed datasets — Temu, TikTok Shop | available, expanding |
| **Agent-generated task** | long-tail sites the preset library does not reach | planned |

The routing slot for the third is already in place, marked `not yet available`. When it
ships, the change is one status line plus a reference file — no restructuring.

Deliberately **not** pre-written: its tool names and call sequence. A placeholder
describing an API that does not exist yet would be called, retried, and worked around by
an agent that trusts the file. Contracts get written after they are verified against the
live service, not before.

## Coverage and gaps

Markets: English/global, Japanese, Spanish, French, German, Italian, Korean.

The skills state gaps plainly rather than substituting a near-miss:

- No Instagram or Facebook templates
- No SEO metrics — no backlinks, domain authority, keyword volume, or traffic
- No US Amazon review template (Germany, Italy, France, UK, Japan have one)
- No Korean lead-generation templates; Korea's strength is e-commerce and social
- Glassdoor is Germany only; no job templates for Italy or Korea
- Almost no German property coverage; flights are Check24 Germany only

## Repository layout

```
├── plugin.json / mcp.json              Agent Plugins spec manifests
├── .claude-plugin/ + .mcp.json         Claude Code manifests
├── skills/
│   ├── octoparse-ultimate-scraper/
│   │   ├── SKILL.md                    routing + verified execution contract
│   │   ├── references/
│   │   │   ├── gotchas.md              traps, verified against the live service
│   │   │   ├── chaining.md             when one template can feed another
│   │   │   ├── dataset-capability.md   typed datasets (not templates)
│   │   │   └── workflows/              9 need-shaped guides
│   │   └── evals/
│   └── octoparse-mcp-setup/
├── data/catalog.json                   routing projection, generated
├── scripts/build_catalog.py            build · validate · candidates
└── templates/                          per-template knowledge packs
```

## Maintaining the catalog

`data/catalog.json` is a thin **routing projection** — id, name, category, language,
execution mode, price. Input and output schemas are deliberately absent: the MCP service
is authoritative for those, and a committed copy would be a stale mirror.

```bash
python3 scripts/build_catalog.py build --snapshot <dir>   # regenerate from upstream
python3 scripts/build_catalog.py validate                 # check curated ids still resolve
python3 scripts/build_catalog.py candidates --need lead-generation --all-languages
```

Curated recommendations carry `<!-- id:NNNN -->` markers keyed on `template_id`.
`validate` re-checks all 313 of them against a fresh catalog, so a template that is
removed, put into maintenance, or switched to local-only fails the build instead of
silently producing a dead recommendation. It also catches rows where the displayed id and
the marker have drifted apart.

Run `validate` after any catalog rebuild or workflow edit.

## Contributing

The catalog and its indexes are **generated** — never hand-edit `data/catalog.json`.
Curation lives in the workflow guides and is joined to the catalog by `template_id`.

Every skill change is evaluated against the AI Native standard in [CLAUDE.md](CLAUDE.md).

## License

MIT. See [LICENSE](LICENSE).
