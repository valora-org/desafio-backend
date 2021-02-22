pipenv run python manage.py migrate
pipenv run python manage.py collectstatic --noinput
pipenv run gunicorn config.wsgi
