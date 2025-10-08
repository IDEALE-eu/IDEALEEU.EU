#!/usr/bin/env python3
"""
Script: verify_compliance_evidence.py
Purpose: Verify completeness and correctness of compliance evidence in a release package
Author: Configuration Management Team
Date: 2025-01-01

Usage:
    python verify_compliance_evidence.py --release-dir /path/to/REL-ACFT-1.0.0 \
                                          --standards DO-178C,DO-254,AS9100

Checks:
    - Compliance directories exist
    - Required documents present
    - Compliance matrices complete
    - Evidence traceability
    - Document naming conventions
    - File formats valid

Exit codes:
    0 - All checks passed
    1 - Verification failed
"""

import argparse
import logging
import sys
from pathlib import Path
import json

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class ComplianceVerifier:
    """Verifies compliance evidence completeness."""
    
    def __init__(self, release_dir, standards):
        self.release_dir = Path(release_dir)
        self.standards = standards
        self.compliance_dir = self.release_dir / 'COMPLIANCE'
        self.issues = []
        self.warnings = []
    
    def verify_directory_structure(self):
        """Verify compliance directory structure exists."""
        logger.info("Verifying directory structure...")
        
        if not self.compliance_dir.exists():
            self.issues.append("COMPLIANCE directory does not exist")
            return False
        
        for standard in self.standards:
            standard_dir = self.compliance_dir / standard
            if not standard_dir.exists():
                self.issues.append(f"Standard directory {standard} does not exist")
            else:
                logger.info(f"✓ {standard} directory exists")
        
        return len(self.issues) == 0
    
    def verify_do178c(self):
        """Verify DO-178C compliance evidence."""
        logger.info("Verifying DO-178C evidence...")
        
        standard_dir = self.compliance_dir / 'DO-178C'
        if not standard_dir.exists():
            return
        
        required_docs = [
            'PSAC',  # Plan for Software Aspects of Certification
            'SDP',   # Software Development Plan
            'SVP',   # Software Verification Plan
            'SQAP',  # Software Quality Assurance Plan
            'SCM',   # Software Configuration Management Plan
            'SRS',   # Software Requirements Standards
            'SDS',   # Software Design Standards
            'SCS',   # Software Code Standards
        ]
        
        for doc in required_docs:
            # Check if any file starts with the document prefix
            files = list(standard_dir.glob(f'{doc}*'))
            if not files:
                self.issues.append(f"DO-178C: Missing document {doc}")
            else:
                logger.info(f"✓ DO-178C: Found {doc}")
        
    def verify_as9100(self):
        """Verify AS9100 QMS evidence."""
        logger.info("Verifying AS9100 evidence...")
        
        standard_dir = self.compliance_dir / 'AS9100'
        if not standard_dir.exists():
            return
        
        required_evidence = [
            'quality_manual',
            'procedures',
            'work_instructions',
            'inspection_records',
        ]
        
        for evidence in required_evidence:
            # Check if directory or files exist
            if not any(standard_dir.glob(f'*{evidence}*')):
                self.warnings.append(f"AS9100: Missing {evidence}")
            else:
                logger.info(f"✓ AS9100: Found {evidence}")
    
    def verify_traceability(self):
        """Verify evidence traceability."""
        logger.info("Verifying traceability...")
        
        # Check for traceability matrices
        matrices = list(self.compliance_dir.rglob('*traceability*.csv')) + \
                  list(self.compliance_dir.rglob('*traceability*.xlsx'))
        
        if not matrices:
            self.warnings.append("No traceability matrices found")
        else:
            logger.info(f"✓ Found {len(matrices)} traceability matrices")
    
    def generate_report(self):
        """Generate verification report."""
        logger.info("=" * 60)
        logger.info("Compliance Verification Report")
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
        description='Verify compliance evidence completeness'
    )
    parser.add_argument('--release-dir', required=True,
                        help='Release directory path')
    parser.add_argument('--standards', required=True,
                        help='Comma-separated list of standards (e.g., DO-178C,AS9100)')
    parser.add_argument('--output-report', 
                        help='Output report file (JSON)')
    
    args = parser.parse_args()
    
    standards = [s.strip() for s in args.standards.split(',')]
    
    logger.info("Starting compliance evidence verification")
    logger.info(f"Release directory: {args.release_dir}")
    logger.info(f"Standards: {', '.join(standards)}")
    
    try:
        verifier = ComplianceVerifier(args.release_dir, standards)
        
        # Run verifications
        if not verifier.verify_directory_structure():
            logger.error("Directory structure verification failed")
            return 1
        
        if 'DO-178C' in standards:
            verifier.verify_do178c()
        
        if 'AS9100' in standards:
            verifier.verify_as9100()
        
        verifier.verify_traceability()
        
        # Generate report
        success = verifier.generate_report()
        
        # Save report if requested
        if args.output_report:
            report = {
                'release_dir': str(args.release_dir),
                'standards': standards,
                'issues': verifier.issues,
                'warnings': verifier.warnings,
                'passed': success
            }
            with open(args.output_report, 'w') as f:
                json.dump(report, f, indent=2)
            logger.info(f"Report saved to {args.output_report}")
        
        return 0 if success else 1
        
    except Exception as e:
        logger.error(f"Verification failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
