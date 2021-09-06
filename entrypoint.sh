#!/bin/bash
sqlite3 db.sqlite3

sqlite3 db.sqlite3 < popule.dumb.sql

python manage.py migrate --no-input
python manage.py collectstatic --no-input

gunicorn quiz.wsgi:application  --bind 0.0.0.0:8000