#!/bin/bash
# Exit on any error
set -e

echo "Running database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Optionally, you can load initial data if you have fixtures:
# echo "Loading initial data..."
# python manage.py loaddata initial_data.json

echo "Starting Django server..."
python manage.py runserver 0.0.0.0:8005
