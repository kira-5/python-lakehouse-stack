import duckdb
import polars as pl

# LEVEL 2: The Logic
# Concept: Zero-Copy data transfer from DuckDB to Polars
# Key Learn: Moving millions of rows in 0ms using Apache Arrow

# 1. Connect to the warehouse
con = duckdb.connect('data/warehouse/lakehouse.duckdb')

# 2. Extract data to Polars (Zero-Copy)
# The .pl() method uses Apache Arrow under the hood
print("Transferring data from DuckDB to Polars...")
df = con.sql("SELECT * FROM 'data/warehouse/users.parquet'").pl()

print("\n--- Polars DataFrame ---")
print(df)

# 3. Perform Logic in Polars (Speed!)
high_id_users = df.filter(pl.col("id") > 2)
print("\n--- Filtered Result ---")
print(high_id_users)
