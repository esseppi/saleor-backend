#! /usr/bin/env bash

cd /var/www/esseppi-backend/
if [ -f ".envs/.production/.django" ]; then
  git checkout .envs/.production/.django
fi
git fetch -a
git checkout origin/master

gcloud secrets versions access latest --secret=esseppi-api-prod-env --format='get(payload.data)' | tr '_-' '/+' | base64 -d > /var/www/esseppi-backend/.envs/.production/.django

export DJANGO_SETTINGS_MODULE=saleor.settings

docker-compose -f production.yml build
docker-compose -f production.yml run --rm django python3 manage.py migrate
docker-compose -f production.yml down
docker-compose -f production.yml up -d

docker system prune -af
