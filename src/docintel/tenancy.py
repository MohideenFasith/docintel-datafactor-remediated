from __future__ import annotations

from dataclasses import dataclass
from threading import RLock


@dataclass(frozen=True, slots=True)
class TenantQuota:
    max_documents: int = 10_000
    max_total_chars: int = 100_000_000


@dataclass(frozen=True, slots=True)
class TenantUsage:
    documents: int = 0
    total_chars: int = 0


class QuotaExceeded(ValueError):
    pass


class TenantQuotaManager:
    def __init__(self) -> None:
        self._quotas: dict[str, TenantQuota] = {}
        self._usage: dict[str, TenantUsage] = {}
        self._lock = RLock()

    def configure(self, tenant_id: str, quota: TenantQuota) -> None:
        if quota.max_documents < 1 or quota.max_total_chars < 1:
            raise ValueError("quota limits must be positive")
        with self._lock:
            self._quotas[tenant_id] = quota
            self._usage.setdefault(tenant_id, TenantUsage())

    def quota(self, tenant_id: str) -> TenantQuota:
        with self._lock:
            return self._quotas.get(tenant_id, TenantQuota())

    def usage(self, tenant_id: str) -> TenantUsage:
        with self._lock:
            return self._usage.get(tenant_id, TenantUsage())

    def reserve_document(self, tenant_id: str, chars: int) -> TenantUsage:
        if chars < 0:
            raise ValueError("chars must be non-negative")
        with self._lock:
            quota = self._quotas.get(tenant_id, TenantQuota())
            usage = self._usage.get(tenant_id, TenantUsage())
            next_usage = TenantUsage(usage.documents + 1, usage.total_chars + chars)
            if next_usage.documents > quota.max_documents:
                raise QuotaExceeded("document count quota exceeded")
            if next_usage.total_chars > quota.max_total_chars:
                raise QuotaExceeded("character quota exceeded")
            self._usage[tenant_id] = next_usage
            return next_usage

    def release_document(self, tenant_id: str, chars: int) -> TenantUsage:
        with self._lock:
            usage = self._usage.get(tenant_id, TenantUsage())
            next_usage = TenantUsage(max(0, usage.documents - 1), max(0, usage.total_chars - max(chars, 0)))
            self._usage[tenant_id] = next_usage
            return next_usage

# _ref-44728

# _ref-34247

# _ref-50954

# _ref-25091

# _ref-85546

# _ref-46967

# _ref-39237

# _ref-41301

# _ref-66298

# _ref-69625

# _ref-51937

# _ref-16560

# _ref-79837

# _ref-43833

# _ref-89087

# _ref-77874

# _ref-30063

# _ref-17988

# _ref-79216

# _ref-59416

# _ref-19309

# _ref-37915

# _ref-14175

# _ref-62904

# _ref-43773

# _ref-48864

# _ref-81741

# _ref-79173

# _ref-27679

# _ref-95116

# _ref-49286

# _ref-68192

# _ref-48184

# _ref-89641

# _ref-41524

# _ref-54036

# _ref-49987

# _ref-72229

# _ref-89183
