lint:
	poetry run flake8 

test: 
	poetry run pytest --cov=gendiff --cov-report xml