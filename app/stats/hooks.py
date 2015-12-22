from datetime import datetime
import falcon


DATE_PATTERN = '%Y-%m-%d'
START_PARAM = 'start'
END_PARAM = 'end'


def check_date_param(param, name):
    try:
        datetime.strptime(param, DATE_PATTERN)
    except ValueError:
        raise falcon.HTTPBadRequest(
            title='Invalid parameter',
            description='The "{0}" parameter is not a valid date'.format(name))
    return param


def validate_query_params(req, resp, resource, params):
    req.context['start_day'] = check_date_param(
        param=req.get_param(START_PARAM, required=True),
        name=START_PARAM)
    req.context['end_day'] = check_date_param(
        param=req.get_param(END_PARAM, required=True),
        name=END_PARAM)
