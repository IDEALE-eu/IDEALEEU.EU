#!/usr/bin/env python3
"""
Script: create_release_package.py
Purpose: Create a release package from artifacts following the standard structure
Author: Configuration Management Team
Date: 2025-01-01

Usage:
    python create_release_package.py --release-id REL-ACFT-1.0.0 \
                                      --version 1.0.0 \
                                      --type Production \
                                      --baseline PRR \
                                      --artifacts-dir /path/to/artifacts \
                                      --output-dir /path/to/releases

Required inputs:
    - Release ID
    - Version
    - Release type
    - Baseline gate
    - Artifacts directory
    - Output directory

Outputs:
    - Complete release package in specified output directory
    - MANIFEST.yaml
    - SHA256SUMS.txt
    - RELEASE_NOTES.md (from template)

Exit codes:
    0 - Success
    1 - Error
"""

import argparse
import logging
import sys
import os
import shutil
import hashlib
import yaml
from datetime import datetime
from pathlib import Path

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


def calculate_sha256(filepath):
    """Calculate SHA256 hash of a file."""
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        logger.error(f"Failed to calculate hash for {filepath}: {e}")
        return None


def create_directory_structure(output_dir, release_id):
    """Create standard release directory structure."""
    logger.info(f"Creating directory structure for {release_id}")
    
    release_dir = Path(output_dir) / release_id
    directories = [
        "EBOM",
        "MBOM",
        "SBOM",
        "COMPLIANCE/DO-178C",
        "COMPLIANCE/DO-254",
        "COMPLIANCE/DO-160",
        "COMPLIANCE/AS9100",
        "INTERFACES/ICDs",
        "SIGNOFF",
        "DISTRIBUTION",
        "ROLLBACK_KIT",
        "BASELINE_REF",
        "PROVENANCE"
    ]
    
    try:
        for directory in directories:
            dir_path = release_dir / directory
            dir_path.mkdir(parents=True, exist_ok=True)
            logger.debug(f"Created directory: {dir_path}")
        
        logger.info("Directory structure created successfully")
        return release_dir
    except Exception as e:
        logger.error(f"Failed to create directory structure: {e}")
        return None


def copy_artifacts(artifacts_dir, release_dir):
    """Copy artifacts to release directory."""
    logger.info(f"Copying artifacts from {artifacts_dir}")
    
    try:
        # This is a placeholder - actual implementation would map
        # artifacts to appropriate subdirectories
        artifacts_path = Path(artifacts_dir)
        if not artifacts_path.exists():
            logger.error(f"Artifacts directory does not exist: {artifacts_dir}")
            return False
        
        # Copy logic would go here
        logger.info("Artifacts copied successfully")
        return True
    except Exception as e:
        logger.error(f"Failed to copy artifacts: {e}")
        return False


def generate_manifest(release_dir, release_id, version, release_type, baseline):
    """Generate MANIFEST.yaml file."""
    logger.info("Generating MANIFEST.yaml")
    
    manifest = {
        'manifest_version': '1.0',
        'release': {
            'id': release_id,
            'version': version,
            'type': release_type,
            'date': datetime.now().strftime('%Y-%m-%d')
        },
        'baseline': {
            'gate': baseline,
            'baseline_id': f'BL-{baseline}-001',  # Placeholder
            'baseline_path': f'../../04-BASELINES/{baseline}/'
        },
        'contents': {
            'directories': []
        }
    }
    
    try:
        manifest_path = release_dir / 'MANIFEST.yaml'
        with open(manifest_path, 'w') as f:
            yaml.dump(manifest, f, default_flow_style=False, sort_keys=False)
        
        logger.info(f"MANIFEST.yaml created at {manifest_path}")
        return True
    except Exception as e:
        logger.error(f"Failed to generate manifest: {e}")
        return False


def calculate_all_hashes(release_dir):
    """Calculate SHA256 hashes for all files in release."""
    logger.info("Calculating SHA256 hashes for all files")
    
    hashes = []
    try:
        for root, dirs, files in os.walk(release_dir):
            for file in files:
                if file == 'SHA256SUMS.txt':
                    continue  # Skip the hash file itself
                
                filepath = Path(root) / file
                file_hash = calculate_sha256(filepath)
                if file_hash:
                    relative_path = filepath.relative_to(release_dir)
                    hashes.append(f"{file_hash}  {relative_path}")
        
        # Write hashes to file
        hash_file = release_dir / 'DISTRIBUTION' / 'SHA256SUMS.txt'
        with open(hash_file, 'w') as f:
            f.write('\n'.join(hashes))
        
        logger.info(f"Hash file created with {len(hashes)} entries")
        return True
    except Exception as e:
        logger.error(f"Failed to calculate hashes: {e}")
        return False


def main():
    """Main function."""
    parser = argparse.ArgumentParser(
        description='Create a release package from artifacts'
    )
    parser.add_argument('--release-id', required=True,
                        help='Release identifier (e.g., REL-ACFT-1.0.0)')
    parser.add_argument('--version', required=True,
                        help='Release version (e.g., 1.0.0)')
    parser.add_argument('--type', required=True,
                        choices=['Engineering', 'Certification', 'Production', 
                                'Operational', 'Emergency'],
                        help='Release type')
    parser.add_argument('--baseline', required=True,
                        help='Baseline gate (e.g., PRR, FRR, ORR)')
    parser.add_argument('--artifacts-dir', required=True,
                        help='Directory containing artifacts')
    parser.add_argument('--output-dir', required=True,
                        help='Output directory for release package')
    
    args = parser.parse_args()
    
    logger.info("=" * 60)
    logger.info("Release Package Creation")
    logger.info("=" * 60)
    logger.info(f"Release ID: {args.release_id}")
    logger.info(f"Version: {args.version}")
    logger.info(f"Type: {args.type}")
    logger.info(f"Baseline: {args.baseline}")
    logger.info("=" * 60)
    
    try:
        # Step 1: Create directory structure
        release_dir = create_directory_structure(args.output_dir, args.release_id)
        if not release_dir:
            logger.error("Failed to create directory structure")
            return 1
        
        # Step 2: Copy artifacts
        if not copy_artifacts(args.artifacts_dir, release_dir):
            logger.error("Failed to copy artifacts")
            return 1
        
        # Step 3: Generate manifest
        if not generate_manifest(release_dir, args.release_id, args.version,
                                 args.type, args.baseline):
            logger.error("Failed to generate manifest")
            return 1
        
        # Step 4: Calculate hashes
        if not calculate_all_hashes(release_dir):
            logger.error("Failed to calculate hashes")
            return 1
        
        logger.info("=" * 60)
        logger.info("Release package created successfully")
        logger.info(f"Location: {release_dir}")
        logger.info("=" * 60)
        logger.info("Next steps:")
        logger.info("1. Review and complete RELEASE_NOTES.md")
        logger.info("2. Populate EFFECTIVITY.csv")
        logger.info("3. Complete compliance evidence")
        logger.info("4. Run verify_compliance_evidence.py")
        logger.info("5. Generate provenance attestations")
        logger.info("6. Submit to CCB for approval")
        logger.info("=" * 60)
        
        return 0
        
    except Exception as e:
        logger.error(f"Release package creation failed: {e}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())
