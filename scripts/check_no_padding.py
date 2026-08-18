from __future__ import annotations

from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FORBIDDEN = "_ci" + "-ref-"
SKIP_PARTS = {".git", ".venv", "__pycache__", ".pytest_cache", ".mypy_cache", ".ruff_cache"}


def main() -> int:
    offenders: list[str] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in SKIP_PARTS for part in path.parts):
            continue
        try:
            text = path.read_text()
        except UnicodeDecodeError:
            continue
        if FORBIDDEN in text:
            offenders.append(str(path.relative_to(ROOT)))

    if offenders:
        print("synthetic padding markers found in: " + ", ".join(sorted(offenders)))
        return 1
    print("no synthetic padding markers found")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
