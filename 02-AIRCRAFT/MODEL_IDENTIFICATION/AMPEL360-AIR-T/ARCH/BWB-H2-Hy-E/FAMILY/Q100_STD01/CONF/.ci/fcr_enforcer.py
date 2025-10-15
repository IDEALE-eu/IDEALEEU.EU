#!/usr/bin/env python3
"""
FCR Enforcer - Functional Compliance Rules CI Check
Validates that CONF directory changes comply with FCR rules.
"""

import sys
import os
import yaml
from pathlib import Path
from typing import List, Tuple

# FCR Rules to enforce
FCR_RULES = {
    "FCR-001": "QS_STATE.yaml must be updated when CONF/ changes",
    "FCR-002": "UTCS.MANIFEST.yaml hash_tree must be updated",
    "FCR-004": "TFA domain tags must be present in headers",
}

def check_fcr_001(changed_files: List[str]) -> Tuple[bool, str]:
    """Check if QS_STATE.yaml was updated when CONF/ changed."""
    conf_files_changed = [f for f in changed_files if "CONF/" in f and f != "CONF/00-CONFIG/QS_STATE.yaml"]
    qs_state_changed = "CONF/00-CONFIG/QS_STATE.yaml" in changed_files
    
    if conf_files_changed and not qs_state_changed:
        return False, f"FCR-001 FAIL: CONF/ files changed but QS_STATE.yaml not updated"
    return True, "FCR-001 PASS"

def check_fcr_002(changed_files: List[str]) -> Tuple[bool, str]:
    """Check if UTCS.MANIFEST.yaml hash_tree was updated."""
    conf_files_changed = [f for f in changed_files if "CONF/" in f and f != "CONF/UTCS.MANIFEST.yaml"]
    manifest_changed = "CONF/UTCS.MANIFEST.yaml" in changed_files
    
    if conf_files_changed and not manifest_changed:
        return False, f"FCR-002 FAIL: CONF/ files changed but UTCS.MANIFEST.yaml not updated"
    
    # Check that hash_tree is not placeholder
    manifest_path = Path("CONF/UTCS.MANIFEST.yaml")
    if manifest_path.exists():
        with open(manifest_path) as f:
            manifest = yaml.safe_load(f)
            if "hash_tree" in manifest and "abcd" in manifest["hash_tree"]:
                return False, "FCR-002 FAIL: hash_tree contains placeholder value"
    
    return True, "FCR-002 PASS"

def check_fcr_004(changed_files: List[str]) -> Tuple[bool, str]:
    """Check that TFA domain tags are present in file headers."""
    domain_files = [f for f in changed_files if any(d in f for d in ["geometry/", "weights/", "performance/", "propulsion/"])]
    
    for filepath in domain_files:
        if not os.path.exists(filepath):
            continue
        
        with open(filepath) as f:
            header = f.read(500)  # Read first 500 chars
            if "tfa_domain" not in header.lower() and "TFA-DOMAINS" not in header:
                return False, f"FCR-004 FAIL: {filepath} missing TFA domain tag"
    
    return True, "FCR-004 PASS"

def main():
    """Main FCR enforcement check."""
    # Get list of changed files from git
    import subprocess
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True,
        text=True
    )
    changed_files = result.stdout.strip().split("\n")
    
    print("=" * 60)
    print("FCR ENFORCER - Checking Functional Compliance Rules")
    print("=" * 60)
    print(f"\nChanged files: {len(changed_files)}")
    
    all_pass = True
    checks = [
        check_fcr_001,
        check_fcr_002,
        check_fcr_004,
    ]
    
    for check in checks:
        passed, message = check(changed_files)
        print(f"\n{message}")
        if not passed:
            all_pass = False
    
    print("\n" + "=" * 60)
    if all_pass:
        print("✅ ALL FCR CHECKS PASSED")
        print("=" * 60)
        return 0
    else:
        print("❌ FCR CHECKS FAILED - Fix issues before merging")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
