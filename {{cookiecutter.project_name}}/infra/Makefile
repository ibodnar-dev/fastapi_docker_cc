dc := docker-compose -f infra/docker/docker-compose.yaml
dc_run_command := ${dc} run --rm app sh -c

run:
	${dc} up

build:
	${dc} build --no-cache

up-build:
	${dc} up --build

bash:
	${dc} exec --workdir /code/app app bash

create-db:
	${dc_run_command} "python create_db.py"

alembic-revision-auto:
	${dc_run_command} "cd app && alembic revision --autogenerate -m '${message}'"

alembic-migrate:
	${dc_run_command} "cd app && alembic upgrade head"
