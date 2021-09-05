#!/bin/bash

# Install new requirements
# echo "Install new requirements"
# pip install -r requirements.txt

# Collect static files
echo "COLLECT STATIC FILES"
python manage.py collectstatic --noinput

# Reset Migrations
# find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
# find . -path "*/migrations/*.pyc"  -delete
# python manage.py makemigrations

# Apply database migrations
echo "APPLY DATABASE MIGRATIONS"
python manage.py migrate

# Start server
echo "STARTING SERVER"
python manage.py runserver 0.0.0.0:${DJANGO_PORT}