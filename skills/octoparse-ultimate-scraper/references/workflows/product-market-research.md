# Product and market research

Finding out what exists and what is selling in a category: listings, search results,
bestseller ranks, assortment, price bands. 87 cloud templates collect e-commerce
**listing** and **search** pages.

If the user already knows which products to watch, that is
`competitor-price-monitoring.md` — the split is listing pages versus detail pages.

Temu and TikTok Shop keyword search uses a separate API; see `../dataset-capability.md`.

`<!-- id:N -->` markers are checked by `scripts/build_catalog.py validate`.

## Step 1 — Discovery mode

| The user asks | Use |
|---|---|
| "what's selling in <category>" | a bestseller / ranking template |
| "what's available for <keyword>" | a keyword search template |
| "everything in <category page>" | a listing template by URL |

Bestseller templates answer demand questions; keyword templates answer assortment and
price-band questions. They are not interchangeable.

## Bestsellers and demand signals

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 2015 <!-- id:2015 --> | Amazon Best Sellers Scraper | global | FREE | free |
| 2008 <!-- id:2008 --> | Amazon Best Sellers Scraper (by Category) | global | FREE | free |
| 2009 <!-- id:2009 --> | Amazon Most Wished For Scraper (by Category) | global | FREE | free |
| 2011 <!-- id:2011 --> | Amazon Most Gifted Scraper (by category) | global | FREE | free |
| 1061 <!-- id:1061 --> | Amazon Kindle Rankings Scraper | Japan | **STANDARD** | free |
| 2035 <!-- id:2035 --> | Hwahae Category Trending Ranking Scraper | Korea | FREE | free |

All free. The Amazon four are the highest-value free templates in the library for demand
research — Best Sellers shows what moves, Most Wished For shows unmet demand.

## Keyword and category search

**Amazon** — mostly per-country, but check the multi-market ones first.

**1153 covers 21 marketplaces** through a `site` picker plus a dependent
`confirm_your_site` field, and it is free. Read its `sourceTree` from
`search_templates(id=1153)` — both levels resolve in that one call, so no
`input_required` round-trip is needed. One template usually replaces the whole country
list below.

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 1153 <!-- id:1153 --> | Amazon Scraper | **21 marketplaces** | FREE | free |
| 1117 <!-- id:1117 --> | Amazon Japan Product Scraper | Japan | **STANDARD** | $0.1/1k |
| 98 <!-- id:98 --> | Amazon Product Scraper | Germany | **STANDARD** | $0.1/1k |
| 112 <!-- id:112 --> | Amazon Product Listing Scraper | Spain | **STANDARD** | free |
| 114 <!-- id:114 --> | Amazon Product Listing Scraper | France | **STANDARD** | free |
| 186 <!-- id:186 --> | Amazon Product Listing Scraper | UK | **STANDARD** | $0.1/1k |
| 109 <!-- id:109 --> | Amazon Product Listing Scraper | India | **STANDARD** | $0.1/1k |

