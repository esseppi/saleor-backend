#! /usr/bin/env bash

cd /var/www/esseppi-backend/

git checkout .envs/.production/.django
git fetch -a
git checkout origin/preprod

#gcloud secrets versions access latest --secret=esseppi-api-staging-env --format='get(payload.data)' | tr '_-' '/+' | base64 -d > /var/www/esseppi-backend/.envs/.production/.django

export DJANGO_SETTINGS_MODULE=saleor.settings

docker-compose -f staging.yml build
docker-compose -f staging.yml run --rm django python3 manage.py migrate
docker-compose -f staging.yml down
docker-compose -f staging.yml up -d

docker system prune -af
