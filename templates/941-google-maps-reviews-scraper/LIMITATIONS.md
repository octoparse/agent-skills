# Google Maps Reviews Scraper Limitations

## Requires Place Detail URLs

This template depends on valid Google Maps place detail URLs.

It should not be treated as a keyword-search template.

## Review Availability Depends on the Place

Some places have:

- many reviews
- very few reviews
- no useful review text

The final output depends on what Google Maps publicly exposes for each place.

## Page Count Is an Approximation

The template uses page count as a review-volume control.

Rule of thumb:

- `1` page is about 10 reviews

But the exact number may vary.

## Not a Lead Discovery Template

This template enriches existing businesses with review data.

If the user first needs businesses to review, use a discovery template upstream.

## Google Platform Interruptions

Heavy activity can still be affected by:

- anti-bot checks
- slower response times
- interruptions in review loading

## Output Is Review-Level

If the user expects one row per business, this template is not the right starting point.

Each row is a review record, not a single business record.
