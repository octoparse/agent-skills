# Google Maps Reviews Scraper Input Parameters

## Input Summary

This template needs:

- one or more Google Maps place detail URLs
- the number of review pages to collect

## Google Maps Place Details Page URLs

- Display name: `Google Maps Place Details Page URLs (up to 10,000)`
- Parameter name: `MainKeys`
- Required: `Yes`
- Input type: `URL list`
- Typical placeholder:

```text
https://goo.gl/maps/1T5eicx7eZxPNsRU8
https://www.google.com/maps/place/Junior's+Restaurant+%26+Bakery/@40.6901493,-73.9840623,17z/data=!3m1!4b1!4m5!3m4!1s0x89c25e9540f32929:0xe9e262856e34ee99!8m2!3d40.6901493!4d-73.9818736
```

Important:

- this field expects place detail URLs
- do not confuse place detail URLs with general search result URLs
- one URL per line is the safest pattern

## Number of Pages

- Display name: `Number of Pages (up to 5,000)`
- Parameter name: `pagesize`
- Required: `Yes`
- Input type: `number`
- Typical placeholder:

```text
enter 1 for 10 reviews, 2 for 20 reviews, etc.
```

Rule of thumb:

- `1` page is about 10 reviews
- `2` pages is about 20 reviews

Use a small number for testing before running large review pulls.

## Common Input Mistakes

### Mistake 1: Passing search result URLs instead of place detail URLs

This is one of the most common failures.

The template needs:

- one business place detail page URL

not:

- a Google Maps keyword search URL

### Mistake 2: Starting with a very high page count

For QA and workflow validation, start small first.

Suggested test input:

- one known place detail URL
- `1` or `2` pages
