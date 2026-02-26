import duckdb
import os

# Create the warehouse directory if it doesn't exist
os.makedirs('data/warehouse', exist_ok=True)

print("🚀 Starting Level 1 Ingestion: CSV -> Parquet (The Shortcut)")

# 1. Ingest Users Table
duckdb.sql("""
    COPY (
        SELECT 
            id::INTEGER as user_id,
            name::VARCHAR as name,
            created_at::TIMESTAMP as join_date
        FROM read_csv_auto('data/raw/users.csv')
    ) TO 'data/warehouse/users_from_csv.parquet' (FORMAT PARQUET);
""")
print("✅ Ingested: users.csv -> warehouse/users_from_csv.parquet")

# 2. Ingest Orders Table
duckdb.sql("""
    COPY (
        SELECT 
            order_id::INTEGER as order_id,
            user_id::INTEGER as user_id,
            amount::DECIMAL(10,2) as amount,
            status::VARCHAR as status,
            order_date::DATE as order_date
        FROM read_csv_auto('data/raw/orders.csv')
    ) TO 'data/warehouse/orders_from_csv.parquet' (FORMAT PARQUET);
""")
print("✅ Ingested: orders.csv -> warehouse/orders_from_csv.parquet")

print("\n🏁 Level 1 (CSV) Complete: The Warehouse is now seeded with E-commerce core tables.")