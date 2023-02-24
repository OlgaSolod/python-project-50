lint:
	@poetry run flake8 gendiff

tests:
	@poetry run pytest

test-coverage: 
	@poetry run pytest --cov=gendiff --cov-report xml