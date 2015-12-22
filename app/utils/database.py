import psycopg2
import psycopg2.extras
from urllib.parse import urlparse
from app.config import DATABASE_URL


def database_connection():
    parsed = urlparse(DATABASE_URL)
    user = parsed.username
    password = parsed.password
    host = parsed.hostname
    port = parsed.port
    database = parsed.path.strip('/')

    # return JSON as strings instead of converting to Python objects
    psycopg2.extras.register_default_json(loads=lambda x: x)
    connection = psycopg2.connect(host=host, port=port, user=user, password=password, database=database)
    connection.set_session(autocommit=True)

    return connection
