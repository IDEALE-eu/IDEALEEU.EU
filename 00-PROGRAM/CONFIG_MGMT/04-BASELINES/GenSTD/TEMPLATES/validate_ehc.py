#!/usr/bin/env python3
"""
GenSTD EHC Validation Script

Validates that a GenSTD baseline meets all EHC (Embedded in Human Comprehensivity)
requirements before approval.

Usage:
    python validate_ehc.py <baseline-directory>

Requirements:
    - Python 3.9+
    - jsonschema
    - textstat (for readability scoring)
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Tuple

def _import_or_exit(module_name: str, install_hint: str):
    try:
        return __import__(module_name)
    except ImportError:
        print(f"Error: {module_name} not installed. Run: pip install {install_hint}")
        sys.exit(1)

jsonschema = _import_or_exit("jsonschema", "jsonschema")
textstat = _import_or_exit("textstat", "textstat")


class Colors:
    """ANSI color codes for terminal output"""
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    RESET = '\033[0m'
    BOLD = '\033[1m'


def print_check(passed: bool, message: str):
    """Print a check result with color"""
    symbol = f"{Colors.GREEN}✓{Colors.RESET}" if passed else f"{Colors.RED}✗{Colors.RESET}"
    print(f"{symbol} {message}")


def validate_manifest_schema(baseline_dir: Path) -> Tuple[bool, Dict]:
    """Validate MANIFEST.json against schema"""
    manifest_path = baseline_dir / "MANIFEST.json"
    schema_path = baseline_dir.parent.parent / "TEMPLATES" / "MANIFEST.schema.json"
    
    if not manifest_path.exists():
        print_check(False, f"MANIFEST.json not found at {manifest_path}")
        return False, {}
    
    if not schema_path.exists():
        print_check(False, f"Schema not found at {schema_path}")
        return False, {}
    
    try:
        with open(manifest_path) as f:
            manifest = json.load(f)
        
        with open(schema_path) as f:
            schema = json.load(f)
        
        jsonschema.validate(instance=manifest, schema=schema)
        print_check(True, "MANIFEST.json valid against schema")
        return True, manifest
    except json.JSONDecodeError as e:
        print_check(False, f"MANIFEST.json invalid JSON: {e}")
        return False, {}
    except jsonschema.ValidationError as e:
        print_check(False, f"MANIFEST.json schema violation: {e.message}")
        return False, {}


def check_required_files(baseline_dir: Path, manifest: Dict) -> bool:
    """Check all required EHC artifacts exist"""
    required_files = manifest.get("docs", [])
    diagram = manifest.get("diagram", "")
    
    all_present = True
    
    # Check docs
    for doc in required_files:
        doc_path = baseline_dir / doc
        if doc_path.exists():
            print_check(True, f"{doc} present")
        else:
            print_check(False, f"{doc} MISSING")
            all_present = False
    
    # Check diagram
    diagram_path = baseline_dir / diagram
    if diagram_path.exists():
        print_check(True, f"{diagram} present")
    else:
        print_check(False, f"{diagram} MISSING")
        all_present = False
    
    return all_present


def validate_summary(baseline_dir: Path) -> Tuple[bool, int, float]:
    """Validate SUMMARY.md word count and readability"""
    summary_path = baseline_dir / "SUMMARY.md"
    
    if not summary_path.exists():
        return False, 0, 0.0
    
    with open(summary_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract summary section (between ## Executive Summary and next ##)
    summary_match = re.search(
        r'## Executive Summary[^\n]*\n(.*?)(?=\n##|\Z)', 
        content, 
        re.DOTALL
    )
    
    if not summary_match:
        print_check(False, "SUMMARY.md: Could not find 'Executive Summary' section")
        return False, 0, 0.0
    
    summary_text = summary_match.group(1).strip()
    
    # Remove markdown formatting for word count
    clean_text = re.sub(r'\[.*?\]', '', summary_text)  # Remove brackets
    clean_text = re.sub(r'\*+', '', clean_text)  # Remove asterisks
    clean_text = re.sub(r'#+', '', clean_text)  # Remove headers
    clean_text = re.sub(r'`+', '', clean_text)  # Remove code markers
    
    word_count = len(clean_text.split())
    
    # Calculate readability (Flesch-Kincaid Grade Level)
    try:
        fk_score = textstat.flesch_kincaid_grade(summary_text)
    except Exception:
        fk_score = 0.0
    
    # Check word count (≤150)
    word_count_ok = word_count <= 150
    print_check(
        word_count_ok, 
        f"SUMMARY.md word count: {word_count}/150 {'✓' if word_count_ok else '✗'}"
    )
    
    # Check readability (target 10-12, accept 8-14)
    readability_ok = 8 <= fk_score <= 14
    print_check(
        readability_ok,
        f"SUMMARY.md readability: FK {fk_score:.1f} (target 10-12) {'✓' if readability_ok else '✗'}"
    )
    
    return word_count_ok and readability_ok, word_count, fk_score


def validate_decisions(baseline_dir: Path) -> bool:
    """Check DECISIONS.md has proper structure"""
    decisions_path = baseline_dir / "DECISIONS.md"
    
    if not decisions_path.exists():
        return False
    
    with open(decisions_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for required sections
    has_format = "### [Decision" in content or "## Decision" in content
    has_alternatives = "Alternatives Considered" in content
    has_rationale = "Rationale" in content
    
    all_ok = has_format and has_alternatives and has_rationale
    
    if all_ok:
        print_check(True, "DECISIONS.md has proper ADR structure")
    else:
        print_check(False, "DECISIONS.md missing required sections")
    
    return all_ok


def validate_glossary(baseline_dir: Path) -> bool:
    """Check GLOSSARY.md maps to org glossary"""
    glossary_path = baseline_dir / "GLOSSARY.md"
    
    if not glossary_path.exists():
        return False
    
    with open(glossary_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for acronyms table
    has_acronyms_table = "| Acronym |" in content
    # Check for org glossary reference
    has_org_link = "/docs/glossary.md" in content
    
    all_ok = has_acronyms_table and has_org_link
    
    if all_ok:
        print_check(True, "GLOSSARY.md complete with org links")
    else:
        print_check(False, "GLOSSARY.md incomplete")
    
    return all_ok


def validate_runbook(baseline_dir: Path, manifest: Dict) -> bool:
    """Check RUNBOOK.md completeness"""
    runbook_path = baseline_dir / "RUNBOOK.md"
    
    if not runbook_path.exists():
        return False
    
    with open(runbook_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check for required sections
    required_sections = [
        "Prerequisites",
        "Step",
        "Verification",
        "Rollback",
        "Troubleshooting"
    ]
    
    all_present = all(section in content for section in required_sections)
    
    # Check time target
    time_target = manifest.get("repro_time_min", 0)
    has_time_target = f"≤{time_target}" in content or f"{time_target} minute" in content
    
    all_ok = all_present and has_time_target
    
    if all_ok:
        print_check(True, f"RUNBOOK.md complete (≤{time_target} min target)")
    else:
        print_check(False, "RUNBOOK.md incomplete or missing time target")
    
    return all_ok


def validate_risks(baseline_dir: Path) -> bool:
    """Check RISKS.md has top 5 risks"""
    risks_path = baseline_dir / "RISKS.md"
    
    if not risks_path.exists():
        return False
    
    with open(risks_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Count risk entries (### Risk)
    risk_count = content.count("### Risk")
    
    # Check for required elements
    has_mitigation = "Mitigation Strategy" in content
    has_residual = "Residual Risk" in content
    has_impact = "Impact" in content
    
    all_ok = risk_count >= 5 and has_mitigation and has_residual and has_impact
    
    if all_ok:
        print_check(True, f"RISKS.md complete with {risk_count} risks documented")
    else:
        print_check(False, f"RISKS.md incomplete (found {risk_count} risks, need 5)")
    
    return all_ok


def validate_cross_references(baseline_dir: Path, manifest: Dict) -> bool:
    """Verify cross-references resolve"""
    docs = manifest.get("docs", [])
    
    all_ok = True
    
    for doc in docs:
        doc_path = baseline_dir / doc
        if not doc_path.exists():
            continue
        
        with open(doc_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find markdown links: [text](path)
        links = re.findall(r'\[.*?\]\((.*?)\)', content)
        
        for link in links:
            # Skip external links
            if link.startswith('http://') or link.startswith('https://'):
                continue
            
            # Skip anchors
            if link.startswith('#'):
                continue
            
            # Check if local file exists
            link_path = baseline_dir / link
            if not link_path.exists():
                print_check(False, f"{doc}: Broken link to {link}")
                all_ok = False
    
    if all_ok:
        print_check(True, "All cross-references resolve")
    
    return all_ok


def main():
    parser = argparse.ArgumentParser(
        description="Validate GenSTD baseline for EHC compliance"
    )
    parser.add_argument(
        "baseline_dir",
        type=Path,
        help="Path to baseline directory"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Verbose output"
    )
    
    args = parser.parse_args()
    
    baseline_dir = args.baseline_dir
    
    if not baseline_dir.exists():
        print(f"{Colors.RED}Error: {baseline_dir} does not exist{Colors.RESET}")
        sys.exit(1)
    
    if not baseline_dir.is_dir():
        print(f"{Colors.RED}Error: {baseline_dir} is not a directory{Colors.RESET}")
        sys.exit(1)
    
    print(f"\n{Colors.BOLD}Running GenSTD EHC validation...{Colors.RESET}\n")
    
    checks = []
    
    # 1. Validate MANIFEST.json
    print(f"{Colors.BLUE}1. Validating MANIFEST.json{Colors.RESET}")
    manifest_ok, manifest = validate_manifest_schema(baseline_dir)
    checks.append(manifest_ok)
    
    if not manifest_ok:
        print(f"\n{Colors.RED}Validation FAILED: MANIFEST.json invalid{Colors.RESET}\n")
        sys.exit(1)
    
    # 2. Check required files exist
    print(f"\n{Colors.BLUE}2. Checking required files{Colors.RESET}")
    files_ok = check_required_files(baseline_dir, manifest)
    checks.append(files_ok)
    
    # 3. Validate SUMMARY.md
    print(f"\n{Colors.BLUE}3. Validating SUMMARY.md{Colors.RESET}")
    summary_ok, word_count, fk_score = validate_summary(baseline_dir)
    checks.append(summary_ok)
    
    # 4. Validate DECISIONS.md
    print(f"\n{Colors.BLUE}4. Validating DECISIONS.md{Colors.RESET}")
    decisions_ok = validate_decisions(baseline_dir)
    checks.append(decisions_ok)
    
    # 5. Validate GLOSSARY.md
    print(f"\n{Colors.BLUE}5. Validating GLOSSARY.md{Colors.RESET}")
    glossary_ok = validate_glossary(baseline_dir)
    checks.append(glossary_ok)
    
    # 6. Validate RUNBOOK.md
    print(f"\n{Colors.BLUE}6. Validating RUNBOOK.md{Colors.RESET}")
    runbook_ok = validate_runbook(baseline_dir, manifest)
    checks.append(runbook_ok)
    
    # 7. Validate RISKS.md
    print(f"\n{Colors.BLUE}7. Validating RISKS.md{Colors.RESET}")
    risks_ok = validate_risks(baseline_dir)
    checks.append(risks_ok)
    
    # 8. Validate cross-references
    print(f"\n{Colors.BLUE}8. Validating cross-references{Colors.RESET}")
    refs_ok = validate_cross_references(baseline_dir, manifest)
    checks.append(refs_ok)
    
    # Summary
    print(f"\n{Colors.BOLD}{'='*60}{Colors.RESET}")
    
    all_passed = all(checks)
    
    if all_passed:
        print(f"{Colors.GREEN}{Colors.BOLD}All validations PASSED ✓{Colors.RESET}\n")
        print(f"Baseline: {manifest.get('id', 'Unknown')}")
        print(f"Tier: GenSTD-{manifest.get('tier', '?')}")
        print(f"Summary: {word_count} words, FK {fk_score:.1f}")
        print(f"\nThis baseline meets all EHC requirements.")
        sys.exit(0)
    else:
        failed_count = sum(1 for c in checks if not c)
        print(f"{Colors.RED}{Colors.BOLD}Validation FAILED{Colors.RESET}")
        print(f"{failed_count} check(s) failed\n")
        print("Fix the issues above and re-run validation.")
        sys.exit(1)


if __name__ == "__main__":
    main()
