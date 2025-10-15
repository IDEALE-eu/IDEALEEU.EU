#!/usr/bin/env python3
"""
Script: hash_evidence.py
Purpose: Compute and verify SHA-256 hashes for compliance evidence files
Author: Compliance Office
Date: 2025-01-01

Usage:
    # Compute hash of a file
    python hash_evidence.py --file /path/to/evidence.pdf --compute
    
    # Verify hash against EVIDENCE_INDEX.csv
    python hash_evidence.py --index ../06-EVIDENCE/EVIDENCE_INDEX.csv --verify
    
    # Update EVIDENCE_INDEX.csv with computed hashes
    python hash_evidence.py --index ../06-EVIDENCE/EVIDENCE_INDEX.csv --update

Functionality:
    - Compute SHA-256 hash of evidence files
    - Verify hashes match EVIDENCE_INDEX.csv
    - Update EVIDENCE_INDEX.csv with new hashes
    - Bulk verification of all evidence files

Exit codes:
    0 - All checks passed
    1 - Verification failed or error occurred
"""

import argparse
import csv
import hashlib
import logging
import sys
from pathlib import Path
from datetime import datetime

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def compute_file_hash(file_path):
    """Compute SHA-256 hash of a file."""
    sha256_hash = hashlib.sha256()
    
    try:
        with open(file_path, "rb") as f:
            # Read file in chunks to handle large files
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        return sha256_hash.hexdigest()
    except Exception as e:
        logger.error(f"Failed to compute hash for {file_path}: {e}")
        return None


