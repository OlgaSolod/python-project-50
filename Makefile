lint:
		poetry run flake8 gendiff

test:
		poetry run python3 -m pytest tests/test_gendiff.py 

test-coverage:
		poetry run python3 -m pytest --cov=gendiff --cov-report xml