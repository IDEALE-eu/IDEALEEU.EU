#!/usr/bin/env python3
"""
Validate Job Specifications

This script validates federated learning job specifications against their schemas.
It acts as a CI/CD gatekeeper to ensure all job specs are well-formed before deployment.

Usage:
    python validate_job_specs.py [--path PATH] [--schema SCHEMA]
    python validate_job_specs.py --validate-all
    
Examples:
    # Validate a specific job spec
    python validate_job_specs.py --path ../EXAMPLES/aircraft_accel_v1/job.yaml
    
    # Validate all job specs in the repository
    python validate_job_specs.py --validate-all
    
    # Validate with custom schema
    python validate_job_specs.py --path job.yaml --schema ../SCHEMAS/job_spec.schema.json
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Dict, List, Tuple

try:
    import yaml
    import jsonschema
    from jsonschema import validate, ValidationError
except ImportError:
    print("ERROR: Required packages not installed.")
    print("Install with: pip install pyyaml jsonschema")
    sys.exit(1)


class JobSpecValidator:
    """Validator for FL job specifications."""
    
    def __init__(self, base_path: Path = None):
        """Initialize validator with base path to JOB_SPECS directory."""
        if base_path is None:
            # Assume script is in TESTS/ directory
            self.base_path = Path(__file__).parent.parent
        else:
            self.base_path = base_path
            
        self.schemas_path = self.base_path / "SCHEMAS"
        self.examples_path = self.base_path / "EXAMPLES"
        self.templates_path = self.base_path / "TEMPLATES"
        
        # Load schemas
        self.schemas = self._load_schemas()
        
    def _load_schemas(self) -> Dict[str, dict]:
        """Load all JSON schemas."""
        schemas = {}
        
        if not self.schemas_path.exists():
            print(f"WARNING: Schemas directory not found: {self.schemas_path}")
            return schemas
            
        for schema_file in self.schemas_path.glob("*.schema.json"):
            try:
                with open(schema_file, 'r') as f:
                    schema_name = schema_file.stem.replace('.schema', '')
                    schemas[schema_name] = json.load(f)
                    print(f"  ✓ Loaded schema: {schema_name}")
            except Exception as e:
                print(f"  ✗ Failed to load schema {schema_file}: {e}")
                
        return schemas
        
    def validate_yaml_file(self, yaml_path: Path, schema_name: str = None) -> Tuple[bool, str]:
        """
        Validate a YAML file against its schema.
        
        Args:
            yaml_path: Path to YAML file
            schema_name: Schema to use (auto-detect if None)
            
        Returns:
            Tuple of (success: bool, message: str)
        """
        if not yaml_path.exists():
            return False, f"File not found: {yaml_path}"
            
        # Load YAML file
        try:
            with open(yaml_path, 'r') as f:
                data = yaml.safe_load(f)
        except yaml.YAMLError as e:
            return False, f"YAML parsing error: {e}"
        except Exception as e:
            return False, f"Failed to read file: {e}"
            
        if data is None:
            return False, "Empty YAML file"
            
        # Auto-detect schema if not specified
        if schema_name is None:
            schema_name = self._detect_schema(yaml_path, data)
            
        if schema_name not in self.schemas:
            return False, f"Schema not found: {schema_name}"
            
        # Validate against schema
        try:
            validate(instance=data, schema=self.schemas[schema_name])
            return True, "Valid"
        except ValidationError as e:
            return False, f"Validation error: {e.message}\nPath: {list(e.path)}"
        except Exception as e:
            return False, f"Validation failed: {e}"
            
    def _detect_schema(self, yaml_path: Path, data: dict) -> str:
        """Auto-detect which schema to use based on file name and content."""
        file_name = yaml_path.name.lower()
        
        # Check file name patterns
        if 'selector' in file_name:
            return 'client_selector'
        elif 'rollout' in file_name:
            return 'rollout'
        elif 'job' in file_name or 'train' in file_name or 'eval' in file_name or 'aggregate' in file_name:
            return 'job_spec'
            
        # Check content structure
        if 'selector_metadata' in data:
            return 'client_selector'
        elif 'rollout_metadata' in data:
            return 'rollout'
        elif 'job_metadata' in data:
            return 'job_spec'
            
        # Default
        return 'job_spec'
        
    def validate_all_examples(self) -> List[Tuple[Path, bool, str]]:
        """Validate all example job specs."""
        results = []
        
        print("\n" + "="*70)
        print("VALIDATING EXAMPLE JOB SPECS")
        print("="*70)
        
        if not self.examples_path.exists():
            print(f"Examples directory not found: {self.examples_path}")
            return results
            
        # Find all YAML files in examples
        for yaml_file in self.examples_path.rglob("*.yaml"):
            # Skip schedule files (different structure, no schema yet)
            if 'schedule' in yaml_file.name.lower():
                continue
                
            print(f"\nValidating: {yaml_file.relative_to(self.base_path)}")
            success, message = self.validate_yaml_file(yaml_file)
            results.append((yaml_file, success, message))
            
            if success:
                print(f"  ✓ {message}")
            else:
                print(f"  ✗ {message}")
                
        return results
        
    def validate_all_templates(self) -> List[Tuple[Path, bool, str]]:
        """Validate all template files."""
        results = []
        
        print("\n" + "="*70)
        print("VALIDATING TEMPLATE FILES")
        print("="*70)
        
        if not self.templates_path.exists():
            print(f"Templates directory not found: {self.templates_path}")
            return results
            
        # Find all YAML files in templates
        for yaml_file in self.templates_path.rglob("*.yaml"):
            # Skip schedule templates (no schema yet)
            if 'schedule' in yaml_file.name.lower():
                print(f"\nSkipping: {yaml_file.relative_to(self.base_path)} (no schema)")
                continue
                
            print(f"\nValidating: {yaml_file.relative_to(self.base_path)}")
            success, message = self.validate_yaml_file(yaml_file)
            results.append((yaml_file, success, message))
            
            if success:
                print(f"  ✓ {message}")
            else:
                print(f"  ✗ {message}")
                
        return results
        
    def generate_report(self, results: List[Tuple[Path, bool, str]]) -> dict:
        """Generate validation report."""
        total = len(results)
        passed = sum(1 for _, success, _ in results if success)
        failed = total - passed
        
        return {
            'total': total,
            'passed': passed,
            'failed': failed,
            'success_rate': (passed / total * 100) if total > 0 else 0,
            'results': results
        }


def main():
    """Main entry point."""
    parser = argparse.ArgumentParser(
        description='Validate FL job specifications against schemas'
    )
    parser.add_argument(
        '--path',
        type=Path,
        help='Path to specific YAML file to validate'
    )
    parser.add_argument(
        '--schema',
        help='Schema name to use (job_spec, client_selector, rollout)'
    )
    parser.add_argument(
        '--validate-all',
        action='store_true',
        help='Validate all examples and templates'
    )
    parser.add_argument(
        '--base-path',
        type=Path,
        help='Base path to JOB_SPECS directory'
    )
    
    args = parser.parse_args()
    
    # Initialize validator
    validator = JobSpecValidator(base_path=args.base_path)
    
    print("="*70)
    print("FEDERATED LEARNING JOB SPECIFICATION VALIDATOR")
    print("="*70)
    print(f"\nBase path: {validator.base_path}")
    print(f"Schemas loaded: {len(validator.schemas)}")
    
    if args.validate_all:
        # Validate all examples and templates
        example_results = validator.validate_all_examples()
        template_results = validator.validate_all_templates()
        
        all_results = example_results + template_results
        report = validator.generate_report(all_results)
        
        # Print summary
        print("\n" + "="*70)
        print("VALIDATION SUMMARY")
        print("="*70)
        print(f"Total files validated: {report['total']}")
        print(f"Passed: {report['passed']}")
        print(f"Failed: {report['failed']}")
        print(f"Success rate: {report['success_rate']:.1f}%")
        
        # Exit with error if any failed
        sys.exit(0 if report['failed'] == 0 else 1)
        
    elif args.path:
        # Validate specific file
        yaml_path = args.path
        if not yaml_path.is_absolute():
            yaml_path = Path.cwd() / yaml_path
            
        print(f"\nValidating: {yaml_path}")
        success, message = validator.validate_yaml_file(yaml_path, args.schema)
        
        if success:
            print(f"✓ {message}")
            sys.exit(0)
        else:
            print(f"✗ {message}")
            sys.exit(1)
    else:
        parser.print_help()
        sys.exit(1)


if __name__ == '__main__':
    main()
