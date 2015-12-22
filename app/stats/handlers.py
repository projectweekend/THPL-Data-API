import falcon
from app.stats import data


class HourlyStatsResource(object):

    def on_get(self, req, res, sensor):
        start_day = req.get_param('start', required=True)
        end_day = req.get_param('end', required=True)
        result = data.hourly_stats(sensor=sensor, start_day=start_day, end_day=end_day)
        if result is None:
            raise falcon.HTTPNotFound
        res.status = falcon.HTTP_200
        res.body = result
