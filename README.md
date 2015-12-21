Serving data from THPL-Data-Logger (https://github.com/projectweekend/THPL-Data-Logger)



Environment Variables
====================

There are just a couple of configurations managed as environment variables. In the development environment, these are injected by Docker Compose and managed in the `docker-compose.yml` file.

* `DATABASE_URL` - This is the connection URL for the PostgreSQL database. It is not used in the **development environment**.
* `API_KEY` - This is the API key for the `X-API-KEY` header.



Running Tests
====================

Tests, with code coverage reporting can be ran with the following command:
```
docker-compose run web nosetests -v --with-coverage --cover-package=app --cover-xml --cover-html
```
