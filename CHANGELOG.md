# Changelog

Claude Code delivers updates only when the manifest `version` changes — pushing commits
without bumping it has no effect, and `/plugin update` will report "already at the latest
version". Every user-visible change therefore needs an entry and a bump.

## 2.2.0 — 2026-08-12

**Action required if you installed 2.1.0 or earlier in Claude Code.** The plugin and the
marketplace were both named `octoparse`, so installing meant typing
`/plugin install octoparse@octoparse`. Remove the old entry and reinstall:

```
/plugin marketplace add octoparse/agent-skills
/plugin install octoparse@octoparse-agent-skills
```

### Changed

- The marketplace is now `octoparse-agent-skills`, and the plugin inside it is `octoparse`.
  One marketplace, one plugin: every official Octoparse capability an agent can use arrives
  through this single install, so nothing has to be discovered or installed twice as more
  skills ship. Nothing about the skills themselves changed.
- `support@octoparse.com` is published in the manifests, so the plugin listing carries a
  way to reach us.
- README: the overview leads with the data an agent can reach, install instructions are
  corrected against the actual CLI syntax, and the free quota is described as a quota
  rather than a tier.

## 2.1.0 — 2026-08-11

Corrections and hardening on top of 2.0.0. **Update if you installed at any point during
the 2.0.0 window**: two of these change the advice the agent gives you.

### Fixed

- **Free allowance is 2,000 rows per month, not per week.** The earlier figure was four
  times too generous, so cost estimates and suggested schedules were wrong. Cadence advice
  is recalculated — most daily schedules do not fit a free account.
- **The agent no longer handles your API key.** It prints instructions and waits; it will
  not accept a key pasted into the conversation, and will not write one to a file, a
  command argument, or an environment variable on your behalf.
- Removed 369 hardcoded prices. Pricing is read live from the service at run time, so
  quotes stay correct across repricing.

### Changed

- Positioned as Octoparse's collection capability rather than a template picker, with
  templates, managed datasets, and planned agent-generated tasks as parallel paths.
- Cost is expressed in rows rather than dollars, since the row allowance is what stops a
  run from completing.
- Seven per-client MCP configuration files collapsed into one, with a diagnosis order that
  resolves most symptoms before any client-specific detail matters.

### Added

- `scripts/check_evals.py` and a CI workflow covering curated references, eval
  consistency, skill frontmatter, manifest version agreement, and internal links.
- Template knowledge packs reconnected, keyed by template id, with the Google Maps
  one-location-per-task constraint now stated in the lead-generation guide.

## 2.0.0 — 2026-08-11

Rebuilt around a single entry-point skill covering the full template library.

### Removed

- `octoparse-lead-generation`, `octoparse-social-media-competitor-monitoring`, and
  `octoparse-link-template`. Their coverage is now inside `octoparse-ultimate-scraper`;
  evals were migrated and the chain-validation rules survive in `references/chaining.md`.

### Added

- `octoparse-ultimate-scraper` with nine workflow guides organised by user need rather
  than by the library's category tags.
- An execution contract verified against the live MCP service. Seven documented behaviours
  turned out not to match it, including local-only templates not being filtered from
  search results and `templateName` being a slug rather than a display name.
- Plugin manifests for both Agent Plugins 1.0.0 and Claude Code, and verified installation
  through skills.sh.

### Changed

- `octoparse-mcp-setup` narrowed from a seven-client configuration matrix to authorization
  and troubleshooting, since the plugin now declares the MCP server itself.
