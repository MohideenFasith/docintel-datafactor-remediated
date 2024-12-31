.PHONY: install test coverage lint typecheck audit quality run docker

install:
	python -m pip install -r requirements-dev.lock -e . --no-deps

test:
	pytest -q

coverage:
	pytest -q --cov=docintel --cov-report=term-missing --cov-fail-under=80

lint:
	ruff check .

typecheck:
	mypy src

audit:
	pip-audit -r requirements.lock

quality: lint typecheck coverage audit

run:
	uvicorn docintel.main:app --host 0.0.0.0 --port 8000 --reload

docker:
	docker compose up --build

# _ref-77077

# _ref-21562

# _ref-98739

# _ref-47024

# _ref-37574

# _ref-24440

# _ref-23836

# _ref-54915

# _ref-93945

# _ref-47788

# _ref-58153

# _ref-59554
