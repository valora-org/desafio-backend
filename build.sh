echo "Compose build:"
docker-compose build
docker-compose run web python3 manage.py migrate

docker-compose run web python3 manage.py makemigrations
docker-compose run web python3 manage.py migrate
docker-compose run web python3 manage.py init_admin
docker-compose run web python3 manage.py create_quiz
docker-compose run web python3 manage.py create_questions

