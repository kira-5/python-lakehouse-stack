import duckdb
import os

# Create the warehouse directory if it doesn't exist
os.makedirs('data/warehouse', exist_ok=True)

print("🚀 Level 1: Remote HTTP Ingestion")

# 1. Enable HTTP support
duckdb.sql("INSTALL httpfs; LOAD httpfs;")

# 2. HTTP Users Example (Public Dataset: Titanic Passengers)
print("\n--- HTTP Users Streaming ---")
remote_users_url = "https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv"

try:
    print(f"Streaming users from {remote_users_url}...")
    duckdb.sql(f"""
        COPY (
            SELECT 
                PassengerId::INTEGER as user_id,
                Name::VARCHAR as name,
                Age::FLOAT as age,
                Sex::VARCHAR as gender
            FROM read_csv_auto('{remote_users_url}')
            LIMIT 100
        ) TO 'data/warehouse/users_from_http.parquet' (FORMAT PARQUET);
    """)
    print("✅ Success: Remote Users -> warehouse/users_from_http.parquet (Typed)")
except Exception as e:
    print(f"⚠️ HTTP Users Streaming failed: {e}")

# 3. HTTP Orders Example (Public Dataset: Hotel Bookings)
print("\n--- HTTP Orders Streaming ---")
remote_orders_url = "https://raw.githubusercontent.com/rfordatascience/tidytuesday/master/data/2020/2020-02-11/hotels.csv"

try:
    print(f"Streaming orders from {remote_orders_url}...")
    duckdb.sql(f"""
        COPY (
            SELECT 
                hotel::VARCHAR as hotel_type,
                lead_time::INTEGER as lead_days,
                arrival_date_year::INTEGER as year,
                arrival_date_month::VARCHAR as month
            FROM read_csv_auto('{remote_orders_url}')
            LIMIT 100
        ) TO 'data/warehouse/orders_from_http.parquet' (FORMAT PARQUET);
    """)
    print("✅ Success: Remote Orders -> warehouse/orders_from_http.parquet (Typed)")
except Exception as e:
    print(f"⚠️ HTTP Orders Streaming failed: {e}")

print("\n🏁 HTTP Ingestion Mission Complete.")
