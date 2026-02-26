# 📄 File Formats: The Input Layer

DuckDB is world-class at handling various file formats. The goal of Level 1 is to master these.

## 1. CSV (The Messy Input)

CSV files are row-based and lack schema information (is "123" a number or a string?).

- **DuckDB Tool**: `read_csv_auto()`
- **Pros**: Human-readable, universal.
- **Cons**: Slow to read, heavy on disk, no "typing" (everything is text initially).

## 2. JSON (The Nested Input)
JSON is great for API responses but hard for traditional databases to query.

- **DuckDB Tool**: `read_json_auto()`
- **Pros**: Handles nested data (lists inside objects).
- **Cons**: Extremely slow for large datasets.

## 3. Parquet (The Lakehouse Gold Standard)
Parquet is a **columnar** storage format. It is the core of every modern Lakehouse.

- **DuckDB Tool**: `read_parquet()`
- **Pros**:
  - **Columnar**: If you only need 2 columns out of 100, Parquet only reads those 2.
  - **Typed**: Stores exact types (Integer, Timestamp, etc.).
  - **Compressed**: Uses 5-10x less space than CSV.
- **Cons**: Binary format (you can't open it in TextEdit).

## 🛠️ The "Ingestion" Pattern
This is the code you follow in `src/01_file_formats`:

```sql
COPY (
    SELECT 
        id::INTEGER as id,
        name::VARCHAR as name
    FROM read_csv_auto('raw_data.csv')
) TO 'warehouse.parquet' (FORMAT PARQUET);
```

> [!TIP]
> Always enforce types using `::TYPE` (casting) when converting from CSV to Parquet to ensure your "Warehouse" is clean.
