# Search visibility

25 cloud templates capturing search engine result pages. Use when the user wants to see
what a search engine returns — for their brand, a competitor, or a keyword set.

**Scope: search results, not SEO metrics.** These templates capture what an engine
returns for a query. Backlinks, domain authority, keyword volume, CPC, traffic estimates
and rank-tracking-over-time are a different class of data and belong to a dedicated SEO
platform — when a request asks for those, say so and point there rather than substituting
SERP data. Read the [Do not](#do-not) section first.

`<!-- id:N -->` markers are checked by `scripts/build_catalog.py validate`.

## Step 1 — Which engine

Engine choice follows the user's market, not habit. Google is not the default everywhere:
Naver leads in Korea and Yahoo holds real share in Japan.

| Market | Reach for |
|---|---|
| global / most Western markets | Google (15) |
| Korea | Naver (1381), then Google |
| Japan | Yahoo! Japan (1734), then Google |
| France | Google, plus Qwant (1488) for public-sector context |
| privacy-conscious segments | DuckDuckGo (1040), Startpage (1479), Ecosia (1091) |
| China | Baidu (1469) |

## Templates

| id | Template | Engine | Market | Acct | Fields |
|---|---|---|---|---|---|
| 15 <!-- id:15 --> | Google Search Scraper | Google | global | FREE | 35 |
| 652 <!-- id:652 --> | Google SERP scraper (Top 5 results) | Google | global | FREE | 2 |
| 1901 <!-- id:1901 --> | Google AI Mode Scraper | Google | global | FREE | 7 |
| 2167 <!-- id:2167 --> | Google Image Scraper | Google | global | FREE | 9 |
| 1734 <!-- id:1734 --> | Yahoo! Japan Searching Scraper | Yahoo | Japan | FREE | 13 |
| 1381 <!-- id:1381 --> | Naver Search Scraper | Naver | Korea | FREE | 7 |
| 2032 <!-- id:2032 --> | RISS Academic Information Search Scraper | RISS | Korea | FREE | 15 |
| 1180 <!-- id:1180 --> | Yahoo Search Scraper | Yahoo | US/EN | FREE | 6 |
| 1181 <!-- id:1181 --> | Yahoo Recherche Scraper | Yahoo | France | FREE | 6 |
| 1194 <!-- id:1194 --> | Yahoo Spain Search Scraper | Yahoo | Spain | FREE | 6 |
| 1471 <!-- id:1471 --> | Bing Search Results Scraper | Bing | global | **STANDARD** | 5 |
| 1488 <!-- id:1488 --> | Qwant Scraper | Qwant | France | FREE | 6 |
| 1091 <!-- id:1091 --> | Ecosia Search Results Scraper | Ecosia | global | FREE | 6 |
| 1040 <!-- id:1040 --> | DuckDuckGo Scraper | DuckDuckGo | global | FREE | 5 |
| 1469 <!-- id:1469 --> | Baidu Scraper | Baidu | China | FREE | 5 |
| 1479 <!-- id:1479 --> | Startpage Scraper | Startpage | global | FREE | 4 |
| 1473 <!-- id:1473 --> | AOL Search Result Scraper | AOL | US | FREE | 4 |
| 1490 <!-- id:1490 --> | Dogpile Scraper | Dogpile | US | FREE | 5 |
| 1492 <!-- id:1492 --> | OneSearch Scraper | OneSearch | US | FREE | 4 |
| 1493 <!-- id:1493 --> | Search Engine Aggregator | multiple | global | **STANDARD** | 5 |
| 1747 <!-- id:1747 --> | Google News Scraper (by URL) | Google News | global | FREE | 8 |

## The field-depth cliff

**15 Google Search Scraper returns 35 fields. Every other engine returns 4 to 13.**

This is the single most important constraint here. Google's template carries position,
sitelinks, ratings, snippet, displayed URL, and pagination state. Bing, DuckDuckGo,
Startpage, AOL, and OneSearch carry roughly title, URL, and description.

Consequences for cross-engine work:

- Comparing across engines is limited to **title, URL, and rough position**. Rich
  snippets, ratings, and sitelinks exist only for Google.
- 652 is cheap but returns **2 fields** and only the top 5 results. It is a presence
  check, not a SERP capture. Use 15 for anything analytical.
- 1493 Search Engine Aggregator queries several engines but returns 5 fields, so it
  inherits the shallow schema rather than Google's.

## Repeat capture

There is no rank tracking. Position over time means re-running and storing results
yourself:

    start_or_stop_task(taskId="<taskId>", action="start")

Each run bills again. Size it before committing to a cadence: weekly capture of a keyword
set is modest, but daily capture across several engines multiplies fast. Quote the cost
from the live `pricing` at the user's result size.

## Do not

- Offer SEO metrics. No backlink, domain-authority, keyword-volume, CPC, or traffic
  template exists. When a user asks for those, say the library does not cover them and
  point them at a dedicated SEO tool. Do not substitute SERP data and call it SEO
  analysis.
- Present 652 as a SERP scraper. Two fields, top 5 results.
- Compare rich snippets across engines. Only Google's template returns them.
- Treat a single capture as a ranking. SERPs are personalised, localised, and volatile;
  one run is one observation from one location.
- Assume Google is the right engine for Korea or Japan without asking.
- Reach for 2150 Google Search Email Finder here — it is a lead-generation template that
  happens to sit in the same category tag. See `lead-generation.md`.

## Report

Give the user: which engines were captured, how many results per query, the field-depth
difference between Google and everything else, the capture timestamp, and — when they
asked an SEO question — a clear statement of what this library cannot answer.
