import duckdb
import os

# Create the warehouse directory if it doesn't exist
os.makedirs('data/warehouse', exist_ok=True)

print("🚀 Starting Level 1 Ingestion: Excel -> Parquet (Business Data Sync)")

# DuckDB's spatial extension includes Excel support.
duckdb.sql("INSTALL spatial; LOAD spatial;")

# 1. Ingest Users from Excel
print("Syncing Users from Excel...")
duckdb.sql("""
    COPY (
        SELECT 
            id::INTEGER as user_id,
            name::VARCHAR as name,
            created_at::TIMESTAMP as join_date
        FROM st_read('data/raw/users.xlsx')
    ) TO 'data/warehouse/users_from_excel.parquet' (FORMAT PARQUET);
""")
print("✅ Ingested: users.xlsx -> warehouse/users_from_excel.parquet")

# 2. Ingest Orders from Excel
print("Syncing Orders from Excel...")
duckdb.sql("""
    COPY (
        SELECT 
            order_id::INTEGER as order_id,
            user_id::INTEGER as user_id,
            amount::DECIMAL(10,2) as amount,
            status::VARCHAR as status,
            order_date::DATE as order_date
        FROM st_read('data/raw/orders.xlsx')
    ) TO 'data/warehouse/orders_from_excel.parquet' (FORMAT PARQUET);
""")
print("✅ Ingested: orders.xlsx -> warehouse/orders_from_excel.parquet")

print("\n🏁 Level 1 (Excel) Complete: Business logic tables are now in the warehouse.")
