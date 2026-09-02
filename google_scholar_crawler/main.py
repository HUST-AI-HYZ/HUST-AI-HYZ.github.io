#!/usr/bin/env python3
"""Fetch publication citation counts from a public Google Scholar profile."""

from __future__ import annotations

import argparse
import html
import json
import os
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path


PROFILE_URL = "https://scholar.google.com/citations"
USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/134.0.0.0 Safari/537.36"
)


def clean_text(value: str) -> str:
    value = re.sub(r"<[^>]+>", "", value)
    return " ".join(html.unescape(value).split())


def fetch_profile(author_id: str, attempts: int) -> tuple[str, str]:
    query = urllib.parse.urlencode(
        {
            "hl": "en",
            "user": author_id,
            "pagesize": 100,
            "view_op": "list_works",
            "sortby": "pubdate",
        }
    )
    url = f"{PROFILE_URL}?{query}"
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept-Language": "en-US,en;q=0.9",
        },
    )

    last_error: Exception | None = None
    for attempt in range(1, attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=30) as response:
                document = response.read().decode("utf-8")
            if "gsc_a_tr" not in document:
                raise RuntimeError("Google Scholar returned a page without publications")
            return url, document
        except (urllib.error.URLError, TimeoutError, RuntimeError) as error:
            last_error = error
            print(
                f"Scholar fetch attempt {attempt}/{attempts} failed: {error}",
                file=sys.stderr,
            )
            if attempt < attempts:
                time.sleep(5 * attempt)

    raise RuntimeError(
        f"Unable to fetch Google Scholar after {attempts} attempts: {last_error}"
    ) from last_error


def parse_profile(author_id: str, source_url: str, document: str) -> dict:
    name_match = re.search(
        r'<meta\s+property="og:title"\s+content="([^"]+)"', document
    )
    citedby_match = re.search(r"Cited by\s+([\d,]+)", html.unescape(document))
    if not name_match or not citedby_match:
        raise RuntimeError("Unable to parse the Scholar profile metadata")

    publications: dict[str, dict[str, object]] = {}
    rows = re.findall(r'<tr\s+class="gsc_a_tr">(.*?)</tr>', document, re.DOTALL)
    for row in rows:
        paper_id_match = re.search(r'citation_for_view=([^&"]+)', row)
        title_match = re.search(
            r'<a(?=[^>]*\bclass="[^"]*\bgsc_a_at\b[^"]*")[^>]*>(.*?)</a>',
            row,
            re.DOTALL,
        )
        citation_match = re.search(
            r'<a(?=[^>]*\bclass="[^"]*\bgsc_a_ac\b[^"]*")[^>]*>(.*?)</a>',
            row,
            re.DOTALL,
        )
        if not paper_id_match or not title_match:
            continue

        paper_id = html.unescape(paper_id_match.group(1))
        if not paper_id.startswith(f"{author_id}:"):
            continue

        citation_text = clean_text(citation_match.group(1)) if citation_match else ""
        publications[paper_id] = {
            "title": clean_text(title_match.group(1)),
            "num_citations": int(citation_text.replace(",", ""))
            if citation_text
            else 0,
        }

    if not publications:
        raise RuntimeError("Unable to parse any publications from the Scholar profile")

    return {
        "name": html.unescape(name_match.group(1)),
        "citedby": int(citedby_match.group(1).replace(",", "")),
        "updated": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "source": source_url,
        "publications": publications,
    }


def comparable(data: dict) -> dict:
    return {key: value for key, value in data.items() if key != "updated"}


def write_if_changed(output_path: Path, data: dict) -> bool:
    if output_path.exists():
        try:
            existing = json.loads(output_path.read_text(encoding="utf-8"))
            if comparable(existing) == comparable(data):
                print("Citation counts have not changed.")
                return False
        except (json.JSONDecodeError, OSError):
            pass

    output_path.parent.mkdir(parents=True, exist_ok=True)
    temporary_path = output_path.with_suffix(f"{output_path.suffix}.tmp")
    temporary_path.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    temporary_path.replace(output_path)
    print(
        f"Updated {len(data['publications'])} publications "
        f"({data['citedby']} total citations) in {output_path}."
    )
    return True


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--author-id",
        default=os.environ.get("GOOGLE_SCHOLAR_ID", ""),
        help="Google Scholar user ID (or set GOOGLE_SCHOLAR_ID)",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("google_scholar_crawler/results/gs_data.json"),
    )
    parser.add_argument("--attempts", type=int, default=4)
    args = parser.parse_args()

    if not args.author_id:
        parser.error("--author-id or GOOGLE_SCHOLAR_ID is required")

    source_url, document = fetch_profile(args.author_id, max(args.attempts, 1))
    data = parse_profile(args.author_id, source_url, document)
    write_if_changed(args.output, data)


if __name__ == "__main__":
    main()
