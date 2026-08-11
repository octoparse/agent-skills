# The dataset capability

A second, growing capability that sits **beside** the template library rather than inside
it. Data is pre-collected into managed datasets and queried, instead of being scraped per
run by a template.

None of the template rules apply here: no `search_templates`, no `execute_task`, no
`lotNo`, no `export_data`. Three different tools, a different lifecycle, and richer
structured output than the equivalent templates give.

**This capability is expanding.** Temu and TikTok Shop are the platforms available today;
more are planned. Do not treat the platform list as the definition of the capability —
when a request names a platform not listed here, check
`describe_ecommerce_dataset`'s accepted `dataset` values and `ecommerce_data_task`'s
accepted `platform` values before concluding it is unsupported. The live tool schema is
authoritative; this file goes stale first.

## Platforms available today

| Platform | `platform` | Sites |
|---|---|---|
| Temu | `temu` | `uk us es fr de it kr br mx ca au pl` |
| TikTok Shop | `tiktokShop` | US only; do not pass `site` |

Referenced by `competitor-price-monitoring`, `product-market-research`, and
`review-reputation-analysis` — the same three tools serve all three needs.

## Which need maps to which `collectionType`

| Need | `collectionType` | Keyed on |
|---|---|---|
| Price / competitor tracking | `productDetail` | `productIds` |
| Market and category research | `keywordSearch` | `keywords` |
| Review and reputation analysis | `reviews` | `productIds` |

## When to prefer this over a template

Not a fallback. For a platform covered here, the dataset path is usually the better
choice:

- The output is a typed schema with stable column names, not scraped page text.
- It carries fields no template exposes — `rebuy_flag`, `ip_location`, structured
  `image_url_list` / `video_url_list`.
- Querying is filterable and sortable server-side, so you fetch what you need rather than
  exporting everything and filtering afterwards.

Reach for a template only when the platform is not covered by the dataset capability.

## Sequence

**1. Describe the dataset first. This step is not optional.**

    describe_ecommerce_dataset(dataset="temuComment")

Returns the real column list with SQL types, plus two things you cannot guess:

- **`itemIdField`** — the column `itemIds` actually filters on. For `temuComment` it is
  `spu_id`, *not* a generic "product id". It differs per dataset; read it, never assume.
- **`queryHints`** — states the mapping explicitly, e.g.
  `itemIds → spu_id, "Product identifier used to collect result rows."`

`filters[].field` and `orderBy[].field` accept only names from this response. Every field
also carries a `version` stamp (`20260727-01` at time of writing), so schemas do change —
describe at the start of a session rather than caching field names across runs.

Verified shape of `temuComment` — 26 columns, and richer than most review templates:

    comment_text  rating_score  comment_time  publish_time  comment_type
    like_count  parent_comment_id  rebuy_flag  ip_location  sort_name
    image_url_list  video_url_list  product_url  product_sku_attr_json
    user_id  user_nick_name  user_avatar_url  spu_id  comment_id  biz_id
    buy_type_name  trace_id  crawl_time  clean_update_time  etl_updated_time
    sr_updated_time

`image_url_list` and `video_url_list` are `array<varchar>`, not strings. `rebuy_flag`
marks repeat purchasers — a signal no template scraper exposes.

**2. Submit.**

    ecommerce_data_task(
      platform="temu",              # temu | tiktokShop
      collectionType="reviews",     # reviews | productDetail | keywordSearch
      site="us",                    # required for Temu; TikTok Shop defaults to US
      productIds=["..."],
      commentPages=10,
      pollReviews=true
    )

`pollReviews=true` makes the call poll for you — 6 attempts, 5 seconds apart — instead
of hand-rolling a wait loop. Use it unless the job is large.

**3. Query.**

    query_collected_reviews(
      dataset="temuComment",
      itemIds=["..."],
      filters=[{"field": "...", "operator": "gte", "value": "..."}],
      orderBy=[{"field": "...", "direction": "desc"}],
      pageSize=20
    )

`itemIds` filters on whatever `describe_ecommerce_dataset` reported as `itemIdField` —
`spu_id` for `temuComment`, and **keywords** for the `keywordSearch` datasets. Confirm it
from `queryHints` rather than assuming.

## Datasets

    temuComment          temuProductDetail          temuKeywordSearch
    tiktokShopComment    tiktokShopProductDetail    tiktokShopKeywordSearch

Pick the dataset matching both the platform and the `collectionType` you submitted.
Querying `temuComment` after submitting `productDetail` returns nothing.

## Constraints

| Limit | Value |
|---|---|
| `productIds` / `keywords` / `items` | 100 max |
| `commentPages` | 1–50, default 10 |
| `limit` | 1–1000; defaults from `commentPages` for reviews, 100 for `keywordSearch` |
| `filters` | 20 max |
| `orderBy` | 5 max |
| `pageSize` | 1–100, default 20 |

Site codes and platform values are listed under
[Platforms available today](#platforms-available-today) — and are the part of this file
most likely to be out of date. Read them off the live tool schema when a request names a
platform or country not shown there.

## Traps

**Temu `productDetail` keys on `productIds`, not URLs.** URLs are optional. When only
some ids have URLs use `productUrlMappings` (one entry per id); `productUrls` is a legacy
positional mode that requires the two arrays to align by index and to be the same length.
Prefer the mapping form — a misaligned positional array silently attributes data to the
wrong product.

**Submission and retrieval are separate.** `ecommerce_data_task` returns once submitted,
not once collected. Without `pollReviews`, an immediate `query_collected_reviews` returns
empty and that is not an error — wait and query again.

**Korea is a `site` code here, not a template market.** `site="kr"` on Temu is the only
Korean e-commerce coverage outside the Korean template set (Gmarket, SSG, Coupang-adjacent
sites). Worth reaching for when a Korean request has no template.

## Verification status

`describe_ecommerce_dataset` is verified against the live service — the field list and
`itemIdField` above are real output, not inferred.

The submit and query steps are documented from the tool schemas and have **not** been run
end to end. Treat the polling behaviour, the `productUrlMappings` semantics, and the
limits table as accurate-but-untested, and check the first response carefully rather than
assuming it matches. Everything in `gotchas.md`, by contrast, is verified.
