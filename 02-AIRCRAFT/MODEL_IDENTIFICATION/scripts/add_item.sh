#!/usr/bin/env bash
# ==============================================================================
# TFA Item Addition Script
# ==============================================================================
# This script adds a new item/artifact to the TFA structure with proper metadata
#
# Usage:
#   ./add_item.sh DOMAIN ATA_CHAPTER ATA_MID COMP EFFECT SUBPROD_ID SUBJECT_ID ITEM_DESC OWNER
#
# Example:
#   ./add_item.sh AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS ATA-53 ATA-53-10 \
#                 ATA-53-10-01 0001-9999 SUBPROD_001 SUBJ_001 design-spec StructuralTeam

set -euo pipefail

# Color codes for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored messages
print_info() { echo -e "${BLUE}ℹ ${1}${NC}"; }
print_success() { echo -e "${GREEN}✓ ${1}${NC}"; }
print_warning() { echo -e "${YELLOW}⚠ ${1}${NC}"; }
print_error() { echo -e "${RED}✗ ${1}${NC}"; }

# Validate arguments
if [ $# -lt 9 ]; then
    print_error "Missing required arguments"
    echo "Usage: $0 DOMAIN ATA_CHAPTER ATA_MID COMP EFFECT SUBPROD_ID SUBJECT_ID ITEM_DESC OWNER"
    echo ""
    echo "Example:"
    echo "  $0 AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS ATA-53 ATA-53-10 \\"
    echo "     ATA-53-10-01 0001-9999 SUBPROD_001 SUBJ_001 design-spec StructuralTeam"
    exit 1
fi

# Parse arguments
DOMAIN="${1:?DOMAIN required}"
ATA_CHAPTER="${2:?ATA_CHAPTER required}"
ATA_MID="${3:?ATA_MID required}"
COMP="${4:?COMP required}"
EFFECT="${5:?EFFECT required}"
SUBPROD_ID="${6:?SUBPROD_ID required}"
SUBJECT_ID="${7:?SUBJECT_ID required}"
ITEM_DESC="${8:?ITEM_DESC required}"
OWNER="${9:?OWNER required}"

# Base path
PRODUCT="AMPEL360-AIR-T"
ARCH="BWB-H2-Hy-E"
FAMILY="Q100_STD01"

ROOT="$PRODUCT/ARCH/$ARCH/FAMILY/$FAMILY/DOMAIN/$DOMAIN/$ATA_CHAPTER/SYSTEMS/$ATA_MID"
BASE="$ROOT/CONF/BASELINE/COMPONENTS/$COMP/SUBPRODUCT/$SUBPROD_ID"
SDIR="$BASE/SUBJECT/$SUBJECT_ID"
REDIR="$SDIR/RANGE-EFFECT/$EFFECT"
IDIR="$REDIR/artifacts/01-$ITEM_DESC"

# Current date
DATE=$(date +%Y-%m-%d)

print_info "Creating item structure..."

# Create directories
mkdir -p "$IDIR/DOC"
print_success "Created directory: $IDIR"

# ============================================================================
# Create SUBPRODUCT_INDEX.csv
# ============================================================================
SPI="$BASE/SUBPRODUCT_INDEX.csv"
if [ ! -f "$SPI" ]; then
    print_info "Creating SUBPRODUCT_INDEX.csv..."
    cat > "$SPI" <<'EOF'
subproduct_id,description,version,status,owner,created_date,modified_date
EOF
fi

# Add entry if not exists
if ! grep -q "^$SUBPROD_ID," "$SPI" 2>/dev/null; then
    echo "$SUBPROD_ID,Subproduct for $COMP,1.0,Active,$OWNER,$DATE,$DATE" >> "$SPI"
    print_success "Added entry to SUBPRODUCT_INDEX.csv"
fi

# ============================================================================
# Create SUBJECT_META.json
# ============================================================================
SMETA="$SDIR/SUBJECT_META.json"
if [ ! -f "$SMETA" ]; then
    print_info "Creating SUBJECT_META.json..."
    cat > "$SMETA" <<EOF
{
  "subject_id": "$SUBJECT_ID",
  "title": "Subject for $COMP",
  "description": "Engineering subject for component $COMP",
  "version": "1.0",
  "status": "active",
  "owner": "$OWNER",
  "created_date": "$DATE",
  "modified_date": "$DATE",
  "tags": [
    "aircraft",
    "component",
    "$COMP"
  ],
  "compliance": {
    "standards": ["AS9100", "ISO9001"],
    "certifications": ["EASA", "FAA"]
  },
  "utcs_anchor": "utcs://AMPEL360/$FAMILY/$SUBJECT_ID"
}
EOF
    print_success "Created SUBJECT_META.json"
fi

# ============================================================================
# Create SUBJECT_MANIFEST.csv
# ============================================================================
SMAN="$SDIR/SUBJECT_MANIFEST.csv"
if [ ! -f "$SMAN" ]; then
    print_info "Creating SUBJECT_MANIFEST.csv..."
    cat > "$SMAN" <<'EOF'
artifact_id,artifact_name,artifact_type,file_path,checksum,version,created_date,status
EOF
fi

# Add artifact entry
ARTIFACT_ID="01-$ITEM_DESC"
if ! grep -q "^$ARTIFACT_ID," "$SMAN" 2>/dev/null; then
    echo "$ARTIFACT_ID,$ITEM_DESC,document,RANGE-EFFECT/$EFFECT/artifacts/$ARTIFACT_ID/,sha256:pending,1.0,$DATE,draft" >> "$SMAN"
    print_success "Added entry to SUBJECT_MANIFEST.csv"
fi

# ============================================================================
# Create SUBJECT_CONFIG.yml
# ============================================================================
SCONF="$SDIR/SUBJECT_CONFIG.yml"
if [ ! -f "$SCONF" ]; then
    print_info "Creating SUBJECT_CONFIG.yml..."
    cat > "$SCONF" <<EOF
# Subject Configuration
subject:
  id: $SUBJECT_ID
  name: Subject for $COMP
  version: "1.0"
  
effectivity:
  range: "$EFFECT"
  applicability: "Aircraft in $FAMILY family"
  
configuration:
  baseline: BASELINE
  approval_required: true
  change_control: true
  
traceability:
  requirements:
    - REQ_001: "System requirements"
    - REQ_002: "Component specifications"
  interfaces:
    - INT_001: "System interfaces"
    
validation:
  analysis_required: true
  testing_required: true
  simulation_required: true
  
metadata:
  owner: $OWNER
  created: $DATE
  modified: $DATE
  status: active
EOF
    print_success "Created SUBJECT_CONFIG.yml"
fi

# ============================================================================
# Create Artifact META.json
# ============================================================================
AMETA="$IDIR/META.json"
print_info "Creating artifact META.json..."
cat > "$AMETA" <<EOF
{
  "artifact_id": "01-$ITEM_DESC",
  "title": "$ITEM_DESC",
  "description": "Artifact for $COMP - $ITEM_DESC",
  "type": "document",
  "version": "1.0",
  "status": "draft",
  "created_date": "$DATE",
  "modified_date": "$DATE",
  "owner": "$OWNER",
  "reviewers": [],
  "classification": "internal",
  "retention_period": "10_years"
}
EOF
print_success "Created META.json"

# ============================================================================
# Create Artifact MANIFEST.csv
# ============================================================================
AMAN="$IDIR/MANIFEST.csv"
print_info "Creating artifact MANIFEST.csv..."
cat > "$AMAN" <<'EOF'
file_name,file_type,file_size,checksum,created_date,created_by,status
EOF
print_success "Created MANIFEST.csv"

# ============================================================================
# Create Artifact CONFIG.yml
# ============================================================================
ACONF="$IDIR/CONFIG.yml"
print_info "Creating artifact CONFIG.yml..."
cat > "$ACONF" <<EOF
# Artifact Configuration
artifact:
  id: 01-$ITEM_DESC
  name: $ITEM_DESC
  type: document
  version: "1.0"
  
access_control:
  read: [engineering, quality, management]
  write: [engineering]
  approve: [chief_engineer, quality_manager]
  
workflow:
  state: draft
  submitted_date: $DATE
  
versioning:
  major: 1
  minor: 0
  patch: 0
  previous_version: null
  change_summary: Initial creation
  
links:
  related_artifacts: []
  parent_requirements: []
  dependent_artifacts: []
EOF
print_success "Created CONFIG.yml"

# ============================================================================
# Create DOC README
# ============================================================================
DREADME="$IDIR/DOC/README.md"
print_info "Creating DOC/README.md..."
cat > "$DREADME" <<EOF
# Documentation for $ITEM_DESC

## Purpose

This directory contains documentation artifacts for: **$ITEM_DESC**

## Contents

Place your documentation files here:
- Design specifications
- Technical drawings
- Analysis reports
- Review documentation
- Approval records

## File Naming Convention

\`\`\`
{document_type}_{item_id}_{version}_{date}.{ext}
\`\`\`

Example: \`design_spec_${COMP}_v1.0_$DATE.pdf\`

## Metadata

- **Artifact ID**: 01-$ITEM_DESC
- **Owner**: $OWNER
- **Created**: $DATE
- **Status**: Draft

---

**Last Updated**: $DATE
EOF
print_success "Created DOC/README.md"

# ============================================================================
# Summary
# ============================================================================
echo ""
print_success "Item creation complete!"
echo ""
echo "Created structure at:"
echo "  $IDIR"
echo ""
echo "Files created:"
echo "  ✓ $SPI"
echo "  ✓ $SMETA"
echo "  ✓ $SMAN"
echo "  ✓ $SCONF"
echo "  ✓ $AMETA"
echo "  ✓ $AMAN"
echo "  ✓ $ACONF"
echo "  ✓ $DREADME"
echo ""
print_info "Next steps:"
echo "  1. Add documentation files to: $IDIR/DOC/"
echo "  2. Update MANIFEST.csv with actual file checksums"
echo "  3. Run validation: make validate DOMAIN=$DOMAIN ATA_CHAPTER=$ATA_CHAPTER ATA_MID=$ATA_MID COMP=$COMP"
