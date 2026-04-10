import yaml
from pathlib import Path

print("=== Running Detection-as-Code (YAML) Engine ===\n")

yaml_dir = Path("detections/yaml")

for yaml_file in yaml_dir.glob("*.yaml"):
    print(f"=== Loading {yaml_file.name} ===")

    with open(yaml_file, "r") as f:
        detection = yaml.safe_load(f)

    print(f"Name: {detection['name']}")
    print(f"Description: {detection['description']}")
    print(f"Log Source: {detection['log_source']}")
    print(f"Severity: {detection['severity']}")
    print(f"Logic Type: {detection['logic']['type']}")
    print(f"Response: {detection['response']['action']}\n")

print("Detection-as-Code Engine Complete.\n")