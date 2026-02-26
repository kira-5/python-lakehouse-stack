# 🗺️ Python Lakehouse Stack: From Files to Lakehouse

A curriculum-based guide to mastering data engineering with Python, DuckDB, Polars, and Lakehouse formats.

## 🚀 The Roadmap

### Level 1: The Basics (File Formats)
**Goal:** Master the "Input" layer.
- **Concepts:** Reading messy CSVs, handling nested JSON, and converting to high-performance Parquet.
- **Key Learn:** Why `read_parquet` is faster than `read_csv` (Columnar vs Row-based).

### Level 2: The Logic (Output Formats)
**Goal:** Get data into the right shape for your code.
- **Concepts:** Moving data from DuckDB into Polars, Pandas, and Arrow.
- **Key Learn:** **Zero-Copy.** Moving millions of rows between DuckDB and Polars in 0ms using Arrow.

### Level 3: The Reliability (Lakehouse Formats)
**Goal:** Solve the "Update Problem."
- **Concepts:** Implementing Delta Lake and Iceberg.
- **Key Learn:** How to `UPDATE` or `DELETE` rows in a Parquet-based world without rewriting the whole dataset.

---

## 📂 Repository Structure

```plaintext
python-lakehouse-stack/
├── pyproject.toml         # Dependency list (DuckDB, Polars, etc.)
├── README.md              # Project documentation
├── .gitignore             # Critical for data engineering
├── data/                  # LOCAL STORAGE (Git-ignored)
│   ├── raw/               # .csv and .json files
│   ├── warehouse/         # .parquet and .duckdb files
│   └── lakehouse/         # Delta/Iceberg table directories
├── notebooks/             # For SQL experimentation
└── src/
    ├── 01_file_formats/   # LEARNING: CSV, JSON -> Parquet
    ├── 02_outputs/        # LEARNING: DuckDB -> Polars, Arrow, Pandas
    ├── 03_lakehouse/      # LEARNING: Updates, Deletes, Time Travel
    └── app/               # PRODUCTION: FastAPI application
```

## 🛠️ Tech Stack
- **Database:** DuckDB
- **DataFrames:** Polars, Pandas
- **Format:** Apache Arrow, Parquet
- **Lakehouse:** Delta Lake, Apache Iceberg
- **API:** FastAPI
