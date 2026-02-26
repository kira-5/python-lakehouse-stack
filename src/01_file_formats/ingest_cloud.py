import duckdb

print("🚀 Level 1: Cloud Storage Ingestion (GCS / S3 / Azure)")

# 1. Enable Cloud Support
duckdb.sql("INSTALL httpfs; LOAD httpfs;")

# 2. GCS Cloud Example (The Configuration)
print("\n--- GCS (Google Cloud Storage) Blueprint ---")
print("In a production Lakehouse, you connect directly to your GCS bucket.")

# This code is a blueprint. In a real environment, you would use service account credentials.
blueprint_code = """
-- 1. Set GCS Credentials
SET gcs_region='us-central1';
SET gcs_access_key_id='GOOG...';
SET gcs_secret_access_key='...';

-- 2. Direct Ingestion from GCS to Warehouse
-- Ingest Users with explicit casting
COPY (
    SELECT 
        id::INTEGER as user_id,
        name::VARCHAR as name,
        email::VARCHAR as email
    FROM 'gcs://my-lakehouse/raw/users/*.parquet'
) TO 'data/warehouse/users_from_cloud.parquet';

-- Ingest Orders with explicit casting
COPY (
    SELECT 
        id::INTEGER as order_id,
        amount::DOUBLE as total,
        status::VARCHAR as status
    FROM 'gcs://my-lakehouse/raw/orders/*.parquet'
) TO 'data/warehouse/orders_from_cloud.parquet';
"""

print(blueprint_code)

# 3. S3 and Azure
print("\n--- S3 & Azure Support ---")
print("DuckDB uses the same 'httpfs' extension for other clouds too:")
print("- AWS: s3://my-bucket/data.csv")
print("- Azure: az://my-container/data.parquet")

print("\n✅ Mastery Tip: Use 'gsutil' or 'gcloud storage' locally, but let DuckDB handle the streaming for speed.")

print("\n🏁 Cloud Ingestion (GCS) Mission Complete.")
