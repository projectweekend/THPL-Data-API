from app import api
from app.stats.handlers import DailyStatsResource, HourlyStatsResource


api.add_route('/v1/stats/daily/{sensor}', DailyStatsResource())
api.add_route('/v1/stats/hourly/{sensor}', HourlyStatsResource())
