from deltalake import write_deltalake
import pandas as pd
import duckdb
import os

# LEVEL 3: The Reliability
# Concept: ACID Transactions on Parquet files (Delta Lake)
# Scenario: Handling an "Order Management" stream with updates/appends

print("🚀 Level 3: ACID Transactions with Delta Lake")

# 1. Setup the Lakehouse path for Orders
lake_path = "data/lakehouse/orders_delta"
os.makedirs("data/lakehouse", exist_ok=True)

# 2. Initial Write: Converting warehouse Parquet to ACID Delta Table
print("Creating ACID Delta Table from warehouse/orders.parquet...")
warehouse_orders = duckdb.sql("SELECT * FROM 'data/warehouse/orders.parquet'").df()
write_deltalake(lake_path, warehouse_orders, mode="overwrite")

# 3. Append: Adding new incoming orders to the Lakehouse
print("Incoming Order Stream: Appending new orders...")
new_orders = pd.DataFrame([
    {"order_id": 107, "user_id": 1, "amount": 99.99, "status": "COMPLETED", "order_date": "2023-04-25"}
])
write_deltalake(lake_path, new_orders, mode="append")

# 4. Read: Querying the reliable Lakehouse using DuckDB
print("\n--- Current Reliable Lakehouse (Orders) ---")
# DuckDB can scan Delta Lake natively via delta_scan
query = f"SELECT * FROM delta_scan('{lake_path}') ORDER BY order_id"
results = duckdb.sql(query).show()

print("\n✅ Success: Your Order data is now protected by ACID transactions.")
