iniciar-app:
	@sudo docker-compose build
	@sudo docker-compose up -d

parar-app:
	@sudo docker-compose down -v

exec-migrate-flush-populate-app:
	@sudo docker-compose run web python manage.py makemigrations
	@sudo docker-compose run web python manage.py migrate
	@sudo docker-compose run web python manage.py flush --noinput
	@sudo docker-compose run web python manage.py shell < populate.py


