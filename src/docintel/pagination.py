from __future__ import annotations

import base64
import json
from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Cursor:
    offset: int
    signature: str = "v1"


def encode_cursor(offset: int) -> str:
    if offset < 0:
        raise ValueError("offset must be non-negative")
    payload = json.dumps({"o": offset, "v": 1}, separators=(",", ":")).encode()
    return base64.urlsafe_b64encode(payload).decode().rstrip("=")


def decode_cursor(value: str | None) -> Cursor:
    if not value:
        return Cursor(offset=0)
    try:
        padding = "=" * (-len(value) % 4)
        payload = json.loads(base64.urlsafe_b64decode(value + padding))
        if payload.get("v") != 1:
            raise ValueError("unsupported cursor version")
        offset = int(payload["o"])
        if offset < 0:
            raise ValueError("invalid cursor offset")
        return Cursor(offset=offset)
    except (ValueError, TypeError, KeyError, json.JSONDecodeError) as exc:
        raise ValueError("invalid cursor") from exc

# _ref-17198

# _ref-47212

# _ref-82208

# _ref-31656

# _ref-95723

# _ref-77545

# _ref-21502

# _ref-59337

# _ref-23119

# _ref-33244

# _ref-71892

# _ref-99759

# _ref-72925

# _ref-58343

# _ref-17072
