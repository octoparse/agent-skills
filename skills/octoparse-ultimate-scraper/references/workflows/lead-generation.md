# Lead generation

106 templates carry the `Lead Generation` tag; 90 are cloud-capable. Two questions
decide which one to use, in this order:

1. **What kind of lead?** — local business, B2B company, or enriching a list they have
2. **Which market?** — determines whether a global template or a national directory wins

Answer 1 first. A user asking for "restaurant leads in Munich" needs the local-discovery
track; Germany then narrows it to `Gelbe Seiten` rather than `Google Maps`.

`<!-- id:N -->` markers are checked by `scripts/build_catalog.py validate`.

## Step 1 — Track

| The user wants | Track |
|---|---|
| restaurants, clinics, salons, gyms, local stores, "businesses in <city>" | **Local discovery** |
| companies, suppliers, agencies, outreach targets, "companies that do X" | **B2B discovery** |
| emails or phones for names/URLs they already have | **Enrichment** |

Mixed asks are almost always discovery → enrichment. Name the primary track, then chain.

## Step 2 — Market

Global templates work anywhere but return generic fields. National directories return
richer contact data for their own country and are usually free.

**Prefer the national directory when the user names one country.** Prefer the global
template when the ask spans countries or names no country at all.

Coverage is uneven, and saying so up front is better than a weak recommendation:

| Market | Lead-gen depth | Go-to sources |
|---|---|---|
| Global / English | 25 | Google Maps, Google Search, Contact Details |
| Germany | 22 | Gelbe Seiten, Das Telefonbuch, Dialo, Golocal, wlw, 11880 |
| France + CH/BE | 18 | Pagesjaunes, Kompass, Local.ch, Pagesdor, Pappers |
| Japan | 11 | Google Maps JP, iTown Page, IPROS, Hot Pepper Beauty |
| Spain + LatAm | 9 | Yellow Pages Latin, Todo Está En Madrid |
| Italy | 5 | Pagine Gialle, Pagine Bianche, Europages |
| **Korea** | — | not covered; see e-commerce and social |

Korea is not covered for lead generation. Say so and offer the Korean templates that do
exist — e-commerce and social are its strongest areas — rather than forcing a
neighbouring-market template.

## Local discovery

**Global**

| id | Template | Acct | Price | Yields |
|---|---|---|---|---|
| 1577 <!-- id:1577 --> | Google Maps Scraper | **STANDARD** | $2/1k | 45 fields; phone, website, hours, coords |
| 1074 <!-- id:1074 --> | Google Maps Listings Scraper (by URLs) | FREE | free | 17 fields; when the user already has map URLs |
| 1875 <!-- id:1875 --> | Superpages Details Page Scraper | FREE | free | US directory; phone, website |
| 1918 <!-- id:1918 --> | BBB Listing Scraper | FREE | free | US; phone plus accreditation signal |

1577 is the default for "find businesses in <place>". Flag two things before running it:
it needs a **STANDARD** account, and it bills $2 per 1,000 lines.

**By market**

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 1059 <!-- id:1059 --> | Gelbe Seiten Scraper | Germany | FREE | free |
| 908 <!-- id:908 --> | Das Telefonbuch Lead Scraper | Germany | FREE | free |
| 1675 <!-- id:1675 --> | Dialo.de Leads Scraper | Germany | FREE | free |
| 1678 <!-- id:1678 --> | Golocal Leads Scraper | Germany | FREE | free |
| 2196 <!-- id:2196 --> | Editus data scraper | Luxembourg | FREE | $0.4/1k |
| 2188 <!-- id:2188 --> | Pagesdor data scraper | Belgium | FREE | $0.8/1k |
| 2261 <!-- id:2261 --> | Local.ch lead Scraper | Switzerland | FREE | $0.6/1k |
| 1865 <!-- id:1865 --> | Google Maps advanced Scraper for Japan | Japan | **STANDARD** | $0.2/1k |
| 1677 <!-- id:1677 --> | Itown Page Listing scraper | Japan | **STANDARD** | $0.65/1k |
| 1129 <!-- id:1129 --> | Hot Pepper Beauty Hair Salons URL Scraper | Japan | FREE | free |
| 1398 <!-- id:1398 --> | Pagine Gialle Shop Detail Scraper | Italy | FREE | free |
| 1726 <!-- id:1726 --> | Pagine Bianche Shop List Scraper | Italy | FREE | free |
| 1352 <!-- id:1352 --> | Yellow Pages Latin Scraper (Details) | LatAm | **STANDARD** | free |
| 1741 <!-- id:1741 --> | Todo Está En Madrid Scraper by URL | Spain | FREE | free |
| 1108 <!-- id:1108 --> | Yellow Pages Details Scraper | Australia | FREE | free |
| 1118 <!-- id:1118 --> | Yellow Pages Canada (Details) | Canada | FREE | free |
| 1453 <!-- id:1453 --> | Fonecta Scraper | Finland | FREE | free |
| 1457 <!-- id:1457 --> | Krak Scraper | Denmark | FREE | free |
| 1458 <!-- id:1458 --> | Gulesider Scraper | Norway | FREE | free |
| 1392 <!-- id:1392 --> | Eniro Scraper | Sweden | FREE | free |
| 1454 <!-- id:1454 --> | Goudengids Scraper | Netherlands | FREE | free |

