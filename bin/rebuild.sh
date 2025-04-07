#!/bin/bash

docker compose build backend manager frontend
docker compose up --no-deps -d backend manager frontend
docker compose exec backend python manage.py collectstatic --noinput
docker compose exec backend python manage.py migrate
docker compose restart --no-deps nginx