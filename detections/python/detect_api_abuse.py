import pandas as pd

print("Loading data and analyzing events...")

df = pd.read_csv("data/api_logs.csv")

suspicious = df[df["user"] != df["resource_owner"]]

results = (
    suspicious.groupby(["user", "ip"])
    .size()
    .reset_index(name="suspicious_accesses")
)

alerts = results[results["suspicious_accesses"] >= 5]

print("=== Suspicious API Access Alerts ===")

if alerts.empty:
    print("No alerts detected.")
else:
    print(alerts.to_string(index=False))

print("\nDetection complete.\n")