Yellow-Pages-style sites usually ship a **Listing** and a **Details** template — 1087/1108
for Australia, 1112/1118 for Canada, 1339/1398 for Italy. Listing is broader and cheaper;
Details carries the contact fields. Start from Details for lead work.

Germany's `Gelbe Seiten` has four variants (1059, 1613, 1682, 1683) splitting on keyword
vs URL input and free vs cloud. Start with 1059 and only move up if the user needs
URL-driven or higher-volume collection.

## B2B discovery

**Global**

| id | Template | Acct | Price | Yields |
|---|---|---|---|---|
| 15 <!-- id:15 --> | Google Search Scraper | FREE | $0.6/1k | SERP results, **no contact data** |
| 2150 <!-- id:2150 --> | Google Search Email Finder (Premium) | FREE | $0.6/1k | search + contact extraction in one pass |
| 2059 <!-- id:2059 --> | b2bMAP Suppliers Scraper | FREE | free | supplier directory |
| 2075 <!-- id:2075 --> | Social Media Finder | FREE | $1/1k | social profiles from a name |

Contacts not needed → **15**. Contacts needed → **2150**.

These two are **not a chain.** Both take a search query, but 15's output does not feed
2150. Pick one.

**By market**

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 1034 <!-- id:1034 --> | North Data Scraper | Germany | FREE | free |
| 1053 <!-- id:1053 --> | Kompass Leads Scraper | Germany | **STANDARD** | $3/1k |
| 895 <!-- id:895 --> | wlw.de Lead Scraper | Germany | FREE | free |
| 1680 <!-- id:1680 --> | Marktplatz Mittelstand Leads Scraper | Germany | FREE | free |
| 2143 <!-- id:2143 --> | Pappers.fr Entreprise Info Scraper | France | FREE | $1.5/1k |
| 2171 <!-- id:2171 --> | Kompass annuaire (détail) | France | FREE | $0.15/1k |
| 2186 <!-- id:2186 --> | Verif annuaire des entreprises (liste) | France | FREE | free |
| 1611 <!-- id:1611 --> | Societe.com Recherche Scraper | France | FREE | free |
| 2178 <!-- id:2178 --> | IPROS Company Search Results Scraper | Japan | FREE | free |
| 2048 <!-- id:2048 --> | Europages Listing Scraper | Italy | FREE | free |

France's Kompass splits list (2195, $0.05/1k) from detail (2171, $0.15/1k) — run the list
first, then the detail pass only on rows worth enriching.

## Enrichment

| id | Template | Input | Acct | Price |
|---|---|---|---|---|
| 1386 <!-- id:1386 --> | Contact Details Scraper | any website URL | FREE | free |
| 1853 <!-- id:1853 --> | Google Maps Email Finder (by URLs) | Google Maps URLs | FREE | free |
| 1576 <!-- id:1576 --> | Google Maps Email Finder | search term + location | **STANDARD** | $0.5/1k |

**1386 is the default.** Free, takes any website URL, crawls to a configurable depth, and
returns emails, phones, and eleven social networks. It attaches to the end of nearly every
discovery template that yields a website.

Pick by what the user already has:

| They have | Use |
|---|---|
| a search term only | 1576 — one step, but STANDARD and billed |
| Google Maps URLs | 1853 — free, one step |
| website URLs from anywhere | 1386 — free, deepest output |

Real chains — the upstream field genuinely feeds the downstream input:

    1577 Google Maps Scraper       ──Website──▶ 1386 Contact Details Scraper
    1875 Superpages Details        ──Website──▶ 1386
    1059 Gelbe Seiten / 908 / 1675 ──Website──▶ 1386

Confirm the upstream template actually populates `Website` before promising the chain.
Several directory templates expose a website column that is empty for most rows.

## Do not

- Recommend `Zillow Details Scraper` (1763), `Idealo Price Comparison Scraper` (876),
  `AutoScout24 Spain Scraper` (1647), `Coppel` (1659), `Elektra` (1661), or `Falabella`
  (1104) for leads. They carry the `Lead Generation` tag but are real-estate and
  e-commerce tools — this noise is heaviest in the Spanish set.
- Treat review templates as a lead source. Reviews enrich a business already found.
- Chain a Google Maps detail template after 1577, 1859, or 1865. All three already
  collect detail pages internally; you would pay twice for the same rows.
- Rule out 1576 or 2150 because the catalog shows no email field. Both hide their real
  output behind an internal second stage — the catalog marks these `unknown`, not absent.
  Confirm against `search_templates(id=…)`.
- Offer a STANDARD-gated template (1577, 1053, 1352, 1677, 1865) to a free account
  without flagging the gate. Some of them are free per line, so the gate is invisible
  from the price.

## Report

Give the user: the template or chain, why it fits their market, the fields they will
actually get, and the honest gap. The gap is usually one of:

- 1577 returns no email; enrichment is a separate, billed step
- website-based enrichment only covers rows where the upstream website column is filled
- a national directory covers one country — a multi-market ask needs one run per market
- Korea is not covered for lead generation; its coverage is e-commerce and social
