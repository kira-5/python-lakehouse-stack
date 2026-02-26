# 💻 DuckDB CLI: Terminal Mastery

The DuckDB Command Line Interface (CLI) is the fastest way to interact with your data without writing Python code.

## 🛠️ Opening DuckDB

| Command | Action |
| :--- | :--- |
| `duckdb` | Opens an **in-memory** database (ephemeral). |
| `duckdb warehouse.db` | Opens a **persistent** database file. |
| `duckdb -c "SQL"` | Runs a single SQL command and exits. |

## 🔘 Essential Dot Commands
Dot commands are used for CLI status and configuration, not data manipulation.

* `.help` - List all commands.
* `.tables` - Show existing tables.
* `.schema [table]` - Show the SQL used to create a table.
* `.mode box` - Make SQL results look beautiful.
* `.open [file]` - Switch to a different database file.
* `.quit` or `.exit` - Leave the CLI.

## ⚡ Querying Files Directly
You don't need a table to see your data. Just point DuckDB at a file.

```sql
/* Querying a Parquet file */
SELECT * FROM 'data/warehouse/users.parquet' LIMIT 10;

/* Querying a CSV file with automatic detection */
SELECT * FROM read_csv_auto('data/raw/users.csv');
```

## 📋 Pro Tips

- **Autocomplete**: Use `Tab` to autocomplete table names and SQL keywords.
- **Semicolons**: Every SQL command **must** end with a `;`.
- **History**: Use the Up/Down arrows to see your previous commands.
