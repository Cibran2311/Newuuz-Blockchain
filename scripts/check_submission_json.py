import json
from pathlib import Path

path = Path("submission.json")

if not path.exists():
    print("submission.json not found. This is OK for the course site repository, but required in student repositories.")
    raise SystemExit(0)

try:
    data = json.loads(path.read_text(encoding="utf-8"))
except Exception as exc:
    print(f"Invalid JSON: {exc}")
    raise SystemExit(1)

for key in ["student", "wallets"]:
    if key not in data:
        print(f"Missing required top-level field: {key}")
        raise SystemExit(1)

print("submission.json is valid.")
