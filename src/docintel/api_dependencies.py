from __future__ import annotations

from fastapi import Depends, Header, HTTPException, Request, status

from .annotations import Annotation
from .errors import PermissionDenied, RateLimitExceeded
from .security import ApiKeyAuthenticator, Principal, SlidingWindowRateLimiter
from .service import DocumentService


def annotation_response(item: Annotation) -> dict[str, object]:
    """Serialize set-backed labels deterministically at the HTTP boundary."""
    return {
        "id": item.id,
        "document_id": item.document_id,
        "author": item.author,
        "body": item.body,
        "labels": sorted(item.labels),
        "created_at": item.created_at,
        "updated_at": item.updated_at,
    }


def service_from_request(request: Request) -> DocumentService:
    return request.app.state.service


def authenticator_from_request(request: Request) -> ApiKeyAuthenticator:
    return request.app.state.authenticator


def limiter_from_request(request: Request) -> SlidingWindowRateLimiter:
    return request.app.state.rate_limiter


def principal(
    request: Request,
    x_api_key: str | None = Header(default=None),
    auth: ApiKeyAuthenticator = Depends(authenticator_from_request),
) -> Principal:
    try:
        result = auth.authenticate(x_api_key)
        key = f"{result.name}:{request.client.host if request.client else 'local'}"
        limiter_from_request(request).check(key)
        return result
    except PermissionDenied as exc:
        raise HTTPException(status.HTTP_401_UNAUTHORIZED, str(exc)) from exc
    except RateLimitExceeded as exc:
        raise HTTPException(
            status.HTTP_429_TOO_MANY_REQUESTS,
            "rate limit exceeded",
            headers={"Retry-After": str(exc)},
        ) from exc

# _ref-92079

# _ref-93393

# _ref-67155

# _ref-11884

# _ref-86058

# _ref-55042

# _ref-92290
