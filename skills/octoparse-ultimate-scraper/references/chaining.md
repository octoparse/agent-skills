# Chaining templates

Feeding one template's output into another's input. Read before presenting any
multi-template workflow.

Most requests need a chain: discovery finds entities, a second pass enriches them. But
false chains are easy to invent and expensive to run, because the upstream pass bills
whether or not the downstream one accepts its output.

## The rule

A chain is valid only when the upstream template produces the **exact URL type or field
type** the downstream template requires.

Two fields both containing the word `URL`, `link`, `page`, `address`, `contact`, or
`details` proves nothing. Neither does a shared search-style input.

## URL types are not interchangeable

These are distinct types. Treat a mismatch as a broken chain unless the downstream
template's own schema says otherwise.

| Type | Points at | Valid input for | Usually invalid as |
|---|---|---|---|
| **Search result URL** | a search or map results page | `by URL` search-result templates | place detail, website, review |
| **Listing page URL** | many entities (category, marketplace search) | listing-level templates | detail templates, review templates |
| **Place details URL** | one business or place | place detail scrapers; review scrapers that ask for place URLs | business website |
| **Business website URL** | the company's own external site | contact and email enrichment | place detail, marketplace detail |
| **Product listing URL** | a category or search page | listing templates | product detail templates |
| **Product detail URL** | one product | detail templates | listing templates |
| **Review page URL** | a review tab or page | review templates | detail templates |
| **Profile URL** | one account | profile and post templates | search templates |

The most common false chain: taking a **place details URL** and feeding it to a contact
enrichment template that wants a **business website URL**. Google Maps yields both, in
different columns — `Page_URL` is the place, `Website` is the site. Only the second works
with `contact-details-scraper`.

## Match the record granularity too

Beyond URL type, the two templates must agree on what one row means:

    list of businesses  ·  single place  ·  single product  ·  business website  ·  review

A listing template emitting one row per business cannot feed a template expecting one row
per review. Insert the intermediate pass rather than skipping it.

## Verify before promising

Three checks, in order:

1. **Does the upstream actually populate the field?** Several directory templates expose a
   website column that is empty for most rows. A chain that works for 5% of rows is not a
   chain — run a small upstream sample and look.
2. **Read the field name off the exported row, not off a schema.** `outputSchema`
   under-reports and uses different casing than the data. See `gotchas.md`.
3. **Confirm the downstream input type** from `search_templates(id=…)`, specifically the
   field's `label` — it usually states the expected URL type outright ("Google Maps
   Listing Page URLs", "Website URL", "Detail page URLs").

When evidence is thin, say the chain is inferred rather than presenting it as verified.

## Chains that are not chains

**Templates with a built-in detail stage.** 21 templates already run listing → detail
internally against an unpublished worker. Chaining a detail template after one of them
re-collects the same pages and bills twice. The list is in `gotchas.md`.

**Templates that merely share an input shape.** `Google Search Scraper` (15) and
`Google Search Email Finder (Premium)` (2150) both take a search query. That makes them
alternatives, not a pipeline — 15's output does not feed 2150.

**Multi-market templates that look like a fan-out.** `Amazon Scraper` (1153) covers 21
marketplaces through one `site` picker. Running 21 country templates in sequence is not a
chain, it is duplicated work.

## Chains worth knowing

    <anything yielding a website URL>  ──Website──▶  contact-details-scraper (1386)
    listing template                  ──product URL──▶  detail template
    supplier directory  ──▶  registry template  ──▶  1386
    discovery template  ──place URL──▶  reviews template

The first is the most reusable in the library: 1386 is free, takes any website URL, and
attaches to the end of most discovery templates.

Cost order matters. Run the cheap wide pass first, filter, then run the expensive narrow
pass. Stepstone listing is $0.1/1k against $2/1k for detail; Kompass France is $0.05
against $0.15; Idealista Italy is $0.04 against $0.3.
