import sqlite3
import pandas as pd
from pathlib import Path

print("=== Running SQL Detection Engine ===\n")

# Create in-memory database
conn = sqlite3.connect(":memory:")

# Load CSVs into database
pd.read_csv("data/auth_logs.csv").to_sql("auth_logs", conn, index=False, if_exists="replace")
pd.read_csv("data/api_logs.csv").to_sql("api_logs", conn, index=False, if_exists="replace")
pd.read_csv("data/cloud_logs.csv").to_sql("cloud_logs", conn, index=False, if_exists="replace")

sql_dir = Path("detections/sql")

for sql_file in sql_dir.glob("*.sql"):
    print(f"\n=== Running {sql_file.name} ===")

    query = sql_file.read_text()
    df = pd.read_sql_query(query, conn)

    if df.empty:
        print("No alerts detected.")
    else:
        print(df.to_string(index=False))

print("\nSQL Detection Engine Complete.\n")