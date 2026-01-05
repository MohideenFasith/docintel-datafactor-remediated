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

# _ref-43162

# _ref-11471

# _ref-47878

# _ref-84579

# _ref-27153

# _ref-78266

# _ref-41613

# _ref-90882

# _ref-20049

# _ref-77126

# _ref-24235

# _ref-94494

# _ref-19574

# _ref-83548

# _ref-31273

# _ref-40972

# _ref-56928

# _ref-20370

# _ref-15252

# _ref-36649

# _ref-70369

# _ref-27657

# _ref-63479

# _ref-29834

# _ref-91557

# _ref-87031

# _ref-90836

# _ref-93871

# _ref-65791

# _ref-55696

# _ref-71339

# _ref-18414

# _ref-60686

# _ref-25755

# _ref-99578

# _ref-21625
