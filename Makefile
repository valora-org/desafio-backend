
-include .env

ENV_FILE_TEMPLATE = "$(PWD)/.env.template"
ENV_FILE = "$(PWD)/.env"


all:
	@echo "Hello $(LOGNAME), nothing to do by default"
	@echo "Try 'make help'"

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

build: delete-container ## Build the container
	@docker-compose build
	@docker-compose up -d

db: ## Create the DataBase
	@docker-compose exec -u postgres db psql -c 'CREATE DATABASE rest_db ENCODING 'UTF8' TEMPLATE template0;'

test: start ## Run tests
	@docker-compose exec app ./manage.py test

restart: ## Restart the container
	@docker-compose restart app

cmd: start ## Access bash
	@docker-compose exec app /bin/bash

shell: start ## Access django shell
	@docker-compose exec app /bin/bash -c "./manage.py shell"

up: start ## Start django dev server
	@docker-compose exec app /bin/bash -c "./manage.py runserver 0.0.0.0:8000"

start:
	@docker-compose start

down: ## Stop container
	@docker-compose stop || true

delete-container: down
	@docker-compose down || true

remove: delete-container ## Delete containers and images

.DEFAULT_GOAL := help