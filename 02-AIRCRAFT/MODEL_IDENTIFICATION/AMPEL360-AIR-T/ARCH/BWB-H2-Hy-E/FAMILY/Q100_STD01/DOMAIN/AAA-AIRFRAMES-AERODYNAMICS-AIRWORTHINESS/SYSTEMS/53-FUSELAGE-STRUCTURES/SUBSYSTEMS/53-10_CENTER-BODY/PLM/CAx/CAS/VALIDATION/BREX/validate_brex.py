#!/usr/bin/env python3
"""
BREX Validator for AMPEL360 AIR-T S1000D Data Modules

Validates Data Modules against the 120 BREX rules defined in
DMC-AMP360-AAA-00-00-00-00A-000A-A_en-US_001-00.xml

Usage:
    python validate_brex.py <path-to-dm-or-directory>

Returns:
    0 if all validations pass (or only warnings)
    1 if any ERROR-level validations fail
"""

import sys
import os
from pathlib import Path
from lxml import etree
import argparse
from typing import List, Tuple

# S1000D Issue 6.0 namespace
NS = {
    's1000d': 'http://www.s1000d.org/S1000D_6-0/xml_schema_flat',
    'xlink': 'http://www.w3.org/1999/xlink'
}

class BREXValidator:
    def __init__(self, brex_file=None):
        """Initialize BREX validator with BREX rule definitions"""
        self.errors = []
        self.warnings = []
        
        # Load BREX file if provided
        if brex_file and os.path.exists(brex_file):
            self.brex_tree = etree.parse(brex_file)
            self.brex_rules = self._load_brex_rules()
        else:
            # Use inline rule definitions (subset)
            self.brex_rules = self._get_inline_rules()
    
    def _load_brex_rules(self):
        """Load rules from BREX DM file"""
        rules = []
        # Parse BREX XML and extract objectPath and objectUse
        for rule in self.brex_tree.xpath('//s1000d:structureObjectRule', namespaces=NS):
            object_path = rule.find('.//s1000d:objectPath', namespaces=NS)
            object_use = rule.find('.//s1000d:objectUse', namespaces=NS)
            if object_path is not None and object_use is not None:
                xpath = object_path.text
                description = object_use.text
                allowed_flag = object_path.get('allowedObjectFlag', '0')
                
                # Extract severity from description
                severity = 'ERROR' if '[ERROR]' in description else 'WARN'
                
                rules.append({
                    'xpath': xpath,
                    'description': description,
                    'severity': severity,
                    'allowed_flag': allowed_flag
                })
        return rules
    
    def _get_inline_rules(self):
        """Get subset of critical BREX rules for validation"""
        return [
            {
                'xpath': '//s1000d:identAndStatusSection[not(s1000d:dmAddress/s1000d:dmIdent/s1000d:dmCode)]',
                'description': '[AMP360-BREX-001] [ERROR] DM must contain <dmCode>.',
                'severity': 'ERROR',
                'allowed_flag': '0'
            },
            {
                'xpath': '//s1000d:identAndStatusSection[not(s1000d:dmAddress/s1000d:dmIdent/s1000d:language)]',
                'description': '[AMP360-BREX-002] [ERROR] DM must contain <language>.',
                'severity': 'ERROR',
                'allowed_flag': '0'
            },
            {
                'xpath': '//s1000d:identAndStatusSection[not(s1000d:dmStatus/s1000d:security)]',
                'description': '[AMP360-BREX-006] [ERROR] DM must contain <security>.',
                'severity': 'ERROR',
                'allowed_flag': '0'
            },
            {
                'xpath': '//s1000d:identAndStatusSection[not(s1000d:dmStatus/s1000d:qualityAssurance)]',
                'description': '[AMP360-BREX-007] [ERROR] DM must contain <qualityAssurance>.',
                'severity': 'ERROR',
                'allowed_flag': '0'
            },
            {
                'xpath': '//s1000d:content[not(node())]',
                'description': '[AMP360-BREX-009] [ERROR] <content> must not be empty.',
                'severity': 'ERROR',
                'allowed_flag': '0'
            },
            {
                'xpath': '//s1000d:externalRef[not(@xlink:href)]',
                'description': '[AMP360-BREX-013] [ERROR] <externalRef> must include @xlink:href.',
                'severity': 'ERROR',
                'allowed_flag': '0'
            },
            {
                'xpath': '//s1000d:dmAddress/s1000d:dmIdent/s1000d:dmCode/@modelIdentCode[. != "AMP360"]',
                'description': '[AMP360-BREX-021] [ERROR] @modelIdentCode must be AMP360.',
                'severity': 'ERROR',
                'allowed_flag': '2'
            },
            {
                'xpath': '//s1000d:dmAddress/s1000d:dmIdent/s1000d:dmCode/@systemDiffCode[. != "AAA"]',
                'description': '[AMP360-BREX-022] [ERROR] @systemDiffCode must be AAA.',
                'severity': 'ERROR',
                'allowed_flag': '2'
            },
            {
                'xpath': '//s1000d:dmAddress/s1000d:dmIdent/s1000d:language/@languageIsoCode[. != "en"]',
                'description': '[AMP360-BREX-031] [ERROR] language/@languageIsoCode must be en.',
                'severity': 'ERROR',
                'allowed_flag': '2'
            },
            {
                'xpath': '//s1000d:dmAddress/s1000d:dmIdent/s1000d:language/@countryIsoCode[. != "US"]',
                'description': '[AMP360-BREX-030] [ERROR] language/@countryIsoCode must be US.',
                'severity': 'ERROR',
                'allowed_flag': '2'
            },
            {
                'xpath': '//s1000d:note//s1000d:warning | //s1000d:note//s1000d:caution',
                'description': '[AMP360-BREX-039] [ERROR] Do not put safety messages inside <note>.',
                'severity': 'ERROR',
                'allowed_flag': '0'
            },
            {
                'xpath': '//s1000d:graphic[not(@xlink:href)]',
                'description': '[AMP360-BREX-086] [ERROR] <graphic> requires @xlink:href.',
                'severity': 'ERROR',
                'allowed_flag': '0'
            },
            {
                'xpath': '//s1000d:identAndStatusSection[not(s1000d:dmAddress/s1000d:dmIdent/s1000d:extension/s1000d:utcs)]',
                'description': '[AMP360-BREX-119] [ERROR] UTCS anchor required in IDS/extension.',
                'severity': 'ERROR',
                'allowed_flag': '0'
            },
        ]
    
    def validate_dm(self, dm_file: Path) -> Tuple[int, int]:
        """
        Validate a Data Module against BREX rules
        
        Returns:
            Tuple of (error_count, warning_count)
        """
        print(f"\nValidating: {dm_file}")
        
        # Parse XML
        try:
            tree = etree.parse(str(dm_file))
        except etree.XMLSyntaxError as e:
            print(f"  [ERROR] XML Syntax Error: {e}")
            self.errors.append(f"{dm_file}: XML Syntax Error: {e}")
            return (1, 0)
        
        # Apply BREX rules
        file_errors = 0
        file_warnings = 0
        
        for rule in self.brex_rules:
            try:
                # Evaluate XPath with namespace
                matches = tree.xpath(rule['xpath'], namespaces=NS)
                
                if matches:
                    severity = rule['severity']
                    description = rule['description']
                    
                    if severity == 'ERROR':
                        print(f"  [ERROR] {description}")
                        self.errors.append(f"{dm_file}: {description}")
                        file_errors += 1
                    else:
                        print(f"  [WARN] {description}")
                        self.warnings.append(f"{dm_file}: {description}")
                        file_warnings += 1
            except etree.XPathEvalError as e:
                print(f"  [WARN] XPath evaluation error in rule '{rule['description']}': {e}")
        
        if file_errors == 0 and file_warnings == 0:
            print(f"  ✓ PASS: All BREX rules passed")
        
        return (file_errors, file_warnings)
    
    def validate_directory(self, directory: Path):
        """Validate all XML files in directory"""
        total_errors = 0
        total_warnings = 0
        files_validated = 0
        
        # Find all XML files
        xml_files = list(directory.rglob('*.xml'))
        
        if not xml_files:
            print(f"No XML files found in {directory}")
            return
        
        print(f"\nFound {len(xml_files)} XML file(s) to validate")
        
        for xml_file in xml_files:
            errors, warnings = self.validate_dm(xml_file)
            total_errors += errors
            total_warnings += warnings
            files_validated += 1
        
        # Summary
        print("\n" + "="*70)
        print(f"VALIDATION SUMMARY")
        print("="*70)
        print(f"Files validated: {files_validated}")
        print(f"Total errors:    {total_errors}")
        print(f"Total warnings:  {total_warnings}")
        
        if total_errors == 0:
            print("\n✓ VALIDATION PASSED (no blocking errors)")
            return 0
        else:
            print(f"\n✗ VALIDATION FAILED ({total_errors} blocking error(s))")
            return 1

def main():
    parser = argparse.ArgumentParser(
        description='Validate S1000D Data Modules against AMPEL360 AIR-T BREX rules'
    )
    parser.add_argument(
        'path',
        type=str,
        help='Path to Data Module file or directory'
    )
    parser.add_argument(
        '--brex',
        type=str,
        help='Path to BREX DM file (optional, uses inline rules if not provided)'
    )
    
    args = parser.parse_args()
    
    path = Path(args.path)
    
    if not path.exists():
        print(f"Error: Path '{path}' does not exist")
        return 1
    
    # Initialize validator
    validator = BREXValidator(brex_file=args.brex)
    
    # Validate
    if path.is_file():
        errors, warnings = validator.validate_dm(path)
        exit_code = 1 if errors > 0 else 0
    else:
        exit_code = validator.validate_directory(path)
    
    return exit_code

if __name__ == '__main__':
    sys.exit(main())
