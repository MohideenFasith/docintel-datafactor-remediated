from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timezone
from threading import RLock
from uuid import uuid4


def _now() -> datetime:
    return datetime.now(timezone.utc)


@dataclass(slots=True)
class Collection:
    id: str
    name: str
    description: str = ""
    document_ids: set[str] = field(default_factory=set)
    created_at: datetime = field(default_factory=_now)
    updated_at: datetime = field(default_factory=_now)


class CollectionStore:
    def __init__(self) -> None:
        self._collections: dict[str, Collection] = {}
        self._lock = RLock()

    @staticmethod
    def _copy(item: Collection) -> Collection:
        return Collection(
            id=item.id,
            name=item.name,
            description=item.description,
            document_ids=set(item.document_ids),
            created_at=item.created_at,
            updated_at=item.updated_at,
        )

    def create(self, name: str, description: str = "") -> Collection:
        name = name.strip()
        if not name:
            raise ValueError("collection name must not be blank")
        with self._lock:
            if any(item.name.casefold() == name.casefold() for item in self._collections.values()):
                raise ValueError("collection name already exists")
            item = Collection(id=f"col_{uuid4().hex}", name=name, description=description.strip())
            self._collections[item.id] = item
            return self._copy(item)

    def get(self, collection_id: str) -> Collection:
        with self._lock:
            if collection_id not in self._collections:
                raise KeyError(collection_id)
            return self._copy(self._collections[collection_id])

    def list(self) -> list[Collection]:
        with self._lock:
            return sorted((self._copy(item) for item in self._collections.values()), key=lambda item: item.name.casefold())

    def add_document(self, collection_id: str, document_id: str) -> Collection:
        with self._lock:
            item = self._collections.get(collection_id)
            if item is None:
                raise KeyError(collection_id)
            item.document_ids.add(document_id)
            item.updated_at = _now()
            return self._copy(item)

    def remove_document(self, collection_id: str, document_id: str) -> Collection:
        with self._lock:
            item = self._collections.get(collection_id)
            if item is None:
                raise KeyError(collection_id)
            item.document_ids.discard(document_id)
            item.updated_at = _now()
            return self._copy(item)

    def delete(self, collection_id: str) -> None:
        with self._lock:
            if self._collections.pop(collection_id, None) is None:
                raise KeyError(collection_id)

# _ref-91971

# _ref-33204

# _ref-59467

# _ref-24869

# _ref-97993

# _ref-31328

# _ref-65934

# _ref-75282

# _ref-26563

# _ref-60566

# _ref-63516

# _ref-52823

# _ref-39865

# _ref-64684

# _ref-72425

# _ref-20863

# _ref-58526

# _ref-35223

# _ref-76745

# _ref-70341

# _ref-73254

# _ref-44859

# _ref-11643

# _ref-28510

# _ref-63532

# _ref-93409

# _ref-34199

# _ref-43669

# _ref-58412

# _ref-34998
