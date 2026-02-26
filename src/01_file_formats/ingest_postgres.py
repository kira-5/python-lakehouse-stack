import duckdb

print("🚀 Starting Level 1 Ingestion: SQL Database (Mirroring Postgres)")

# 1. Enable Postgres support
duckdb.sql("INSTALL postgres; LOAD postgres;")

# 2. Explain the Connection logic
print("\n--- Postgres Mirroring Concept ---")
print("In this stack, we use DuckDB to 'attach' a Postgres database.")
print("This allows us to query Postgres tables as if they were local and pipe them directly to Parquet.")

print("\nExample Command:")
print("ATTACH 'dbname=myshop user=admin password=secret host=localhost' AS my_db (TYPE postgres);")
print("ATTACH 'dbname=myshop user=admin password=secret host=localhost' AS my_db (TYPE postgres);")
print("-- Selective sync (The Gatekeeper pattern)")
print("COPY (SELECT id, name, created_at FROM my_db.users) TO 'data/warehouse/users_from_postgres.parquet';")
print("COPY (SELECT id, user_id, amount FROM my_db.orders) TO 'data/warehouse/orders_from_postgres.parquet';")

print("\n✅ This 'Mirroring' pattern is the most efficient way to build an analytical Lakehouse")
print("   without impacting the performance of your production application.")

print("\n🏁 Level 1 (Postgres) Complete.")
