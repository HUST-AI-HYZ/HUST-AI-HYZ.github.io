# Google Scholar citation data

Citation data is refreshed automatically by
`.github/workflows/update_google_scholar_citations.yml`. The workflow runs
daily and can also be started from the GitHub Actions page with
`workflow_dispatch`.

The crawler reads the public Google Scholar profile and updates
`gs_data.json` only when citation counts change. The website fetches this file
from the repository at runtime, with the deployed local copy as a fallback.
Paper badges are rendered only when `num_citations` is greater than 20.

The site reads:

- `citedby`: total citation count.
- `updated`: timestamp of the last changed citation data.
- `source`: public Google Scholar profile URL.
- `publications`: per-paper counts keyed by Google Scholar paper ID.

Example:

```json
{
  "name": "Yuanzhe Hu",
  "citedby": 525,
  "updated": "2026-09-02T19:07:33+00:00",
  "source": "https://scholar.google.com/citations?...",
  "publications": {
    "ehBiQEUAAAAJ:paper_id": {
      "num_citations": 12
    }
  }
}
```
