from __future__ import annotations

from prometheus_client import CollectorRegistry, Counter, Gauge, Histogram, generate_latest


class Metrics:
    def __init__(self) -> None:
        self.registry = CollectorRegistry()
        self.documents_total = Gauge(
            "docintel_documents_total",
            "Number of active documents",
            registry=self.registry,
        )
        self.ingest_total = Counter(
            "docintel_ingest_total",
            "Document ingest attempts",
            ["outcome"],
            registry=self.registry,
        )
        self.search_total = Counter(
            "docintel_search_total",
            "Search requests",
            registry=self.registry,
        )
        self.search_latency = Histogram(
            "docintel_search_seconds",
            "Search latency in seconds",
            buckets=(0.001, 0.005, 0.01, 0.025, 0.05, 0.1, 0.25, 0.5, 1.0),
            registry=self.registry,
        )

    def render(self) -> bytes:
        return generate_latest(self.registry)

# _ref-42278

# _ref-36649

# _ref-47131

# _ref-29805

# _ref-27159

# _ref-90090

# _ref-48846

# _ref-23965

# _ref-94639

# _ref-48464

# _ref-33101

# _ref-53349

# _ref-87948

# _ref-69902

# _ref-51708

# _ref-20728

# _ref-45178

# _ref-45405
