import duckdb
import pandas as pd

# 🚀 Level 2: The Handshake (DuckDB -> Pandas)

print("🧠 Mission: The Pandas Bridge")
print("Pandas is the 'Standard English' of Python Data Science.")

# 1. Connect to our Warehouse (Parquet files from Level 1)
# We use duckdb.sql() to reach into the Parquet files we "Locked" in the Vault.
users_parquet = 'data/warehouse/users_from_csv.parquet'

print(f"\nReading from {users_parquet}...")

# 2. Convert to Pandas using the native .df() method
# This is highly optimized, though not as "Zero-Copy" as Arrow/Polars
df = duckdb.sql(f"SELECT * FROM '{users_parquet}' LIMIT 5").df()

print("\n✅ Success: Data is now a Pandas DataFrame!")
print(f"Type: {type(df)}")
print("\n--- First 5 Rows ---")
print(df)

# 3. Why do this? Compatibility!
print("\n🎯 Why Pandas? You can now use 1,000s of legacy libraries:")
print("- Matplotlib/Seaborn for charts")
print("- Scikit-learn for Machine Learning")
print("- Exporting to CSV/Excel for business users")

print("\n🏁 Bridge to Pandas Complete.")
