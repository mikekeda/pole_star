# !/bin/bash

# Collect static files
echo "Wait for postgres"
wait-for-it.sh db:5432

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Run test
echo "Starting server"
python manage.py test

# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000
