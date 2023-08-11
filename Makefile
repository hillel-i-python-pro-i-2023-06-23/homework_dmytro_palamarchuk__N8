.PHONY: d-homework-i-run
# Make all actions needed for run homework from zero.
d-homework-i-run:
	@make d-run

.PHONY: d-homework-i-purge
# Make all actions needed for purge homework related data.
d-homework-i-purge:
	@make d-purge

.PHONY: d-run
# Just run
d-run:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 USER_ID="$(shell id -u)" GROUP_ID="$(shell id -g)" \
		docker compose up --build --exit-code-from app

.PHONY: d-stop
# Stop services
d-stop:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 USER_ID="$(shell id -u)" GROUP_ID="$(shell id -g)" \
		docker compose down

.PHONY: d-purge
# Purge all data related with services
d-purge:
	@COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 USER_ID="$(shell id -u)" GROUP_ID="$(shell id -g)" \
		docker compose down --volumes --remove-orphans --rmi local --timeout 0

.PHONY: init-dev
# Init environment for development
init-dev:
	@pip install --upgrade pip && \
	pip install --requirement requirements.txt && \
	pre-commit install

.PHONY: init-configs
# Configuration files initialization
init-configs:
	@cp docker-compose.override.dev.yml docker-compose.override.yml

.PHONY: homework-i-run
# Run homework.
homework-i-run:
	@python run.py

.PHONY: homework-i-purge
homework-i-purge:
	@echo Goodbye

.PHONY: pre-commit-run
# Run tools for files from commit.
pre-commit-run:
	@pre-commit run

.PHONY: pre-commit-run-all
# Run tools for all files.
pre-commit-run-all:
	@pre-commit run --all-files
