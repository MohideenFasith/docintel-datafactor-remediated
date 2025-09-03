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

# _ref-45441

# _ref-50174

# _ref-11935

# _ref-21844

# _ref-86878

# _ref-87120

# _ref-71148

# _ref-16592

# _ref-92808

# _ref-80697

# _ref-83927

# _ref-27088

# _ref-29128

# _ref-79462

# _ref-15591

# _ref-88082

# _ref-13896

# _ref-64896

# _ref-30273

# _ref-13618

# _ref-97621

# _ref-89643

# _ref-46248

# _ref-81739

# _ref-89295

# _ref-11682

# _ref-63009
