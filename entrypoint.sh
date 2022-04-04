#!/bin/sh

python manage.py makemigrations --no-input
python manage.py migrate --no-input
python manage.py loaddata dictionary.json
python manage.py collectstatic --no-input
python manage.py ensure_initial_users
python manage.py dbbackup # Create a backup of the database to easily restore

gunicorn api.wsgi:application --bind 0.0.0.0:8000