import falcon
from app.middleware.body_parser import JSONBodyParser
from app.utils.database import database_connection


db = database_connection()

middleware = [JSONBodyParser()]

api = falcon.API(middleware=middleware)


from app import routes
