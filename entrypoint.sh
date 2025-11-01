#!/bin/bash
set -e

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL ($DB_HOST:$DB_PORT)..."
until nc -z "$DB_HOST" "$DB_PORT"; do
  sleep 0.5
done
echo "PostgreSQL is ready!"

# Run migrations and static collection
echo "Running database migrations..."
python manage.py migrate --noinput

echo "Collecting static files..."
python manage.py collectstatic --noinput

# Start server
echo "Starting Django development server..."
python manage.py runserver 0.0.0.0:8005
