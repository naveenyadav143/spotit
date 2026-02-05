#!/usr/bin/env bash

echo "Running migrations..."
python manage.py migrate --noinput

echo "Creating default superuser..."

python manage.py shell << END
from django.contrib.auth import get_user_model

User = get_user_model()

username = "Srinivas"
email = "srinivas@gmail.com"
password = "Sri@1234"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser created.")
else:
    print("Superuser already exists.")
END

echo "Starting Gunicorn..."
gunicorn lostfound.wsgi:application
