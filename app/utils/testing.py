import json

from urllib.parse import urlparse
from falcon.testing import TestBase
from app import api, db
from app.config import API_KEY, CONTENT_TYPE_METHODS, DATABASE_URL


HEADERS = {
    'Content-Type': 'application/json',
    'X-API-KEY': API_KEY
}


class APITestCase(TestBase):

    def setUp(self):
        super(APITestCase, self).setUp()
        self.db = db
        self._empty_tables()

    def _empty_tables(self):
        parsed = urlparse(DATABASE_URL)

        app_tables_query = """
        SELECT          table_name
        FROM            information_schema.tables
        WHERE           table_schema = 'public' AND
                        table_catalog = '{0}' AND
                        table_name != 'schema_version';""".format(parsed.path.strip('/'))
        cursor = self.db.cursor()
        cursor.execute(app_tables_query)
        tables = [r[0] for r in cursor.fetchall()]
        for t in tables:
            query = 'TRUNCATE TABLE {0} CASCADE;'.format(t)
            cursor.execute(query)
            self.db.commit()
        cursor.close()

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
