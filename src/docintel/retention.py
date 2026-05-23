from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta, timezone

from .models import DocumentRecord


@dataclass(frozen=True, slots=True)
class RetentionPolicy:
    name: str
    max_age_days: int
    sources: frozenset[str] = frozenset()
    required_tags: frozenset[str] = frozenset()

    def __post_init__(self) -> None:
        if self.max_age_days < 1:
            raise ValueError("max_age_days must be positive")

    def matches(self, document: DocumentRecord) -> bool:
        if self.sources and document.source not in self.sources:
            return False
        if self.required_tags and not self.required_tags.issubset(set(document.tags)):
            return False
        return True

    def expired(self, document: DocumentRecord, *, now: datetime | None = None) -> bool:
        timestamp = now or datetime.now(timezone.utc)
        return self.matches(document) and document.created_at <= timestamp - timedelta(days=self.max_age_days)


def select_expired(documents: list[DocumentRecord], policies: list[RetentionPolicy], *, now: datetime | None = None) -> dict[str, str]:
    expired: dict[str, str] = {}
    for document in documents:
        for policy in policies:
            if policy.expired(document, now=now):
                expired[document.id] = policy.name
                break
    return expired

# _ref-84774

# _ref-58135

# _ref-33504

# _ref-97452

# _ref-78106

# _ref-55769

# _ref-13105

# _ref-63952

# _ref-54751

# _ref-32263

# _ref-13850

# _ref-85176

# _ref-16278

# _ref-86991

# _ref-72315

# _ref-53503

# _ref-22114

# _ref-41567

# _ref-65091

# _ref-85653

# _ref-14640

# _ref-51030

# _ref-38864

# _ref-12498

# _ref-99465

# _ref-88463

# _ref-89372

# _ref-61147
