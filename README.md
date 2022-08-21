### Requirements
cookiecutter

### Installation
```bash
cookiecutter git@github.com:ibodnar-dev/fastapi_docker_cc.git -c <branch-name>
```
You'll be then prompted to choose your project name and the name of your first app
### Project Setup
- Move `Makefile` and `.gitignore` from `infra` to the root of the project
- run the `build` or `up-build` target from the `Makefile`
