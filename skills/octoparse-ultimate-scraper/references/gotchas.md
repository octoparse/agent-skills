# Gotchas

Traps that are not visible from a template's name, its description, or the MCP tool
descriptions. Read before the first `execute_task` of a session.

## Execution contract

### `templateName` is a slug, and it is not the display name

Everything else in this skill routes by `template_id`, but `execute_task` takes
`templateName` — which is the template's **slug**, not its title:

| id | `templateName` (pass this) | `displayName` (never pass this) |
|---|---|---|
| 1386 | `contact-details-scraper` | Contact Details Scraper |
| 1576 | `google-maps-contact-scraper` | Google Maps Email Finder |
| 1853 | `google-maps-email-finder-by-urls` | Google Maps Email Finder (by URLs) |
| 2006 | `aaaaaaaaa` | LinkedIn Company Profile Scraper |

Take it from `search_templates(id=…)` and copy it verbatim — **including when it is a
placeholder string** like `aaaaaaaaa`. That is the real key for those templates.

`displayName` also drifts from the title in any offline listing: template 1737 is
"Expedia Japan Flight Scraper" in the snapshot and "[JP]Expedia Flight Scraper" live.
Never match templates by name across sources; match by id.

### Field names are normalised — offline names are worthless

The live `inputSchema[].field` values are generated from the field labels and match no
other source. For template 1386:

| Offline / documentation | Live `field` |
|---|---|
| `MainKeys` | `website_URL` |
| `Depth` | `maximum_Crawl_Depth` |
| `Total_num` | `maximum_Pages_per_URL` |
| `Lock_domain` | `restrict_to_Same_Domain` |

Not one matches. Always build `parameters` from a fresh `search_templates(id=…)`, never
from a remembered field name, a workflow guide, or a previous run of a similar template.

### `parameters` is a string, not an object

    parameters="{\"keywords\":[\"wireless earbuds\"],\"number_of_Pages_to_Scrape\":\"1\"}"

A JSON object encoded as a string. Keys are exactly `inputSchema[].field`. Value shape
follows `uiType`, and the distinction is load-bearing:

| `uiType` | Value | Note |
|---|---|---|
| `Input`, `Dropdown`, `Switch`, `DatetimePicker` | string | a number is still a string: `"1"` |
| `MultiInput`, `CheckboxList`, `MultiSelectDropdown` | string[] | an array **even for a single value** |

`uiType` is not a closed set — empty strings and unfamiliar values appear. When a field
carries `valueFormat: "string[]"` that settles the shape regardless of `uiType`; failing
that, fall back to `type`.

Passing a bare string where the schema wants `string[]` is the most common preflight
rejection.

### `input_required` is a handshake, not a failure

Templates with source-backed fields (site pickers, region pickers, category trees)
resolve in stages. `execute_task` returns `input_required` plus the next
`sourceOptions`; add the chosen option `key` to `parameters` and call again. Repeat
until it runs. Do not treat the first `input_required` as an error and switch
templates.

For the root level, read `sourceTree` from `search_templates(id=…)` and pass option
`key` values — not the display labels.

### A timeout does not mean the task did not run

`execute_task` blocks up to 45 seconds. If the client gives up first, the cloud task is
already created and consuming quota. The returned `taskId` is lost.

This is why `taskName` must always be set and always be unique: `search_tasks(keyword="<taskName>")`
is the only way back. Without it you cannot poll, cannot export, and cannot stop the
run — but it still bills. Never fire a second `execute_task` for the same intent after
a timeout; search first.

### `export_data` needs `lotNo`, not just `taskId`

Both are returned by `execute_task` and by `get_task_status`. A `taskId` alone cannot
export.

### `collectedRows: 0` is ambiguous

It defaults to `0`, so it means either "running, nothing yet" or "finished, found
nothing". Only `status` separates them. Never report "no results" off `collectedRows`
while `status` is `running`.

### Export 50+ rows via curl, not paging

At 50 or more rows the `export_data` response carries `directAccess` with a signed link
and a prebuilt `curlTemplate` that writes to `directAccess.outputFile`. Run the curl and
read the file. Paging 500 rows through the tool at `pageSize=100` is five large tool
responses in context to reach the same data that one curl puts on disk.

