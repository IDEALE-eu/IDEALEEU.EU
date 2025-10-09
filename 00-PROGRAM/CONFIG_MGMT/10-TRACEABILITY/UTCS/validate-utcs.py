#!/usr/bin/env python3
import json, sys, pathlib
from jsonschema import validate
root = pathlib.Path(__file__).resolve().parents[0]
schema = json.loads((root/"SCHEMAS/utcs-record.schema.json").read_text())
errors = 0
for p in (root/"RECORDS").rglob("*.json"):
    try:
        validate(json.loads(p.read_text()), schema)
    except Exception as e:
        print(f"[UTCS] INVALID {p}: {e}")
        errors += 1
sys.exit(1 if errors else 0)
