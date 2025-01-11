from docintel.jobs import JobQueue
from docintel.models import JobStatus


def test_job_queue_success():
    seen = []
    queue = JobQueue()
    queue.register("collect", lambda payload: seen.append(payload["value"]))
    job = queue.enqueue("collect", {"value": 7})
    result = queue.run_next()
    assert result.id == job.id
    assert result.status == JobStatus.SUCCEEDED
    assert seen == [7]


def test_job_queue_failure_is_recorded():
    queue = JobQueue()
    job = queue.enqueue("missing", {})
    result = queue.run_next()
    assert result.id == job.id
    assert result.status == JobStatus.FAILED
    assert "no handler" in result.error

# _ref-75713

# _ref-83695

# _ref-67723

# _ref-23937

# _ref-43371

# _ref-32275

# _ref-19856

# _ref-88700

# _ref-18722

# _ref-98690

# _ref-59167

# _ref-65623
