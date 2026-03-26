from __future__ import annotations

import hashlib
import hmac
import time
from collections import defaultdict, deque
from dataclasses import dataclass
from threading import RLock

from .errors import PermissionDenied, RateLimitExceeded


@dataclass(frozen=True, slots=True)
class Principal:
    name: str
    role: str


class ApiKeyAuthenticator:
    def __init__(self, api_key: str | None = None, admin_api_key: str | None = None) -> None:
        self._api_key_digest = self._digest(api_key) if api_key else None
        self._admin_digest = self._digest(admin_api_key) if admin_api_key else None

    @staticmethod
    def _digest(value: str) -> bytes:
        return hashlib.sha256(value.encode()).digest()

    def authenticate(self, provided: str | None) -> Principal:
        if self._api_key_digest is None and self._admin_digest is None:
            return Principal(name="anonymous", role="admin")
        if not provided:
            raise PermissionDenied("missing API key")
        digest = self._digest(provided)
        if self._admin_digest and hmac.compare_digest(digest, self._admin_digest):
            return Principal(name="admin-key", role="admin")
        if self._api_key_digest and hmac.compare_digest(digest, self._api_key_digest):
            return Principal(name="api-key", role="writer")
        raise PermissionDenied("invalid API key")

    @staticmethod
    def require(principal: Principal, *roles: str) -> None:
        if principal.role not in roles:
            raise PermissionDenied(f"role {principal.role!r} is not allowed")


class SlidingWindowRateLimiter:
    def __init__(self, limit: int, window_seconds: float = 60.0) -> None:
        if limit < 1 or window_seconds <= 0:
            raise ValueError("invalid rate limiter configuration")
        self.limit = limit
        self.window_seconds = window_seconds
        self._events: dict[str, deque[float]] = defaultdict(deque)
        self._lock = RLock()

    def check(self, key: str, *, now: float | None = None) -> int:
        timestamp = time.monotonic() if now is None else now
        threshold = timestamp - self.window_seconds
        with self._lock:
            events = self._events[key]
            while events and events[0] <= threshold:
                events.popleft()
            if len(events) >= self.limit:
                retry_after = max(1, int(events[0] + self.window_seconds - timestamp + 0.999))
                raise RateLimitExceeded(str(retry_after))
            events.append(timestamp)
            return self.limit - len(events)

# _ref-39855

# _ref-28144

# _ref-68174

# _ref-46816

# _ref-88412

# _ref-65101

# _ref-16610

# _ref-39150

# _ref-90439

# _ref-59788

# _ref-93666

# _ref-29246

# _ref-31444

# _ref-67807

# _ref-60367

# _ref-65731

# _ref-77516

# _ref-35475

# _ref-94074

# _ref-59033

# _ref-20532

# _ref-89970

# _ref-56353

# _ref-39715

# _ref-50590

# _ref-36133

# _ref-65321
