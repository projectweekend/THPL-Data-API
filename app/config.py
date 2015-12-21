import os


API_KEY = os.getenv('API_KEY')
assert API_KEY

CONTENT_TYPE_METHODS = ('POST', 'PUT', 'PATCH', )

DATABASE_URL = os.getenv('DATABASE_URL')
if DATABASE_URL is None:
    compose_database_host = os.getenv('DB_PORT_5432_TCP_ADDR')
    assert compose_database_host
    DATABASE_URL = 'postgres://postgres@{0}:5432/postgres'.format(compose_database_host)
