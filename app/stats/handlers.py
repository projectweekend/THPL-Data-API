import falcon
from app.stats import data
from app.stats.hooks import validate_query_params


class HourlyStatsResource(object):

    @falcon.before(validate_query_params)
    def on_get(self, req, res, sensor):
        result = data.hourly_stats(
            sensor=sensor,
            start_day=req.context['start_day'],
            end_day=req.context['end_day'])
        if result is None:
            raise falcon.HTTPNotFound
        res.status = falcon.HTTP_200
        res.body = result


class DailyStatsResource(object):

    @falcon.before(validate_query_params)
    def on_get(self, req, res, sensor):
        result = data.daily_stats(
            sensor=sensor,
            start_day=req.context['start_day'],
            end_day=req.context['end_day'])
        if result is None:
            raise falcon.HTTPNotFound
        res.status = falcon.HTTP_200
        res.body = result
