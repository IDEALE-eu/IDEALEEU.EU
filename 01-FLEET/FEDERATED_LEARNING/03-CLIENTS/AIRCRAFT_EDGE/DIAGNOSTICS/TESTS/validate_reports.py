#!/usr/bin/env python3
"""
Validate Diagnostic Reports

This script validates diagnostic report JSON files against the schema
and checks for common issues.

Usage:
    python validate_reports.py <report_file_or_directory>
    python validate_reports.py /var/fl-client/reports/
    python validate_reports.py /var/fl-client/reports/diag_report_20251011_190000.json
"""

import sys
import json
import argparse
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Any

try:
    import jsonschema
    JSONSCHEMA_AVAILABLE = True
except ImportError:
    JSONSCHEMA_AVAILABLE = False
    print("WARNING: jsonschema library not available. Install with: pip install jsonschema")


class ReportValidator:
    """Validator for diagnostic reports."""
    
    def __init__(self, schema_path: Path):
        """Initialize validator with schema."""
        self.schema_path = schema_path
        self.schema = None
        
        if schema_path.exists() and JSONSCHEMA_AVAILABLE:
            with open(schema_path, 'r') as f:
                self.schema = json.load(f)
        elif not schema_path.exists():
            print(f"WARNING: Schema not found: {schema_path}")
        
        self.results = {
            "total": 0,
            "valid": 0,
            "invalid": 0,
            "errors": []
        }
    
    def validate_report(self, report_path: Path) -> bool:
        """Validate a single report file."""
        self.results["total"] += 1
        
        try:
            with open(report_path, 'r') as f:
                report = json.load(f)
            
            # Schema validation
            if self.schema and JSONSCHEMA_AVAILABLE:
                try:
                    jsonschema.validate(instance=report, schema=self.schema)
                except jsonschema.ValidationError as e:
                    self.results["invalid"] += 1
                    self.results["errors"].append({
                        "file": str(report_path),
                        "error": f"Schema validation failed: {e.message}"
                    })
                    return False
            
            # Semantic validation
            if not self._validate_semantics(report, report_path):
                return False
            
            self.results["valid"] += 1
            return True
        
        except json.JSONDecodeError as e:
            self.results["invalid"] += 1
            self.results["errors"].append({
                "file": str(report_path),
                "error": f"Invalid JSON: {e}"
            })
            return False
        
        except Exception as e:
            self.results["invalid"] += 1
            self.results["errors"].append({
                "file": str(report_path),
                "error": f"Unexpected error: {e}"
            })
            return False
    
    def _validate_semantics(self, report: Dict[str, Any], report_path: Path) -> bool:
        """Validate semantic rules."""
        errors = []
        
        # Check timestamp format
        try:
            timestamp = report.get("timestamp", "")
            datetime.fromisoformat(timestamp.replace("Z", "+00:00"))
        except (ValueError, AttributeError):
            errors.append("Invalid timestamp format")
        
        # Check aircraft ID format
        aircraft_id = report.get("aircraft_id", "")
        if not aircraft_id.startswith("AC-H2-"):
            errors.append(f"Invalid aircraft_id format: {aircraft_id}")
        
        # Check overall status consistency
        overall_status = report.get("overall_status", "")
        diagnostics = report.get("diagnostics", {})
        
        if diagnostics:
            statuses = [v.get("status", "") for v in diagnostics.values()]
            
            # If any diagnostic is unhealthy, overall should be unhealthy
            if "unhealthy" in statuses and overall_status != "unhealthy":
                errors.append(f"Inconsistent status: diagnostics contain 'unhealthy' but overall is '{overall_status}'")
        
        # Check that required diagnostics are present
        required_diagnostics = ["health", "network", "storage", "security", "training"]
        missing = [d for d in required_diagnostics if d not in diagnostics]
        if missing:
            errors.append(f"Missing diagnostics: {', '.join(missing)}")
        
        # Report errors
        if errors:
            self.results["invalid"] += 1
            self.results["errors"].append({
                "file": str(report_path),
                "error": "; ".join(errors)
            })
            return False
        
        return True
    
    def validate_directory(self, directory: Path) -> None:
        """Validate all report files in a directory."""
        report_files = list(directory.glob("*.json"))
        
        if not report_files:
            print(f"No JSON files found in {directory}")
            return
        
        print(f"Found {len(report_files)} report files")
        
        for report_file in report_files:
            self.validate_report(report_file)
    
    def print_summary(self) -> int:
        """Print validation summary and return exit code."""
        print("\n=== Validation Summary ===")
        print(f"Total reports: {self.results['total']}")
        print(f"Valid: {self.results['valid']}")
        print(f"Invalid: {self.results['invalid']}")
        
        if self.results["errors"]:
            print("\n=== Errors ===")
            for error in self.results["errors"]:
                print(f"File: {error['file']}")
                print(f"Error: {error['error']}")
                print()
        
        if self.results["invalid"] > 0:
            return 1
        else:
            print("All reports are valid!")
            return 0


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description="Validate diagnostic report files"
    )
    parser.add_argument(
        "path",
        type=str,
        help="Path to report file or directory containing report files"
    )
    parser.add_argument(
        "--schema",
        type=str,
        default=None,
        help="Path to schema file (default: ../SCHEMAS/diag_report.schema.json)"
    )
    
    args = parser.parse_args()
    
    # Determine schema path
    if args.schema:
        schema_path = Path(args.schema)
    else:
        script_dir = Path(__file__).parent
        schema_path = script_dir.parent / "SCHEMAS" / "diag_report.schema.json"
    
    # Create validator
    validator = ReportValidator(schema_path)
    
    # Validate
    target_path = Path(args.path)
    
    if not target_path.exists():
        print(f"ERROR: Path not found: {target_path}")
        return 1
    
    if target_path.is_file():
        validator.validate_report(target_path)
    elif target_path.is_dir():
        validator.validate_directory(target_path)
    else:
        print(f"ERROR: Invalid path: {target_path}")
        return 1
    
    # Print summary
    return validator.print_summary()


if __name__ == "__main__":
    sys.exit(main())
