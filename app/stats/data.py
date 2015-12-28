from app import db


def latest_reading(sensor):
    query = """
    WITH result AS (
        SELECT      *
        FROM        thpl_data
        WHERE       sensor = %s
        ORDER BY    logged_at DESC
        LIMIT       1
    )
    SELECT      ROW_TO_JSON(result.*)
    FROM        result;
    """
    with db.cursor() as cursor:
        cursor.execute(query, (sensor, ))
        result = cursor.fetchone()
    return result[0] if result else None


def hourly_stats(sensor, start_day, end_day):
    query = """
    WITH result AS (
        SELECT      *
        FROM        thpl_hourly_agg
        WHERE       sensor = %s AND
                    hour >= %s AND
                    hour < %s
        ORDER BY    hour DESC
    )
    SELECT      JSON_AGG(result.*)
    FROM        result;
    """
    with db.cursor() as cursor:
        cursor.execute(query, (sensor, start_day, end_day, ))
        result = cursor.fetchone()
    return result[0] if result else None


def daily_stats(sensor, start_day, end_day):
    query = """
    WITH result AS (
        SELECT      *
        FROM        thpl_daily_agg
        WHERE       sensor = %s AND
                    day >= %s AND
                    day < %s
        ORDER BY    day DESC
    )
    SELECT      JSON_AGG(result.*)
    FROM        result;
    """
    with db.cursor() as cursor:
        cursor.execute(query, (sensor, start_day, end_day, ))
        result = cursor.fetchone()
    return result[0] if result else None
