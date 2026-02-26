import duckdb
from pathlib import Path

# PRODUCTION: Shared Database Connection
# This utility ensures we always point to the same file

DB_PATH = Path("data/warehouse/lakehouse.duckdb")

def get_connection():
    """Returns a persistent DuckDB connection"""
    # Create parent directories if they don't exist
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    return duckdb.connect(str(DB_PATH))

def initialize_db():
    """Run initial setup (extensions, settings)"""
    con = get_connection()
    con.execute("INSTALL json;") # Ensure JSON extension is ready
    con.execute("LOAD json;")
    con.close()
    print("Database initialized.")
