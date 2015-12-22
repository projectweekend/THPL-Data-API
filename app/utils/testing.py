import json

from falcon.testing import TestBase
from app import api
from app.config import API_KEY, CONTENT_TYPE_METHODS


HEADERS = {
    'Content-Type': 'application/json',
    'X-API-KEY': API_KEY
}


class APITestCase(TestBase):

    def setUp(self):
        super(APITestCase, self).setUp()

    def _simulate_request(self, method, path, data, token=None, **kwargs):
        headers = HEADERS.copy()

        if token:
            headers['Authorization'] = token

        if 'headers' in kwargs:
            more_headers = kwargs.pop('headers')
            headers.update(more_headers)

        # Content-Type is only sent on POST, PUT, PATCH
        if method not in CONTENT_TYPE_METHODS:
            headers.pop('Content-Type')

        self.api = api

        result = self.simulate_request(
            path=path,
            method=method,
            headers=headers,
            body=json.dumps(data),
            **kwargs)
        try:
            return json.loads(result[0].decode('utf-8'))
        except IndexError:
            return None

    def simulate_get(self, path, token=None, **kwargs):
        return self._simulate_request(
            method='GET',
            path=path,
            data=None,
            token=token,
            **kwargs)

    def simulate_post(self, path, data, token=None, **kwargs):
        return self._simulate_request(
            method='POST',
            path=path,
            data=data,
            token=token,
            **kwargs)

    def simulate_put(self, path, data, token=None, **kwargs):
        return self._simulate_request(
            method='PUT',
            path=path,
            data=data,
            token=token,
            **kwargs)

    def simulate_patch(self, path, data, token=None, **kwargs):
        return self._simulate_request(
            method='PATCH',
            path=path,
            data=data,
            token=token,
            **kwargs)

    def simulate_delete(self, path, token=None, **kwargs):
        return self._simulate_request(
            method='DELETE',
            path=path,
            data=None,
            token=token,
            **kwargs)