The signed link is short-lived. Fetch promptly or re-request it.

## Billing

Every template bills **per output line** (`PAY_PER_LINE`), not per task or per hour.
Many are free; the rest span roughly two orders of magnitude. `search_templates` returns
the current `pricing` string for each — quote that, never a remembered figure.

### A free account is not limited to free templates

MCP and API usage on a free account carries an allowance of **2,000 rows per month**. Paid
templates run against it like any other, so "this template is billed" is not a reason to
steer a free-tier user away — it is a reason to size the run.

This makes rows, not dollars, the binding constraint for most users, and 2,000 a month is
tight: a single broad listing pass can consume a quarter of it. Frame every estimate that
way — "this will use about 400 of your 2,000 monthly rows" is more useful than a price
quote, and it is the number that actually stops a run from completing.

**You cannot check the remaining allowance.** No tool reports quota — there is no account
endpoint in the current tool set. So:

- Treat the monthly figure as a budget the user tracks, not one you can verify.
- Size proactively rather than probing. A run that exhausts the allowance fails partway
  and the rows already collected are still spent.
- When a run stops unexpectedly on a free account and the inputs were valid, an exhausted
  allowance is the first thing to raise.

Two habits follow. A wide listing pass followed by a narrow detail pass conserves the
allowance as well as money. And a recurring job — re-running through
`start_or_stop_task` — draws on it every time, which rules out most daily cadences on a
free account: 100 rows a day is 3,000 a month, already over.

On a free account, propose a cadence the allowance can actually sustain, or say plainly
that the schedule needs a paid plan.

### Other consequences

- Confirm result size before running anything list-shaped. A template that "tries to
  collect all available results" with no cap can produce far more lines than intended.
- A failed downstream step does not refund upstream lines. Validate a chain on a small
  run first.
- There is no dry-run. The old docs mention `validateOnly` and `targetMaxRows`; neither
  parameter exists. Preflight validates inputs automatically but does not simulate a run.
- Re-running via `start_or_stop_task(action="start")` bills again.

### Three separate limits, only one of them live

They are independent, and confusing them produces bad advice:

| Limit | Means | Source |
|---|---|---|
| **Price** | cost per output line | live, `pricing` from `search_templates` |
| **Allowance** | 2,000 rows/month on a free account | not queryable — estimate |
| **Account tier** | whether the template runs at all | offline snapshot only |

`pricing` is live, so quote it. Workflow guides describe cost only in relative terms
("detail costs roughly twenty times listing") so they stay correct across repricing.

The **account tier has no field in the service response**. It comes from the snapshot and
can be wrong in both directions — a template marked `FREE` may still fail on entitlement,
and a `STANDARD` marking may since have been relaxed. Raise it as a caution, then act on
whatever the run actually does.

A `STANDARD` template fails for a free account **regardless of remaining allowance** — the
tier gate is not a quota. `Google Maps Scraper` (1577), `Kompass Leads Scraper` (1053) and
`Yellow Pages Philippines Scraper` (1447) all sit behind it, and 1447 is free per line, so
price reveals nothing about the gate. Per the snapshot, 479 templates are `FREE` and 193
are `STANDARD`.

## Templates that already collect detail pages

21 templates run a listing → detail pass internally, against a worker template that is
**not published in the library**. Chaining a detail-page template after one of these
re-collects the same rows and bills for both passes.

    103   Mynavi Job Scraper
    249   Ekiten Store Listing Scraper
    263   Twitter Scraper (by Account URL)
    288   Twitter Advanced Search Scraper
    560   Hot Pepper Beauty Scraper | Hair Salon
    1107  🔥 Indeed Job Scraper
    1576  Google Maps Email Finder
    1577  Google Maps Scraper
    1689  いい部屋ネット 物件情報
    1838  Twitter Advanced Search Comments Scraper
    1842  Tabelog Store list and details Scraper
    1859  Google Maps Listing and Details Page Scraper (Cloud)
    1865  Google Maps advanced Scraper for Japan
    1868  SUUMO Rental Property Scraper
    1875  Superpages Details Page Scraper (Cloud)
    1945  🔥 Indeed Job Scraper (by URL)
    1955  Pagesjaunes Emails Scraper
    2001  JP Indeed Job Scraper by URL (cloud only)
    2124  Google News Scraper (Cloud)
    2150  Google Search Email Finder (Premium)
    2202  Doda Job Detail Scraper

