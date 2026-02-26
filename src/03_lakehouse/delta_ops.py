from deltalake import DeltaTable, write_deltalake
import pandas as pd
import duckdb
import os

# LEVEL 3: The Reliability
# Concept: ACID Transactions on Parquet files
# Key Learn: How to UPDATE or DELETE without rewriting everything

table_path = "data/lakehouse/users_delta"

# 1. Initial Write (Create Delta Table)
print("Creating Delta Table...")
df = pd.DataFrame({"id": [1, 2], "name": ["Alice", "Bob"]})
write_deltalake(table_path, df, mode="overwrite")

# 2. Append new data
print("Appending data...")
new_df = pd.DataFrame({"id": [3], "name": ["Charlie"]})
write_deltalake(table_path, new_df, mode="append")

# 3. Read back using DuckDB (The "Lakehouse" pattern)
print("\n--- Current Delta Table ---")
print(duckdb.sql(f"SELECT * FROM delta_scan('{table_path}')").show())
