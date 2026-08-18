from __future__ import annotations

import re
import tomllib
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PIN = re.compile(r"^([A-Za-z0-9_.-]+)==([^;\\s]+)$")


def normalized(name: str) -> str:
    return name.lower().replace("_", "-").replace(".", "-")


def lock_pins(path: Path) -> dict[str, str]:
    pins: dict[str, str] = {}
    for line in path.read_text().splitlines():
        match = PIN.match(line.strip())
        if match:
            pins[normalized(match.group(1))] = match.group(2)
    return pins


def direct_pin(requirement: str) -> tuple[str, str] | None:
    match = PIN.match(requirement)
    if not match:
        return None
    return normalized(match.group(1)), match.group(2)


def main() -> int:
    project = tomllib.loads((ROOT / "pyproject.toml").read_text())
    runtime = lock_pins(ROOT / "requirements.lock")
    dev = lock_pins(ROOT / "requirements-dev.lock")
    missing: list[str] = []

    for requirement in project["project"]["dependencies"]:
        direct = direct_pin(requirement)
        if direct is None:
            missing.append(f"runtime requirement is not exactly pinned: {requirement}")
            continue
        name, version = direct
        if runtime.get(name) != version:
            missing.append(f"runtime lock mismatch: {name}=={version}")

    for requirement in project["project"]["optional-dependencies"]["dev"]:
        direct = direct_pin(requirement)
        if direct is None:
            missing.append(f"dev requirement is not exactly pinned: {requirement}")
            continue
        name, version = direct
        if dev.get(name) != version:
            missing.append(f"dev lock mismatch: {name}=={version}")

    runtime_manifest = lock_pins(ROOT / "requirements.txt")
    dev_manifest = lock_pins(ROOT / "requirements-dev.txt")
    expected_runtime = {direct_pin(req) for req in project["project"]["dependencies"]}
    expected_dev = {direct_pin(req) for req in project["project"]["optional-dependencies"]["dev"]}
    expected_runtime = {item for item in expected_runtime if item is not None}
    expected_dev = {item for item in expected_dev if item is not None}
    if set(runtime_manifest.items()) != expected_runtime:
        missing.append("requirements.txt must exactly mirror direct runtime pins")
    if set(dev_manifest.items()) != expected_dev:
        missing.append("requirements-dev.txt must exactly mirror direct dev pins")

    if missing:
        print("\n".join(missing))
        return 1
    print("lock files and conventional manifests match pyproject pins")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
