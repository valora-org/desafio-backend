build:
	docker-compose -f local.yml build

run:
	docker-compose -f local.yml up

tests:
	docker-compose -f local.yml run --rm django /bin/bash -c "\
		python manage.py migrate;\
		coverage run -m pytest"
	@docker-compose -f local.yml down > /dev/null 2>&1

report:
	docker-compose -f local.yml run --rm django /bin/bash -c "coverage report"
	@docker-compose -f local.yml down > /dev/null 2>&1

loaddata:
	docker-compose -f local.yml run --rm django /bin/bash -c "\
		python manage.py migrate;\
		python manage.py loaddata data --app users;\
		python manage.py loaddata data --app ranking;\
		python manage.py loaddata data --app categories;\
		python manage.py loaddata data --app questions;\
		"

C=echo Type command
run_cmd:
	docker-compose -f local.yml run --rm django /bin/bash -c "$(C)"
	@docker-compose -f local.yml down > /dev/null 2>&1

clear_volumes:
	docker-compose -f local.yml down -v

clear_db: clear_volumes
	docker image rm quiz_production_postgres
