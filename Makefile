dc := docker-compose -f infra/docker/docker-compose.yaml
dc_run_command := ${dc} run --rm app sh -c

run:
	${dc} up

build:
	${dc} build

up-build:
	${dc} up --build

bash:
	${dc} exec --workdir /code/app app bash
