# Social listening and brand monitoring

45 cloud templates across social platforms and news. Use when the user needs to **find**
mentions, track accounts, or monitor conversation.

When they already know which posts to read and just want the comments, go to
`review-reputation-analysis.md`. The boundary is discovery versus depth.

`<!-- id:N -->` markers are checked by `scripts/build_catalog.py validate`.

## Step 1 — Discovery or tracking?

| The user asks | Approach |
|---|---|
| "what are people saying about <brand>" | search / hashtag templates across platforms |
| "watch <competitor>'s account" | profile and post-list templates for that account |
| "what's trending in <topic>" | trending and subreddit templates |
| "who is talking about us" | search templates, then a comments pass |

Brand monitoring is almost always two passes: search to find the posts, then a comments
template on the posts that matter.

## Twitter / X

| id | Template | Acct |
|---|---|---|
| 288 <!-- id:288 --> | Twitter Advanced Search Scraper | FREE |
| 209 <!-- id:209 --> | Twitter Scraper (by hashtag) | FREE |
| 208 <!-- id:208 --> | Twitter (X) Comments Scraper | FREE |
| 263 <!-- id:263 --> | Twitter Scraper (by Account URL) | FREE |
| 1838 <!-- id:1838 --> | Twitter Advanced Search Comments Scraper | FREE |
| 1606 <!-- id:1606 --> | Twitter Follower & Following Scraper | **STANDARD** |
| 2146 <!-- id:2146 --> | Twitter People Search Scraper | FREE |

288, 263, and 1838 all have an internal detail stage — do not chain a Twitter detail
template after them, and do not rule them out because the catalog shows no fields.

## TikTok

| id | Template | Acct |
|---|---|---|
| 2106 <!-- id:2106 --> | TikTok Profile Scraper | FREE |
| 802 <!-- id:802 --> | TikTok Video Details & Comments Scraper | **STANDARD** |
| 1996 <!-- id:1996 --> | TikTok Video Details Scraper | FREE |
| 799 <!-- id:799 --> | TikTok Search Scraper (No Login Required) | **STANDARD** |
| 1578 <!-- id:1578 --> | TikTok Search Scraper (Login Required) | FREE |

**1578 is free but requires a logged-in session**; 799 is billed and does not. Ask which
trade-off the user prefers before picking.

802 returns details **and** comments for less per line than 1996 charges for details
alone. Prefer 802.

## YouTube

| id | Template | Acct |
|---|---|---|
| 262 <!-- id:262 --> | YouTube Channel Scraper | FREE |
| 1813 <!-- id:1813 --> | YouTube Channel Scraper (Free) | FREE |
| 10 <!-- id:10 --> | YouTube Video List Scraper | FREE |
| 1745 <!-- id:1745 --> | YouTube Video List Scraper (by URL) | FREE |
| 252 <!-- id:252 --> | YouTube Details & Comments Scraper | FREE |
| 265 <!-- id:265 --> | YouTube Comments & Replies Scraper | **STANDARD** |
| 1494 <!-- id:1494 --> | YouTube Community Scraper | FREE |
| 1440 <!-- id:1440 --> | YouTube Transcript Scraper | **STANDARD** |

262 returns 40 fields but is billed; 1813 is free and thinner. Start free, upgrade if the
missing fields matter.

1440 Transcript is the only template in the library that returns spoken content — useful
when the brand mention is in the audio, not the description.

## Reddit

| id | Template | Acct |
|---|---|---|
| 2067 <!-- id:2067 --> | Reddit Search Scraper | FREE |
| 2037 <!-- id:2037 --> | Reddit Subreddit Scraper | FREE |
| 1957 <!-- id:1957 --> | Reddit Post & Comments Scraper | **STANDARD** |
| 1044 <!-- id:1044 --> | Reddit Trending Scraper | FREE |

Reddit is the cheapest platform covered here by a wide margin. The natural sequence is
2067 to find threads, then 1957 for full comment trees.

## Korea

Korea's social coverage is its second-strongest area after e-commerce.

| id | Template | Acct |
|---|---|---|
| 1552 <!-- id:1552 --> | Dcinside Scraper | FREE |
| 1640 <!-- id:1640 --> | Naver Blog SERP Scraper | **STANDARD** |
| 1667 <!-- id:1667 --> | Naver News Scraper | FREE |

Naver Blog is where Korean brand conversation happens — closer to a review platform than
a blog host. Dcinside is the main forum. For Korean listening, these three beat any
global template.

## Other platforms and news

| id | Template | Market | Acct |
|---|---|---|---|
| 1783 <!-- id:1783 --> | Xiaohongshu Search Result Scraper (by keyword) | China | FREE |
| 1353 <!-- id:1353 --> | Xiaohongshu Hashtag Page Scraper | China | FREE |
| 1464 <!-- id:1464 --> | Gab Scraper | global | FREE |
| 2075 <!-- id:2075 --> | Social Media Finder | global | FREE |
| 500 <!-- id:500 --> | Email & Social Media Finder | Germany | FREE |
| 1370 <!-- id:1370 --> | Google News Scraper | global | FREE |
| 1747 <!-- id:1747 --> | Google News Scraper (by URL) | global | FREE |
| 557 <!-- id:557 --> | Yahoo News Scraper | Japan | **STANDARD** |
| 1116 <!-- id:1116 --> | Yahoo News Comments Scraper | Japan | **STANDARD** |
| 884 <!-- id:884 --> | News Picks Article Scraper | Japan | **STANDARD** |

**Instagram and Facebook are not covered.** When a brief names either, say so and run the
platforms that are — X, Reddit, TikTok, and YouTube carry most brand conversation and are
covered in depth above.

## Do not

- Promise Instagram or Facebook coverage. Neither exists.
- Promise sentiment scores. Templates return post and comment text; scoring is a
  post-export step.
- Chain a detail template after 288, 263, or 1838 — all three already run an internal
  second pass.
- Read follower counts or engagement as reach. They are the numbers shown on the page at
  collection time, with no de-duplication or bot filtering.
- Use 1578 without confirming the user can supply a logged-in TikTok session, or 799
  without flagging that it is billed.
- Treat a hashtag or search result as complete. Platforms cap how far pagination goes;
  a run returns a recent slice.

## Report

Give the user: which platforms were covered and which were not (naming Instagram and
Facebook explicitly if relevant), the volume collected against the slice limit, the
collection window, and that sentiment analysis is still theirs to do.
