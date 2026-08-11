# Google Maps Scraper Limitations

## Google Maps Result Limits

Google Maps commonly limits each keyword + location query to a finite result set.

To widen coverage, this template uses region splitting and multiple search points. That improves reach, but it can also create overlap.

## Duplicate Risk

Because nearby grid points can overlap, the same business may appear more than once during collection.

Important:

- duplicate appearance does not automatically mean duplicate billing
- Octoparse billing logic can filter unique records
- users should still expect overlap in raw collection behavior

## One Location Per Task

This template is designed for one location per task.

If the user wants:

- New York
- Boston
- Chicago

use separate tasks instead of one combined input.

## Small Area Oversplitting

Very small or overly precise locations can cause oversplitting.

That can lead to:

- unnecessary overlap
- repeated coverage
- inefficient runs



## Result Variability

Output volume can vary depending on:

- the keyword
- the location
- Google Maps availability
- category density
- time-sensitive Google Maps changes

## Not a Review-First Template

This template can return review counts and rating summaries, but it is not the best choice when the main goal is collecting review text.

For review text, use a review-specific downstream template.

## Not a Direct Email Template

This template may return:

- website
- phone
- rating
- address

but it should not be treated as a guaranteed direct email extractor.

If email is required, a downstream website-based enrichment step is often needed.
