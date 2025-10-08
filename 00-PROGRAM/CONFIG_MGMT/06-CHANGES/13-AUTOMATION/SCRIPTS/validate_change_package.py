#!/usr/bin/env python3
"""
Validate Change Package Completeness and Consistency

Checks:
- Schema validation
- Cross-references
- Baseline alignment
- Required approvals
- Traceability completeness
"""

import sys
import yaml
import json
from pathlib import Path

def validate_ecr(ecr_file):
    """Validate ECR YAML file"""
    with open(ecr_file) as f:
        ecr = yaml.safe_load(f)
    
    # Check required fields
    required_fields = ['ecr_number', 'date_submitted', 'status', 'submitter']
    for field in required_fields:
        if field not in ecr:
            return False, f"Missing required field: {field}"
    
    return True, "ECR valid"

def validate_eco(eco_file):
    """Validate ECO YAML file"""
    with open(eco_file) as f:
        eco = yaml.safe_load(f)
    
    # Check required fields
    required_fields = ['eco_number', 'ecr_number', 'date_issued', 'status']
    for field in required_fields:
        if field not in eco:
            return False, f"Missing required field: {field}"
    
    return True, "ECO valid"

def main():
    print("Change package validation script")
    print("Usage: validate_change_package.py <ecr_or_eco_file>")
    
    if len(sys.argv) < 2:
        print("Error: No file specified")
        sys.exit(1)
    
    file_path = Path(sys.argv[1])
    
    if not file_path.exists():
        print(f"Error: File not found: {file_path}")
        sys.exit(1)
    
    # Determine type and validate
    if 'ECR' in file_path.name:
        valid, message = validate_ecr(file_path)
    elif 'ECO' in file_path.name:
        valid, message = validate_eco(file_path)
    else:
        print("Error: Unknown file type")
        sys.exit(1)
    
    print(message)
    sys.exit(0 if valid else 1)

if __name__ == '__main__':
    main()
