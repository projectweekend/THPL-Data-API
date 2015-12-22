from app import db


def hourly_stats(start_day, end_day):
    query = """
    WITH result AS (
    	SELECT		*
    	FROM 		thpl_hourly_agg
    	WHERE 		hour >= %s AND
    				hour < %s
    	ORDER BY 	hour DESC
    )
    SELECT		JSON_AGG(result.*)
    FROM 		result;
    """
    with db.cursor() as cursor:
        cursor.execute(query, (start_day, end_day, ))
        result = cursor.fetchone()
    return result[0] if result else '[]'


def daily_stats(start_day, end_day):
    query = """
    WITH result AS (
    	SELECT		*
    	FROM 		thpl_daily_agg
    	WHERE 		day >= %s AND
    				day < %s
    	ORDER BY 	day DESC
    )
    SELECT		JSON_AGG(result.*)
    FROM 		result;
    """
    with db.cursor() as cursor:
        cursor.execute(query, (start_day, end_day, ))
        result = cursor.fetchone()
    return result[0] if result else '[]'
