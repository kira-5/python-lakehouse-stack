Level 1: The Basics (File Formats)
Goal: Master the "Input" layer.

Concepts: How to read messy CSVs, handle nested JSON, and convert them to high-performance Parquet.

Key Learn: Why read_parquet is faster than read_csv (Columnar vs Row-based).

Level 2: The Logic (Output Formats)
Goal: Get data into the right shape for your code.

Concepts: Moving data from DuckDB into Polars, Pandas, and Arrow.

Key Learn: Zero-Copy. Moving millions of rows between DuckDB and Polars in 0ms using Arrow.

Level 3: The Reliability (Lakehouse Formats)
Goal: Solve the "Update Problem."

Concepts: Implementing Delta Lake and Iceberg.

Key Learn: How to UPDATE or DELETE rows in a Parquet-based world without rewriting the whole dataset.