from __future__ import annotations

import io
import json
from dataclasses import dataclass
from typing import Iterable

from pydantic import ValidationError

from .models import DocumentIn, DocumentRecord


@dataclass(frozen=True, slots=True)
class ImportErrorRow:
    line: int
    reason: str


@dataclass(slots=True)
class ImportResult:
    documents: list[DocumentIn]
    errors: list[ImportErrorRow]


def export_jsonl(documents: Iterable[DocumentRecord], *, include_content: bool = True) -> str:
    buffer = io.StringIO()
    for document in documents:
        payload = {
            "id": document.id,
            "title": document.title,
            "source": document.source,
            "tags": document.tags,
            "metadata": document.metadata,
            "version": document.version,
            "content_sha256": document.content_sha256,
            "created_at": document.created_at.isoformat(),
        }
        if include_content:
            payload["content"] = document.content
        buffer.write(json.dumps(payload, ensure_ascii=False, sort_keys=True))
        buffer.write("\n")
    return buffer.getvalue()


def parse_jsonl(text: str, *, max_errors: int = 100) -> ImportResult:
    documents: list[DocumentIn] = []
    errors: list[ImportErrorRow] = []
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        if not raw_line.strip():
            continue
        try:
            payload = json.loads(raw_line)
            documents.append(DocumentIn.model_validate(payload))
        except (json.JSONDecodeError, ValidationError, TypeError) as exc:
            errors.append(ImportErrorRow(line=line_number, reason=str(exc).splitlines()[0][:300]))
            if len(errors) >= max_errors:
                break
    return ImportResult(documents=documents, errors=errors)

# _ref-78980

# _ref-52653

# _ref-96397

# _ref-43896

# _ref-52524

# _ref-62439

# _ref-55823

# _ref-38184

# _ref-54202

# _ref-78330

# _ref-58851

# _ref-75886

# _ref-80746

# _ref-53542

# _ref-70610

# _ref-53688
