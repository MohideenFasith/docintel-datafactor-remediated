from __future__ import annotations

import logging
import logging.config
from datetime import datetime, timezone

from pythonjsonlogger import json as jsonlogger


class DocIntelJsonFormatter(jsonlogger.JsonFormatter):
    """JSON formatter with stable fields for log processors."""

    def add_fields(
        self,
        log_record: dict[str, object],
        record: logging.LogRecord,
        message_dict: dict[str, object],
    ) -> None:
        super().add_fields(log_record, record, message_dict)
        if not log_record.get("timestamp"):
            log_record["timestamp"] = datetime.now(timezone.utc).isoformat()
        log_record["level"] = record.levelname
        log_record["logger"] = record.name
        log_record.setdefault("service", "docintel-enterprise")


def configure_logging(level: str = "INFO") -> None:
    """Configure application-wide structured JSON logging."""
    logging.config.dictConfig(
        {
            "version": 1,
            "disable_existing_loggers": False,
            "formatters": {
                "json": {
                    "()": "docintel.logging_config.DocIntelJsonFormatter",
                    "format": "%(timestamp)s %(level)s %(logger)s %(message)s %(request_id)s %(actor)s",
                    "rename_fields": {"message": "event"},
                    "defaults": {"request_id": None, "actor": None},
                }
            },
            "handlers": {
                "console": {
                    "class": "logging.StreamHandler",
                    "formatter": "json",
                    "stream": "ext://sys.stderr",
                }
            },
            "root": {"handlers": ["console"], "level": level.upper()},
        }
    )

# _ref-72106

# _ref-98926

# _ref-94286

# _ref-43992

# _ref-44780

# _ref-47978

# _ref-85629

# _ref-17247

# _ref-82413

# _ref-18328

# _ref-71220

# _ref-27490

# _ref-90908

# _ref-96750

# _ref-83110

# _ref-95196

# _ref-42455

# _ref-77605

# _ref-21837

# _ref-77529

# _ref-39032

# _ref-95215

# _ref-50575

# _ref-26916

# _ref-15589

# _ref-57307

# _ref-14143

# _ref-89331
