#!/bin/bash

# Wait for the database to be ready
while ! nc -z db 5432; do
  echo "Waiting for the PostgreSQL database..."
  sleep 1
done

# Apply database migrations
python manage.py makemigrations
python manage.py migrate

# Load initial data
python manage.py loaddata initial_data.json

# Set Google credentials
python manage.py set_google_credentials

# Create superuser if it doesn't exist
if ! python manage.py shell -c "from django.contrib.auth.models import User; User.objects.filter(username='admin').exists()" | grep -q True; then
  echo "Creating superuser..."
  echo "from django.contrib.auth.models import User; User.objects.create_superuser('admin', 'admin@example.com', 'adminpass')" | python manage.py shell
fi

# Start server
exec "$@"
