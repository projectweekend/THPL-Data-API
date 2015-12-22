from app import api
from app.stats.handlers import HourlyStatsResource


api.add_route('/v1/stats/hourly', HourlyStatsResource())
