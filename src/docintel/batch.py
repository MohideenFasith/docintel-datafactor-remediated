from __future__ import annotations

from dataclasses import dataclass, field

from .errors import DocIntelError
from .models import DocumentIn, DocumentRecord
from .service import DocumentService


@dataclass(slots=True)
class BatchFailure:
    index: int
    title: str
    error: str


@dataclass(slots=True)
class BatchResult:
    succeeded: list[DocumentRecord] = field(default_factory=list)
    failed: list[BatchFailure] = field(default_factory=list)


class BatchIngestor:
    def __init__(self, service: DocumentService) -> None:
        self.service = service

    def ingest(self, documents: list[DocumentIn], *, actor: str = "batch", stop_on_error: bool = False) -> BatchResult:
        result = BatchResult()
        for index, document in enumerate(documents):
            try:
                result.succeeded.append(self.service.ingest(document, actor=actor))
            except (DocIntelError, ValueError) as exc:
                result.failed.append(BatchFailure(index=index, title=document.title, error=str(exc)))
                if stop_on_error:
                    break
        return result

# _ref-17865

# _ref-61289

# _ref-69657

# _ref-50884

# _ref-28358

# _ref-89724

# _ref-20367

# _ref-97881

# _ref-56735

# _ref-49437

# _ref-28384

# _ref-84838

# _ref-61846

# _ref-10427

# _ref-47860

# _ref-93617

# _ref-87320

# _ref-83849

# _ref-44982

# _ref-11587

# _ref-67310

# _ref-92597

# _ref-86422

# _ref-54838

# _ref-41777

# _ref-51771

# _ref-24246

# _ref-57386

# _ref-20423
