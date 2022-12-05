lint:
		poetry run flake8 gendiff

test:
		python3 -m pytest tests/test_gendiff.py 