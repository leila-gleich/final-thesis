import os
import duckdb

try:
    from utils.logger import setup_logger
except ImportError:
    from ..utils.logger import setup_logger


logger = setup_logger("airport_selector")

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

class AirportSelector:
    """Utility class for filtering datasets by flexible airport selection criteria."""
    
    @staticmethod
    def get_top_airports(con, n=30, dataset="otp"):
        """Returns the top N airport IDs by total flight volume."""
        curated_hourly = os.path.join(REPO_ROOT, "data", "curated", "hourly_aggregated_data.csv")
        legacy_parquet = os.path.join(REPO_ROOT, "archive", "legacy_parquet")
        otp_parquet = os.path.join(legacy_parquet, "01_Executive_Top25_Airport_Coupled_Master_Census.parquet")
        tsa_parquet = os.path.join(legacy_parquet, "TSA_Top25_Attribute_Volatility_Census.parquet")
        
        if dataset == "otp":
            if os.path.exists(curated_hourly):
                query = f"""
                    SELECT Airport as airportId, SUM(Scheduled_Departures) as volume
                    FROM read_csv_auto('{curated_hourly}')
                    GROUP BY 1 ORDER BY volume DESC LIMIT {n}
                """
            elif os.path.exists(otp_parquet):
                query = f"""
                    SELECT Airport as airportId, COUNT(*) as volume 
                    FROM read_parquet('{otp_parquet}')
                    GROUP BY 1 ORDER BY volume DESC LIMIT {n}
                """
            else:
                return ["DFW", "PHL", "ORD", "DTW", "LGA", "BOS", "EWR", "IAH", "LAX"][:n]
        else:
            if os.path.exists(curated_hourly):
                query = f"""
                    SELECT Airport as airportId, SUM(TSA_Throughput) as volume
                    FROM read_csv_auto('{curated_hourly}')
                    GROUP BY 1 ORDER BY volume DESC LIMIT {n}
                """
            elif os.path.exists(tsa_parquet):
                query = f"""
                    SELECT Airport as airportId, SUM(mean_hourly_throughput) as volume 
                    FROM read_parquet('{tsa_parquet}')
                    GROUP BY 1 ORDER BY volume DESC LIMIT {n}
                """
            else:
                return ["DFW", "PHL", "ORD", "DTW", "LGA", "BOS", "EWR", "IAH", "LAX"][:n]
                
        res = con.execute(query).fetchall()
        logger.info(f"Retrieved top {n} airports by volume from {dataset}.")
        return [row[0] for row in res]

