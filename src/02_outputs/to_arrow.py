import duckdb

# LEVEL 2: The Logic
# Concept: DuckDB -> Apache Arrow (In-Memory Columnar format)
# This is the "Universal Language" of this stack

con = duckdb.connect('data/warehouse/lakehouse.duckdb')

print("Fetching Arrow Table...")
arrow_table = con.sql("SELECT * FROM 'data/warehouse/users.parquet'").arrow()

print(f"Type: {type(arrow_table)}")
print(f"Columns: {arrow_table.column_names}")
print(f"Row count: {len(arrow_table)}")
