import duckdb

def get_preflight_train_data(con, start_date_id=20190101, end_date_id=20241231, top_airports=None):
    """Extracts sanitized pre-flight training dataset with zero data leakage."""
    airport_filter = ""
    if top_airports:
        airport_list_str = ", ".join(map(str, top_airports))
        airport_filter = f"AND originAirportId IN ({airport_list_str})"
        
    query = f"""
    SELECT 
        dateId,
        airlineId,
        originAirportId,
        destAirportId,
        crsDepTime,
        crsArrTime,
        crsElapsedTime,
        distance,
        distanceGroup,
        depTimeBlockId,
        arrTimeBlockId,
        cancelled,
        depDel15
    FROM vw_otp_preflight_ml
    WHERE dateId BETWEEN {start_date_id} AND {end_date_id}
    {airport_filter}
    """
    return con.execute(query).df()
