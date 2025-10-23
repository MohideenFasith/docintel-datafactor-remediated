from __future__ import annotations

import argparse
import json
from pathlib import Path

from .models import DocumentIn
from .service import DocumentService


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="docintel", description="DocIntel local utility")
    sub = parser.add_subparsers(dest="command", required=True)

    ingest = sub.add_parser("ingest", help="ingest a UTF-8 text file")
    ingest.add_argument("path", type=Path)
    ingest.add_argument("--title")
    ingest.add_argument("--tag", action="append", default=[])

    search = sub.add_parser("search", help="search documents ingested during the same process")
    search.add_argument("query")
    search.add_argument("--limit", type=int, default=10)
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    service = DocumentService()
    if args.command == "ingest":
        text = args.path.read_text(encoding="utf-8")
        record = service.ingest(
            DocumentIn(title=args.title or args.path.name, content=text, source="cli", tags=args.tag),
            actor="cli",
        )
        print(record.model_dump_json(indent=2))
        return 0
    if args.command == "search":
        print(json.dumps(service.search(args.query, args.limit).model_dump(mode="json"), indent=2))
        return 0
    return 2


if __name__ == "__main__":
    raise SystemExit(main())

# _ref-63737

# _ref-28920

# _ref-76724

# _ref-53699

# _ref-89282

# _ref-74069

# _ref-22662

# _ref-28834

# _ref-99711

# _ref-22788

# _ref-21719

# _ref-33022

# _ref-91009

# _ref-44637

# _ref-69080

# _ref-39604

# _ref-12842

# _ref-79675

# _ref-13745
