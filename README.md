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



Routes
====================

### Get a list of hourly stats

**GET:**
```
/v1/stats/hourly
```

**Query Parameters:**

* `start` - Start day - Example: `2015-12-19`
* `end` - End day - Example: `2015-12-20`

**Response:**
```json
[
    {
        "id": 107,
        "sensor": "home",
        "hour": "2015-12-19T23:00:00",
        "avg_temp": 68.7323,
        "avg_humidity": 19.4587,
        "avg_pressure": 1004.5114,
        "min_temp": 68.1800,
        "min_humidity": 19.1000,
        "min_pressure": 1004.3200,
        "max_temp": 69.4400,
        "max_humidity": 19.7100,
        "max_pressure": 1004.7200
    }
]
```

**Status Codes:**
* `200` if successful
* `400` if invalid query parameters
* `401` if invalid credentials
