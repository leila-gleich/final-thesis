import duckdb
import os

def get_db_connection(db_path="data/warehouse.duckdb"):
    """Returns a DuckDB connection singleton."""
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    return duckdb.connect(db_path)
