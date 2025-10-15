#!/usr/bin/env python3
"""
Path Validator - Validates TFA naming conventions and path grammar
Ensures domain directories follow IDEALE-EU standards.
"""

import sys
import os
import re
from pathlib import Path
from typing import List, Tuple

# TFA Domain naming rules
VALID_DOMAINS = ["AAA", "CQH", "EEE", "PPP", "LIB", "IIS", "AAP", "CCC", "DDD", "EDI", "EER", "IIF", "LCC", "MMM", "OOO"]

# Path grammar rules
PATH_RULES = {
    "domain_uppercase": r"^[A-Z]{3}(-[A-Z]+)*/$",
    "subdirs_lowercase": r"^[a-z_]+/$",
    "yaml_files": r"^[A-Z_]+\.yaml$",
    "md_files": r"^[A-Z_↔]+\.md$",
}

def check_domain_naming(path: str) -> Tuple[bool, str]:
    """Check if domain directories use uppercase."""
    parts = path.split("/")
    
    for i, part in enumerate(parts):
        # Check if this looks like a domain directory
        if any(domain in part for domain in VALID_DOMAINS):
            if part != part.upper():
                return False, f"Domain directory should be uppercase: {part}"
    
    return True, "Domain naming OK"

def check_subdirectory_naming(path: str) -> Tuple[bool, str]:
    """Check if technical subdirectories use lowercase."""
    technical_dirs = ["geometry", "weights", "performance", "propulsion", "avionics"]
    parts = path.split("/")
    
    for part in parts:
        if any(tech in part.lower() for tech in technical_dirs):
            if part != part.lower():
                return False, f"Technical directory should be lowercase: {part}"
    
    return True, "Subdirectory naming OK"

def check_conf_structure(base_path: Path) -> Tuple[bool, List[str]]:
    """Validate CONF directory structure."""
    errors = []
    
    required_dirs = [
        "00-CONFIG",
        "02-RELEASE_TAGS",
        "03-TRACEABILITY",
        "04-ICD_LINKS",
    ]
    
    for req_dir in required_dirs:
        if not (base_path / req_dir).exists():
            errors.append(f"Missing required directory: {req_dir}")
    
    required_files = [
        "UTCS.MANIFEST.yaml",
        "UTCS.INDEX.md",
        "README.md",
    ]
    
    for req_file in required_files:
        if not (base_path / req_file).exists():
            errors.append(f"Missing required file: {req_file}")
    
    return len(errors) == 0, errors

def main():
    """Main path validation check."""
    import subprocess
    result = subprocess.run(
        ["git", "diff", "--name-only", "HEAD~1", "HEAD"],
        capture_output=True,
        text=True
    )
    changed_files = result.stdout.strip().split("\n")
    
    print("=" * 60)
    print("PATH VALIDATOR - Checking TFA Naming Conventions")
    print("=" * 60)
    
    all_pass = True
    
    for filepath in changed_files:
        if "CONF/" not in filepath:
            continue
        
        # Check domain naming
        passed, message = check_domain_naming(filepath)
        if not passed:
            print(f"❌ {filepath}: {message}")
            all_pass = False
        
        # Check subdirectory naming
        passed, message = check_subdirectory_naming(filepath)
        if not passed:
            print(f"❌ {filepath}: {message}")
            all_pass = False
    
    # Check CONF structure
    conf_path = Path("02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/CONF")
    if conf_path.exists():
        passed, errors = check_conf_structure(conf_path)
        if not passed:
            print("\n❌ CONF Structure Issues:")
            for error in errors:
                print(f"   - {error}")
            all_pass = False
    
    print("\n" + "=" * 60)
    if all_pass:
        print("✅ ALL PATH VALIDATION CHECKS PASSED")
        print("=" * 60)
        return 0
    else:
        print("❌ PATH VALIDATION FAILED - Fix naming issues")
        print("=" * 60)
        return 1

if __name__ == "__main__":
    sys.exit(main())
