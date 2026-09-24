import duckdb
from src.utils.logger import setup_logger

logger = setup_logger("airport_selector")

class AirportSelector:
    """Utility class for filtering datasets by flexible airport selection criteria."""
    
    @staticmethod
    def get_top_airports(con, n=30, dataset="otp"):
        """Returns the top N airport IDs by total flight volume."""
        if dataset == "otp":
            query = f"""
                SELECT originAirportId as airportId, COUNT(*) as volume 
                FROM read_parquet('data/processed/otpv0.parquet')
                WHERE originAirportId > 0
                GROUP BY 1 ORDER BY volume DESC LIMIT {n}
            """
        else:
            query = f"""
                SELECT airportId, SUM(throughput) as volume 
                FROM read_parquet('data/processed/tsav0.parquet')
                WHERE airportId > 0
                GROUP BY 1 ORDER BY volume DESC LIMIT {n}
            """
        res = con.execute(query).fetchall()
        logger.info(f"Retrieved top {n} airports by volume from {dataset}.")
        return [row[0] for row in res]