Contact **enrichment** after one of these is still legitimate — `Google Maps Scraper`
(1577) yields `Website` but no email, so feeding websites into `Contact Details Scraper`
(1386) adds real data. What is wasteful is re-collecting the *same* page type.

### `FollowField` in output is internal

It is the handoff slot for that internal second stage and is null or meaningless to the
user. Drop it from reports and from any schema shown to the user.

## Catalog data quality

### 13 templates have unusable slugs

Their titles are legitimate; only the slug is a placeholder. `search_templates(slug=…)`
cannot find them. **Look them up by `id`.**

    1542  ffffff        🔥 LinkedIn Job Scraper
    1626  eeeeeee       LinkedIn Job Details Page Scraper
    1737  1737          Expedia Japan Flight Scraper            (LOCAL)
    1746  dddddddd      LinkedIn Job Scraper                    (LOCAL)
    1749  1749          Stanby Jobs Scraper
    1753  1753          CHINTAI Real Estate Listing Scraper
    1764  1764          エン派遣 Recruitment Information          (LOCAL)
    1768  1768          Hanmoto Book Infomation Scraper
    1773  cccccc        LinkedIn Posts Scraper                  (LOCAL)
    1776  1776          KyujinBox Jobs Infomation
    1784  bbbbbbbbbbbb  LinkedIn Español Empleo Scraper         (LOCAL)
    1852  1852          AutoReserve Restaurant Listing Scraper  (LOCAL)
    2006  aaaaaaaaa     LinkedIn Company Profile Scraper

This is also why every curation file in this skill keys on `template_id`.

### `language` is the interface language, not the target country

It says which locale the template was published for, not which country's site it
scrapes. The gap is wide enough to pick the wrong template:

| id | `language` | actually scrapes |
|---|---|---|
| 1392 | `EN_US` | Eniro — Sweden |
| 1453 | `EN_US` | Fonecta — Finland |
| 1457 | `EN_US` | Krak — Denmark |
| 1458 | `EN_US` | Gulesider — Norway |
| 1454 | `EN_US` | Goudengids — Netherlands |
| 1976 | `IT_IT` | Local.ch — Switzerland |
| 2261 | `FR_FR` | Local.ch — Switzerland |

Read the target country off the **site name**, not the language field. `GLOBAL` is the
only value that reliably means multi-country.

### Categories overlap and carry noise

120 templates sit in two categories, and the second is often a stretch. Inside
`Lead Generation` you will find `Zillow Details Scraper` (1763, real estate),
`Idealo Price Comparison Scraper` (876), and `AutoScout24 Spain Scraper` (1647) —
none of which are lead-generation tools. Do not recommend a template because a category
tag matched; check that its output actually answers the request.

### 47 templates are in `MAINTENANCE`

Concentrated in E-Commerce (19), with the rest spread across Real Estate, Jobs,
Directories, Lead Generation, and Travel. They may fail or return partial data. Prefer a
`PUBLISHED` alternative; if a `MAINTENANCE` template is genuinely the only fit, say so
before running it.

## Coverage

### Local-only templates ARE returned — you must filter them out yourself

This is the correction that matters most. The API documentation states that
`search_templates` returns "cloud-capable templates only". **It does not.** A semantic
query for Amazon Germany returns 20 templates of which 6 are `executionMode: ["Local"]`,
and exact lookup returns them too (template 1737 resolves fine and is local-only).

`executionMode` is an **array**. A template is runnable through MCP only if it contains
`"Cloud"`:

    ["Cloud"]           runnable
    ["Cloud", "Local"]  runnable
    ["Local"]           NOT runnable -- desktop client only

Check it on every candidate before `execute_task`. Ranking on `score` alone will hand
you a template that cannot run, and the failure surfaces late.

When the only template for a site is local-only, the useful answer is "this exists but
only runs in the Octoparse desktop client", not "no template found".

### Semantic search recall is uneven

A narrow query can return very few results and miss the obvious best match: querying for
"extract email addresses and phone numbers from a company website" returns 3 templates
and **does not include `Contact Details Scraper` (1386)** — the exact match, which
resolves instantly by id.

