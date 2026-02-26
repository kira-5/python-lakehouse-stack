from fastapi import FastAPI
from src.app.database import get_connection

# PRODUCTION: FastAPI application
# Bridging your Data Warehouse to the Web

app = FastAPI(title="Python Lakehouse Stack")

@app.get("/")
def read_root():
    return {"status": "Lakehouse API is Online"}

@app.get("/users")
def get_users():
    """Query the Parquet warehouse via the API"""
    con = get_connection()
    # Querying the Parquet file directly for high speed
    res = con.sql("SELECT * FROM 'data/warehouse/users.parquet'").df()
    return res.to_dict(orient="records")
