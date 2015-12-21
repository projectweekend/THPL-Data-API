import falcon
from app.config import API_KEY


class APIKey(object):

    def process_request(self, req, res):
        api_key = req.get_header('X-API-KEY')
        if api_key != API_KEY:
            raise falcon.HTTPUnauthorized(
                title='Not Authorized',
                description='Invalid API Key')
