import falcon
from app.utils.testing import APITestCase


HOURLY_STATS_ROUTE = '/v1/stats/hourly'
DAILY_STATS_ROUTE = '/v1/stats/daily'
LATEST_READING_ROUTE = '/v1/sensor'
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
    'hour': str,
    'day': str,
    'temp_f': float,
    'temp_c': float,
    'humidity': float,
    'pressure': float,
    'luminosity': float,
    'logged_at': str
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


class DailyResourceTestCase(APITestCase):

    def test_daily_stats(self):
        route = '{0}/home'.format(DAILY_STATS_ROUTE)
        query_string = 'start={0}&end={1}'.format(VALID_START_PARAM, VALID_END_PARAM)
        body = self.simulate_get(path=route, query_string=query_string)
        self.assertEqual(self.srmock.status, falcon.HTTP_OK)
        self.assertEqual(len(body), 1)
        for reading in body:
            for k, v in reading.items():
                self.assertIsInstance(v, READING_TYPES[k])

    def test_daily_stats_with_invalid_date_params(self):
        route = '{0}/home'.format(DAILY_STATS_ROUTE)
        query_string = 'start={0}&end={1}'.format(INVALID_START_PARAM, VALID_END_PARAM)
        self.simulate_get(path=route, query_string=query_string)
        self.assertEqual(self.srmock.status, falcon.HTTP_BAD_REQUEST)

    def test_daily_stats_not_found(self):
        route = '{0}/not-a-sensor-name'.format(DAILY_STATS_ROUTE)
        query_string = 'start={0}&end={1}'.format(VALID_START_PARAM, VALID_END_PARAM)
        self.simulate_get(path=route, query_string=query_string)
        self.assertEqual(self.srmock.status, falcon.HTTP_NOT_FOUND)


class LatestReadingTestCase(APITestCase):

    def test_latest_reading(self):
        route = '{0}/home'.format(LATEST_READING_ROUTE)
        body = self.simulate_get(path=route)
        self.assertEqual(self.srmock.status, falcon.HTTP_OK)
        for k, v in body.items():
            self.assertIsInstance(v, READING_TYPES[k])

    def test_latest_reading_not_found(self):
        route = '{0}/not-a-sensor-name'.format(LATEST_READING_ROUTE)
        self.simulate_get(path=route)
        self.assertEqual(self.srmock.status, falcon.HTTP_NOT_FOUND)
