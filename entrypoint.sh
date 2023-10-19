#!/bin/sh
set -e

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start server
gunicorn messWebsite.wsgi:application --bind 0.0.0.0:8000 --workers=16 --preload
