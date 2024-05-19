run:
	@uvicorn store_api.main:app --reload
run-docker:
	@docker compose up -d
precommit-install:
	@poetry run pre-commit install
precommit-check:
	@poetry run pre-commit run --files .
test:
	@poetry run pytest
test-matching:
	@poetry run pytest -s -rx -k $(K) --pdb ./tests/
