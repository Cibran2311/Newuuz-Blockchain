from __future__ import annotations

import argparse
import json
from pathlib import Path

from jsonschema import Draft202012Validator, FormatChecker


ROOT = Path(__file__).resolve().parents[1]
DEFAULT_SCHEMA = ROOT / "schemas" / "submission.schema.json"


def validate_submission(path: Path, schema_path: Path = DEFAULT_SCHEMA) -> list[str]:
    if not path.exists():
        return [f"{path} was not found"]

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        return [f"Invalid JSON at line {exc.lineno}, column {exc.colno}: {exc.msg}"]

    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(data), key=lambda item: list(item.path))
    return [
        f"{'.'.join(map(str, error.absolute_path)) or '<root>'}: {error.message}"
        for error in errors
    ]


def main() -> int:
    parser = argparse.ArgumentParser(description="Validate a course submission.json")
    parser.add_argument("path", nargs="?", default="submission.json")
    parser.add_argument("--schema", default=str(DEFAULT_SCHEMA))
    args = parser.parse_args()

    errors = validate_submission(Path(args.path), Path(args.schema))
    if errors:
        print("submission.json is invalid:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("submission.json is valid.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
