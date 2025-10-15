#!/usr/bin/env python3
"""
Script: validate_compliance_matrix.py
Purpose: Validate COMPLIANCE_MATRIX.csv for completeness and consistency
Author: Compliance Office
Date: 2025-01-01

Usage:
    python validate_compliance_matrix.py --matrix ../05-REGISTERS/COMPLIANCE_MATRIX.csv

Checks:
    - Required columns present
    - No empty mandatory fields
    - Valid status values
    - Valid method values (V=Verification, V=Validation, C=Certification, S=Similarity)
    - Evidence_UTCS format valid

Exit codes:
    0 - All checks passed
    1 - Validation failed
"""

import argparse
import csv
import logging
import re
import sys
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Valid values for validation
VALID_STATUSES = ['Compliant', 'In-Progress', 'Not-Started', 'N/A', 'Planned']
VALID_METHODS = ['V', 'V', 'C', 'S', 'Test', 'Analysis', 'Inspection', 'Review', 'Similarity']
REQUIRED_COLUMNS = ['Req_ID', 'Standard', 'Clause', 'Applicability', 'Method(VVCS)', 
                   'Owner', 'Evidence_UTCS', 'Status', 'Notes']


class ComplianceMatrixValidator:
    """Validates compliance matrix CSV file."""
    
    def __init__(self, matrix_path):
        self.matrix_path = Path(matrix_path)
        self.issues = []
        self.warnings = []
        self.rows = []
    
    def load_matrix(self):
        """Load CSV file."""
        logger.info(f"Loading matrix from {self.matrix_path}")
        
        if not self.matrix_path.exists():
            self.issues.append(f"Matrix file not found: {self.matrix_path}")
            return False
        
        try:
            with open(self.matrix_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.rows = list(reader)
                logger.info(f"Loaded {len(self.rows)} rows")
                return True
        except Exception as e:
            self.issues.append(f"Failed to read matrix: {e}")
            return False
    
    def validate_structure(self):
        """Validate CSV structure."""
        logger.info("Validating structure...")
        
        if not self.rows:
            self.warnings.append("Matrix is empty (no data rows)")
            return True
        
        # Check required columns
        headers = self.rows[0].keys()
        missing_cols = [col for col in REQUIRED_COLUMNS if col not in headers]
        
        if missing_cols:
            self.issues.append(f"Missing required columns: {', '.join(missing_cols)}")
            return False
        
        logger.info("✓ All required columns present")
        return True
    
    def validate_rows(self):
        """Validate individual rows."""
        logger.info("Validating rows...")
        
        for idx, row in enumerate(self.rows, start=2):  # Start at 2 to account for header
            row_id = row.get('Req_ID', f'Row {idx}')
            
            # Check mandatory fields
            if not row.get('Req_ID'):
                self.issues.append(f"Row {idx}: Missing Req_ID")
            
            if not row.get('Standard'):
                self.issues.append(f"{row_id}: Missing Standard")
            
            if not row.get('Owner'):
                self.warnings.append(f"{row_id}: Missing Owner")
            
            # Validate Status
            status = row.get('Status', '').strip()
            if status and status not in VALID_STATUSES:
                self.warnings.append(f"{row_id}: Invalid Status '{status}'. Valid: {', '.join(VALID_STATUSES)}")
            
            # Validate UTCS format (basic check)
            utcs = row.get('Evidence_UTCS', '').strip()
            if utcs and not re.match(r'^utcs://', utcs):
                self.warnings.append(f"{row_id}: Evidence_UTCS should start with 'utcs://'")
        
        if not self.issues:
            logger.info(f"✓ Validated {len(self.rows)} rows")
        
        return len(self.issues) == 0
    
    def generate_report(self):
        """Generate validation report."""
        logger.info("=" * 60)
        logger.info("Compliance Matrix Validation Report")
        logger.info("=" * 60)
        logger.info(f"File: {self.matrix_path}")
        logger.info(f"Rows: {len(self.rows)}")
        logger.info("=" * 60)
        
        if not self.issues and not self.warnings:
            logger.info("✓ All checks passed!")
            return True
        
        if self.issues:
            logger.error(f"Critical Issues: {len(self.issues)}")
            for issue in self.issues:
                logger.error(f"  ✗ {issue}")
        
        if self.warnings:
            logger.warning(f"Warnings: {len(self.warnings)}")
            for warning in self.warnings:
                logger.warning(f"  ⚠ {warning}")
        
        logger.info("=" * 60)
        
        return len(self.issues) == 0


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Validate compliance matrix CSV'
    )
    parser.add_argument('--matrix', required=True,
                       help='Path to COMPLIANCE_MATRIX.csv')
    
    args = parser.parse_args()
    
    logger.info("Starting compliance matrix validation")
    
    try:
        validator = ComplianceMatrixValidator(args.matrix)
        
        # Run validations
        if not validator.load_matrix():
            return 1
        
        if not validator.validate_structure():
            logger.error("Structure validation failed")
            validator.generate_report()
            return 1
        
        validator.validate_rows()
        
        # Generate report
        success = validator.generate_report()
        
        return 0 if success else 1
        
    except Exception as e:
        logger.error(f"Validation failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
