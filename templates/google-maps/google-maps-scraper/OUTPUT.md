# Google Maps Scraper Output Fields

## Output Overview

`Google Maps Scraper` returns business-level records from Google Maps listing and place detail pages.

This template is best understood as a `detail-level` output template.

## High-Value Output Fields

These are the fields most useful for lead generation, local research, and downstream enrichment:

| Field | Meaning |
|---|---|
| `keyword` | The original search keyword used for the record |
| `Title` | Business name |
| `Review_Count` | Number of Google Maps reviews |
| `Rating` | Average rating |
| `Address` | Full business address |
| `Country` | Country field when available |
| `City` | City field when available |
| `State` | State or region field when available |
| `Website` | Official business website |
| `Phone` | Business phone number |
| `Open_Time` | Current opening-hour summary |
| `Page_URL` | Google Maps place detail URL |
| `Google_id` | Google Maps business identifier |
| `Place_id` | Google place identifier |
| `Category` | Business category |
| `Description` | Google Maps business description when available |
| `Price_Range` | Price indicator when available |
| `Current_Status` | Open or closed status when available |
| `Latitude` | Latitude |
| `Longitude` | Longitude |

## Additional Rich Fields

This template may also return:

- `Additional_info`
- `Main_image`
- `Image_1`
- `Image_2`
- `Image_3`
- `Plus_code_URL`
- `Plus_code`
- `Delivery`
- day-by-day opening hour fields such as:
  - `Open_Time_Monday`
  - `Open_Time_Tuesday`
  - `Open_Time_Wednesday`
  - `Open_Time_Thursday`
  - `Open_Time_Friday`
  - `Open_Time_Saturday`
  - `Open_Time_Sunday`
- popularity fields such as:
  - `Popular_times_0`
  - `Popular_times_1`
  - `Popular_times_2`
  - `Popular_times_3`
  - `Popular_times_4`
  - `Popular_times_5`
  - `Popular_times_6`

## Fields Useful for Downstream Linking

These fields are especially useful when chaining to other templates:

- `Page_URL`
  - often the most important downstream linking field
- `Website`
  - useful for website-based contact enrichment
- `Title`
  - useful for reporting and QA
- `Rating`
  - useful for prioritization and ranking

## Practical Output Uses

Use these outputs for:

- local business lead lists
- map-based competitor research
- location-based outreach lists
- website enrichment workflows
- review-enrichment workflows
