# 🏛️ Level 1: The Input (Ingestion Strategy)

Level 1 is where we move from the "RAM Laboratory" to the **Data Warehouse**. It focuses on the "First Mile"—getting data from the outside world into our Lakehouse safely and efficiently.

---

## 🚀 Quick Start: Run the Missions

Run these commands in order to populate your Lakehouse warehouse using different ingestion strategies:

```bash
# 1. Core Ingestion (CSV)
python src/01_file_formats/ingest_csv.py

# 2. Semi-Structured (JSON + Flattening)
python src/01_file_formats/ingest_json.py

# 3. Business Data (Excel)
python src/01_file_formats/ingest_excel.py

# 4. Remote APIs (HTTP Streaming)
python src/01_file_formats/ingest_http.py

# 5. Cloud Blueprint (S3/GCS Concept)
python src/01_file_formats/ingest_cloud.py

# 6. Database Blueprint (SQL Mirroring Concept)
python src/01_file_formats/ingest_postgres.py
```

---

## 🎯 The Main Objective: Consistency

Raw files like CSV and JSON are dangerous because they have no "Rules." A CSV might have a "Date" column that is actually just a string of text, or an "ID" that changes from numbers to words.

Level 1 is where we move from the "RAM Laboratory" to the **Data Warehouse**.

### 🛑 Graduation from In-Memory

Unlike **Level 0**, which was "In-Memory Only," **Level 1 is about Persistence**.

| Level | Mode | Storage | Analogy |
| :--- | :--- | :--- | :--- |
| **Level 0** | **In-Memory** | Disappears when script ends | The RAM Laboratory |
| **Level 1** | **Persistent** | Saved to `data/warehouse/*.parquet` | The Vault |

### 🛠️ Why this matters

Every script we wrote in Level 1 (CSV, JSON, Excel, etc.) uses the `COPY (...) TO '...parquet'` command. This command tells DuckDB: *"Process this in memory for speed, but **burn the result onto the disk** so it lives forever."*

---

## 🛠️ What we cover in Level 1

### 1. `ingest_csv.py` (Structured Input)

*   **The Problem**: CSVs are slow to read and have no metadata.
*   **The Solution**: Use DuckDB to read the CSV, apply a **Strict Schema**, and save it as a Parquet "Gold" file.

### 2. `ingest_json.py` (Semi-Structured Input)

*   **The Problem**: JSON is often "nested" (objects inside objects), which traditional SQL engines struggle to handle.
*   **The Solution**: DuckDB automatically "flattens" these nested structures into a flat table format during ingestion.

---

## 📂 The Input Spectrum

Level 1 isn't just for one file type. DuckDB allows us to ingest data from a wide "spectrum" of sources:

| Source | File Type | Feature |
| :--- | :--- | :--- |
| **Flat Files** | `.csv`, `.tsv`, `.txt` | The most common but "messiest" source. |
| **Semi-Structured** | `.json`, `.ndjson` | Includes nested objects and lists. |
| **Spreadsheets** | `.xlsx`, `.ods` | Business data from Excel. |
| **Cloud Files** | `s3://`, `gcs://` | Reading directly from a Cloud Bucket. |
| **Remote APIs** | `https://...` | Downloading raw data via URL. |
| **SQL Databases** | Postgres, MySQL | Syncing data from an existing transactional DB. |

---

## 🧠 Key Concept: "Schema Enforcement"

In a Lakehouse stack, we **never** just copy a CSV. We always follow this 3-step mantra:

1.  **Inspect**: Look at the raw file to see what it *looks* like.
2.  **Define**: Explicitly tell the computer what the types *should* be (Integer, Date, Boolean).
3.  **Convert**: Transform the data into Parquet to bake in those types forever.

---

## 🚄 Why Parquet?

By the end of Level 1, your `data/warehouse/` will contain files that are:

*   **Fast**: Columnar storage means we only read the data we need.
*   **Typed**: The data types are stored *inside* the file.
*   **Compressed**: Typically 5x to 10x smaller than CSV.
*   **Attributed**: Filenames include the source (e.g., `_from_json`) for lineage tracking.

---

## ❓ FAQ: Architecture and Decisions

### Q1: Why call it a "Lakehouse" if we have a warehouse folder?

In a traditional **Data Warehouse**, your data is trapped inside a proprietary database (like Oracle or SQL Server). You can't just "grab" the files.

In a **Data Lakehouse**:

*   The **"Lake"** part means your data lives as open files (Parquet) on a standard filesystem (S3, Azure Blob, or your local `data/` folder).
*   The **"House"** part means we add structure (Schema) and ACID transactions (using Delta/Iceberg later) to those files.

We use the folder name `warehouse/` as a "Curriculum Label" to show where the "Clean" data lives, but technically, it's all part of the Lake.

### Q2: Why output Parquet instead of CSV or DuckDB (.db)?

| Format | Why not? |
| :--- | :--- |
| **CSV** | **Too Dumb**. No types, no compression, and massive file sizes. |
| **DuckDB (.db)** | **Too Locked-In**. If you save as a `.db` file, *only* DuckDB can read it. If a teammate wants to use Spark, Snowflake, or a different BI tool, they are stuck. |
| **Parquet** | **The Goldilocks Format**. It is engine-agnostic. DuckDB writes it, Polars reads it, Snowflake imports it, and AWS Athena queries it. It's the "Portable Warehouse" format. |

