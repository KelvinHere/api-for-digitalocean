# Random Word API

A Dockerized Django REST API that returns a random word and its meaning, deployed to a DigitalOcean VPS using docker-compose.

[LINK TO API HOMEPAGE](http://46.101.13.65:8000)

## FEATURES

- Call API with /word you will get the word and its meaning this can be accessed anonymously no authentication needed
- Update Word / Meaning using token authentication.  POST user name & password to secure a token at ``` /api-token-auth/ ```
- Request history displays previous 5 days activity of API
- API throttle rates set at N anonymous/logged in requests per hour
- Static files handled by WhiteNoise
- Docker sets up Admin & initial user through ```python manage.py ensure_initial_users``` command in the word app securely using environment variables.
- Automated CI/CD pipeline using Github Actions / Docker Compose / DigitalOcean.

## Upcoming features

- Admin rights to create and delete words
- Decoupled Postgres database

## Deployment

* Prerequisites
    * A machine with Docker installed

1. Clone the repo
1. Create a .env.compose file in the project root, populate as below and fill in passwords/emails
``` 
IN_DOCKER=TRUE
SECRET_KEY=PLACE_DJANGO_SECRET_KEY_HERE
DEBUG=FALSE
SU_NAME=ADMIN
SU_PASS=ADMIN_PASSWORD
SU_EMAIL=ADMIN_EMAIL
USER_NAME=USER1
USER_PASS=USER_PASSWORD
USER_EMAIL=USER_EMAIL
```
3. Build the docker image with ```docker-compose build```
4. Activate the container with ```docker-compose up```
5. The website should now be accessible through 'your IP' + :8000 as the port

## Testing

* Retrieving random word (Manual tests)
    * Homepage button
    * IP:8000/word
    * Get request with POSTMAN
    * Python Requests library from another website

* Updating word by PK (Manual tests)
    * Passing valid token & valid JSON payload updates word
    * Passing invalid token & valid JSON payload get denied
    * Passing valid token & invalid JSON payload ????

* Deployment
    * Test deployment on local development machine
    * Test docker container on local development machine
    * Test docker container on remote VPS

## Technologies

* Docker
* Docker-Compose
* Django
* DjangoRestFramework
* WhiteNoise
* Gunicorn
* DigitalOcean VPS

## Credit
[Dictionary](https://github.com/matthewreagan/WebstersEnglishDictionary) data taken from [Gutenber Project - a library of over 60,000 free eBooks](https://www.gutenberg.org/)