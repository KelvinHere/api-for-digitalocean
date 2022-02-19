# Random Word API

A Dockerized Django API that returns a random word and its meaning deployable to DigitalOcean via docker-compose

## FEATURES

- Call API with /word you will get the word and its meaning
- Static files handled by WhiteNoise

## Upcoming features

- API call limiter
- Admin rights to edit, create and delete words
- Automated CI/CD pipeline
- Postgres database rather than SQLite

## Deployment

- Prerequisites 
    - Docker

- Clone repo
- run `docker-compose build`
- run `docker-compose up`

## Technologies

Django
DjangoRestFramework
WhiteNoise
Gunicorn
DigitalOcean