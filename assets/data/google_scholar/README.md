# Google Scholar citation data

This directory replaces the old scheduled Google Scholar crawler.

Update `gs_data.json` manually when citation counts change. The site reads:

- `citedby`: total citation count.
- `publications`: optional per-paper counts keyed by Google Scholar paper ID.

Example:

```json
{
  "name": "Yuanzhe Hu",
  "citedby": 123,
  "updated": "2026-05-01",
  "publications": {
    "ehBiQEUAAAAJ:paper_id": {
      "num_citations": 12
    }
  }
}
```
