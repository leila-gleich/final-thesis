import duckdb

def add_rolling_features(con, table_name="vw_tsa_active_throughput"):
    """Calculates 7-day and 30-day moving average throughput per airport."""
    query = f"""
    SELECT 
        dateId,
        airportId,
        SUM(throughput) as dailyThroughput,
        AVG(SUM(throughput)) OVER(PARTITION BY airportId ORDER BY dateId ROWS BETWEEN 6 PRECEDING AND CURRENT ROW) as rolling7DayAvg,
        AVG(SUM(throughput)) OVER(PARTITION BY airportId ORDER BY dateId ROWS BETWEEN 29 PRECEDING AND CURRENT ROW) as rolling30DayAvg
    FROM {table_name}
    GROUP BY dateId, airportId
    """
    return con.execute(query).df()

extract_temporal_features = add_rolling_features

