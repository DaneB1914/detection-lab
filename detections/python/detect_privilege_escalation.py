import pandas as pd

print("Loading data and analyzing events...")

df = pd.read_csv("data/cloud_logs.csv")

high_risk_actions = [
    "attach_admin_policy",
    "disable_logging",
]

alerts = df[df["action"].isin(high_risk_actions)]

print("=== Privilege Escalation / Defense Evasion Alerts ===")

if alerts.empty:
    print("No alerts detected.")
else:
    print(alerts.to_string(index=False))

print("\nDetection complete.\n")