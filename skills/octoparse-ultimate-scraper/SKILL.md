---
name: octoparse-ultimate-scraper
description: Universal web data extraction through Octoparse cloud templates. Scrape business listings, leads, contacts, e-commerce products and prices, reviews, job postings, real-estate and travel listings, social media, directories, and search results across Google Maps, Google Search, Amazon, Temu, TikTok Shop, LinkedIn, Indeed, Yellow Pages, Zillow, Booking, and hundreds of regional sites in 8 languages. Use for lead generation, price monitoring, review analysis, competitor tracking, recruitment research, market research, or any request to scrape, crawl, collect, or extract structured data from a website.
---

# Octoparse universal scraper

Data extraction through ~670 preset Octoparse templates, run as cloud tasks via the Octoparse MCP server.

**Division of responsibility — read this before anything else:**

- **This skill routes.** Which template fits, which is the default, which pairs are real chains, what to avoid.
- **The MCP service executes and holds truth about schemas.** Input/output fields, `sourceTree`, and current availability come from `search_templates` at run time, never from memory.
- **`data/catalog.json` is a routing projection only** (id, name, category, language, `run_on`, price). It is regenerated from upstream and carries no schemas.

Never assemble `parameters` from this skill's prose or from a remembered field name. Always read the live `inputSchema` first.

## Prerequisites

Octoparse MCP server connected and authorized. If `search_templates` fails with an auth error, use the `octoparse-mcp-setup` skill.

## Workflow

### Step 1 — Pick the capability

Octoparse exposes distinct capabilities that share no tools. Pick before doing anything
else.

| Request | Capability | Status |
|---|---|---|
| Product details, reviews, or keyword search on a **dataset-covered platform** — today Temu and TikTok Shop | **Dataset** — `references/dataset-capability.md` | available, expanding |
| A site covered by a preset template | **Template** — continue below | available |
| A site no template and no dataset covers | **Agent-generated task** | not yet available |

The dataset capability is expanding beyond those two platforms, and for a platform it
covers it is the better choice, not a fallback — typed schema, server-side filtering, and
fields no template exposes. Check `references/dataset-capability.md` before assuming a
platform is template-only.

**Long-tail sites have no path today.** An agent-generated task capability is planned to
cover sites the preset library does not reach. Until it ships, an uncovered site is a
genuine "no" — say so plainly and stop. Do not improvise by bending a nearby template
onto a site it was not built for: it will either fail or return the wrong page's data,
and it bills either way.

Before concluding a site is uncovered, exhaust the real options: the workflow guide's
curated ids, a semantic search phrased as full intent, and the dataset capability's
current platform list. Semantic recall is uneven, so a thin result set is not proof.

### Step 2 — Route to a workflow guide

Guides are organised by what the user is trying to accomplish, not by the library's
category tags. Read the matching guide before selecting a template — each carries a
curated shortlist, the market coverage, and the traps for that domain.

| The user wants to… | Read `references/workflows/…` |
|---|---|
| find leads, contacts, emails, local business lists | `lead-generation.md` |
| track prices or stock for products they already follow | `competitor-price-monitoring.md` |
| find what exists or what is selling in a category | `product-market-research.md` |
| analyse reviews, ratings, or reputation | `review-reputation-analysis.md` |
| vet companies, find suppliers, check registries | `company-supplier-research.md` |
| research hiring, job postings, or the talent market | `talent-recruitment.md` |
| research property, rentals, hotels, or flights | `property-travel-market.md` |
| monitor social conversation, brand mentions, or news | `social-listening.md` |
| capture search engine results for keywords | `serp-visibility.md` |

Presenting a multi-template workflow? Read `references/chaining.md` first. A chain is
only real when the upstream URL type matches the downstream input type, and the upstream
pass bills whether or not the downstream one accepts its output.

Two boundaries worth knowing, because requests land on them constantly:

- **Price monitoring vs market research** — detail pages vs listing pages. "Watch these
  20 products" is the first; "what sells in this category" is the second.
- **Lead generation vs company research** — a contactable list vs a judgement about a
  company. The same directory site serves both; the difference is which fields matter.

No guide fits, or the guide's shortlist misses the target site — search the full library:

    search_templates(query="<site + data + intent, in one sentence>", limit=10)

Describe the complete intent, not a keyword. `"collect product name price and rating from Amazon Japan search results"` beats `"amazon"`.

**Filter the results yourself on `executionMode`.** It is an array; only templates
containing `"Cloud"` can run through MCP. Local-only templates are returned by both
search modes despite what the API docs claim — roughly a third of a typical result set.
Ranking by `score` alone will hand you a template that cannot run.

Semantic recall is uneven. A narrow query can return a handful of results and miss the
obvious best match, so treat a thin result set as a failed search, not as evidence that
nothing exists — fall back to the workflow guide's curated ids and look them up directly.

