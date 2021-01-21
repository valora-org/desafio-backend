build_local_docker:
	docker-compose -f local.yml build

run_local_docker:
	docker-compose -f local.yml up

run_tests:
	docker-compose -f local.yml run --rm django /bin/bash -c "python manage.py migrate; coverage run -m pytest"
	docker-compose -f local.yml down

tests_report:
	docker-compose -f local.yml run --rm django /bin/bash -c "coverage report"
	docker-compose -f local.yml down

C=echo Type command
run_cmd:
	docker-compose -f local.yml run --rm django /bin/bash -c "$(C)"
	docker-compose -f local.yml down

clear_volumes:
	docker-compose -f local.yml down -v
