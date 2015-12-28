from app import api
from app.stats.handlers import DailyStatsResource, HourlyStatsResource, LatestReadingResource


api.add_route('/v1/sensor/{sensor}', LatestReadingResource())
api.add_route('/v1/stats/daily/{sensor}', DailyStatsResource())
api.add_route('/v1/stats/hourly/{sensor}', HourlyStatsResource())
