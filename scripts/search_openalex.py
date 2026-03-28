#!/usr/bin/env python3
"""Search OpenAlex works and export a compact JSON payload.

This script is intentionally metadata-first: it does not fetch full text.
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from typing import Any, Dict, List, Optional
from urllib.parse import urlencode
from urllib.request import Request, urlopen

API_URL = "https://api.openalex.org/works"
MAX_PER_PAGE = 200
DEFAULT_TIMEOUT = 30


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Search OpenAlex works by query.")
    parser.add_argument("--query", required=True, help="Search query string.")
    parser.add_argument("--limit", type=int, default=10, help="Maximum number of records to return.")
    parser.add_argument(
        "--per-page",
        type=int,
        default=25,
        help="Results per page (max 200).",
    )
    parser.add_argument("--output", help="Write JSON output to this path. Defaults to stdout.")
    parser.add_argument(
        "--mailto",
        default=os.environ.get("OPENALEX_MAILTO"),
        help="Optional contact email for polite OpenAlex requests.",
    )
    parser.add_argument(
        "--sleep-seconds",
        type=float,
        default=0.1,
        help="Small delay between page requests.",
    )
    return parser.parse_args()


def build_url(query: str, per_page: int, page: int, mailto: Optional[str]) -> str:
    params = {
        "search": query,
        "per-page": min(max(per_page, 1), MAX_PER_PAGE),
        "page": max(page, 1),
    }
    if mailto:
        params["mailto"] = mailto
    return f"{API_URL}?{urlencode(params)}"


def fetch_json(url: str) -> Dict[str, Any]:
    request = Request(
        url,
        headers={
            "User-Agent": "ee-research-planner-openalex-search/1.0",
            "Accept": "application/json",
        },
    )
    with urlopen(request, timeout=DEFAULT_TIMEOUT) as response:
        return json.load(response)


def pick_venue(record: Dict[str, Any]) -> Optional[str]:
    primary_location = record.get("primary_location") or {}
    source = primary_location.get("source") or {}
    if source.get("display_name"):
        return source["display_name"]
    host_venue = record.get("host_venue") or {}
    if host_venue.get("display_name"):
        return host_venue["display_name"]
    return None


def pick_authors(record: Dict[str, Any]) -> List[str]:
    authors = []
    for authorship in record.get("authorships") or []:
        author = authorship.get("author") or {}
        name = author.get("display_name")
        if name:
            authors.append(name)
    return authors


def simplify_record(record: Dict[str, Any]) -> Dict[str, Any]:
    open_access = record.get("open_access") or {}
    primary_location = record.get("primary_location") or {}
    concepts = record.get("concepts") or []
    return {
        "id": record.get("id"),
        "title": record.get("display_name"),
        "year": record.get("publication_year"),
        "venue": pick_venue(record),
        "type": record.get("type"),
        "doi": record.get("doi"),
        "cited_count": record.get("cited_by_count"),
        "authors": pick_authors(record),
        "abstract_inverted_index": record.get("abstract_inverted_index"),
        "ids": record.get("ids") or {},
        "open_access": {
            "is_oa": open_access.get("is_oa"),
            "oa_status": open_access.get("oa_status"),
            "oa_url": open_access.get("oa_url"),
            "any_repository_has_fulltext": open_access.get("any_repository_has_fulltext"),
            "landing_page_url": primary_location.get("landing_page_url"),
            "pdf_url": primary_location.get("pdf_url"),
        },
        "concepts": [
            {
                "display_name": concept.get("display_name"),
                "score": concept.get("score"),
            }
            for concept in concepts[:8]
            if concept.get("display_name")
        ],
    }


def collect_results(query: str, limit: int, per_page: int, mailto: Optional[str], sleep_seconds: float) -> Dict[str, Any]:
    results: List[Dict[str, Any]] = []
    meta: Dict[str, Any] = {}
    page = 1

    while len(results) < limit:
        url = build_url(query=query, per_page=per_page, page=page, mailto=mailto)
        payload = fetch_json(url)
        if not meta:
            meta = payload.get("meta") or {}
        page_results = payload.get("results") or []
        if not page_results:
            break

        for record in page_results:
            results.append(simplify_record(record))
            if len(results) >= limit:
                break

        page += 1
        if len(results) < limit:
            time.sleep(max(sleep_seconds, 0.0))

    return {
        "source": "openalex",
        "query": query,
        "requested_limit": limit,
        "per_page": min(max(per_page, 1), MAX_PER_PAGE),
        "retrieved_count": len(results),
        "api_meta": meta,
        "results": results,
    }


def main() -> int:
    args = parse_args()
    if args.limit < 1:
        raise SystemExit("--limit must be >= 1")
    if args.per_page < 1:
        raise SystemExit("--per-page must be >= 1")

    payload = collect_results(
        query=args.query,
        limit=args.limit,
        per_page=args.per_page,
        mailto=args.mailto,
        sleep_seconds=args.sleep_seconds,
    )

    rendered = json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(rendered)
            f.write("\n")
    else:
        sys.stdout.write(rendered)
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())