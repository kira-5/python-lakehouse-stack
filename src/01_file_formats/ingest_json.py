import duckdb
import os

# Create the warehouse directory if it doesn't exist
os.makedirs('data/warehouse', exist_ok=True)

print("🚀 Starting Level 1 Ingestion: JSON -> Parquet (Flattening Nested Data)")

# 1. Ingest Users Profile (Flattened)
print("Flattening nested User profiles...")
duckdb.sql("""
    COPY (
        SELECT 
            user_id::INTEGER as user_id,
            profile.email::VARCHAR as email,
            profile.city::VARCHAR as city,
            len(logins)::INTEGER as session_count
        FROM read_json_auto('data/raw/users.json')
    ) TO 'data/warehouse/users_from_json.parquet' (FORMAT PARQUET);
""")
print("✅ Ingested: users.json (profile) -> warehouse/users_from_json.parquet")

# 2. Ingest Orders with Items (Flattening)
print("Flattening order items...")
duckdb.sql("""
    COPY (
        SELECT 
            order_id::INTEGER as order_id,
            user_id::INTEGER as user_id,
            amount::DECIMAL(10,2) as total_amount,
            status::VARCHAR as status,
            order_date::DATE as order_date,
            list_extract(items, 1).SKU::VARCHAR as first_item_sku -- Explaining how to touch nested lists
        FROM read_json_auto('data/raw/orders.json')
    ) TO 'data/warehouse/orders_from_json.parquet' (FORMAT PARQUET);
""")
print("✅ Ingested: orders.json (items) -> warehouse/orders_from_json.parquet")

print("\n🏁 Level 1 (JSON) Complete: Nested data is now flat and structured.")
