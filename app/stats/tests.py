import falcon
from app.utils.testing import APITestCase


HOURLY_STATS_ROUTE = '/v1/stats/hourly'
VALID_START_PARAM = '2015-12-19'
VALID_END_PARAM = '2015-12-20'
INVALID_START_PARAM = 'not a date'
INVALID_END_PARAM = 'not a date'
READING_TYPES = {
    'id': int,
    'sensor': str,
    'avg_humidity': float,
    'max_humidity': float,
    'min_humidity': float,
    'avg_pressure': float,
    'max_pressure': float,
    'min_pressure': float,
    'avg_temp': float,
    'max_temp': float,
    'min_temp': float,
    'hour': str
}


class HourlyResourceTestCase(APITestCase):

    def test_hourly_stats(self):
        route = '{0}/home'.format(HOURLY_STATS_ROUTE)
        query_string = 'start={0}&end={1}'.format(VALID_START_PARAM, VALID_END_PARAM)
        body = self.simulate_get(path=route, query_string=query_string)
        self.assertEqual(self.srmock.status, falcon.HTTP_OK)
        self.assertEqual(len(body), 24)
        for reading in body:
            for k, v in reading.items():
                self.assertIsInstance(v, READING_TYPES[k])

    def test_hourly_stats_with_invalid_date_params(self):
        route = '{0}/home'.format(HOURLY_STATS_ROUTE)
        query_string = 'start={0}&end={1}'.format(INVALID_START_PARAM, VALID_END_PARAM)
        self.simulate_get(path=route, query_string=query_string)
        self.assertEqual(self.srmock.status, falcon.HTTP_BAD_REQUEST)

    def test_hourly_stats_not_found(self):
        route = '{0}/not-a-sensor-name'.format(HOURLY_STATS_ROUTE)
        query_string = 'start={0}&end={1}'.format(VALID_START_PARAM, VALID_END_PARAM)
        self.simulate_get(path=route, query_string=query_string)
        self.assertEqual(self.srmock.status, falcon.HTTP_NOT_FOUND)
