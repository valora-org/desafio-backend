echo "Compose build:"
docker-compose build

echo "makemigrations"
docker-compose run web python3 manage.py makemigrations

echo "migrate"
docker-compose run web python3 manage.py migrate

echo "populate area:"

echo "populate admin base"
docker-compose run web python3 manage.py init_admin

echo "populate quiz base"
docker-compose run web python3 manage.py create_quiz

echo "populate question by quiz"
docker-compose run web python3 manage.py create_questions

