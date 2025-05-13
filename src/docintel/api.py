from __future__ import annotations

from fastapi import APIRouter, Depends, HTTPException, Query, Request, Response, status

from .api_dependencies import principal, service_from_request
from .api_features import router as feature_router
from .errors import DocumentNotFound, DuplicateDocument, InvalidDocument
from .models import DocumentIn, DocumentPatch
from .security import Principal
from .service import DocumentService

router = APIRouter()


@router.get("/health")
def health(request: Request) -> dict:
    return {"status": "ok", "environment": request.app.state.settings.app_env}


@router.get("/ready")
def ready(service: DocumentService = Depends(service_from_request)) -> dict:
    return {"status": "ready", **service.stats()}


@router.post("/documents", status_code=status.HTTP_201_CREATED)
def ingest(
    payload: DocumentIn,
    user: Principal = Depends(principal),
    service: DocumentService = Depends(service_from_request),
):
    try:
        return service.ingest(payload, actor=user.name)
    except DuplicateDocument as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, f"duplicate of {exc}") from exc
    except InvalidDocument as exc:
        raise HTTPException(status.HTTP_413_REQUEST_ENTITY_TOO_LARGE, str(exc)) from exc


@router.get("/documents")
def list_documents(
    offset: int = Query(default=0, ge=0),
    limit: int = Query(default=50, ge=1, le=100),
    source: str | None = None,
    tag: str | None = None,
    _: Principal = Depends(principal),
    service: DocumentService = Depends(service_from_request),
):
    return service.list(offset=offset, limit=limit, source=source, tag=tag)


@router.get("/documents/{document_id}")
def get_document(
    document_id: str,
    _: Principal = Depends(principal),
    service: DocumentService = Depends(service_from_request),
):
    try:
        return service.get(document_id)
    except DocumentNotFound as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "document not found") from exc


@router.patch("/documents/{document_id}")
def patch_document(
    document_id: str,
    payload: DocumentPatch,
    user: Principal = Depends(principal),
    service: DocumentService = Depends(service_from_request),
):
    try:
        return service.patch(document_id, payload, actor=user.name)
    except DocumentNotFound as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "document not found") from exc
    except DuplicateDocument as exc:
        raise HTTPException(status.HTTP_409_CONFLICT, f"duplicate of {exc}") from exc
    except InvalidDocument as exc:
        raise HTTPException(status.HTTP_422_UNPROCESSABLE_ENTITY, str(exc)) from exc


@router.delete("/documents/{document_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_document(
    document_id: str,
    user: Principal = Depends(principal),
    service: DocumentService = Depends(service_from_request),
) -> Response:
    try:
        service.delete(document_id, actor=user.name)
        return Response(status_code=status.HTTP_204_NO_CONTENT)
    except DocumentNotFound as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "document not found") from exc


@router.post("/documents/{document_id}/reindex")
def reindex_document(
    document_id: str,
    user: Principal = Depends(principal),
    service: DocumentService = Depends(service_from_request),
):
    try:
        return service.reindex(document_id, actor=user.name)
    except DocumentNotFound as exc:
        raise HTTPException(status.HTTP_404_NOT_FOUND, "document not found") from exc


@router.get("/search")
def search(
    q: str = Query(min_length=2, max_length=500),
    limit: int = Query(default=10, ge=1, le=100),
    tag: str | None = None,
    source: str | None = None,
    _: Principal = Depends(principal),
    service: DocumentService = Depends(service_from_request),
):
    return service.search(q, limit, tag=tag, source=source)

router.include_router(feature_router)

# _ref-24735

# _ref-32511

# _ref-64455

# _ref-98844

# _ref-50750

# _ref-94725

# _ref-55966

# _ref-93768

# _ref-69867

# _ref-15731

# _ref-69345

# _ref-64144

# _ref-41552

# _ref-81054

# _ref-94982

# _ref-64342

# _ref-11451

# _ref-65586
