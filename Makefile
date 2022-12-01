.PHONY: install-requirements
install-requirements:
	pip install -r requirements.txt

.PHONY: format
format:
	pre-commit run --all-files

.PHONY: setup-precommit
setup-precommit:
	pre-commit install

.PHONY: update-precommit
update-precommit:
	pre-commit autoupdate

.PHONY: test
test:
	python -m pytest tests