### Q3: What is the difference between `write_table` (Level 0) and `COPY` (Level 1)?

In Level 0, we used `pq.write_table(arrow_table)` (**The Bridge**). In Level 1, we use `COPY ... TO` (**The Shortcut**).

**1. Level 0: `pq.write_table(arrow_table)` (The Bridge)**

*   **How it works**: Uses **Python** as the middleman. DuckDB hands a "bucket" of data (Arrow) to Python, and Python saves it.
*   **Why do it?**: Use this when your Python code needs to "touch" or "inspect" the data before it gets saved.

**2. Level 1: `COPY ... TO` (The Shortcut)**

*   **How it works**: The **DuckDB Engine** handles it natively (C++). Python just sends the command.
*   **Why do it?**: **Pure Speed**. Because data never enters Python, it is incredibly fast for bulk ingestion.

### Q4: What are all the input sources we can ingest in Level 1?

DuckDB is the "Swiss Army Knife" of ingestion. It allows your Lakehouse to absorb data from almost anywhere:

| Source | Technical Action | Feature |
| :--- | :--- | :--- |
| **Flat Files** | `read_csv_auto()` | Delimiters, headers, and types are auto-detected. |
| **Semi-Structured** | `read_json_auto()` | Handles nested objects and NDJSON arrays. |
| **Spreadsheets** | `st_read()` | Directly query Excel `.xlsx` files as SQL tables. |
| **GCS Buckets** | `httpfs` extension | Query `gcs://` or `s3://` without downloading first. |
| **Remote APIs** | `https://...` | Stream data directly from a public URL into the lake. |
| **SQL Databases** | `postgres_scan()` | Sync data from Postgres/MySQL via direct connection. |

### Q5: What is the difference between `duckdb.sql()` and `duckdb.connect()`?

When you see `import duckdb`, you have two ways to talk to the engine:

1.  **`duckdb.sql("...")` (Module-Level)**: This uses a **Global In-Memory Connection**. It is the "Auto-Pilot" mode.
    *   **Can it talk to Postgres?** Yes! Just run `ATTACH '...' (TYPE POSTGRES);` on this global connection.
    *   **Best For**: Stateless ingestion pipes (Level 1) where you just move data from A to B.

2.  **`duckdb.connect('file.db')` (Connection-Level)**: This is the "Manual Pilot" mode. Use this when:
    *   **Persistence is needed**: You want to save your work into a permanent `.duckdb` warehouse file.
    *   **Isolation is needed**: You are building a complex app and want private "sandboxes" for different threads.

### 🚪 The "Room & Door" Analogy

Think of it like this:

*   **`duckdb.sql()`**: You are standing in a room (the global memory) and calling out commands. You can shout *"Connect to Postgres!"* (`ATTACH`) and it will happen in that room.
*   **`duckdb.connect()`**: You are opening a **specific door** to a specific room.
    *   If that door is a file (`duckdb.connect('warehouse.db')`), your room is **Permanent**.
    *   If that door is just memory (`duckdb.connect()`), your room is **Private** and isolated from everyone else.

### 🍱 The Rule of Thumb

*   **Level 1 (Ingestion)**: We use `duckdb.sql()` because we are just passing through. We grab data from CSV/JSON/Postgres/HTTP and quickly "dump" it into Parquet files. We don't need a permanent database "room" because the Parquet files *are* our storage.
*   **Level 2/3 (Logic & Apps)**: We will start using `duckdb.connect('main.db')` when we want to build a real analytical application that needs to remember state across multiple Python sessions.

---

## 🛡️ The "Schema Trap": Why not just `SELECT *`?

It’s tempting to just `SELECT *` and let DuckDB guess. Here is why we **Inspect → Define → Convert**:

1.  **Schema Drift**: If CSV column 10 is empty for 10,000 rows, DuckDB might guess `FLOAT`. If row 10,001 contains "Unknown", the ingestion crashes. By defining `VARCHAR`, we prevent the crash.
2.  **Standardization**: Your source might have `join_date` as a string. Your warehouse *needs* it to be a `TIMESTAMP`. Casting during ingestion means Level 2 logic can trust the types.
3.  **Storage Efficiency**: A column guessed as `VARCHAR` takes more space than a `DATE` or `INTEGER`. Parquet uses specific encodings based on the type you choose.
4.  **Downstream Safety**: If you use `SELECT *`, you are at the mercy of the source. If the source adds a "debug_log" column, it enters your warehouse. Manual selection acts as a **Data Gatekeeper**.

> [!IMPORTANT]
> **Postgres Exception**: For SQL databases, the schema is already "locked" in the source. We trust the Postgres types, so we often *can* `SELECT *` safely there.

---

**The Technical Deep-Dive:**

*   **CSV/TSV**: We *override* auto-detection with explicit types for production safety.
*   **JSON**: We use dot notation (e.g., `profile.email`) to flatten objects into columns immediately.
*   **Excel**: DuckDB can read Excel sheets directly, often 10x faster than traditional Python readers.
*   **GCS/Cloud**: This uses "Range Requests," pulling only the specific bytes needed for a query. Use `gs://` paths with service account credentials.
*   **HTTP/URL**: Pull public datasets directly into your warehouse without a middleman script.
*   **Databases**: "Mirror" a production database for analysis without putting load on the live app.
