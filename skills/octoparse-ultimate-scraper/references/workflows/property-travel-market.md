# Property and travel market

72 cloud templates covering real-estate listings and travel inventory — rentals, sales,
hotels, flights. Grouped together because both are listing markets: the user wants
prices, inventory, and availability for a place.

`<!-- id:N -->` markers are checked by `scripts/build_catalog.py validate`.

## Step 1 — Which market

| The user wants | Section |
|---|---|
| homes or land to buy | [Property for sale](#property-for-sale) |
| rentals | [Rentals](#rentals) |
| hotel rates or availability | [Hotels](#hotels) |
| short-term rentals | [Short-term rentals](#short-term-rentals) |
| flights | [Flights](#flights) |

Japan, France, Spain, and Italy carry the deepest property coverage. German property is
not covered here — German strength sits in directories and B2B registries, see
`lead-generation.md` and `company-supplier-research.md`.

## Property for sale

| id | Template | Market | Acct | Price | Fields |
|---|---|---|---|---|---|
| 1200 <!-- id:1200 --> | Suumo Used Apartment Detail Scraper | Japan | FREE | free | 34 |
| 40 <!-- id:40 --> | Suumo Detached House Details Scraper | Japan | FREE | free | 30 |
| 1731 <!-- id:1731 --> | Homes Detached House detail pages Scraper | Japan | FREE | free | 28 |
| 1987 <!-- id:1987 --> | Suumo Land Listings Scraper | Japan | FREE | free | 14 |
| 431 <!-- id:431 --> | Idealista Details Scraper | Spain | **STANDARD** | $0.2/1k | 20 |
| 1376 <!-- id:1376 --> | Idealista Real Estate Listing Scraper | Italy | **STANDARD** | $0.04/1k | 15 |
| 1379 <!-- id:1379 --> | Idealista Real Estate Detail Scraper | Italy | **STANDARD** | $0.3/1k | 15 |
| 1628 <!-- id:1628 --> | Trovacasa Scraper | Italy | FREE | free | 16 |
| 1574 <!-- id:1574 --> | Seloger biens à vendre Scraper | France | **STANDARD** | $0.8/1k | 17 |
| 2239 <!-- id:2239 --> | Leboncoin Immobilier Infos Scraper | France | FREE | $1.5/1k | 16 |
| 369 <!-- id:369 --> | Lamudi Post Details Scraper | LatAm | FREE | free | 15 |
| 385 <!-- id:385 --> | Metros Cúbicos Details Scraper | Mexico | FREE | free | 14 |
| 421 <!-- id:421 --> | Vivanuncios Post Details Scraper | Spain/MX | FREE | free | 16 |
| 1763 <!-- id:1763 --> | Zillow Details Scraper | US | FREE | $1/1k | 14 |
| 1559 <!-- id:1559 --> | Zillow Listing Scraper (by keyword) | US | FREE | free | — |
| 2156 <!-- id:2156 --> | Zillow Profile Scraper | US | **STANDARD** | $1/1k | 19 |

**Japan's Suumo family is the richest property data in the library** — 34 fields on used
apartments, including the structured attributes (age, layout, station distance) that
Japanese listings carry and Western sites do not.

Idealista Italy splits listing at $0.04/1k from detail at $0.3/1k. Run listing wide,
detail narrow.

2156 Zillow Profile is **agents**, not properties — it belongs to lead generation. Use
1763 or 1559 for property data.

## Rentals

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 1753 <!-- id:1753 --> | CHINTAI Real Estate Listing Scraper | Japan | FREE | free |
| 808 <!-- id:808 --> | Apamanshop Rental Listings Scraper | Japan | FREE | free |

Rental coverage is Japan-only. For other markets, the for-sale templates above often
carry rentals too if the user supplies rental listing URLs — check the template's input
schema before promising it.

1753 has an unusable slug (`1753`) — look it up by id.

## Hotels

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 1550 <!-- id:1550 --> | Google Hotel Scraper | global | FREE | free |
| 1705 <!-- id:1705 --> | Google Hotel Scraper (by URLs) | global | FREE | free |
| 205 <!-- id:205 --> | Trip.com Scraper | global | **STANDARD** | free |
| 1037 <!-- id:1037 --> | Booking.com Hotel Details Scraper | Germany | FREE | free |
| 1035 <!-- id:1035 --> | Booking Hotel Listing Scraper | Germany | FREE | free |
| 927 <!-- id:927 --> | Booking Hôtel Info Scraper | France | FREE | $0.3/1k |
| 1692 <!-- id:1692 --> | Booking Details Scraper for Spanish | Spain | FREE | free |
| 1691 <!-- id:1691 --> | Hoteles Details Scraper | Spain | **STANDARD** | $2/1k |
| 1310 <!-- id:1310 --> | Jalan Hotel Listings Scraper | Japan | FREE | free |
| 1279 <!-- id:1279 --> | Tripadvisor Hotel Details Scraper | Japan | **STANDARD** | $0.8/1k |
| 1421 <!-- id:1421 --> | Agoda Hotel Scraper | Korea | FREE | free |

**1550 Google Hotel is the best free starting point** — global, no account gate, and it
aggregates rates across booking sites.

Booking.com is split by locale (1037/1035 Germany, 927 France, 1692 Spain). There is no
global Booking template; pick the locale matching the user's market.

## Short-term rentals

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 120 <!-- id:120 --> | Airbnb Room Details Scraper | global | FREE | free |
| 2219 <!-- id:2219 --> | Airbnb Hotel Details Scraper (Japan) | Japan | **STANDARD** | $0.5/1k |

For Airbnb reviews rather than listings, see `review-reputation-analysis.md`.

## Flights

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 1568 <!-- id:1568 --> | Check24 Flight Scraper | Germany | FREE | free |

Flights are covered for Germany only. For any other market, say so rather than
substituting a travel-aggregator template.

## Do not

- Promise live availability or bookable rates. Every template returns what the page
  showed at collection time; travel pricing moves within hours.
- Promise German property data, or flight coverage outside Germany. Point the user at
  the markets that are covered instead.
- Use 2156 Zillow Profile for property data — it returns agents.
- Run detail templates across a whole listing result. Idealista Italy and Seloger both
  bill far more per line for detail than listing.
- Read listing counts as market inventory. Portals de-duplicate and syndicate; the same
  property appears on several sites and sometimes several times on one.

## Report

Give the user: which portals were covered for their market, the listing count, the
collection timestamp (because pricing decays fast), and the coverage gaps — German
property, flights outside Germany, rentals outside Japan.
