# Reviews and reputation

44 cloud templates collect review or comment text. They are scattered across five
category tags — Reviews, E-Commerce, Travel, Maps, Directories — so the category tag is
useless for finding them. Select on **where the reviews live**, below.

Temu and TikTok Shop reviews use a separate API; see `../dataset-capability.md`.

`<!-- id:N -->` markers are checked by `scripts/build_catalog.py validate`.

## Step 1 — Where do the reviews live?

| The user cares about | Section |
|---|---|
| a local business, restaurant, clinic, shop | [Local business](#local-business) |
| a product they sell or compete with | [Marketplace](#marketplace) |
| a hotel, rental, or destination | [Travel](#travel) |
| their app | [Apps](#apps) |
| what people say in public, unprompted | [Social and forums](#social-and-forums) |
| their employer brand | [Employer](#employer) |

Most reputation work needs two of these, not one. A restaurant chain cares about Google
Maps **and** TripAdvisor; a DTC brand cares about Amazon **and** Trustpilot.

## Local business

| id | Template | Market | Acct |
|---|---|---|---|
| 941 <!-- id:941 --> | Google Maps Reviews Scraper | global | **STANDARD** |
| 990 <!-- id:990 --> | Google Maps Reviews Scraper Lite | global | FREE |
| 1150 <!-- id:1150 --> | Google Maps Reviews Scraper (by Reviewer) | global | FREE |
| 1419 <!-- id:1419 --> | Kakao Map Review Scraper | Korea | FREE |
| 1462 <!-- id:1462 --> | Foursquare Reviews Scraper (by URL) | global | FREE |
| 1679 <!-- id:1679 --> | Golocal Reviews Scraper | Germany | FREE |
| 2209 <!-- id:2209 --> | Trustpilot Reviews Scraper (Cloud) | global | FREE |

**990 before 941.** The Lite version is free and returns 21 fields against 941's 16;
reach for 941 only if the user hits a limit the Lite version imposes.

1150 inverts the query — it collects everything one *reviewer* wrote, which is how you
investigate suspected review fraud rather than measure sentiment.

Reviews are downstream of discovery. The user needs place URLs first; if they do not
have them, run a Google Maps listing template from `lead-generation.md` and feed its
`Page_URL` in.

## Marketplace

Amazon review templates are per-country and are the richest in the library.

| id | Template | Market | Acct | Fields |
|---|---|---|---|---|
| 764 <!-- id:764 --> | Amazon Review Scraper | Germany | **STANDARD** | 51 |
| 2066 <!-- id:2066 --> | Amazon Reviews Scraper | Italy | FREE | 47 |
| 732 <!-- id:732 --> | Amazon Review Scraper | France | FREE | 36 |
| 2039 <!-- id:2039 --> | Amazon Review Scraper | UK | FREE | 36 |
| 1203 <!-- id:1203 --> | Amazon Review Details Scraper | Japan | **STANDARD** | 29 |
| 931 <!-- id:931 --> | Best Buy Reviews Scraper | US | FREE | 17 |
| 1670 <!-- id:1670 --> | Musinsa Review Scraper | Korea | FREE | 16 |
| 2251 <!-- id:2251 --> | Vinted Avis Scraper | France | FREE | 15 |
| 37 <!-- id:37 --> | Rakuten Product Review Scraper | Japan | FREE | 10 |
| 38 <!-- id:38 --> | Yahoo Shopping Review Scraper (by URL) | Japan | FREE | 10 |

Review **text** for amazon.com is not covered. The global product template (2218, see
`competitor-price-monitoring.md`) carries rating aggregates for US products; offer that,
and say plainly that per-review text is not available for that marketplace.

## Travel

| id | Template | Market | Acct |
|---|---|---|---|
| 793 <!-- id:793 --> | TripAdvisor Hotel Reviews Scraper | global | **STANDARD** |
| 1006 <!-- id:1006 --> | Tripadvisor Review Scraper | Germany | **STANDARD** |
| 1014 <!-- id:1014 --> | Booking.com Reviews Scraper | Japan | FREE |
| 1994 <!-- id:1994 --> | Airbnb EN Review Details Scraper | global | FREE |
| 2204 <!-- id:2204 --> | Airbnb Japan Review Details Scraper | Japan | **STANDARD** |
| 1598 <!-- id:1598 --> | Yeogi Hotel Review Scraper | Korea | **STANDARD** |
| 1705 <!-- id:1705 --> | Google Hotel Scraper (by URLs) | global | FREE |

1006 is the most expensive review template here — roughly three times 793 for the same
platform. Use 793 unless German-locale review text is specifically required.

## Apps

| id | Template | Market | Acct |
|---|---|---|---|
| 1141 <!-- id:1141 --> | App Store Reviews Scraper | global | **STANDARD** |
| 68 <!-- id:68 --> | Google Play Review Scraper | global | **STANDARD** |
| 672 <!-- id:672 --> | Google Play Review Scraper (Cloud) | global | **STANDARD** |
| 1068 <!-- id:1068 --> | Google Play APP Avis Scraper | France | FREE |

All free per line but STANDARD-gated except 1068. For a free account, 1068 is the only
app-review option.

## Social and forums

| id | Template | Market | Acct |
|---|---|---|---|
| 1957 <!-- id:1957 --> | Reddit Post & Comments Scraper | global | **STANDARD** |
| 2037 <!-- id:2037 --> | Reddit Subreddit Scraper | global | FREE |
| 208 <!-- id:208 --> | Twitter (X) Comments Scraper | global | FREE |
| 802 <!-- id:802 --> | TikTok Video Details & Comments Scraper | global | **STANDARD** |
| 265 <!-- id:265 --> | YouTube Comments & Replies Scraper | global | **STANDARD** |
| 252 <!-- id:252 --> | YouTube Details & Comments Scraper | global | FREE |
| 1814 <!-- id:1814 --> | YouTube Comments Scraper (Short Video) | global | FREE |
| 1116 <!-- id:1116 --> | Yahoo News Comments Scraper | Japan | **STANDARD** |
| 1873 <!-- id:1873 --> | Allociné Cinéma Critiques Scraper | France | FREE |
| 1516 <!-- id:1516 --> | IMDb Review Scraper | global | FREE |
| 723 <!-- id:723 --> | Goodreads Comments Scraper | global | FREE |

This section overlaps `social-listening.md`. The boundary: come here when the user knows
*which* posts or videos to read; go there when they need to find the mentions first.

## Employer

| id | Template | Market | Acct |
|---|---|---|---|
| 926 <!-- id:926 --> | Openwork Job Reviews Scraper (Cloud only) | Japan | **STANDARD** |
| 983 <!-- id:983 --> | Kununu.com Leads Scraper | Germany | FREE |

Only Japan and Germany are covered. No Glassdoor template exists.

## Do not

- Promise sentiment scoring. Every template returns review **text and rating**; no
  template computes sentiment. Analysis happens after export, by you or the user.
- Run a review template as the first step. All of them need URLs or IDs for things
  already found — discovery comes first.
- Assume one Amazon review template covers several countries, or that review text is
  available for amazon.com.
- Reach for a template for Temu or TikTok Shop reviews — use `../dataset-capability.md`
  with `collectionType="reviews"`.
- Quote review counts as complete. Most platforms cap how deep review pagination goes;
  a run returns a recent slice, not the full history.

## Report

Give the user: which platforms are covered and which are not, the review volume actually
collected versus the total shown on the platform, and the fact that sentiment analysis is
a step they still have to do. When a platform they named has no template — US Amazon
reviews, Glassdoor — say so directly rather than substituting a neighbour.
