lint:
		poetry run flake8 gendiff

test:
		poetry run -m pytest tests/test_gendiff.py 