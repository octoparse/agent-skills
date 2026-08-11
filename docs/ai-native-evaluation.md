# AI Native Evaluation Report

Required by [CLAUDE.md](../CLAUDE.md). Assesses the repository after the restructure into a
single need-shaped skill with a verified execution contract.

**Date:** 2026-08-11
**Scope:** `octoparse-ultimate-scraper`, `octoparse-mcp-setup`
**Target:** ⭐⭐⭐⭐⭐ (95/100), the bar CLAUDE.md sets for open-source skills

## Modified files

Every file in `skills/` was rewritten or created during this pass. Supporting changes:
`data/catalog.json` (generated), `scripts/build_catalog.py`, `scripts/check_evals.py`,
`.github/workflows/validate.yml`, both plugin manifest sets, `README.md`,
`CONTRIBUTING.md`.

Retired: `octoparse-lead-generation`, `octoparse-social-media-competitor-monitoring`,
`octoparse-link-template`. Their evals were migrated and their chain-validation content
survives in `references/chaining.md`.

## Score

| Dimension | Score | Notes |
|---|---|---|
| Instruction Clarity | 20/20 | Seven numbered steps, each opening on a verb. Conditions are testable, not descriptive: `executionMode` contains `"Cloud"`, `templates/<id>-*/` exists, `status` is `running`, result set ≥ 50 rows. |
| Execution Predictability | 20/20 | Capability table decides the path before anything else; workflow table routes to one guide; `uiType` table determines parameter shape. Success and failure paths are separate, and every failure names an exit. |
| Error Handling Completeness | 20/20 | OAuth retries capped at 3 with an API-key fallback; polling capped at 8 checks with a documented hand-back; `input_required` classified as a handshake rather than an error; timeout recovery through `search_tasks`. |
| Cross-System Compatibility | 20/20 | Two plugin manifest sets that do not collide, seven MCP clients with their wrapper-key differences tabulated, three-tier client detection, and CI asserting version agreement across ecosystems. |
| Efficiency Optimization | 20/20 | One guide loaded per request rather than nine; curl path above 50 rows instead of paging; conditional reads that skip when a path is absent; schemas fetched at run time rather than carried. |
| **Total** | **100/100** | |
| **Rating** | **⭐⭐⭐⭐⭐** | |

Two items failed on first pass and were fixed rather than scored around: polling had no
maximum attempt count, and client detection had been dropped from `octoparse-mcp-setup`
while slimming it. Both are now in place.

## Key improvements

1. **Routing follows user need, not category tags.** The upstream tags describe where data
   comes from — `Directories`, `Maps` and `Search Engine` are source types nobody asks for
   by name, and 60 of the 103 `Directories` templates are also tagged `Lead Generation`.
   Routing on tags both missed templates and surfaced irrelevant ones: 44 templates collect
   review text while the `Reviews` tag covers only 20. Nine intent-shaped guides replace it,
   reaching 288 curated templates against roughly 34 before.

2. **The execution contract is verified, not inferred.** Seven documented behaviours turned
   out to be wrong against the live service, including local-only templates not being
   filtered from search results, `templateName` being a slug rather than a display name, and
   input field names being normalised beyond recognition. Written from the API documentation
   alone, every `execute_task` call would have failed.

3. **Generated data is separated from curated judgement, and the join is enforced.** The
   catalog is a routing projection with no schemas; curation joins by `template_id` through
   markers that CI re-checks, so a removed or downgraded template fails the build instead of
   producing a dead recommendation.

4. **Volatile data was removed rather than validated.** 369 hardcoded prices came out once
   the service was confirmed to return `pricing` live. The comparisons those figures carried
   survive as ratios, which stay true across repricing.

5. **Cost is expressed in the unit that binds.** A free account has 2,000 rows per month
   covering paid templates too, so rows — not dollars — decide whether a job completes.

## Remaining issues

- **Curation rests largely on a snapshot.** 288 templates are recommended; 13 were checked
  against the live service. The rest come from a 2026-07-24 export, and the snapshot and
  service are known to drift in both directions.
- **Account tier and remaining allowance are not queryable.** Tier comes from the snapshot
  and can be wrong either way; allowance cannot be read at all, so sizing is an estimate and
  an exhausted allowance surfaces only as a partial failure with rows already spent. Both
  are service-side gaps worth closing.
- **Behavioural evals are not executed in CI.** They need an agent, an authorized
  connection, and budget. `check_evals.py` enforces internal consistency only.
- **Template knowledge packs cover 2 of ~670 templates**, and both date from March. Their
  input documentation predates the field-name normalisation and should be re-verified.

## Target AI systems

- [x] Claude Code — plugin validated, MCP calls executed end to end
- [x] Cursor — Claude Code plugin format, tool-ceiling caveat documented
- [x] VS Code — `servers` key and settings-nesting difference documented
- [x] Gemini CLI / Qwen Code — trust mode and tool filtering documented
- [x] TRAE / OpenClaw — wrapper key and `mcporter` indirection documented
- [x] Agent Plugins 1.0.0 clients — root manifests conform
- [x] skills.sh (20+ agents) — verified discovering both skills with full descriptions

## On the rubric itself

Two notes for whoever maintains CLAUDE.md.

**The arithmetic is inconsistent.** Dimension weights are 25/25/20/15/15, but each dimension
holds four checklist items at 5 points each, so every dimension is worth 20. Separately,
`Rating = Total / 20` yields 4.5 for a score of 90 while the band table places 81–100 at
five stars. Scoring above uses items × 5 and the band table.

**The rubric has no item for factual accuracy.** Nothing in the checklist asks whether
documented behaviour matches the running system. A skill can score 100 while confidently
instructing an agent to call an API that does not behave as described — which is exactly
the state this repository was in before the contract was verified, and it was the single
largest defect found. Worth adding as a dimension.
