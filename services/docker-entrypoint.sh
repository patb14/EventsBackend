#!/bin/sh

# Collect static files
echo "Collect static files"
python manage.py collectstatic --noinput

# Apply database migrations
echo "Apply database migrations"
python manage.py migrate

# Create Super User
echo "Creating Super User"
# TODO: LOL
DJANGO_SUPERUSER_USERNAME=admin \
DJANGO_SUPERUSER_PASSWORD=password \
DJANGO_SUPERUSER_EMAIL="admin@admin.com" \
python manage.py createsuperuser --noinput

# TODO
#echo "DB Seed"
#python manage.py loaddata ./events/testing/seed_data/event_locations.json
#python manage.py loaddata ./events/testing/seed_data/genders.json
#python manage.py loaddata ./events/testing/seed_data/levels_of_play.json
#python manage.py loaddata ./events/testing/seed_data/player_positions.json
#python manage.py loaddata ./events/testing/seed_data/sessions.json
#python manage.py loaddata ./events/testing/seed_data/events.json


# Start server
echo "Starting server"
python manage.py runserver 0.0.0.0:8000