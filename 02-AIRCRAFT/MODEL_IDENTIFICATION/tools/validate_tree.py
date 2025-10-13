#!/usr/bin/env python3
"""
TFA Structure Validator
=======================
Validates the TFA (Threading Functional Architecture/Artifact) directory structure
and ensures all required files and metadata are present and valid.

Usage:
    python3 validate_tree.py --domain DOMAIN --ata-chapter ATA_CHAPTER \
                             --ata-mid ATA_MID --comp COMP

Example:
    python3 validate_tree.py --domain AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \
                             --ata-chapter ATA-53 --ata-mid ATA-53-10 \
                             --comp ATA-53-10-01
"""

import argparse
import json
import csv
import os
import sys
from pathlib import Path
from typing import List, Dict, Tuple

# ANSI color codes
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    NC = '\033[0m'  # No Color

def print_info(msg: str):
    print(f"{Colors.BLUE}ℹ {msg}{Colors.NC}")

def print_success(msg: str):
    print(f"{Colors.GREEN}✓ {msg}{Colors.NC}")

def print_warning(msg: str):
    print(f"{Colors.YELLOW}⚠ {msg}{Colors.NC}")

def print_error(msg: str):
    print(f"{Colors.RED}✗ {msg}{Colors.NC}")

class TFAValidator:
    """Validator for TFA structure"""
    
    def __init__(self, base_path: Path, domain: str, ata_chapter: str, 
                 ata_mid: str, comp: str):
        self.base_path = base_path
        self.domain = domain
        self.ata_chapter = ata_chapter
        self.ata_mid = ata_mid
        self.comp = comp
        self.errors = []
        self.warnings = []
        self.success_count = 0
        
        # Build paths
        self.product = "AMPEL360-AIR-T"
        self.arch = "BWB-H2-Hy-E"
        self.family = "Q100_STD01"
        
        self.root = base_path / self.product / "ARCH" / self.arch / "FAMILY" / \
                    self.family / "DOMAIN" / domain / ata_chapter / "SYSTEMS" / ata_mid
        self.plm_root = self.root / "PLM" / "CAx"
        self.conf_root = self.root / "CONF" / "BASELINE" / "COMPONENTS" / comp
    
    def validate_plm_structure(self) -> bool:
        """Validate PLM/CAx directory structure"""
        print_info("Validating PLM/CAx structure...")
        
        required_cax = ["CAD", "CAE", "CAM", "CAI", "CAO", "CAP", "CAS", "CAV", "CMP"]
        all_present = True
        
        for cax in required_cax:
            cax_path = self.plm_root / cax
            if cax_path.exists() and cax_path.is_dir():
                print_success(f"Found {cax} directory")
                self.success_count += 1
            else:
                print_error(f"Missing {cax} directory at: {cax_path}")
                self.errors.append(f"Missing PLM/CAx/{cax} directory")
                all_present = False
        
        return all_present
    
    def validate_json_file(self, file_path: Path, required_keys: List[str]) -> bool:
        """Validate a JSON file"""
        if not file_path.exists():
            print_error(f"Missing file: {file_path.name}")
            self.errors.append(f"Missing file: {file_path}")
            return False
        
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
            
            missing_keys = [key for key in required_keys if key not in data]
            if missing_keys:
                print_warning(f"{file_path.name}: Missing keys: {', '.join(missing_keys)}")
                self.warnings.append(f"{file_path}: Missing keys: {missing_keys}")
                return False
            
            print_success(f"Valid JSON: {file_path.name}")
            self.success_count += 1
            return True
            
        except json.JSONDecodeError as e:
            print_error(f"{file_path.name}: Invalid JSON - {e}")
            self.errors.append(f"Invalid JSON in {file_path}: {e}")
            return False
    
    def validate_csv_file(self, file_path: Path, required_headers: List[str]) -> bool:
        """Validate a CSV file"""
        if not file_path.exists():
            print_error(f"Missing file: {file_path.name}")
            self.errors.append(f"Missing file: {file_path}")
            return False
        
        try:
            with open(file_path, 'r') as f:
                reader = csv.reader(f)
                headers = next(reader, None)
                
                if not headers:
                    print_error(f"{file_path.name}: Empty CSV file")
                    self.errors.append(f"Empty CSV file: {file_path}")
                    return False
                
                missing_headers = [h for h in required_headers if h not in headers]
                if missing_headers:
                    print_warning(f"{file_path.name}: Missing headers: {', '.join(missing_headers)}")
                    self.warnings.append(f"{file_path}: Missing headers: {missing_headers}")
                    return False
                
                print_success(f"Valid CSV: {file_path.name}")
                self.success_count += 1
                return True
                
        except Exception as e:
            print_error(f"{file_path.name}: Error reading CSV - {e}")
            self.errors.append(f"Error reading CSV {file_path}: {e}")
            return False
    
    def validate_yml_file(self, file_path: Path) -> bool:
        """Validate a YAML file (basic check)"""
        if not file_path.exists():
            print_error(f"Missing file: {file_path.name}")
            self.errors.append(f"Missing file: {file_path}")
            return False
        
        try:
            # Basic validation - just check if file is readable and not empty
            with open(file_path, 'r') as f:
                content = f.read().strip()
                if not content:
                    print_error(f"{file_path.name}: Empty YAML file")
                    self.errors.append(f"Empty YAML file: {file_path}")
                    return False
            
            print_success(f"Valid YAML: {file_path.name}")
            self.success_count += 1
            return True
            
        except Exception as e:
            print_error(f"{file_path.name}: Error reading YAML - {e}")
            self.errors.append(f"Error reading YAML {file_path}: {e}")
            return False
    
    def validate_component_structure(self) -> bool:
        """Validate component configuration structure"""
        print_info("Validating component structure...")
        
        # Find all subproducts
        subprod_dirs = list(self.conf_root.glob("SUBPRODUCT/*"))
        
        if not subprod_dirs:
            print_warning(f"No subproducts found in: {self.conf_root / 'SUBPRODUCT'}")
            self.warnings.append("No subproducts found")
            return False
        
        all_valid = True
        for subprod_dir in subprod_dirs:
            subprod_id = subprod_dir.name
            print_info(f"Validating subproduct: {subprod_id}")
            
            # Validate SUBPRODUCT_INDEX.csv
            index_file = subprod_dir / "SUBPRODUCT_INDEX.csv"
            if not self.validate_csv_file(index_file, 
                ["subproduct_id", "description", "version", "status", "owner"]):
                all_valid = False
            
            # Find all subjects
            subject_dirs = list((subprod_dir / "SUBJECT").glob("*"))
            
            for subject_dir in subject_dirs:
                if not subject_dir.is_dir():
                    continue
                    
                subject_id = subject_dir.name
                print_info(f"Validating subject: {subject_id}")
                
                # Validate SUBJECT_META.json
                meta_file = subject_dir / "SUBJECT_META.json"
                if not self.validate_json_file(meta_file,
                    ["subject_id", "title", "version", "status", "owner"]):
                    all_valid = False
                
                # Validate SUBJECT_MANIFEST.csv
                manifest_file = subject_dir / "SUBJECT_MANIFEST.csv"
                if not self.validate_csv_file(manifest_file,
                    ["artifact_id", "artifact_name", "artifact_type"]):
                    all_valid = False
                
                # Validate SUBJECT_CONFIG.yml
                config_file = subject_dir / "SUBJECT_CONFIG.yml"
                if not self.validate_yml_file(config_file):
                    all_valid = False
                
                # Validate artifacts
                range_dirs = list((subject_dir / "RANGE-EFFECT").glob("*"))
                for range_dir in range_dirs:
                    artifacts_dir = range_dir / "artifacts"
                    if artifacts_dir.exists():
                        artifact_dirs = [d for d in artifacts_dir.iterdir() if d.is_dir()]
                        for artifact_dir in artifact_dirs:
                            print_info(f"Validating artifact: {artifact_dir.name}")
                            
                            # Validate artifact files
                            if not self.validate_json_file(artifact_dir / "META.json",
                                ["artifact_id", "title", "type", "version", "status"]):
                                all_valid = False
                            
                            if not self.validate_csv_file(artifact_dir / "MANIFEST.csv",
                                ["file_name", "file_type", "created_date", "status"]):
                                all_valid = False
                            
                            if not self.validate_yml_file(artifact_dir / "CONFIG.yml"):
                                all_valid = False
        
        return all_valid
    
    def validate(self) -> bool:
        """Run all validations"""
        print(f"\n{Colors.BLUE}{'='*70}{Colors.NC}")
        print(f"{Colors.BLUE}TFA Structure Validation{Colors.NC}")
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}\n")
        
        print_info(f"Domain: {self.domain}")
        print_info(f"ATA Chapter: {self.ata_chapter}")
        print_info(f"System: {self.ata_mid}")
        print_info(f"Component: {self.comp}")
        print_info(f"Root path: {self.root}\n")
        
        if not self.root.exists():
            print_error(f"Root directory does not exist: {self.root}")
            print_info("Run 'make init' to create the structure")
            return False
        
        # Run validations
        plm_valid = self.validate_plm_structure()
        print()
        
        conf_valid = self.validate_component_structure()
        print()
        
        # Print summary
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}")
        print(f"{Colors.BLUE}Validation Summary{Colors.NC}")
        print(f"{Colors.BLUE}{'='*70}{Colors.NC}\n")
        
        print(f"{Colors.GREEN}Successful checks: {self.success_count}{Colors.NC}")
        
        if self.warnings:
            print(f"{Colors.YELLOW}Warnings: {len(self.warnings)}{Colors.NC}")
            for warning in self.warnings:
                print(f"  {Colors.YELLOW}⚠{Colors.NC} {warning}")
        
        if self.errors:
            print(f"{Colors.RED}Errors: {len(self.errors)}{Colors.NC}")
            for error in self.errors:
                print(f"  {Colors.RED}✗{Colors.NC} {error}")
            print()
            print_error("Validation FAILED")
            return False
        else:
            print()
            print_success("Validation PASSED")
            return True

def main():
    parser = argparse.ArgumentParser(
        description="Validate TFA structure and metadata",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 validate_tree.py --domain AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS \\
                           --ata-chapter ATA-53 --ata-mid ATA-53-10 \\
                           --comp ATA-53-10-01
        """
    )
    
    parser.add_argument('--domain', required=True, help='Domain ID')
    parser.add_argument('--ata-chapter', required=True, help='ATA chapter (e.g., ATA-53)')
    parser.add_argument('--ata-mid', required=True, help='System ID (e.g., ATA-53-10)')
    parser.add_argument('--comp', required=True, help='Component ID (e.g., ATA-53-10-01)')
    parser.add_argument('--path', default='.', help='Base path (default: current directory)')
    
    args = parser.parse_args()
    
    base_path = Path(args.path).resolve()
    
    validator = TFAValidator(
        base_path=base_path,
        domain=args.domain,
        ata_chapter=args.ata_chapter,
        ata_mid=args.ata_mid,
        comp=args.comp
    )
    
    success = validator.validate()
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
