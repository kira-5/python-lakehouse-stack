import duckdb

# LEVEL 2: The Logic
# Concept: DuckDB -> Apache Arrow (The Universal Language)
# Scenario: Converting the entire Warehouse into a memory-shared state

print("🚀 Level 2: Interoperability with Apache Arrow")

# Fetch both tables into Arrow format
print("Converting users.parquet to Arrow...")
users_arrow = duckdb.sql("SELECT * FROM 'data/warehouse/users.parquet'").arrow()

print("Converting orders.parquet to Arrow...")
orders_arrow = duckdb.sql("SELECT * FROM 'data/warehouse/orders.parquet'").arrow()

print(f"\n✅ Users Columns: {users_arrow.column_names}")
print(f"✅ Orders Columns: {orders_arrow.column_names}")

print(f"\nTotal users in memory (Arrow): {len(users_arrow)}")
print(f"Total orders in memory (Arrow): {len(orders_arrow)}")

# These objects can now be passed to Spark, Pandas, or even C++ apps without copying.
