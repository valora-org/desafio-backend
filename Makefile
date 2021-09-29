build:
	docker-compose build

start:
	docker-compose up -d

stop:
	docker-compose stop

down:
	docker-compose down

create-super-user:
	docker-compose run --rm web python manage.py createsuperuser --noinput

migrate:
	docker-compose run --rm web python manage.py migrate

start-services:
	make build start migrate create-super-user

test:
	docker-compose run --rm web python manage.py test

build-data:
	python insert_data.py
