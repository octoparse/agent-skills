# Google Maps Scraper Input Parameters

## Input Summary

This template requires three core inputs and one optional enrichment toggle.

## Search Term

- Display name: `Search Term (up to 10,000)`
- Parameter name: `MainKeys`
- Required: `Yes`
- Input type: `keyword list`
- Typical placeholder:

```text
coffee
barber shop
```

Use this field for the business type or keyword you want to search on Google Maps.

Good examples:

- `coffee shop`
- `dentist`
- `real estate agent`
- `restaurant`

Important:

- Keep the keyword specific
- Avoid entering many synonyms for the same concept in one task
- Running near-duplicate search terms can increase overlap and duplicate results

## Number of Pages

- Display name: `Number of pages (Up to 50)`
- Parameter name: `PageSize`
- Required: `Yes`
- Input type: `number`
- Typical placeholder:

```text
Input values scale results: 1=20, 2=40, 3=60, etc. (20 results per increment). For maximum data, use 50—this scrapes all available results.
```

Use this field to control result volume.

Rule of thumb:

- `1` is about 20 results
- `2` is about 40 results
- `3` is about 60 results

Recommended usage:

- use `1-3` for testing
- use larger values for production runs
- use `50` only when the user wants broad coverage and understands the run may be heavier

## Location

- Display name: `Location`
- Parameter name: `Location`
- Required: `Yes`
- Input type: `text`
- Typical placeholder:

```text
New York
```

Use one city, region, or area per task.

Good examples:

- `New York`
- `Liverpool`
- `Tokyo`
- `Berlin`

Important:

- This template is designed for one location per task
- If the user wants multiple cities, create separate tasks
- Extremely small areas can increase oversplitting and duplicate overlap

## Get Q&As

- Display name: `Get Q&As`
- Parameter name: `get_FAQ`
- Required: `No`
- Input type: `boolean`

Enable this only when the user explicitly needs Google Maps Q&A fields.

Use cases:

- service details
- parking details
- visitor experience details
- place-specific questions and answers

## Common Input Mistakes

### Mistake 1: Entering many synonyms in the same run

Bad example:

```text
cafe
coffee shop
coffeehouse
```

Why it is risky:

- these are highly overlapping intents
- they can increase duplicate coverage and processing cost

### Mistake 2: Using multiple locations in one task

Bad example:

```text
New York
Boston
Chicago
```

Better approach:

- create one task per location

### Mistake 3: Starting with the maximum page count

For setup and QA, start small first.

Suggested test input:

```text
Search Term: dentist
Number of Pages: 2
Location: Chicago
```
