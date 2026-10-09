# Rumah Terukur | Vijeron

Original, bilingual home-measurement and material-planning site for `rumah.vijeron.com`.

## Pages and tools

- Eight original guides in Indonesian and English. Each has a worked example, a limitation and source links.
- Two browser-only calculators: paint for four walls of a rectangular room, and tile boxes from a measured area.
- Users enter product coverage and allowance. The site does not invent universal coverage, current prices or supplier availability.
- Static HTML, per-page canonicals, `hreflang` ID/EN, Article or WebPage JSON-LD, sitemap, robots.txt and ads.txt.
- GA4 `G-79X7K7H4MJ` and AdSense `ca-pub-6180580801533680` on content pages. Consent defaults denied and Funding Choices code is present. Ad serving depends on account approval and applicable consent.

## Build and check

Requires Python 3.10+ and no third-party packages:

```powershell
python build.py
python check.py
node --check assets/calculator.js
```

Commit the generated `dist/` with source files. In Cloudflare Pages, connect this repository's `main` branch, leave the build command blank and set output directory to `dist`. Attach `rumah.vijeron.com` through the Pages custom-domain workflow so Cloudflare creates the matching DNS record.

## Editorial boundaries

- `content.py` is original site copy. Sources verify definitions and method limits; no source article, image or test result is republished.
- Update the date in `build.py` only after material editorial changes.
- A paint estimate excludes ceiling, trim, primer, can sizes and site-specific surface condition. A tile estimate does not simulate layout or guarantee sufficient stock.
- Input values and results stay in the browser. GA4 tool events include only tool name and page language.
- This is not a building survey, structural design, contractor quotation or product endorsement. No real-project photographs or first-hand product tests are claimed.
