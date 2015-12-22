import falcon
from app.utils.testing import APITestCase


HOURLY_STATS_ROUTE = '/v1/stats/hourly'


class HourlyResourceTestCase(APITestCase):

    def test_hourly_stats(self):
        body = self.simulate_get(HOURLY_STATS_ROUTE)
        self.assertEqual(self.srmock.status, falcon.HTTP_200)