### Step 3 — Fetch the live schema

Exact lookup on the chosen template:

    search_templates(id=<template_id>)

This is the authoritative source for everything you need to run the template. Take three
things from it:

- **`templateName`** — `execute_task` is keyed by this, and it is a **slug**
  (`contact-details-scraper`), not the display name. Copy it verbatim, including when it
  is a placeholder string like `aaaaaaaaa`.
- **`inputSchema[].field`** — the exact `parameters` keys. Field names here are
  normalised and do not match any other source; never carry a field name over from
  documentation, memory, or a previous template.
- **`executionMode`** — confirm it contains `"Cloud"`. Exact lookup returns local-only
  templates too.

If exact lookup returns nothing, the template is not currently served by MCP. Say so and stop; do not substitute a different template silently, and do not retry.

**If `templates/<id>-*/` exists for the chosen template, read its `LIMITATIONS.md`.** A
few high-traffic templates carry a knowledge pack with operational behaviour that no
schema exposes — result caps, how the template splits a region, whether one task can span
several locations. Most templates have no pack; skip this step when the directory is
absent.

### Step 4 — Confirm scope, then run

Skip confirmation for small lookups. For anything that produces a list, settle target site/region, result size, and required fields first — templates bill per output line.

    execute_task(
      templateName="<from Step 3>",
      parameters="<JSON object string keyed by inputSchema[].field>",
      taskName="<unique, descriptive>"
    )

`parameters` is a **JSON object encoded as a string**, not an object. Keys are exactly
`inputSchema[].field`. Value shape follows each field's `uiType`:

| `uiType` | Value |
|---|---|
| `Input`, `Dropdown`, `Switch`, `DatetimePicker` | string — a number is still a string: `"1"` |
| `MultiInput`, `CheckboxList`, `MultiSelectDropdown` | string[] — an array even for a single value |

When a field carries `valueFormat: "string[]"`, that settles it regardless of `uiType`.
Unfamiliar and empty `uiType` values do occur; fall back to `valueFormat`, then to `type`.

Always pass a unique `taskName`. The call blocks up to 45 seconds; if the client times out first, the run still exists and `search_tasks(keyword="<taskName>")` is the only way back to its `taskId`.

**Source-backed fields:** when `inputSchema[].sourceBacked` is true, the allowed values
come from `sourceTree` in the Step 3 response. `sourceTree` resolves **every level at
once** — a root option carries its dependent field's options inside `children` — so read
both levels there and pass the option `key` values (not the labels). Doing that avoids
the round-trip entirely.

If a dependent selection is still missing, `execute_task` returns `input_required` plus
the next `sourceOptions`; add the chosen `key` and call again. This is a normal handshake,
not an error.

Returns `taskId`, `lotNo`, `collectedRows`, and `status` (`running` / `completed` / `stopped`). Keep `taskId` **and** `lotNo` — export needs both.

### Step 5 — Poll only if still running

Small jobs finish inside the 45-second window and come back `completed` — skip straight
to export. Poll only when `execute_task` returned `running`:

    get_task_status(taskId="<taskId>")

`collectedRows` defaults to `0`, so it cannot distinguish "running, nothing yet" from "finished, found nothing". Read `status` for that.

Poll at widening intervals. If `status` is still `running` after several minutes, report progress and current `collectedRows` rather than blocking further.

### Step 6 — Export

    export_data(taskId="<taskId>", lotNo="<lotNo>", page=1, pageSize=20)

Paged; `pageSize` maxes at 100. There is no file-format parameter — the tool returns rows.

**At 50+ total rows, do not page through the tool.** The response carries `directAccess` with a short-lived signed link and a ready `curlTemplate` that writes to `directAccess.outputFile`. Run the curl, then read the file. Paging large result sets through the tool floods context for no benefit.

### Step 7 — Report

State: row count, where the data landed, the fields that matter for the user's goal, and the honest limitations from the workflow guide. Suggest the next enrichment step only when the guide documents a real one.

Name output columns from the **exported rows**, not from `outputSchema` — the schema
under-reports. See `references/gotchas.md`.

## Dataset path

Temu and TikTok Shop bypass templates entirely, using a submit-then-query API with three
tools: `describe_ecommerce_dataset`, `ecommerce_data_task`, and `query_collected_reviews`.
None of the template rules above apply.

Read `references/dataset-capability.md` for the sequence, dataset names, limits, and
traps.

## Managing existing work

- `search_tasks(keyword=…, status=…)` — find a prior run; also the recovery path after a client timeout.
- `start_or_stop_task(taskId=…, action="start"|"stop")` — re-run or halt. Rejects if the task is already in the target state.

## Troubleshooting

Read `references/gotchas.md` before the first `execute_task` of a session. It covers billing traps, the templates that already collect detail pages internally, unusable slugs, misleading `language` values, and category noise.
