# Company and supplier research

Vetting companies rather than contacting them: registry data, financials, filings,
supplier catalogues, service-provider directories.

**Boundary with `lead-generation.md`:** go there when the goal is a contactable list —
emails, phones, outreach. Come here when the goal is judging or shortlisting a company.
The same directory site often serves both; the difference is which fields matter.

`<!-- id:N -->` markers are checked by `scripts/build_catalog.py validate`.

## Registries and company data

The only source of legally-filed company data — registration numbers, officers,
financials, filings. Coverage is Europe and Japan; there is no US or UK registry template.

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 1034 <!-- id:1034 --> | North Data Scraper | Germany | FREE | free |
| 2143 <!-- id:2143 --> | Pappers.fr Entreprise Info Scraper (avancé) | France | FREE | $1.5/1k |
| 1611 <!-- id:1611 --> | Societe.com Recherche Scraper | France | FREE | free |
| 1036 <!-- id:1036 --> | Societe.com Info Scraper | France | FREE | free |
| 2186 <!-- id:2186 --> | Verif annuaire des entreprises (liste) | France | FREE | free |
| 2189 <!-- id:2189 --> | Verif annuaire des entreprises (détail) | France | FREE | free |
| 1311 <!-- id:1311 --> | Baseconnect Company Info Scraper | Japan | FREE | free |

France has the deepest registry coverage — three independent sources (Pappers, Societe,
Verif), which is enough to cross-check a company. Germany has one (North Data). Japan has
one (Baseconnect).

Societe and Verif each split **search/list** from **detail**. Run the list template to
find companies, then the detail template only on the shortlist.

## Supplier and B2B catalogues

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 2059 <!-- id:2059 --> | b2bMAP Suppliers Scraper | global | FREE | free |
| 895 <!-- id:895 --> | wlw.de Lead Scraper | Germany | FREE | free |
| 1762 <!-- id:1762 --> | Wlw.de Detail Scraper (stable) | Germany | FREE | free |
| 1680 <!-- id:1680 --> | Marktplatz Mittelstand Leads Scraper | Germany | FREE | free |
| 1053 <!-- id:1053 --> | Kompass Leads Scraper | Germany | **STANDARD** | $3/1k |
| 2195 <!-- id:2195 --> | Kompass annuaire des entreprises (liste) | France | FREE | $0.05/1k |
| 2171 <!-- id:2171 --> | Kompass annuaire des entreprises (détail) | France | FREE | $0.15/1k |
| 1199 <!-- id:1199 --> | Kompass Data Scraper | global | FREE | free |
| 1633 <!-- id:1633 --> | Europages Listing Scraper | France | FREE | free |
| 2048 <!-- id:2048 --> | Europages Listing Scraper (for Italy) | Italy | FREE | free |
| 2178 <!-- id:2178 --> | IPROS Company Search Results Scraper | Japan | FREE | free |
| 2184 <!-- id:2184 --> | IPROS Product Search Results Scraper | Japan | FREE | free |
| 2191 <!-- id:2191 --> | MISUMI Product Listing Scraper | Japan | **STANDARD** | free |

**Kompass has four templates at wildly different prices** for overlapping data: French
list at $0.05/1k, French detail at $0.15/1k, global at free, German at $3/1k. Check the
free global template (1199) covers the need before reaching for 1053 — it is sixty times
the price per line.

Japan's industrial sourcing is well covered: IPROS by company (2178) or by product
(2184), MISUMI for parts catalogues (2191). This is the strongest Japanese B2B set.

## Service providers and software vendors

| id | Template | Market | Acct | Price |
|---|---|---|---|---|
| 858 <!-- id:858 --> | Clutch Scraper (Company Listing) | global | **STANDARD** | free |
| 772 <!-- id:772 --> | GoodFirms Scraper (Company Directory) | global | FREE | free |
| 886 <!-- id:886 --> | GoodFirms Scraper (Software Directory) | global | **STANDARD** | free |
| 887 <!-- id:887 --> | GoodFirms Scraper (Service Directory) | global | **STANDARD** | free |
| 2006 <!-- id:2006 --> | LinkedIn Company Profile Scraper | global | **STANDARD** | free |

For agency and software-vendor shortlisting, Clutch and GoodFirms carry ratings and
service categories that registries do not.

2006 is one of the 13 templates with an unusable slug (`aaaaaaaaa`) — look it up by id.
LinkedIn templates are also the most fragile in the library; expect partial results.

## Typical sequence

Vetting is usually three passes, each narrowing the set:

    1. discover     supplier catalogue or service directory  ──▶ candidate companies
    2. verify       registry template on the shortlist       ──▶ filings, size, status
    3. contact      1386 Contact Details Scraper             ──▶ outreach details

Step 3 belongs to `lead-generation.md`. Only run it on companies that survive step 2 —
enriching contacts for companies you are about to reject is wasted spend.

## Do not

- Expect US or UK registry data. Coverage is Germany, France, and Japan only. For those
  markets, say so rather than substituting a directory listing for filed data.
- Treat a Yellow-Pages-style directory as company data. `Gelbe Seiten`, `Pagesjaunes`,
  and `Yellow Pages` carry name, address, phone and category — not registration numbers,
  officers, or financials. They belong in `lead-generation.md`.
- Reach for 1053 Kompass Germany at $3/1k before checking whether 1199 Kompass (free)
  answers the question.
- Use consumer directories — Tabelog, Guru Navi, Hot Pepper, Just Eat, Craigslist — for
  B2B research. They surface in the same category tag but describe restaurants and
  classifieds.
- Rely on LinkedIn templates for anything time-critical.

## Report

Give the user: which companies were found, what was verifiable from a registry versus
what came from a self-reported directory listing, and the coverage gap for their markets.
The registry/directory distinction matters — directory data is submitted by the company
itself and is not independently filed.
