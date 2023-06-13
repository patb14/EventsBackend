# How To Run
Create a .env file in the root folder and add set the following env vars:

* DJANGO_SUPERUSER_USERNAME
* DJANGO_SUPERUSER_PASSWORD
* DJANGO_SUPERUSER_EMAIL
* POSTGRES_USER
* POSTGRES_PASSWORD
* POSTGRES_DB

Then simply compose:

`docker-compose -f docker-compose.dev.yml build`\
`docker-compose -f docker-compose.dev.yml up -d`

# TODO
Encrypt at rest