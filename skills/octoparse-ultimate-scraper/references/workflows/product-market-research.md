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

| id | Template | Market | Acct |
|---|---|---|---|
| 2015 <!-- id:2015 --> | Amazon Best Sellers Scraper | global | FREE |
| 2008 <!-- id:2008 --> | Amazon Best Sellers Scraper (by Category) | global | FREE |
| 2009 <!-- id:2009 --> | Amazon Most Wished For Scraper (by Category) | global | FREE |
| 2011 <!-- id:2011 --> | Amazon Most Gifted Scraper (by category) | global | FREE |
| 1061 <!-- id:1061 --> | Amazon Kindle Rankings Scraper | Japan | **STANDARD** |
| 2035 <!-- id:2035 --> | Hwahae Category Trending Ranking Scraper | Korea | FREE |

All free. The Amazon four are the highest-value free templates in the library for demand
research — Best Sellers shows what moves, Most Wished For shows unmet demand.

## Keyword and category search

**Amazon** — mostly per-country, but check the multi-market ones first.

**1153 covers 21 marketplaces** through a `site` picker plus a dependent
`confirm_your_site` field, and it is free. Read its `sourceTree` from
`search_templates(id=1153)` — both levels resolve in that one call, so no
`input_required` round-trip is needed. One template usually replaces the whole country
list below.

| id | Template | Market | Acct |
|---|---|---|---|
| 1153 <!-- id:1153 --> | Amazon Scraper | **21 marketplaces** | FREE |
| 1117 <!-- id:1117 --> | Amazon Japan Product Scraper | Japan | **STANDARD** |
| 98 <!-- id:98 --> | Amazon Product Scraper | Germany | **STANDARD** |
| 112 <!-- id:112 --> | Amazon Product Listing Scraper | Spain | **STANDARD** |
| 114 <!-- id:114 --> | Amazon Product Listing Scraper | France | **STANDARD** |
| 186 <!-- id:186 --> | Amazon Product Listing Scraper | UK | **STANDARD** |
| 109 <!-- id:109 --> | Amazon Product Listing Scraper | India | **STANDARD** |

**Marketplaces and retailers by market**

| id | Template | Market | Acct |
|---|---|---|---|
| 1063 <!-- id:1063 --> | eBay Listing Page Scraper (by keyword) | US/EN | FREE |
| 1383 <!-- id:1383 --> | eBay Product Listing Scraper | Italy | FREE |
| 748 <!-- id:748 --> | eBay Product Listing Scraper | Germany | **STANDARD** |
| 804 <!-- id:804 --> | AliExpress Scraper | global | **STANDARD** |
| 1855 <!-- id:1855 --> | DHgate Listing Scraper | global | **STANDARD** |
| 822 <!-- id:822 --> | Shein Scraper (Product Listing by Keyword) | global | **STANDARD** |
| 1378 <!-- id:1378 --> | Google Shopping Price Monitor (by Keyword) | US/EN | **STANDARD** |
| 356 <!-- id:356 --> | Rakuten Product Listing Scraper | Japan | **STANDARD** |
| 1294 <!-- id:1294 --> | Yahoo Shopping Scraper | Japan | **STANDARD** |
| 101 <!-- id:101 --> | Yahoo Auctions Product Scraper | Japan | FREE |
| 1197 <!-- id:1197 --> | Mercari Product Listings Scraper | Japan | **STANDARD** |
| 559 <!-- id:559 --> | Buyma Product Listing Scraper | Japan | FREE |
| 2134 <!-- id:2134 --> | Monotaro Product Search Results Scraper | Japan | FREE |
| 913 <!-- id:913 --> | Otto Scraper (Produkt Liste) | Germany | **STANDARD** |
| 750 <!-- id:750 --> | Kleinanzeigen Scraper (Product Listing) | Germany | **STANDARD** |
| 1057 <!-- id:1057 --> | REWE Scraper (Lieferung) | Germany | FREE |
| 1609 <!-- id:1609 --> | Decathlon.fr Data Scraper | France | FREE |
| 2275 <!-- id:2275 --> | ManoMano Produit Listing Scraper | France | FREE |
| 1601 <!-- id:1601 --> | Vinted Data Scraper (by keywords) | France | FREE |
| 1928 <!-- id:1928 --> | Zalando.fr Product Scraper | France | FREE |
| 1477 <!-- id:1477 --> | Leroy Merlin Product Scraper | Italy | **STANDARD** |
| 1623 <!-- id:1623 --> | Mercadona Scraper | Spain | FREE |
| 1627 <!-- id:1627 --> | Carrefour Spain Listing Scraper | Spain | FREE |
| 1537 <!-- id:1537 --> | Wallapop Scraper (by Keywords) | Spain | **STANDARD** |
| 2272 <!-- id:2272 --> | MercadoLibre Listing Pages Scraper (by URL) | LatAm | FREE |
| 1104 <!-- id:1104 --> | Falabella Retails Listing Scraper (Keywords) | LatAm | FREE |
| 2107 <!-- id:2107 --> | Frávega Product Listing Scraper (Keyword) | Argentina | FREE |

**Korea** — the deepest non-Japanese market here, and the only place Korean coverage is
strong. Reach for it confidently.

| id | Template | Acct |
|---|---|---|
| 1456 <!-- id:1456 --> | Gmarket Product List Scraper | FREE |
| 2180 <!-- id:2180 --> | SSG Product List Scraper | FREE |
| 2056 <!-- id:2056 --> | ZIGZAG Product Listing Crawler | FREE |
| 2038 <!-- id:2038 --> | 29cm Product Listing Crawler | FREE |
| 2074 <!-- id:2074 --> | Kurly product list scraper | FREE |
| 2181 <!-- id:2181 --> | Oasis Product List Scraper | FREE |
| 2041 <!-- id:2041 --> | WConcept Product Listing Crawler | FREE |
| 1478 <!-- id:1478 --> | Ali Express Product List Scraper (Korean) | **STANDARD** |

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
