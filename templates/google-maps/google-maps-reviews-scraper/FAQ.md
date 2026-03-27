# Google Maps Reviews Scraper FAQ

## What is this template best for?

It is best for extracting:

- review text
- reviewer names
- review timestamps
- review likes
- review images

## Can I use keywords instead of URLs?

No. This template expects Google Maps place detail URLs.

If you only have keywords, use an upstream Google Maps discovery template first.

## How many reviews does one page represent?

As a rule of thumb:

- `1` page is about 10 reviews

Use that as a planning estimate, not a guaranteed exact count.

## Can I use this to find the best restaurant?

Yes, if you already have place URLs and want review-level evidence for ranking or comparison.

## Does this template return one row per business?

No. It returns one row per review.

If you want one row per business, start with a Google Maps business discovery template instead.
