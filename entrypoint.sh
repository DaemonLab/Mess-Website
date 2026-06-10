#!/bin/sh
set -e

# Apply database migrations
python manage.py migrate --noinput

# Collect static files
python manage.py collectstatic --noinput

# Start server
# Counts are env-tunable (see docker-compose.yml). gthread + --max-requests keep
# memory bounded; the previous 16 sync workers were OOM-killed under load.
gunicorn messWebsite.wsgi:application \
    --bind 0.0.0.0:8000 \
    --worker-class=gthread \
    --workers="${GUNICORN_WORKERS:-3}" \
    --threads="${GUNICORN_THREADS:-4}" \
    --timeout="${GUNICORN_TIMEOUT:-300}" \
    --graceful-timeout=30 \
    --max-requests=1000 \
    --max-requests-jitter=100 \
    --preload
