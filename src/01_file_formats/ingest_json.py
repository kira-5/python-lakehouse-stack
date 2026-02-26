import duckdb

# Convert nested JSON to Parquet
# LEVEL 1: Master the "Input" layer
# Concept: Flattening nested data and enforcing schema

print("Starting JSON ingestion...")

duckdb.sql("""
    COPY (
        SELECT 
            user_id::INTEGER as id,
            profile.email::VARCHAR as email,
            profile.city::VARCHAR as city,
            len(logins)::INTEGER as login_count
        FROM read_json_auto('data/raw/users.json')
    ) TO 'data/warehouse/users_from_json.parquet' (FORMAT PARQUET);
""")

print("Conversion complete: JSON -> Parquet (Flattened & Typed)")