**Marketplaces and retailers by market**

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 1063 <!-- id:1063 --> | eBay Listing Page Scraper (by keyword) | US/EN | FREE | free |
| 1383 <!-- id:1383 --> | eBay Product Listing Scraper | Italy | FREE | free |
| 748 <!-- id:748 --> | eBay Product Listing Scraper | Germany | **STANDARD** | free |
| 804 <!-- id:804 --> | AliExpress Scraper | global | **STANDARD** | $0.06/1k |
| 1855 <!-- id:1855 --> | DHgate Listing Scraper | global | **STANDARD** | free |
| 822 <!-- id:822 --> | Shein Scraper (Product Listing by Keyword) | global | **STANDARD** | $2/1k |
| 1378 <!-- id:1378 --> | Google Shopping Price Monitor (by Keyword) | US/EN | **STANDARD** | free |
| 356 <!-- id:356 --> | Rakuten Product Listing Scraper | Japan | **STANDARD** | free |
| 1294 <!-- id:1294 --> | Yahoo Shopping Scraper | Japan | **STANDARD** | $0.1/1k |
| 101 <!-- id:101 --> | Yahoo Auctions Product Scraper | Japan | FREE | free |
| 1197 <!-- id:1197 --> | Mercari Product Listings Scraper | Japan | **STANDARD** | $0.05/1k |
| 559 <!-- id:559 --> | Buyma Product Listing Scraper | Japan | FREE | free |
| 2134 <!-- id:2134 --> | Monotaro Product Search Results Scraper | Japan | FREE | free |
| 913 <!-- id:913 --> | Otto Scraper (Produkt Liste) | Germany | **STANDARD** | free |
| 750 <!-- id:750 --> | Kleinanzeigen Scraper (Product Listing) | Germany | **STANDARD** | free |
| 1057 <!-- id:1057 --> | REWE Scraper (Lieferung) | Germany | FREE | free |
| 1609 <!-- id:1609 --> | Decathlon.fr Data Scraper | France | FREE | free |
| 2275 <!-- id:2275 --> | ManoMano Produit Listing Scraper | France | FREE | free |
| 1601 <!-- id:1601 --> | Vinted Data Scraper (by keywords) | France | FREE | free |
| 1928 <!-- id:1928 --> | Zalando.fr Product Scraper | France | FREE | free |
| 1477 <!-- id:1477 --> | Leroy Merlin Product Scraper | Italy | **STANDARD** | $0.05/1k |
| 1623 <!-- id:1623 --> | Mercadona Scraper | Spain | FREE | free |
| 1627 <!-- id:1627 --> | Carrefour Spain Listing Scraper | Spain | FREE | free |
| 1537 <!-- id:1537 --> | Wallapop Scraper (by Keywords) | Spain | **STANDARD** | $0.3/1k |
| 2272 <!-- id:2272 --> | MercadoLibre Listing Pages Scraper (by URL) | LatAm | FREE | $1/1k |
| 1104 <!-- id:1104 --> | Falabella Retails Listing Scraper (Keywords) | LatAm | FREE | free |
| 2107 <!-- id:2107 --> | Frávega Product Listing Scraper (Keyword) | Argentina | FREE | free |

**Korea** — the deepest non-Japanese market here, and the only place Korean coverage is
strong. Reach for it confidently.

| id | Template | Acct | Price |
|---|---|---|---|
| 1456 <!-- id:1456 --> | Gmarket Product List Scraper | FREE | free |
| 2180 <!-- id:2180 --> | SSG Product List Scraper | FREE | free |
| 2056 <!-- id:2056 --> | ZIGZAG Product Listing Crawler | FREE | free |
| 2038 <!-- id:2038 --> | 29cm Product Listing Crawler | FREE | free |
| 2074 <!-- id:2074 --> | Kurly product list scraper | FREE | free |
| 2181 <!-- id:2181 --> | Oasis Product List Scraper | FREE | free |
| 2041 <!-- id:2041 --> | WConcept Product Listing Crawler | FREE | free |
| 1478 <!-- id:1478 --> | Ali Express Product List Scraper (Korean) | **STANDARD** | $0.06/1k |

## Listing then detail

Listing output is thin by design — most templates here return 5 to 13 fields, against 20
to 47 for detail templates. Listings carry name, display price, and URL; they omit stock,
seller, variants, specs, and shipping.

The standard two-pass:

    listing template  ──product URLs──▶  detail template (competitor-price-monitoring.md)

Run the listing pass wide, filter to what matters, then run the detail pass narrow.
Running detail across a full listing result is the most common way to overspend here.

## Do not

- Use a listing template when the user needs specs, stock, or seller data. Check the
  field count first — under about 10 fields, it is a listing template.
- Reach for a per-country Amazon template before checking 1153, which is free and covers
  21 marketplaces from a single `site` picker.
- Promise local currency. Verified: a run against amazon.de returned prices in USD,
  because the cloud runner's location drives currency, not the site selection.
- Read bestseller rank as sales volume. Rank is ordinal; no template returns units sold.
- Treat a keyword search as exhaustive. Results are what the site's search returned on
  that run, ranked by the site's own relevance, not a full catalogue.
- Reach for a template for Temu or TikTok Shop — use `../dataset-capability.md`
  with `collectionType="keywordSearch"`.

## Report

Give the user: how many products came back, which fields the listing pass actually
carries, and that a detail pass is needed for anything beyond name and price. Say
explicitly that search results are a ranked slice, not the full assortment.
