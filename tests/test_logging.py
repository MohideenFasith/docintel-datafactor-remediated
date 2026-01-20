from __future__ import annotations

import json
import logging
from io import StringIO

from docintel.logging_config import DocIntelJsonFormatter, configure_logging


def test_configure_logging_installs_json_formatter() -> None:
    configure_logging("INFO")
    root = logging.getLogger()
    assert root.handlers
    assert isinstance(root.handlers[0].formatter, DocIntelJsonFormatter)


def test_json_log_contains_correlation_fields() -> None:
    stream = StringIO()
    handler = logging.StreamHandler(stream)
    handler.setFormatter(
        DocIntelJsonFormatter(
            "%(timestamp)s %(level)s %(logger)s %(message)s %(request_id)s %(actor)s",
            rename_fields={"message": "event"},
            defaults={"request_id": None, "actor": None},
        )
    )
    logger = logging.getLogger("docintel.integration")
    logger.handlers = [handler]
    logger.propagate = False
    logger.setLevel(logging.INFO)

    logger.info(
        "document_ingested",
        extra={"request_id": "req-42", "actor": "writer", "document_id": "doc-7"},
    )

    payload = json.loads(stream.getvalue())
    assert payload["event"] == "document_ingested"
    assert payload["request_id"] == "req-42"
    assert payload["actor"] == "writer"
    assert payload["document_id"] == "doc-7"
    assert payload["service"] == "docintel-enterprise"

# _ref-57147

# _ref-54127

# _ref-24875

# _ref-82957

# _ref-89938

# _ref-56421

# _ref-83402

# _ref-74631

# _ref-20185

# _ref-49743

# _ref-45249

# _ref-36860

# _ref-23804

# _ref-99823

# _ref-28772

# _ref-58981

# _ref-62957

# _ref-71257

# _ref-40338

# _ref-92043

# _ref-80809

# _ref-16010

# _ref-48417

# _ref-75641
