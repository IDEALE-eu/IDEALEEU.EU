#!/usr/bin/env python3
import csv, sys, pathlib
headers = ["from_sta","to_sta","interface_type","signal_medium","protocol_spec","power_W","data_rate","notes"]
errors = 0
for p in pathlib.Path(".").rglob("INTERFACE_MATRIX/*.csv"):
    with p.open() as f:
        rd = csv.reader(f)
        first = next(rd, [])
        if first != headers:
            print(f"[IFC] {p} header mismatch. Expected: {headers}")
            errors += 1
print(f"[IFC] OK" if errors==0 else f"[IFC] FAIL")
sys.exit(1 if errors else 0)
