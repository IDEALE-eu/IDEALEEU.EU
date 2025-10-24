#!/usr/bin/env python3
"""
Metadata Checker Script

This script validates that all required metadata fields are present
in case metadata files.
"""

import argparse
import sys
import yaml
from pathlib import Path
from typing import List, Tuple


REQUIRED_FIELDS = [
    "case_id",
    "description",
    "revision",
    "solver",
    "solver_version",
    "author",
    "owner",
    "approver",
    "last_updated"
]


def check_metadata(file_path: Path) -> Tuple[bool, List[str]]:
    """
    Check if metadata file has all required fields.
    
    Args:
        file_path: Path to metadata YAML file
        
    Returns:
        Tuple of (is_valid, list_of_errors)
    """
    errors = []
    
    if not file_path.exists():
        return False, [f"Metadata file not found: {file_path}"]
    
    try:
        with open(file_path, 'r') as f:
            metadata = yaml.safe_load(f)
    except Exception as e:
        return False, [f"Failed to parse YAML: {e}"]
    
    if not isinstance(metadata, dict):
        return False, ["Metadata must be a dictionary"]
    
    # Check required fields
    for field in REQUIRED_FIELDS:
        if field not in metadata:
            errors.append(f"Missing required field: {field}")
        elif metadata[field] in ["string", "int", None]:
            errors.append(f"Field '{field}' has placeholder value")
    
    # Check units if present
    if "units" in metadata:
        units = metadata["units"]
        if not isinstance(units, dict):
            errors.append("'units' must be a dictionary")
    
    return len(errors) == 0, errors


def main():
    parser = argparse.ArgumentParser(description="Check CAE metadata files")
    parser.add_argument("files", nargs="*", help="Metadata files to check")
    parser.add_argument("--dir", help="Directory to recursively search for metadata files")
    
    args = parser.parse_args()
    
    files_to_check = []
    
    if args.dir:
        dir_path = Path(args.dir).resolve()
        files_to_check.extend(dir_path.rglob("*metadata*.yaml"))
        files_to_check.extend(dir_path.rglob("*metadata*.yml"))
    
    if args.files:
        files_to_check.extend([Path(f) for f in args.files])
    
    if not files_to_check:
        print("ERROR: No files to check")
        return 1
    
    all_valid = True
    
    for file_path in files_to_check:
        print(f"\nChecking: {file_path}")
        is_valid, errors = check_metadata(file_path)
        
        if is_valid:
            print("  ✓ Valid")
        else:
            print("  ✗ Invalid")
            for error in errors:
                print(f"    - {error}")
            all_valid = False
    
    return 0 if all_valid else 1


if __name__ == "__main__":
    sys.exit(main())
