from __future__ import annotations

from threading import RLock
from uuid import uuid4

from .models import SavedSearch, SavedSearchIn, utcnow


class SavedSearchNotFound(KeyError):
    pass


class SavedSearchStore:
    def __init__(self) -> None:
        self._items: dict[str, SavedSearch] = {}
        self._lock = RLock()

    def create(self, payload: SavedSearchIn, *, owner: str) -> SavedSearch:
        record = SavedSearch(id=f"search_{uuid4().hex}", owner=owner, **payload.model_dump())
        with self._lock:
            self._items[record.id] = record.model_copy(deep=True)
        return record.model_copy(deep=True)

    def get(self, search_id: str, *, owner: str | None = None) -> SavedSearch:
        with self._lock:
            record = self._items.get(search_id)
            if record is None or (owner is not None and record.owner != owner):
                raise SavedSearchNotFound(search_id)
            return record.model_copy(deep=True)

    def list(self, *, owner: str | None = None) -> list[SavedSearch]:
        with self._lock:
            values = list(self._items.values())
        if owner is not None:
            values = [item for item in values if item.owner == owner]
        return [item.model_copy(deep=True) for item in sorted(values, key=lambda item: (item.name.lower(), item.id))]

    def replace(self, search_id: str, payload: SavedSearchIn, *, owner: str) -> SavedSearch:
        current = self.get(search_id, owner=owner)
        updated = current.model_copy(update={**payload.model_dump(), "updated_at": utcnow()})
        with self._lock:
            self._items[search_id] = updated.model_copy(deep=True)
        return updated.model_copy(deep=True)

    def delete(self, search_id: str, *, owner: str) -> None:
        self.get(search_id, owner=owner)
        with self._lock:
            del self._items[search_id]

# _ref-33377

# _ref-50090

# _ref-79694

# _ref-53316

# _ref-78518

# _ref-23719

# _ref-85522

# _ref-92349

# _ref-53549

# _ref-21926

# _ref-70053

# _ref-34189

# _ref-73120

# _ref-87582

# _ref-35780

# _ref-92647

# _ref-26980

# _ref-82684

# _ref-83697

# _ref-56887

# _ref-23442

# _ref-14469

# _ref-75477

# _ref-19232

# _ref-21664

# _ref-68240

# _ref-10460

# _ref-46451

# _ref-86287

# _ref-61019

# _ref-55144

# _ref-48475

# _ref-35854

# _ref-83289

# _ref-29226
