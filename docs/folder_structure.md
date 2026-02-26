python-lakehouse-stack/
├── pyproject.toml         # Your dependency list (DuckDB, Polars, etc.)
├── README.md              # Your "fdocs" and project documentation
├── .gitignore             # Critical for data engineering
├── data/                  # LOCAL STORAGE (Git-ignored)
│   ├── raw/               # Drop your .csv and .json files here
│   ├── warehouse/         # Your .parquet and .duckdb files
│   └── lakehouse/         # Your Delta/Iceberg table directories
├── notebooks/             # For SQL experimentation
│   └── 00_playground.ipynb
└── src/
    ├── 01_file_formats/   # LEARNING: CSV, JSON -> Parquet
    │   ├── ingest_csv.py
    │   └── ingest_json.py
    ├── 02_outputs/        # LEARNING: DuckDB -> Polars, Arrow, Pandas
    │   ├── to_polars.py
    │   └── to_arrow.py
    ├── 03_lakehouse/      # LEARNING: Updates, Deletes, Time Travel
    │   ├── delta_ops.py   # CRUD operations with Delta Lake
    │   └── iceberg_ops.py # ACID transactions with Iceberg
    └── app/               # PRODUCTION: Your FastAPI application
        ├── main.py
        └── database.py