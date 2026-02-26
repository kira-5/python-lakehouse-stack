import pandas as pd
import os

# Ensure the directory exists
os.makedirs('data/raw', exist_ok=True)

# 1. Users Data
users_df = pd.DataFrame([
    {"id": 1, "name": "Alice", "created_at": "2023-01-01 10:00:00"},
    {"id": 2, "name": "Bob", "created_at": "2023-01-02 11:30:00"},
    {"id": 3, "name": "Charlie", "created_at": "2023-01-03 12:15:00"},
    {"id": 4, "name": "Diana", "created_at": "2023-01-04 09:45:00"},
    {"id": 5, "name": "Edward", "created_at": "2023-01-05 14:20:00"}
])

# 2. Orders Data
orders_df = pd.DataFrame([
    {"order_id": 101, "user_id": 1, "amount": 300.50, "status": "COMPLETED", "order_date": "2023-01-05"},
    {"order_id": 102, "user_id": 1, "amount": 250.00, "status": "COMPLETED", "order_date": "2023-01-07"},
    {"order_id": 103, "user_id": 2, "amount": 50.00, "status": "PENDING", "order_date": "2023-02-16"},
    {"order_id": 104, "user_id": 3, "amount": 600.00, "status": "COMPLETED", "order_date": "2023-03-12"},
    {"order_id": 105, "user_id": 4, "amount": 100.00, "status": "CANCELLED", "order_date": "2023-04-21"},
    {"order_id": 106, "user_id": 4, "amount": 150.00, "status": "COMPLETED", "order_date": "2023-04-22"}
])

# Export to Excel
print("🚀 Generating Excel files for Level 1...")
users_df.to_excel("data/raw/users.xlsx", index=False)
orders_df.to_excel("data/raw/orders.xlsx", index=False)

print("✅ Created: data/raw/users.xlsx")
print("✅ Created: data/raw/orders.xlsx")
