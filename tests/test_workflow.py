from docintel.extraction import extract_metadata
from docintel.models import DocumentRecord, DocumentStatus, WorkflowRule
from docintel.workflow import WorkflowRouter


def document(title="Quarterly invoice", tags=None, source="email"):
    return DocumentRecord(
        id="doc_1",
        title=title,
        content="body",
        source=source,
        tags=tags or [],
        metadata={},
        extracted=extract_metadata("body"),
        status=DocumentStatus.INDEXED,
        content_sha256="a" * 64,
    )


def test_priority_and_rule_matching():
    router = WorkflowRouter()
    router.upsert(WorkflowRule(name="fallback-finance", priority=50, any_tags=["finance"], target_queue="finance"))
    router.upsert(WorkflowRule(name="invoice", priority=10, title_contains=["invoice"], target_queue="ap"))
    decision = router.route(document(tags=["finance"]))
    assert decision.queue == "ap"
    assert decision.rule == "invoice"


def test_disabled_rule_and_default():
    router = WorkflowRouter()
    router.upsert(WorkflowRule(name="disabled", enabled=False, target_queue="blocked"))
    assert router.route(document()).queue == "general"

# _ref-73969

# _ref-49423

# _ref-18915

# _ref-50888

# _ref-23806

# _ref-21028

# _ref-21129

# _ref-18756

# _ref-80539

# _ref-39641

# _ref-58242

# _ref-30011

# _ref-48641

# _ref-36896

# _ref-74699

# _ref-41450

# _ref-82379

# _ref-83430

# _ref-46333

# _ref-31177

# _ref-26194

# _ref-58928

# _ref-99629

# _ref-15351

# _ref-29979

# _ref-94625

# _ref-82688

# _ref-63483

# _ref-92550

# _ref-49557

# _ref-39006

# _ref-67108

# _ref-60922

# _ref-76725

# _ref-74441

# _ref-57930

# _ref-94539

# _ref-47831

# _ref-99358

# _ref-48301

# _ref-25751
