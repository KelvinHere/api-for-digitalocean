#!/bin/sh

python manage.py migrate --no-input
python restexample/manage.py loaddata dictionary.json
python manage.py collectstatic --no-input

gunicorn api.wsgi:application --bind 0.0.0.0:8000