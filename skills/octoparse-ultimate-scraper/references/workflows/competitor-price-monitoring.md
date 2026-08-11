# Competitor and price monitoring

Watching products the user already tracks: price, stock, ratings, seller. 50 cloud
templates collect e-commerce **detail** pages.

If the user instead wants to discover what is selling in a category, that is
`product-market-research.md` — the split is detail pages versus listing pages.

Temu and TikTok Shop use a separate API; see `../dataset-capability.md`.

`<!-- id:N -->` markers are checked by `scripts/build_catalog.py validate`.

## Step 1 — Establish the input key

Detail templates need product identity, and the accepted form differs. Ask which the
user has before choosing:

| They have | Look for |
|---|---|
| ASINs | an "ASIN" template — 355 (JP), 99 (DE) |
| product URLs | a "by URL" template — most detail templates |
| search keywords | a keyword-driven detail template — 1931 (eBay), or route via listing first |

If they have only a category or a brand, run a listing template from
`product-market-research.md` first, then feed its product URLs into a detail template.

## Step 2 — Match the marketplace

Amazon is the deepest family and is **per-country, not global** — a template for one
Amazon domain will not scrape another.

| id | Template | Market | Acct | Fields |
|---|---|---|---|---|
| 2218 <!-- id:2218 --> | Amazon Details Scraper | global | **STANDARD** | 47 |
| 97 <!-- id:97 --> | Amazon Product Scraper (US) | US | **STANDARD** | 31 |
| 201 <!-- id:201 --> | Amazon Japan Product Details Scraper | Japan | FREE | 29 |
| 355 <!-- id:355 --> | Amazon Japan Product Scraper by Asin | Japan | **STANDARD** | 21 |
| 99 <!-- id:99 --> | Amazon Details ASIN Scraper | Germany | **STANDARD** | 20 |
| 113 <!-- id:113 --> | Amazon Product Details Scraper | Spain | **STANDARD** | 20 |
| 117 <!-- id:117 --> | Amazon Product Details Scraper | France | FREE | 18 |
| 444 <!-- id:444 --> | Amazon Product Detail Scraper | Mexico | **STANDARD** | 16 |
| 1153 <!-- id:1153 --> | Amazon Scraper | US/EN | FREE | 25 |

**2218 is the default when the country is not fixed** — it spans 22 marketplaces from one
template. Reach for a country template when the user needs fields that only the local
storefront exposes.

**A country template does not guarantee local currency.** Verified: scraping amazon.de
returned prices in USD, because the cloud runner's location drives currency and shipping,
not the site selection. If local currency matters, use a template with a postal-code or
zip field (99 for Germany, 97 for the US) and set it. Otherwise tell the user prices may
need conversion.

The ASIN variants (355, 99) are the cheapest per line. Prefer them whenever the user
already has ASINs.

**Other marketplaces**

| id | Template | Market | Acct |
|---|---|---|---|
| 933 <!-- id:933 --> | eBay Product Scraper (US) | US | FREE |
| 204 <!-- id:204 --> | eBay UK Product Scraper | UK | FREE |
| 749 <!-- id:749 --> | eBay Product Details Scraper | Germany | **STANDARD** |
| 761 <!-- id:761 --> | eBay Produits Détails Scraper | France | FREE |
| 1377 <!-- id:1377 --> | Google Shopping Price Monitor (by URL) | US/EN | **STANDARD** |
| 1410 <!-- id:1410 --> | Google Shopping Product Scraper | US/EN | **STANDARD** |
| 1058 <!-- id:1058 --> | Target Product Details Scraper | US | FREE |
| 1077 <!-- id:1077 --> | Costco Product Details Scraper | US | FREE |
| 315 <!-- id:315 --> | Etsy Scraper | global | **STANDARD** |
| 804 <!-- id:804 --> | AliExpress Scraper | global | **STANDARD** |
| 1618 <!-- id:1618 --> | Otto Scraper (Produkt Details) | Germany | **STANDARD** |
| 751 <!-- id:751 --> | Kleinanzeigen Scraper (Product Details) | Germany | **STANDARD** |
| 1094 <!-- id:1094 --> | Rossmann Online Data Scraper | Germany | FREE |
| 1404 <!-- id:1404 --> | Mercari Product Details (Cloud Only) | Japan | **STANDARD** |
| 632 <!-- id:632 --> | Mercari Product Details Scraping by URL | Japan | FREE |
| 1109 <!-- id:1109 --> | Falabella Retail Details Scraper | LatAm | FREE |
| 1709 <!-- id:1709 --> | Home Depot México Details Scraper | Mexico | FREE |
| 1621 <!-- id:1621 --> | AutoScout24 Scraper | Italy | FREE |
| 2274 <!-- id:2274 --> | ManoMano Produit Details Scraper | France | FREE |
| 1556 <!-- id:1556 --> | Leboncoin Data Scraper | France | FREE |
| 1952 <!-- id:1952 --> | Vinted Advanced Scraper (by URL) | France | **STANDARD** |
| 2093 <!-- id:2093 --> | Auction Product Info Scraper | Korea | FREE |
| 2148 <!-- id:2148 --> | Gmarket product information scraper | Korea | FREE |

Korea's e-commerce coverage is the strongest part of its template set — 13 templates,
against zero for lead generation. Reach for it confidently here.

## Step 3 — Repeat runs

There is no scheduler in this toolset. Monitoring over time means re-running:

    start_or_stop_task(taskId="<taskId>", action="start")

This bills again at full rate and draws on the monthly row allowance again. Say so before
setting up a cadence: 500 products collected daily is 15,000 rows a month against an
allowance of 2,000, and even a single 500-row pass spends a quarter of it. On a free
account a weekly cadence over a small set is realistic; a daily one is not. Size against
rows first, price second.

Re-running loses nothing: each run creates a new `lotNo`, and `search_tasks` finds prior
runs by `taskName`. Use a stable, descriptive `taskName` so the history stays readable.

## Do not

- Assume every Amazon template is single-country. The older ones are, but 2218 and
  2280 span 22 marketplaces and 1153 covers 21 via a `site` picker. Check `sourceTree`
  before duplicating work across country templates.
- Promise local currency from a country template. Verified: amazon.de returned USD.
- Use a listing template to monitor price. Listing pages carry a display price but omit
  stock, seller, variant, and shipping fields.
- Promise price history. Every template returns the price at collection time; history
  only exists if the user re-runs and stores the results themselves.
- Reach for a template for Temu or TikTok Shop. They are not in the template library —
  use `../dataset-capability.md`.
- Ignore the STANDARD gate on 2218, 97, 355, 99, 113, 1377, 1410, 315, and 804. Several
  are free per line, so the gate is invisible from the price column.

## Report

Give the user: the template, the input key it needs (ASIN / URL / keyword), the fields
returned, the per-run cost at their result size, and the fact that repeat monitoring is
manual re-running rather than a schedule.
