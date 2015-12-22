import falcon
from app.utils.testing import APITestCase


HOURLY_STATS_ROUTE = '/v1/stats/hourly'
VALID_START_PARAM = '2015-12-19'
VALID_END_PARAM = '2015-12-20'
INVALID_START_PARAM = 'not a date'
INVALID_END_PARAM = 'not a date'


class HourlyResourceTestCase(APITestCase):

    def test_hourly_stats(self):
        pass

    def test_hourly_stats_not_found(self):
        route = '{0}/not-a-sensor-name'.format(HOURLY_STATS_ROUTE)
        query_string = 'start={0}&end={1}'.format(VALID_START_PARAM, VALID_END_PARAM)
        self.simulate_get(path=route, query_string=query_string)
        self.assertEqual(self.srmock.status, falcon.HTTP_NOT_FOUND)
