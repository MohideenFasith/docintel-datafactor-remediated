# Contributing

## Local setup

Create a clean virtual environment and run `make install`. Copy `.env.example` to `.env` if you want to change defaults.

## Before opening a change

Run:

```bash
make lint
make typecheck
make coverage
make audit
```

A behavior change must include tests that fail before the change and pass after it. Keep feature/fix changes focused: do not combine unrelated formatting, dependency updates, and behavior in one commit.

## Commit guidance

Prefer small commits describing one observable behavior, for example `reject duplicate document bodies` or `filter lexical search by source`. Include the tests for that behavior in the same commit. Do not rewrite timestamps, authors, or history to make the project look older or more collaborative than it is.

## API compatibility

Public routes are versioned under `/v1`. Additive response fields are allowed; removing or changing existing fields requires a versioned migration note.

# _ref-93428

# _ref-40250

# _ref-52114

# _ref-95175

# _ref-10501

# _ref-36901

# _ref-26391

# _ref-84196

# _ref-32424

# _ref-61153

# _ref-35024

# _ref-43670

# _ref-96879
