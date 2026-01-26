# Changelog

## 0.3.1

- Enforce tracked reproducibility inputs in CI alongside lock-drift validation.
- Configure application-wide JSON logging with correlation fields and dedicated tests.
- Promote Sentry to a runtime exception-tracking integration that remains disabled when no DSN is configured.
- Reject real network connections throughout the pytest suite and add an end-to-end HTTP document lifecycle test.
- Make annotation label serialization deterministic while preserving set semantics in the domain store.

## 0.3.0

- Add owner-scoped saved searches with stored filters and executable queries.
- Add configurable ingestion policies for blocked phrases, metadata-count limits, and automatic tags.
- Add bounded search analytics with top-query and zero-result reporting plus admin reset.
- Expose collections and annotations through audited API workflows.
- Add content revisions that re-extract, re-chunk, re-index, and preserve version history with unified diffs.
- Replace ad-hoc JSON formatting with `python-json-logger`, add request correlation IDs, exception logging, and optional Sentry hooks.
- Add transitive runtime locking, lock-drift validation, Dependabot, split CI jobs, and a clean-container smoke test.

## 0.2.0

- Expand document lifecycle with update, delete, reindex, listing, and duplicate-content protection.
- Add overlap-aware chunking, entity extraction, BM25-style lexical search, source/tag filters, and snippets.
- Add API-key authentication, writer/admin roles, sliding-window rate limiting, PII redaction, and hardened container defaults.
- Add audit events, structured JSON logging, Prometheus metrics, workflow rules, collections, annotations, version snapshots, retention policies, tenant quotas, batch ingest, JSONL transfer, webhook signing/retry state, and a local job queue.
- Add pinned runtime dependencies, lint/type/coverage/security-audit CI gates, Make targets, expanded onboarding/architecture/security/operations documentation, and broad unit/API coverage.

# _ref-44295

# _ref-62246

# _ref-61208

# _ref-87968

# _ref-92291

# _ref-92879

# _ref-69019

# _ref-57801

# _ref-54438

# _ref-28905

# _ref-68068

# _ref-63427

# _ref-24964

# _ref-32704

# _ref-11826

# _ref-33404

# _ref-77200

# _ref-52792

# _ref-22922

# _ref-90355

# _ref-69447

# _ref-77077

# _ref-97620

# _ref-60857

# _ref-28070

# _ref-15314

# _ref-58456

# _ref-39452

# _ref-91146

# _ref-24278

# _ref-67531

# _ref-96009

# _ref-79178

# _ref-86836

# _ref-40705

# _ref-15847

# _ref-49607

# _ref-71046

# _ref-29033

# _ref-61958

# _ref-87776

# _ref-49303

# _ref-75492

# _ref-67156

# _ref-68133

# _ref-51290

# _ref-91773
