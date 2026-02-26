import duckdb
import os
import shutil

# 🚀 Level 3: The Architecture (Managing 1 Billion Updates)
# Scenario: Simulating the Data Flow for COW vs. MOR

print("🏛️ Level 3: The Data Flow (COW vs. MOR)")

# Setup a dummy data directory
DATA_DIR = "data/level_3_sim"
os.makedirs(DATA_DIR, exist_ok=True)

# 1. Create Initial Data (The "Base" file)
print("\n--- 1. Creating Base Data ---")
base_sql = "SELECT range as id, 'User_' || range as name, 100 as balance FROM range(5)"
duckdb.sql(base_sql).write_parquet(f"{DATA_DIR}/base.parquet")
print(f"File created: {DATA_DIR}/base.parquet")

# ---------------------------------------------------------
# PATTERN A: COW (Copy-on-Write)
# ---------------------------------------------------------
print("\n--- 2. PATTERN: COW (Copy-on-Write) ---")
print("Scenario: Update User_0's balance to 500")

# Logic: Read the whole file -> Change 1 row -> Rewrite the WHOLE file
cow_sql = f"""
    COPY (
        SELECT id, name, 
        CASE WHEN id = 0 THEN 500 ELSE balance END as balance
        FROM '{DATA_DIR}/base.parquet'
    ) TO '{DATA_DIR}/base_updated_cow.parquet' (FORMAT PARQUET)
"""
duckdb.sql(cow_sql)
print(f"⚠️ COW Flow: To change ONE row, we had to write a NEW file: {DATA_DIR}/base_updated_cow.parquet")

# ---------------------------------------------------------
# PATTERN B: MOR (Merge-on-Read)
# ---------------------------------------------------------
print("\n--- 3. PATTERN: MOR (Merge-on-Read) ---")
print("Scenario: Update User_1's balance to 999")

# Logic: DON'T touch the base file. Just write a tiny "Delta" file.
delta_sql = "SELECT 1 as id, 999 as balance"
duckdb.sql(delta_sql).write_parquet(f"{DATA_DIR}/delta_user_1.parquet")
print(f"✅ MOR Flow: The base file is UNTOUCHED. We only wrote a tiny delta: {DATA_DIR}/delta_user_1.parquet")

# 4. The Handshake (Merging on Read)
print("\n--- 4. The Handshake (Reading MOR) ---")
# When reading, we join the base with the deltas to get the "Current" state
query = f"""
    SELECT 
        b.id, b.name,
        COALESCE(d.balance, b.balance) as balance
    FROM '{DATA_DIR}/base.parquet' b
    LEFT JOIN '{DATA_DIR}/delta_user_1.parquet' d ON b.id = d.id
"""
print("Result of Merge-on-Read Query:")
duckdb.sql(query).show()

# ---------------------------------------------------------
# 5. Compaction (The Nightly Cleanup)
# ---------------------------------------------------------
print("\n--- 5. Compaction (Turning MOR into COW) ---")
print("Merging all deltas back into a single fast file for tomorrow morning...")
duckdb.sql(query).write_parquet(f"{DATA_DIR}/compacted_final.parquet")
print(f"Final compacted state: {DATA_DIR}/compacted_final.parquet")

print("\n🏁 Mission Complete: You have seen the internal flow of a Billion-Row Lakehouse!")
