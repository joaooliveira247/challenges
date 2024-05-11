run:
	@uvicorn store_api.main:app --reload

precommit-install:
	@poetry run pre-commit install
precommit-check:
	@poetry run pre-commit run --files .
test:
	@poetry run pytest
