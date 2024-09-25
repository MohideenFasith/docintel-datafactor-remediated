from docintel.batch import BatchIngestor
from docintel.models import DocumentIn
from docintel.service import DocumentService


def test_batch_ingest_tracks_success_and_duplicate_failure():
    ingestor = BatchIngestor(DocumentService())
    result = ingestor.ingest([
        DocumentIn(title="A", content="same"),
        DocumentIn(title="B", content="same"),
        DocumentIn(title="C", content="different"),
    ])
    assert len(result.succeeded) == 2
    assert len(result.failed) == 1
    assert result.failed[0].index == 1


def test_batch_stop_on_error():
    ingestor = BatchIngestor(DocumentService())
    result = ingestor.ingest([
        DocumentIn(title="A", content="same"),
        DocumentIn(title="B", content="same"),
        DocumentIn(title="C", content="not reached"),
    ], stop_on_error=True)
    assert len(result.succeeded) == 1
    assert len(result.failed) == 1

# _ref-96500

# _ref-96416

# _ref-61153

# _ref-80807

# _ref-63036
