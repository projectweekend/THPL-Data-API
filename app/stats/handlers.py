import falcon
from app.stats import data


class HourlyStatsResource(object):

    def on_get(self, req, res):
        start_day = req.get_param('start', required=True)
        end_day = req.get_param('end', required=True)
        res.status = falcon.HTTP_200
        res.body = data.hourly_stats(start_day=start_day, end_day=end_day)
