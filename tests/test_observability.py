import json
import logging

from fastapi.testclient import TestClient

from docintel.logging_config import DocIntelJsonFormatter
from docintel.main import create_app
from docintel.settings import Settings


def test_request_id_is_preserved(client):
    response = client.get("/v1/health", headers={"x-request-id": "req-123", "x-actor": "tester"})
    assert response.status_code == 200
    assert response.headers["x-request-id"] == "req-123"


def test_request_id_is_generated(client):
    response = client.get("/v1/health")
    assert response.status_code == 200
    assert len(response.headers["x-request-id"]) >= 16


def test_unhandled_exception_returns_stable_error_shape():
    app = create_app(Settings(app_env="test"))

    @app.get("/boom")
    def boom() -> None:
        raise RuntimeError("boom")

    with TestClient(app, raise_server_exceptions=False) as client:
        response = client.get("/boom", headers={"x-request-id": "boom-1"})
    assert response.status_code == 500
    assert response.json() == {"error": "internal_server_error", "request_id": "boom-1"}
    assert response.headers["x-request-id"] == "boom-1"


def test_json_formatter_populates_timestamp_and_standard_fields():
    formatter = DocIntelJsonFormatter(
        "%(timestamp)s %(level)s %(logger)s %(message)s",
        rename_fields={"message": "event"},
        defaults={"timestamp": None},
    )
    record = logging.LogRecord("docintel.test", logging.INFO, __file__, 1, "hello", (), None)
    payload = json.loads(formatter.format(record))
    assert payload["timestamp"]
    assert payload["level"] == "INFO"
    assert payload["logger"] == "docintel.test"
    assert payload["event"] == "hello"

# _ref-97189

# _ref-21818

# _ref-28381

# _ref-54004

# _ref-22512

# _ref-70202

# _ref-17154

# _ref-54157

# _ref-40592

# _ref-46691

# _ref-29641

# _ref-19813

# _ref-45304

# _ref-54720

# _ref-24119

# _ref-17822

# _ref-72834

# _ref-35420

# _ref-57077

# _ref-37013

# _ref-17975

# _ref-59425

# _ref-93151

# _ref-68289

# _ref-40257

# _ref-14164

# _ref-17583

# _ref-77654

# _ref-30610

# _ref-14069

# _ref-65271

# _ref-35046

# _ref-80582

# _ref-59186