class EvidenceHashManager:
    """Manages hashing and verification of evidence files."""
    
    def __init__(self, index_path=None):
        self.index_path = Path(index_path) if index_path else None
        self.evidence_entries = []
        self.issues = []
        self.verified_count = 0
    
    def load_index(self):
        """Load evidence index CSV."""
        if not self.index_path or not self.index_path.exists():
            self.issues.append(f"Evidence index not found: {self.index_path}")
            return False
        
        try:
            with open(self.index_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                self.evidence_entries = list(reader)
                logger.info(f"Loaded {len(self.evidence_entries)} evidence entries")
                return True
        except Exception as e:
            self.issues.append(f"Failed to read index: {e}")
            return False
    
    def verify_evidence(self, base_path=None):
        """Verify hashes of all evidence files in index."""
        logger.info("Verifying evidence hashes...")
        
        if base_path is None:
            base_path = self.index_path.parent.parent  # Go up to COMPLIANCE dir
        else:
            base_path = Path(base_path)
        
        for entry in self.evidence_entries:
            evidence_id = entry.get('Evidence_ID', 'Unknown')
            utcs = entry.get('UTCS', '')
            stored_hash = entry.get('Hash(SHA256)', '').strip()
            
            if not stored_hash:
                self.issues.append(f"{evidence_id}: No hash stored")
                continue
            
            # Try to find the file based on UTCS or Evidence_ID
            # This is a simplified lookup - in production, you'd have a proper mapping
            file_pattern = f"**/*{evidence_id}*"
            files = list(base_path.glob(file_pattern))
            
            if not files:
                logger.warning(f"{evidence_id}: Evidence file not found (searched: {file_pattern})")
                continue
            
            if len(files) > 1:
                logger.warning(f"{evidence_id}: Multiple files match, using first: {files[0]}")
            
            file_path = files[0]
            computed_hash = compute_file_hash(file_path)
            
            if computed_hash is None:
                continue
            
            if computed_hash == stored_hash:
                logger.info(f"✓ {evidence_id}: Hash verified")
                self.verified_count += 1
            else:
                self.issues.append(
                    f"{evidence_id}: Hash mismatch!\n"
                    f"  Expected: {stored_hash}\n"
                    f"  Computed: {computed_hash}"
                )
        
        return len(self.issues) == 0
    
    def update_hash(self, file_path, evidence_id=None):
        """Update or add hash for a specific evidence file."""
        file_path = Path(file_path)
        
        if not file_path.exists():
            self.issues.append(f"File not found: {file_path}")
            return False
        
        computed_hash = compute_file_hash(file_path)
        if computed_hash is None:
            return False
        
        logger.info(f"Computed hash for {file_path.name}: {computed_hash}")
        
        # If index exists, try to update it
        if self.index_path and self.index_path.exists():
            self.load_index()
            
            # Find matching entry
            found = False
            for entry in self.evidence_entries:
                if evidence_id and entry.get('Evidence_ID') == evidence_id:
                    entry['Hash(SHA256)'] = computed_hash
                    entry['Date'] = datetime.now().strftime('%Y-%m-%d')
                    found = True
                    logger.info(f"Updated hash for {evidence_id}")
                    break
            
            if not found and evidence_id:
                # Add new entry
                new_entry = {
                    'Evidence_ID': evidence_id,
                    'Title': file_path.name,
                    'UTCS': '',
                    'Hash(SHA256)': computed_hash,
                    'Related_Req_ID': '',
                    'Owner': '',
                    'Rev': '1.0',
                    'Date': datetime.now().strftime('%Y-%m-%d')
                }
                self.evidence_entries.append(new_entry)
                logger.info(f"Added new entry for {evidence_id}")
            
            # Write back
            try:
                with open(self.index_path, 'w', encoding='utf-8', newline='') as f:
                    if self.evidence_entries:
                        fieldnames = self.evidence_entries[0].keys()
                        writer = csv.DictWriter(f, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(self.evidence_entries)
                logger.info(f"Updated index: {self.index_path}")
            except Exception as e:
                self.issues.append(f"Failed to write index: {e}")
                return False
        
        return True
    
    def generate_report(self):
        """Generate verification report."""
        logger.info("=" * 60)
        logger.info("Evidence Hash Verification Report")
        logger.info("=" * 60)
        
        if self.evidence_entries:
            logger.info(f"Total entries: {len(self.evidence_entries)}")
            logger.info(f"Verified: {self.verified_count}")
        
        if not self.issues:
            logger.info("✓ All checks passed!")
            return True
        
        logger.error(f"Issues: {len(self.issues)}")
        for issue in self.issues:
            logger.error(f"  ✗ {issue}")
        
        logger.info("=" * 60)
        
        return len(self.issues) == 0


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Compute and verify SHA-256 hashes for evidence files'
    )
    parser.add_argument('--file', 
                       help='Evidence file to hash')
    parser.add_argument('--index',
                       help='Path to EVIDENCE_INDEX.csv')
    parser.add_argument('--evidence-id',
                       help='Evidence ID for the file')
    parser.add_argument('--compute', action='store_true',
                       help='Compute hash of file')
    parser.add_argument('--verify', action='store_true',
                       help='Verify hashes in index')
    parser.add_argument('--update', action='store_true',
                       help='Update hash in index')
    parser.add_argument('--base-path',
                       help='Base path to search for evidence files')
    
    args = parser.parse_args()
    
    if not any([args.compute, args.verify, args.update]):
        parser.error("Specify at least one action: --compute, --verify, or --update")
    
    try:
        manager = EvidenceHashManager(args.index)
        
        if args.compute and args.file:
            # Just compute and print hash
            hash_val = compute_file_hash(args.file)
            if hash_val:
                print(f"SHA-256: {hash_val}")
                return 0
            else:
                return 1
        
        if args.update and args.file:
            # Update hash in index
            if not args.index:
                logger.error("--index required for --update")
                return 1
            
            success = manager.update_hash(args.file, args.evidence_id)
            return 0 if success else 1
        
        if args.verify:
            # Verify all hashes in index
            if not args.index:
                logger.error("--index required for --verify")
                return 1
            
            if not manager.load_index():
                return 1
            
            manager.verify_evidence(args.base_path)
            success = manager.generate_report()
            
            return 0 if success else 1
        
        return 0
        
    except Exception as e:
        logger.error(f"Operation failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
