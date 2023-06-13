# How To Run
Create a .env file in the root folder and add the following keys and set their data

* DJANGO_SUPERUSER_USERNAME
* DJANGO_SUPERUSER_PASSWORD
* DJANGO_SUPERUSER_EMAIL

Then simply compose:

`docker-compose -f docker-compose.dev.yml build`\
`docker-compose -f docker-compose.dev.yml up -d`

# TODO
Encrypt at rest