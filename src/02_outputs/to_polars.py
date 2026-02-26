import duckdb
import polars as pl
import os

# LEVEL 2: The Logic
# Concept: Zero-Copy data transfer from DuckDB to Polars
# Scenario: Identifying high-value customers by joining warehouse tables

# 1. Connect to our local warehouse files
print("🚀 Level 2: Analytical Logic with Polars")

# We can query Parquet files directly as if they were tables
# In this example, we join Users and Orders from the warehouse
query = """
    SELECT 
        u.name,
        SUM(o.amount) as total_spent,
        COUNT(o.order_id) as order_count
    FROM 'data/warehouse/users_from_csv.parquet' u
    JOIN 'data/warehouse/orders_from_csv.parquet' o ON u.user_id = o.user_id
    GROUP BY ALL
    ORDER BY total_spent DESC
"""

# 2. Extract results to Polars (Zero-Copy)
print("Transferring Joined Data from DuckDB room to Polars logic...")
df = duckdb.sql(query).pl()

print("\n--- Polars DataFrame (VIPs) ---")
print(df)

# 3. Further Logic in Polars (Fast & Fluent)
vips = df.filter(pl.col("total_spent") > 500)
print("\n--- Filtered VIPs (Spent > $500) ---")
print(vips)
