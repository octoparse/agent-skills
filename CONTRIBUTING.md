# Contributing

Notes for maintainers. User-facing documentation lives in [README.md](README.md).

## Layout

```
├── plugin.json / mcp.json              Agent Plugins 1.0.0 manifests
├── .claude-plugin/ + .mcp.json         Claude Code manifests
├── skills/
│   ├── octoparse-ultimate-scraper/
│   │   ├── SKILL.md                    routing + execution contract
│   │   ├── references/
│   │   │   ├── gotchas.md              execution traps
│   │   │   ├── chaining.md             when one template can feed another
│   │   │   ├── dataset-capability.md   typed datasets (not templates)
│   │   │   └── workflows/              9 need-shaped guides
│   │   └── evals/                      behavioural + trigger cases
│   └── octoparse-mcp-setup/
├── data/catalog.json                   routing projection, generated
├── scripts/build_catalog.py            build · validate · candidates
└── templates/<id>-<slug>/              optional per-template knowledge packs
```

Both plugin manifest sets are maintained: Claude Code does not read the Agent Plugins
paths, and Agent Plugins clients do not read Claude Code's. The paths do not collide and
`skills/` is shared, so the only duplication is version and description metadata — keep
them in sync when bumping a release.

## Generated versus curated

`data/catalog.json` is a **generated routing projection** — id, name, category, language,
execution mode, price. Never hand-edit it.

Input and output schemas are deliberately excluded. The MCP service is authoritative for
those and serves them at run time; a committed copy would drift and mislead. The catalog
exists only to route, and the skills are written to fetch live schemas before building any
call.

Curated judgement — which template is the default for a need, which chains are real, what
to avoid — lives in the workflow guides and joins to the catalog by `template_id`.

```bash
python3 scripts/build_catalog.py build --snapshot <dir>   # regenerate from upstream
python3 scripts/build_catalog.py validate                 # check curated ids still resolve
python3 scripts/build_catalog.py candidates --need lead-generation --all-languages
```

## Validation

Every curated recommendation carries an `<!-- id:NNNN -->` marker. `validate` re-checks
all of them against a fresh catalog and fails when a referenced template is removed, moves
to maintenance status, or becomes local-only — so a stale recommendation surfaces at build
time instead of reaching a user. It also catches rows whose displayed id has drifted from
its marker.

Run it after any catalog rebuild or workflow edit.

```bash
python3 scripts/build_catalog.py validate   # curated ids still resolve
python3 scripts/check_evals.py              # eval sets stay wired to reality
claude plugin validate .                    # Claude Code manifest
```

`.github/workflows/validate.yml` runs the first two on every push and pull request,
plus skill frontmatter, manifest parsing and version agreement across the two plugin
ecosystems, and internal link resolution across the skill tree.

**CI does not run the behavioural evals.** Those need an agent, an authorized MCP
connection, and budget — a row of collected data costs against the account's allowance.
`check_evals.py` instead enforces that the eval set stays honest: no case asserting a
renamed file, a template id that no longer resolves, a single assertion, or a trigger set
without negatives. That is the failure mode worth automating, because an eval set nobody
executes still looks fine in review while quietly asserting against paths that no longer
exist.

Run the behavioural evals manually against a live connection before a release.

## Template knowledge packs

`templates/<id>-<slug>/` holds operational behaviour for a single template that no schema
exposes — result caps, how a location is split internally, whether one task can span
several inputs. `SKILL.md` reads a pack's `LIMITATIONS.md` when one exists for the chosen
template and skips the step otherwise.

Directories are keyed by `template_id` so they join to the catalog the same way curated
recommendations do. Packs are deliberately sparse: write one when a template is a
high-traffic default and its real behaviour keeps surprising people, not as a goal to
cover the library.

## Writing workflow guides

Guides are organised by **what the user is trying to accomplish**, not by the library's
category tags. Tags describe where data comes from, and one need is often spread across
several of them, so routing on tags alone both misses templates and surfaces irrelevant
ones. `NEEDS` in `scripts/build_catalog.py` encodes the mapping used to generate curation
worksheets.

Each guide should carry:

- a first step that narrows by intent, then by market
- a curated shortlist with account tier and per-line price visible in the row
- real chains only — verify the upstream field type matches the downstream input, and
  check the upstream actually populates it
- an explicit **Do not** section
- an honest statement of what is not covered

The **Do not** section is not padding. A wrong recommendation spends the user's money and
returns unusable data, so failure modes deserve at least as much care as the happy path.

## Documenting behaviour

Everything in `SKILL.md` and `references/gotchas.md` is an executable instruction — the
agent will act on it literally. Two consequences:

**Verify before documenting.** Behaviour inferred from API documentation has repeatedly
turned out not to match the service. Check against a live call, and mark anything
unverified as such (see the verification note at the end of `dataset-capability.md`).

**Never document an API that does not exist yet.** Reserve the routing slot for a planned
capability if useful, but leave its tool names and call sequence unwritten. An agent that
trusts a placeholder will call it, retry, and improvise around the failure.

## Skill quality standard

Every skill change is evaluated against the AI Native standard in [CLAUDE.md](CLAUDE.md).
The current assessment is in [docs/ai-native-evaluation.md](docs/ai-native-evaluation.md);
update it when skill behaviour changes.
