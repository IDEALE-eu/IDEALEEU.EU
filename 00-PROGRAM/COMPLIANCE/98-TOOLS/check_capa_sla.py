#!/usr/bin/env python3
"""
Script: check_capa_sla.py
Purpose: Check CAPA due dates and flag SLA breaches
Author: Compliance Office
Date: 2025-01-01

Usage:
    python check_capa_sla.py --log ../04-AUDITS/CAPA_LOG.csv
    
    # With custom SLA days by severity
    python check_capa_sla.py --log ../04-AUDITS/CAPA_LOG.csv --critical-days 3 --high-days 14 --medium-days 30

Functionality:
    - Parse CAPA_LOG.csv
    - Check due dates against current date
    - Flag overdue CAPAs
    - Apply SLA rules by severity
    - Generate breach report

SLA Rules (default):
    - Critical: 3 days
    - High: 14 days
    - Medium: 30 days
    - Low: 90 days

Exit codes:
    0 - No overdue CAPAs or warnings only
    1 - One or more CAPAs overdue
"""

import argparse
import csv
import logging
import sys
from datetime import datetime, timedelta
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Default SLA days by severity
DEFAULT_SLA = {
    'Critical': 3,
    'High': 14,
    'Medium': 30,
    'Low': 90
}


class CAPAChecker:
    """Checks CAPA due dates and SLA compliance."""
    
    def __init__(self, log_path, sla_rules=None):
        self.log_path = Path(log_path)
        self.sla_rules = sla_rules or DEFAULT_SLA
        self.capas = []
        self.overdue = []
        self.at_risk = []  # Due within 20% of SLA
        self.issues = []
    
    def load_capa_log(self):
        """Load CAPA log CSV."""
        logger.info(f"Loading CAPA log from {self.log_path}")
        
        if not self.log_path.exists():
            self.issues.append(f"CAPA log not found: {self.log_path}")
            return False
        
        try:
            with open(self.log_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.capas = list(reader)
                logger.info(f"Loaded {len(self.capas)} CAPA entries")
                return True
        except Exception as e:
            self.issues.append(f"Failed to read CAPA log: {e}")
            return False
    
    def parse_date(self, date_str):
        """Parse date string in various formats."""
        if not date_str or not date_str.strip():
            return None
        
        date_str = date_str.strip()
        
        # Try multiple date formats
        formats = [
            '%Y-%m-%d',
            '%Y/%m/%d',
            '%d-%m-%Y',
            '%d/%m/%Y',
            '%m/%d/%Y',
        ]
        
        for fmt in formats:
            try:
                return datetime.strptime(date_str, fmt)
            except ValueError:
                continue
        
        logger.warning(f"Could not parse date: {date_str}")
        return None
    
    def check_capa_sla(self):
        """Check CAPA SLA compliance."""
        logger.info("Checking CAPA SLA compliance...")
        
        today = datetime.now()
        
        for capa in self.capas:
            capa_id = capa.get('CAPA_ID', 'Unknown')
            status = capa.get('Status', '').strip()
            severity = capa.get('Severity', '').strip()
            due_date_str = capa.get('Due', '')
            
            # Skip closed CAPAs
            if status.lower() in ['closed', 'cancelled', 'complete', 'completed']:
                continue
            
            # Parse due date
            due_date = self.parse_date(due_date_str)
            if not due_date:
                self.issues.append(f"{capa_id}: Invalid or missing due date '{due_date_str}'")
                continue
            
            # Calculate days until due
            days_until_due = (due_date - today).days
            
            # Get SLA for severity
            sla_days = self.sla_rules.get(severity, self.sla_rules.get('Medium', 30))
            at_risk_threshold = int(sla_days * 0.2)  # 20% of SLA
            
            if days_until_due < 0:
                # Overdue
                self.overdue.append({
                    'CAPA_ID': capa_id,
                    'Severity': severity,
                    'Due': due_date_str,
                    'Days_Overdue': abs(days_until_due),
                    'Finding': capa.get('Finding', ''),
                    'Owner': capa.get('Owner', '')
                })
            elif days_until_due <= at_risk_threshold:
                # At risk (due soon)
                self.at_risk.append({
                    'CAPA_ID': capa_id,
                    'Severity': severity,
                    'Due': due_date_str,
                    'Days_Remaining': days_until_due,
                    'Finding': capa.get('Finding', ''),
                    'Owner': capa.get('Owner', '')
                })
        
        return True
    
    def generate_report(self):
        """Generate CAPA SLA report."""
        logger.info("=" * 60)
        logger.info("CAPA SLA Compliance Report")
        logger.info("=" * 60)
        logger.info(f"Report Date: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
        logger.info(f"Total CAPAs: {len(self.capas)}")
        logger.info("=" * 60)
        
        # Overdue CAPAs
        if self.overdue:
            logger.error(f"OVERDUE CAPAs: {len(self.overdue)}")
            logger.error("-" * 60)
            for capa in sorted(self.overdue, key=lambda x: x['Days_Overdue'], reverse=True):
                logger.error(
                    f"  ✗ {capa['CAPA_ID']} [{capa['Severity']}] - "
                    f"{capa['Days_Overdue']} days overdue (Due: {capa['Due']})"
                )
                logger.error(f"    Finding: {capa['Finding'][:80]}")
                logger.error(f"    Owner: {capa['Owner']}")
                logger.error("")
        else:
            logger.info("✓ No overdue CAPAs")
        
        # At-risk CAPAs
        if self.at_risk:
            logger.warning(f"AT-RISK CAPAs: {len(self.at_risk)}")
            logger.warning("-" * 60)
            for capa in sorted(self.at_risk, key=lambda x: x['Days_Remaining']):
                logger.warning(
                    f"  ⚠ {capa['CAPA_ID']} [{capa['Severity']}] - "
                    f"{capa['Days_Remaining']} days remaining (Due: {capa['Due']})"
                )
                logger.warning(f"    Finding: {capa['Finding'][:80]}")
                logger.warning(f"    Owner: {capa['Owner']}")
                logger.warning("")
        else:
            logger.info("✓ No at-risk CAPAs")
        
        # Issues
        if self.issues:
            logger.error(f"ISSUES: {len(self.issues)}")
            logger.error("-" * 60)
            for issue in self.issues:
                logger.error(f"  ✗ {issue}")
        
        logger.info("=" * 60)
        
        # Summary
        logger.info("Summary:")
        logger.info(f"  Overdue: {len(self.overdue)}")
        logger.info(f"  At-Risk: {len(self.at_risk)}")
        logger.info(f"  Issues: {len(self.issues)}")
        logger.info("=" * 60)
        
        return len(self.overdue) == 0


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Check CAPA due dates and SLA compliance'
    )
    parser.add_argument('--log', required=True,
                       help='Path to CAPA_LOG.csv')
    parser.add_argument('--critical-days', type=int, default=3,
                       help='SLA days for Critical severity (default: 3)')
    parser.add_argument('--high-days', type=int, default=14,
                       help='SLA days for High severity (default: 14)')
    parser.add_argument('--medium-days', type=int, default=30,
                       help='SLA days for Medium severity (default: 30)')
    parser.add_argument('--low-days', type=int, default=90,
                       help='SLA days for Low severity (default: 90)')
    
    args = parser.parse_args()
    
    # Build SLA rules
    sla_rules = {
        'Critical': args.critical_days,
        'High': args.high_days,
        'Medium': args.medium_days,
        'Low': args.low_days
    }
    
    logger.info("Starting CAPA SLA check")
    logger.info(f"SLA Rules: {sla_rules}")
    
    try:
        checker = CAPAChecker(args.log, sla_rules)
        
        # Load and check
        if not checker.load_capa_log():
            logger.error("Failed to load CAPA log")
            return 1
        
        checker.check_capa_sla()
        
        # Generate report
        success = checker.generate_report()
        
        return 0 if success else 1
        
    except Exception as e:
        logger.error(f"Check failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
