#!/usr/bin/env python3
import subprocess, sys, pathlib
base = pathlib.Path(__file__).resolve().parents[1]/"10-TRACEABILITY/UTCS/validate-utcs.py"
sys.exit(subprocess.call([str(base)]))
