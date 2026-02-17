from __future__ import annotations

import logging

import sentry_sdk

logger = logging.getLogger(__name__)


def configure_error_tracking(dsn: str | None, environment: str) -> bool:
    """Configure Sentry when a DSN is present; remain a no-op otherwise."""
    if not dsn:
        logger.info(
            "error_tracking_disabled",
            extra={"environment": environment, "provider": "sentry"},
        )
        return False

    sentry_sdk.init(
        dsn=dsn,
        environment=environment,
        send_default_pii=False,
        traces_sample_rate=0.0,
    )
    logger.info(
        "error_tracking_enabled",
        extra={"environment": environment, "provider": "sentry"},
    )
    return True


def capture_exception(error: BaseException, *, request_id: str | None = None) -> None:
    """Capture an unhandled error and attach the request id for correlation."""
    with sentry_sdk.new_scope() as scope:
        if request_id:
            scope.set_tag("request_id", request_id)
        sentry_sdk.capture_exception(error)

# _ref-44329

# _ref-11686

# _ref-84683

# _ref-91550

# _ref-14808

# _ref-32138

# _ref-27145

# _ref-89990

# _ref-80851

# _ref-42536

# _ref-85693

# _ref-53849

# _ref-97677

# _ref-33493

# _ref-80872

# _ref-20757

# _ref-42007

# _ref-69693

# _ref-18310

# _ref-84778

# _ref-74817

# _ref-29822

# _ref-75305

# _ref-45999
