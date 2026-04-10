import subprocess

scripts = [
    "detections/python/detect_bruteforce.py",
    "detections/python/detect_api_abuse.py",
    "detections/python/detect_privilege_escalation.py",
]

print("=== Running Detection Lab ===")

for script in scripts:
    print(f"\nRunning {script}...\n")
    subprocess.run(["python", script])

print("\nRunning SQL Detection Engine...\n")
subprocess.run(["python", "run_sql_detections.py"])

print("\nRunning Detection-as-Code Engine...\n")
subprocess.run(["python", "run_yaml_detections.py"])