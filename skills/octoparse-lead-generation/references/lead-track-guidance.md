# Lead Track Guidance

Use this file after `lead-template-shortlist.json`.

## local-business-leads

Use this track when the user wants:

- restaurants
- salons
- clinics
- gyms
- shops
- map listings
- directory-based local businesses

Typical outputs:

- business name
- address
- phone
- website
- rating
- page URL

Default recommendations:

- `1577 Google Maps Scraper` for discovery
- `941 Google Maps Reviews Scraper` only when reviews are explicitly needed
- `1463 Superpages Scraper` or `944 Yellow Pages Scraper (Cloud)` when a stable directory workflow is a better fit
- `1683 Gelbe Seiten Details Scraper (Cloud by URLs)` for German directory detail enrichment

## b2b-company-leads

Use this track when the user wants:

- company contacts
- outreach targets
- website-based discovery
- search-engine lead discovery
- email-oriented company prospecting

Typical outputs:

- result title
- result URL
- source URL
- company page URL
- search-discovered targets

Default recommendations:

- `15 Google Search Scraper` for broad discovery
- `2150 Google Search Email Finder (Premium)` when the request is explicitly email-focused

## Common Rules

- Prefer one primary recommendation.
- Add one alternative only when it covers a meaningfully different geography, directory source, or enrichment need.
- Do not widen to the full lead-generation category until the shortlist clearly fails.