Treat a thin result set as a failed search, not as proof that nothing exists. Fall back
to the curated ids in the workflow guide and look those up directly.

### The catalog and the MCP service drift in both directions

`data/catalog.json` is built from an upstream snapshot; the service is fed separately.
Neither is a superset of the other:

- A template in the catalog can be missing from the service.
- The service carries templates newer than the snapshot — `amazon-search-scraper` (2280)
  is live but absent from a catalog whose highest id is 2275.

So the catalog is a routing aid, never an availability guarantee, and never a reason to
stop searching. When `search_templates(id=…)` returns nothing, tell the user that
template is not currently callable through MCP and stop — do not retry and do not
silently substitute. When a semantic result carries an id the catalog does not know,
trust the service: it is newer.

### Other fields that differ from any offline copy

- `pricing` reads `"$0.3 / 1,000 rows"` live versus `"$0.3/1,000 lines"` offline.
- For the built-in two-stage templates, the live `outputSchema` is the **merged** schema
  and is far better than the offline one. Template 1576 shows one field offline and 56 live.

### `outputSchema` under-reports what a run actually returns

Verified against a real run of `contact-details-scraper` (1386). Its live `outputSchema`
lists **4** fields — `email`, `phone`, `social_media_links`, `contact_details`. The run
returned **18**:

    start_URL  domain  depth  referrer_URL  current_URL  emails  phones
    uncertain_Phones  twitter  youTube  facebook  linkedIn  instagram  tiktok
    pinterest  snapchat  threads  telegram  github  errorMassage

None of the four advertised names appear verbatim in the data. `outputSchema` is also
frequently `null` in search results, and its absence says nothing at all.

Treat `outputSchema` as a hint about *what kind* of data comes back, never as the field
list. The authoritative field set is the first row of `export_data`. Do not promise the
user specific output column names before a run — describe the data, then confirm the
columns from the export.

### Output field names are normalised too, in a different style from input

Input fields come back as `website_URL`, `maximum_Crawl_Depth`. Output fields come back
camel-cased from the underlying names: `start_URL`, `uncertain_Phones`, `youTube`,
`linkedIn`, `errorMassage` — where any offline copy has `Start_URL`, `Uncertain_Phones`,
`YouTube`, `LinkedIn`, `ErrorMassage`.

This matters when chaining: the upstream field you feed into a downstream template must
be read off the actual exported row, not off a schema or an offline listing. And note
`errorMassage` is misspelled in the product — match it exactly.

### Selecting a country site does not guarantee that country's currency

Verified: running `amazon-product-scraper-by-keywords` with `site: "Germany (Deutschland)"`
and `confirm_your_site: ["https://www.amazon.de/"]` returned prices as **`USD 33.97`**,
with `delivery_raw` reading "Delivers to United States".

The template hit amazon.de, but the cloud runner's own location drove currency and
shipping. Site selection controls **which marketplace** is scraped, not **which locale**
the page renders in.

So do not promise locale-correct pricing from a country template. If the user needs local
currency, check whether the template exposes a postal-code or zip field — several do
(`98` for Germany, `97` for the US, `1155`, `1337`) — and set it. Otherwise state that
prices come back in the runner's currency and may need conversion.

### Some templates return a junk field that floods context

The Amazon scraper returns `current_progress` containing a raw HTML fragment padded with
hundreds of newlines and spaces — in the verified run, one field held more characters
than the other twenty-four combined.

Drop obvious junk columns before showing rows to the user or feeding them anywhere. The
useful signal in that particular field ("1-16 of 362 results") is worth extracting; the
markup around it is not. `FollowField` and `errorMassage` are similarly noise in most runs.

### `directAccess` appears at 50 rows, and 48 is not 50

Verified: a 48-row export returned no `directAccess` block. The threshold is real and
exact. Do not write logic that assumes the curl path is always available — check for the
block, and page through the tool when it is absent.

### Small runs complete synchronously

`execute_task` returned `status: "completed"` with `collectedRows: 1` inside its 45-second
window; no polling was needed. Call `get_task_status` only when `execute_task` comes back
`running`. For a one-row job it returns exactly the same object.

`export_data` at 1 row carried no `directAccess` block — that appears at 50+ rows, as
documented. Do not depend on it being present for small result sets.
