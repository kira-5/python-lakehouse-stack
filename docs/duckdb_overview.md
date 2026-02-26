# 🦆 DuckDB Mastery: Technical Overview

DuckDB is an analytical in-process SQL database management system. Think of it as **SQLite for Data Science**.

## 🚀 Key Features

* **Columnar Execution**: Unlike PostgreSQL or SQLite (row-based), DuckDB processes data by columns. This makes analytical queries (aggregations, filters) incredibly fast.
* **In-Process**: No server to install. It runs inside your Python script, Notebook, or CLI.
* **Zero Dependencies**: A single file/binary is all you need.
* **Direct Querying**: You can query Parquet, CSV, and JSON files without "importing" them into a database.

## 🧠 Why we use it in a Lakehouse
DuckDB acts as the **"Computation Engine"**. It handles the heavy lifting of reading files from storage (`data/raw`) and writing high-performance formats to the warehouse (`data/warehouse`).

## 📚 Documentation index

1. [Persistence & Connections](duckdb_persistence.md) - Understanding memory vs. disk.
2. [CLI Guide](duckdb_cli_guide.md) - Mastering the terminal.
3. [File Formats](duckdb_file_formats.md) - CSV, JSON, and the magic of Parquet.
4. [Zero-Copy Data Transfer](duckdb_zero_copy.md) - How to move millions of rows in 0ms.
