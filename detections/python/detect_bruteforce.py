import pandas as pd

print("Loading data and analyzing events...")

df = pd.read_csv("data/auth_logs.csv")

failed = df[df["status"] == "failed"]

results = (
    failed.groupby(["ip", "user"])
    .size()
    .reset_index(name="failed_attempts")
)

alerts = results[results["failed_attempts"] >= 5]

print("=== Brute Force Alerts ===")

if alerts.empty:
    print("No alerts detected.")
else:
    print(alerts.to_string(index=False))

print("\nDetection complete.\n")