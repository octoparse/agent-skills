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
├── scripts/check_evals.py              eval-set consistency
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
- a curated shortlist with the account tier visible in the row — but **not** the price,
  which the service returns live and which decays the moment it is written down
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

## Known limitations

Standing gaps, not bugs. Worth knowing before trusting an area more than it deserves.

- **Curation rests largely on a snapshot.** 288 templates are recommended; roughly a dozen
  have been checked against the live service. The rest come from a 2026-07-24 export, and
  snapshot and service drift in both directions. `validate` proves an id exists in the
  snapshot, not that the template still runs or that its inputs are unchanged.
- **Account tier and remaining allowance cannot be queried.** Tier comes from the snapshot
  and can be wrong either way. Allowance cannot be read at all, so run sizing is an
  estimate and an exhausted allowance shows up as a partial failure with rows already
  spent. Both are service-side gaps worth closing.
- **Template knowledge packs cover 2 of ~670 templates**, both written in March. Their
  input documentation predates the field-name normalisation and should be re-verified
  before being trusted.
- **Behavioural evals do not run in CI.** `check_evals.py` enforces internal consistency
  only; actual behaviour is a manual pre-release check.

## Skill quality standard

[CLAUDE.md](CLAUDE.md) carries a 20-item AI Native checklist. Use it as a review aid when
writing or reworking a skill — walking it caught two real defects during the restructure,
a missing polling cap and missing client detection, that ordinary review had passed over.

It measures form, not accuracy: nothing in it asks whether documented behaviour matches
the running service. A skill can score full marks while instructing an agent to call an
API that does not work as described. Pair it with the rule above — verify against a live
call before documenting.

Enforcement lives in CI, not in a written assessment. A committed score is a snapshot that
stops being true on the next change and that nobody returns to update.
