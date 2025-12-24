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

# _ref-50252

# _ref-51863

# _ref-59183

# _ref-18630

# _ref-17993

# _ref-51639

# _ref-37711

# _ref-63809

# _ref-96597

# _ref-88814

# _ref-63984

# _ref-41481

# _ref-22992

# _ref-92784

# _ref-40094

# _ref-80836

# _ref-61769

# _ref-96406

# _ref-45939

# _ref-59454

# _ref-36217

# _ref-62338

# _ref-82427

# _ref-74525

# _ref-74785

# _ref-85419

# _ref-99120

# _ref-94531

# _ref-69954

# _ref-14515

# _ref-32814

# _ref-82908

# _ref-82443
