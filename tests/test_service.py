import pytest

from docintel.errors import DuplicateDocument, InvalidDocument
from docintel.models import DocumentIn, DocumentPatch, WorkflowRule
from docintel.service import DocumentService
from docintel.settings import Settings


def service():
    return DocumentService(settings=Settings(max_document_chars=2_000, default_chunk_chars=250, default_chunk_overlap=25))


def test_ingest_search_patch_delete_lifecycle():
    svc = service()
    record = svc.ingest(DocumentIn(title="CUDA Notes", content="CUDA kernel fusion and paged attention.", tags=["ml"]))
    assert record.chunk_count == 1
    assert svc.search("paged attention").hits[0].document_id == record.id
    patched = svc.patch(record.id, DocumentPatch(title="GPU Notes", tags=["gpu"]))
    assert patched.title == "GPU Notes"
    assert svc.search("GPU").hits[0].document_id == record.id
    svc.delete(record.id)
    assert svc.search("CUDA").total == 0
    assert svc.stats()["documents"] == 0


def test_duplicate_content_rejected():
    svc = service()
    payload = DocumentIn(title="One", content="same content")
    svc.ingest(payload)
    with pytest.raises(DuplicateDocument):
        svc.ingest(DocumentIn(title="Two", content="same content"))


def test_oversized_document_rejected():
    svc = DocumentService(settings=Settings(max_document_chars=1_000))
    with pytest.raises(InvalidDocument):
        svc.ingest(DocumentIn(title="Large", content="x" * 1_001))


def test_workflow_route():
    svc = service()
    record = svc.ingest(DocumentIn(title="Vendor invoice", content="Amount USD 42.00", tags=["finance"]))
    svc.upsert_workflow(WorkflowRule(name="invoice", title_contains=["invoice"], target_queue="accounts-payable"))
    assert svc.route(record.id).queue == "accounts-payable"


def test_audit_records_mutations():
    svc = service()
    record = svc.ingest(DocumentIn(title="A", content="audit me"), actor="alice")
    svc.patch(record.id, DocumentPatch(title="B"), actor="alice")
    actions = [event.action for event in svc.audit.list(actor="alice")]
    assert actions == ["document.patch", "document.ingest"]

# _ref-68530

# _ref-71668

# _ref-35542

# _ref-53257

# _ref-18354

# _ref-67068

# _ref-37694

# _ref-92589

# _ref-47885

# _ref-66197

# _ref-82549

# _ref-38813

# _ref-99516

# _ref-98477

# _ref-81626

# _ref-38276

# _ref-44281

# _ref-33485

# _ref-67201

# _ref-11954

# _ref-42389

# _ref-99964

# _ref-56323

# _ref-90612

# _ref-88264
