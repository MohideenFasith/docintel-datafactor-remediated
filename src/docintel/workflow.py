from __future__ import annotations

from threading import RLock

from .errors import WorkflowNotFound
from .models import DocumentRecord, WorkflowDecision, WorkflowRule


class WorkflowRouter:
    def __init__(self) -> None:
        self._rules: dict[str, WorkflowRule] = {}
        self._lock = RLock()

    def upsert(self, rule: WorkflowRule) -> WorkflowRule:
        normalized = rule.model_copy(
            update={
                "any_tags": [tag.strip().lower() for tag in rule.any_tags if tag.strip()],
                "title_contains": [term.strip().lower() for term in rule.title_contains if term.strip()],
            }
        )
        with self._lock:
            self._rules[normalized.name] = normalized
        return normalized

    def delete(self, name: str) -> None:
        with self._lock:
            if name not in self._rules:
                raise WorkflowNotFound(name)
            del self._rules[name]

    def list(self) -> list[WorkflowRule]:
        with self._lock:
            return sorted(self._rules.values(), key=lambda rule: (rule.priority, rule.name))

    def route(self, document: DocumentRecord) -> WorkflowDecision:
        for rule in self.list():
            if not rule.enabled:
                continue
            if self._matches(rule, document):
                return WorkflowDecision(
                    queue=rule.target_queue,
                    rule=rule.name,
                    reason=f"matched workflow rule {rule.name}",
                )
        return WorkflowDecision(queue="general", reason="no workflow rule matched")

    @staticmethod
    def _matches(rule: WorkflowRule, document: DocumentRecord) -> bool:
        if rule.source_equals is not None and document.source != rule.source_equals:
            return False
        if rule.any_tags and not set(rule.any_tags).intersection(document.tags):
            return False
        lowered_title = document.title.lower()
        if rule.title_contains and not any(term in lowered_title for term in rule.title_contains):
            return False
        return True

# _ref-44563

# _ref-56074

# _ref-49293

# _ref-98699

# _ref-43336

# _ref-58951

# _ref-89056

# _ref-40968

# _ref-56329

# _ref-46263

# _ref-27265

# _ref-37140

# _ref-31495

# _ref-81200

# _ref-56093

# _ref-96328

# _ref-51002

# _ref-18677

# _ref-24079

# _ref-89346

# _ref-97234

# _ref-35235

# _ref-77002

# _ref-74279

# _ref-57247

# _ref-50731

# _ref-39474

# _ref-37125

# _ref-22525

# _ref-23750

# _ref-52277

# _ref-58439

# _ref-96977

# _ref-84675

# _ref-55402

# _ref-45342

# _ref-61991

# _ref-20382
