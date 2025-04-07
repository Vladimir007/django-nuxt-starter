#!/bin/bash

docker compose up -d --build
docker compose exec backend python manage.py collectstatic --noinput
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createcachetable
docker compose exec backend python manage.py enable-periodic