from __future__ import annotations

from collections import deque
from threading import RLock
from uuid import uuid4

from .models import AuditEvent


class AuditLog:
    def __init__(self, max_events: int = 10_000) -> None:
        if max_events < 1:
            raise ValueError("max_events must be positive")
        self._events: deque[AuditEvent] = deque(maxlen=max_events)
        self._lock = RLock()

    def record(
        self,
        *,
        actor: str,
        action: str,
        resource_type: str,
        resource_id: str,
        outcome: str = "success",
        detail: dict | None = None,
    ) -> AuditEvent:
        event = AuditEvent(
            id=f"aud_{uuid4().hex}",
            actor=actor,
            action=action,
            resource_type=resource_type,
            resource_id=resource_id,
            outcome=outcome,
            detail=detail or {},
        )
        with self._lock:
            self._events.append(event)
        return event

    def list(self, *, limit: int = 100, actor: str | None = None, action: str | None = None) -> list[AuditEvent]:
        with self._lock:
            events = list(self._events)
        events.reverse()
        if actor:
            events = [event for event in events if event.actor == actor]
        if action:
            events = [event for event in events if event.action == action]
        return events[:limit]

# _ref-50240

# _ref-24709

# _ref-88250

# _ref-50037

# _ref-97221

# _ref-76167

# _ref-55178

# _ref-97104

# _ref-61863

# _ref-37866

# _ref-94564

# _ref-71708

# _ref-63943

# _ref-49374

# _ref-12846

# _ref-80844

# _ref-38997

# _ref-74065

# _ref-81808

# _ref-60732
