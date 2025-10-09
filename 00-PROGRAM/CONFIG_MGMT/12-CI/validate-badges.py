#!/usr/bin/env python3
import json, csv, pathlib, sys
root = pathlib.Path(__file__).resolve().parents[1]/"11-BADGES"
errors = 0
for j in root.joinpath("ISSUED").rglob("*.json"):
    try: json.loads(j.read_text())
    except Exception as e:
        print(f"[BADGE] INVALID {j}: {e}"); errors += 1
log = root/"LOG/badge-log.csv"
if not log.exists(): print("[BADGE] Missing badge-log.csv"); errors += 1
sys.exit(1 if errors else 0)
