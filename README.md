# 🗺️ Python Lakehouse Stack: From Files to Lakehouse

A curriculum-based guide to mastering data engineering with Python, DuckDB, Polars, and Lakehouse formats.

### 📚 Quick Links

- **[Documentation Index](docs/index.md)** - Key concepts, CLI guides, and technical deep-dives.
- **[Curriculum Roadmap](docs/roadmap.md)** - Your learning path.

### Level 1: The Input (File Formats)
**Goal:** Master the "Ingestion" layer.
- **Concepts:** Reading messy CSVs, handling nested JSON, and converting to high-performance Parquet.
- **Mission:** **[Level 1 Guide](docs/level_1_ingestion.md)**
- **Code:** `src/01_file_formats/`

### Level 2: The Logic (Output Formats)
**Goal:** Get data into the right shape for your code.
- **Concepts:** Moving data from DuckDB into Polars, Pandas, and Arrow.
- **Mission:** **[Level 2 Guide](docs/level_2_outputs.md)**
- **Code:** `src/02_outputs/`

### Level 3: The Architecture (Lakehouse Formats)
**Goal:** Solve the "Update Problem" at scale.
- **Concepts:** Implementing Delta Lake and Iceberg for ACID transactions.
- **Mission:** **[Level 3 Guide](docs/level_3_architecture.md)**
- **Code:** `src/03_lakehouse/`

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
