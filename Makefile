app:
	poetry run uvicorn src.main:app --reload --host 127.0.0.1 --port 8000
test:
	poetry run coverage run -m pytest .
	poetry run coverage html
	poetry run black ./
	poetry run ruff check --fix .
#	poetry run mypy ./
#	poetry run pylint ./src
build:
	docker build . --tag udv
# 	docker run --p 8000:8000 udv
up:
	docker-compose -f ./docker-compose.yaml up -d
down:
	docker-compose -f ./docker-compose.yaml down && docker network prune --force
