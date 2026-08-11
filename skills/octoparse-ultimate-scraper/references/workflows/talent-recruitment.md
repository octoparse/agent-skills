# Jobs and talent market

46 cloud templates collect job postings. Two distinct uses: sourcing candidates from
postings, and reading the market — who is hiring, for what, at what salary.

Japan is by far the deepest market here (18 templates). There is no US-focused job board
template beyond LinkedIn and Craigslist.

`<!-- id:N -->` markers are checked by `scripts/build_catalog.py validate`.

## Step 1 — Which question?

| The user asks | Read as |
|---|---|
| "find candidates for X" | sourcing — but see the warning below |
| "who is hiring for X" | market signal — hiring volume as a growth indicator |
| "what do X roles pay" | compensation research |
| "what does <company> post" | competitor headcount tracking |

**These templates collect job postings, not candidate profiles.** Nothing in the library
returns résumés or candidate contact details. Sourcing here means identifying employers
and roles, then reaching people through another channel. Say this before promising a
candidate list.

## Global

| id | Template | Acct | Price | Note |
|---|---|---|---|---|
| 1542 <!-- id:1542 --> | 🔥 LinkedIn Job Scraper | FREE | $0.3/1k | broadest coverage |
| 1626 <!-- id:1626 --> | LinkedIn Job Details Page Scraper | **STANDARD** | free | detail pass |
| 2000 <!-- id:2000 --> | Craigslist Job Details Scraper | FREE | free | US classifieds |

1542 and 1626 both have unusable slugs (`ffffff`, `eeeeeee`) — look them up by id.
LinkedIn templates are the most fragile in the library; expect partial results and
retries, and do not build a time-critical workflow on them.

## Japan

| id | Template | Acct | Price | Fields |
|---|---|---|---|---|
| 1291 <!-- id:1291 --> | Hello Work Job Listings Scraper (Cloud Only) | **STANDARD** | free | 59 |
| 1323 <!-- id:1323 --> | Hello Work Job Details Scraper | FREE | free | 18 |
| 2220 <!-- id:2220 --> | En Japan Job Listings Scraper | **STANDARD** | free | 16 |
| 1749 <!-- id:1749 --> | Stanby Jobs Scraper | **STANDARD** | free | 15 |
| 223 <!-- id:223 --> | Doda Job Listing Scraper | FREE | free | 9 |
| 1685 <!-- id:1685 --> | BAITORU Job Scraper | FREE | free | 10 |
| 932 <!-- id:932 --> | Haken Rikunabi Job Scraper | **STANDARD** | $0.1/1k | 9 |
| 1974 <!-- id:1974 --> | Yahoo! Jobcatalog List Scraper | FREE | free | 9 |
| 1776 <!-- id:1776 --> | KyujinBox Jobs Infomation | FREE | free | 9 |
| 794 <!-- id:794 --> | ReKatsu Job Listing Scraper | **STANDARD** | free | 8 |
| 916 <!-- id:916 --> | Kamome Job Listings Scraper | **STANDARD** | free | 8 |
| 785 <!-- id:785 --> | Woman Type Job Details Scraper | FREE | free | 9 |
| 926 <!-- id:926 --> | Openwork Job Reviews Scraper (Cloud only) | **STANDARD** | free | 12 |

**1291 Hello Work is the single richest job template in the library at 59 fields** — it
is the government employment service, so coverage is broad and the data is structured.
Start here for any Japanese labour-market question.

1749 and 1776 have unusable slugs (`1749`, `1776`) — look them up by id.

926 is employer reviews, not postings — it belongs with `review-reputation-analysis.md`
but is listed here because employer brand and hiring usually come up together.

## Germany

| id | Template | Acct | Price |
|---|---|---|---|
| 921 <!-- id:921 --> | Stepstone Details Job Scraper | **STANDARD** | $2/1k |
| 881 <!-- id:881 --> | Stepstone Listing Job Scraper | **STANDARD** | $0.1/1k |
| 1951 <!-- id:1951 --> | Stepstone Listing Scraper by url | FREE | $0.1/1k |
| 1056 <!-- id:1056 --> | Joblift.de Job Scraper | FREE | free |
| 1050 <!-- id:1050 --> | Glassdoor Job Scraper (for Germany) | FREE | free |
| 1209 <!-- id:1209 --> | Jobs.ch Job Scraper | FREE | free |
| 1051 <!-- id:1051 --> | Freelancermap Job Scraper (Listing) | FREE | free |
| 1052 <!-- id:1052 --> | Freelancermap Job Scraper (Details) | FREE | free |

Stepstone splits listing ($0.1/1k) from detail ($2/1k) — a twentyfold difference. Run the
listing pass to filter, then detail only on what survives.

Glassdoor is covered for Germany only.

## France

| id | Template | Acct | Price |
|---|---|---|---|
| 1028 <!-- id:1028 --> | wttj Offres d'emploi Scraper | FREE | free |
| 1666 <!-- id:1666 --> | Hellowork Data Scraper | FREE | free |
| 1632 <!-- id:1632 --> | Francetravail Détails Scraper | FREE | free |
| 1612 <!-- id:1612 --> | Emploi-territorial Data Scraper | FREE | free |
| 2211 <!-- id:2211 --> | Leboncoin Emploi Infos Scraper | FREE | $1.5/1k |
| 1290 <!-- id:1290 --> | Malt freelance Info Scraper | FREE | $0.3/1k |

1632 Francetravail is the public employment service — the French counterpart to Hello
Work, and the best free source for market-wide French hiring data.

1290 Malt is the only freelance-marketplace template outside Germany's Freelancermap.

## Spain and Australia

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 1206 <!-- id:1206 --> | InfoJobs Listing Scraper | Spain | FREE | free |
| 1207 <!-- id:1207 --> | InfoJobs Details Scraper | Spain | FREE | free |
| 1663 <!-- id:1663 --> | SeasonalJobs Scraper | Spain | **STANDARD** | $0.3/1k |
| 1949 <!-- id:1949 --> | Seek Listing Scraper (by URL) | Australia | FREE | free |
| 2142 <!-- id:2142 --> | Seek Details Scraper (by URL) | Australia | FREE | free |

Italy and Korea are not covered for jobs.

## Do not

- Promise candidate résumés or contact details. No template returns them.
- Run a detail template across a full listing result. Stepstone detail is $2/1,000 lines
  against $0.1 for listing; filter first.
- Build a scheduled workflow on LinkedIn templates.
- Offer Glassdoor outside Germany, or job coverage for Italy or Korea. Name the markets
  that are covered instead.
- Read posting counts as headcount. A company may repost, cross-post, or advertise roles
  it never fills.

## Report

Give the user: which boards were covered for their market, the posting count, and the
gap between postings and actual hiring. When they asked for candidates, restate plainly
that the output is employers and roles, not people.
