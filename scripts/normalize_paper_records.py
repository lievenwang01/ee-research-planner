#!/usr/bin/env python3
"""Normalize paper metadata records into a common schema.

Supports JSON input from search_openalex.py, raw OpenAlex responses, or a plain list of records.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Normalize paper JSON records.")
    parser.add_argument("--input", required=True, help="Input JSON path.")
    parser.add_argument("--output", help="Output JSON path. Defaults to stdout.")
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def iter_records(payload: Any) -> Iterable[Dict[str, Any]]:
    if isinstance(payload, list):
        for item in payload:
            if isinstance(item, dict):
                yield item
        return

    if not isinstance(payload, dict):
        return

    if isinstance(payload.get("results"), list):
        for item in payload["results"]:
            if isinstance(item, dict):
                yield item
        return

    if isinstance(payload.get("records"), list):
        for item in payload["records"]:
            if isinstance(item, dict):
                yield item
        return


def reconstruct_abstract(inverted_index: Optional[Dict[str, List[int]]]) -> Optional[str]:
    if not inverted_index:
        return None

    positioned_tokens = []
    for token, positions in inverted_index.items():
        for position in positions:
            positioned_tokens.append((position, token))

    if not positioned_tokens:
        return None

    words = [token for _, token in sorted(positioned_tokens, key=lambda item: item[0])]
    return " ".join(words)


def normalize_doi(value: Optional[str]) -> Optional[str]:
    if not value:
        return None
    value = value.strip()
    value = re.sub(r"^https?://(dx\.)?doi\.org/", "", value, flags=re.IGNORECASE)
    return value or None


def pick_authors(record: Dict[str, Any]) -> List[str]:
    if isinstance(record.get("authors"), list):
        return [str(author) for author in record["authors"] if author]

    authors = []
    for authorship in record.get("authorships") or []:
        author = authorship.get("author") or {}
        name = author.get("display_name")
        if name:
            authors.append(name)
    return authors


def pick_venue(record: Dict[str, Any]) -> Optional[str]:
    if record.get("venue"):
        return record["venue"]
    primary_location = record.get("primary_location") or {}
    source = primary_location.get("source") or {}
    if source.get("display_name"):
        return source["display_name"]
    return None


def pick_open_access(record: Dict[str, Any]) -> Dict[str, Any]:
    existing = record.get("open_access") if isinstance(record.get("open_access"), dict) else {}
    primary_location = record.get("primary_location") or {}
    return {
        "is_oa": existing.get("is_oa"),
        "oa_status": existing.get("oa_status"),
        "oa_url": existing.get("oa_url"),
        "any_repository_has_fulltext": existing.get("any_repository_has_fulltext"),
        "landing_page_url": existing.get("landing_page_url") or primary_location.get("landing_page_url"),
        "pdf_url": existing.get("pdf_url") or primary_location.get("pdf_url"),
    }


def infer_version_hint(record: Dict[str, Any]) -> Optional[str]:
    publication_type = record.get("type") or record.get("type_crossref")
    if not publication_type:
        return None
    mapping = {
        "article": "journal",
        "journal-article": "journal",
        "proceedings-article": "conference",
        "conference-paper": "conference",
        "posted-content": "preprint",
        "preprint": "preprint",
        "dissertation": "thesis",
        "book-chapter": "book-chapter",
    }
    return mapping.get(publication_type, str(publication_type))


def normalize_record(record: Dict[str, Any], default_query: Optional[str]) -> Dict[str, Any]:
    abstract_text = reconstruct_abstract(record.get("abstract_inverted_index"))
    open_access = pick_open_access(record)
    evidence_level = "E1 abstract" if abstract_text else "E0 metadata"

    normalized = {
        "source": "openalex",
        "search_query": record.get("search_query") or default_query,
        "id": record.get("id"),
        "title": record.get("title") or record.get("display_name"),
        "authors": pick_authors(record),
        "year": record.get("year") or record.get("publication_year"),
        "venue": pick_venue(record),
        "version_hint": infer_version_hint(record) or "unknown",
        "doi": normalize_doi(record.get("doi") or (record.get("ids") or {}).get("doi")),
        "cited_count": record.get("cited_count") or record.get("cited_by_count"),
        "ids": record.get("ids") or {},
        "concepts": record.get("concepts") or [],
        "abstract_available": bool(abstract_text),
        "abstract_text": abstract_text,
        "abstract_inverted_index": record.get("abstract_inverted_index"),
        "open_access": open_access,
        "candidate_access_path": "metadata-first; OA links noted, full text not fetched",
        "evidence_level": evidence_level,
        "usage_tag_suggestion": "map",
        "normalization_note": "Metadata-normalized only. Method/setup/baseline details still require manual evidence extraction.",
    }
    return normalized


def normalize_payload(payload: Any) -> Dict[str, Any]:
    default_query = payload.get("query") if isinstance(payload, dict) else None
    records = [normalize_record(record, default_query=default_query) for record in iter_records(payload)]
    return {
        "schema": "ee-research-planner.paper-record.v1",
        "source": payload.get("source", "unknown") if isinstance(payload, dict) else "unknown",
        "query": default_query,
        "record_count": len(records),
        "records": records,
    }


def main() -> int:
    args = parse_args()
    payload = load_json(Path(args.input))
    normalized = normalize_payload(payload)
    rendered = json.dumps(normalized, ensure_ascii=False, indent=2, sort_keys=True)

    if args.output:
        Path(args.output).write_text(rendered + "\n", encoding="utf-8")
    else:
        sys.stdout.write(rendered)
        sys.stdout.write("\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())