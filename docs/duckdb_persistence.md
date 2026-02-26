# DuckDB Persistence: Module Level vs. Connection Objects

In DuckDB, the way you execute queries determines where the data lives and how long it lasts. This guide explains the two primary ways to interact with DuckDB in Python.

## 1. Module-Level: `duckdb.sql(...)`
When you call `duckdb.sql()` directly on the `duckdb` module, it uses a **shared, global, in-memory connection**.

* **Storage:** Always in memory.
* **Persistence:** ❌ **Ephemeral.** Data is deleted the moment your Python script or notebook kernel stops.
* **Best For:**
  - One-off file conversions (e.g., CSV → Parquet).
  - Fast transformations where you don't need a database file.
  - Quick "peeking" at data.

```python
import duckdb

# This runs in a hidden memory space
duckdb.sql("SELECT 42").show()
```

---

## 2. Connection Object: `duckdb.connect(...)`
This creates a specific connection instance. It is the "standard" way for backend and production applications.

### A. Persistent Storage (File-Based)
If you provide a file path, DuckDB creates or opens a `.duckdb` file. Everything you do on this connection is saved to disk.

```python
# Connect to a real database file
con = duckdb.connect('data/warehouse/main.duckdb')

# This table will still be there tomorrow!
con.sql("CREATE TABLE users AS SELECT * FROM 'data/raw/users.csv'")
con.close()
```

### B. Isolated Memory Space
If you call `.connect()` without a path (or with `':memory:'`), it creates a *private* in-memory session.

```python
con = duckdb.connect() # Private in-memory session
con.sql("SET memory_limit = '4GB'")
```

---

## Summary Comparison

| Feature | `duckdb.sql()` (Module) | `con = duckdb.connect()` |
| :--- | :--- | :--- |
| **Default Storage** | Global In-Memory | Memory (Private) or Disk (File) |
| **Data Lifecycle** | Dies with the script | Survives if linked to a file |
| **Isolated Session** | No (Global) | Yes (Private instance) |
| **Best Level** | **Level 1:** File conversions | **Level 2 & 3:** Logic & Lakehouse |

## Recommendation for this Repository

* Level 1 (File Formats): Stick to `duckdb.sql()` for simple script-based ingestion.
* Level 2 & 3 (Logic/Lakehouse): Use `duckdb.connect('data/warehouse/main.duckdb')` to maintain a persistent data warehouse structure.
