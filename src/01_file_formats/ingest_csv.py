import duckdb

# Convert a CSV to Parquet while forcing specific types
# This is a classic backend 'Ingestion' pattern
duckdb.sql("""
    COPY (
        SELECT 
            id::INTEGER as id,
            name::VARCHAR as name,
            created_at::TIMESTAMP as created_at
        FROM read_csv_auto('data/raw/users.csv')
    ) TO 'data/warehouse/users.parquet' (FORMAT PARQUET);
""")
print("Conversion complete: CSV -> Parquet with strict typing.")