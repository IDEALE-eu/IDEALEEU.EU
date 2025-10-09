#!/usr/bin/env bash
set -euo pipefail

# Validation script for 06-DIMENSIONS-STATIONS system structure
# Validates compliance with the defined subsystem structure and CI requirements

SYSTEM_PATH="02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB/VERSION/Q100/AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS/SYSTEMS/06-DIMENSIONS-STATIONS"
ERRORS=0
WARNINGS=0

# Color codes for output
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

error() {
  echo -e "${RED}✗ ERROR:${NC} $1"
  ((ERRORS++))
}

warning() {
  echo -e "${YELLOW}⚠ WARNING:${NC} $1"
  ((WARNINGS++))
}

success() {
  echo -e "${GREEN}✓${NC} $1"
}

info() {
  echo -e "${BLUE}ℹ${NC} $1"
}

# Check if system exists
if [[ ! -d "$SYSTEM_PATH" ]]; then
  error "System directory not found: $SYSTEM_PATH"
  exit 1
fi

echo ""
echo "=========================================="
echo "06-DIMENSIONS-STATIONS Validation"
echo "=========================================="
echo ""

info "Validating system-level files..."

# Check INTEGRATION_VIEW.md
if [[ ! -f "$SYSTEM_PATH/INTEGRATION_VIEW.md" ]]; then
  error "Missing INTEGRATION_VIEW.md"
else
  # Check for minimum content
  if [[ $(wc -l < "$SYSTEM_PATH/INTEGRATION_VIEW.md") -lt 10 ]]; then
    warning "INTEGRATION_VIEW.md appears incomplete (less than 10 lines)"
  else
    success "INTEGRATION_VIEW.md exists and has content"
  fi
fi

# Check INTERFACE_MATRIX directory and CSV
if [[ ! -d "$SYSTEM_PATH/INTERFACE_MATRIX" ]]; then
  error "Missing INTERFACE_MATRIX/ directory"
else
  if ! ls "$SYSTEM_PATH/INTERFACE_MATRIX"/*.csv &> /dev/null; then
    error "No CSV files found in INTERFACE_MATRIX/"
  else
    csv_count=$(ls "$SYSTEM_PATH/INTERFACE_MATRIX"/*.csv 2>/dev/null | wc -l)
    success "INTERFACE_MATRIX/ exists with $csv_count CSV file(s)"
    
    # Validate CSV header
    for csv_file in "$SYSTEM_PATH/INTERFACE_MATRIX"/*.csv; do
      if ! head -n1 "$csv_file" | grep -q "from_ata,to_ata,interface"; then
        warning "CSV file $(basename "$csv_file") missing standard header"
      fi
      
      # Check for at least 2 lines (header + data)
      if [[ $(wc -l < "$csv_file") -lt 2 ]]; then
        warning "CSV file $(basename "$csv_file") has no data rows"
      fi
    done
  fi
fi

# Check SUBSYSTEMS directory
if [[ ! -d "$SYSTEM_PATH/SUBSYSTEMS" ]]; then
  error "Missing SUBSYSTEMS/ directory"
  exit 1
fi

echo ""
info "Validating subsystems..."

# Expected subsystems for 06-DIMENSIONS-STATIONS
EXPECTED_SUBSYSTEMS=(
  "06-10_REFERENCE_FRAMES"
  "06-20_MEASUREMENT_POINTS"
  "06-30_ALIGNMENT_TARGETS"
  "06-40_CALIBRATION_PROTOCOLS"
  "06-50_GEOMETRIC_MODELS"
)

# Check each expected subsystem
for subsystem in "${EXPECTED_SUBSYSTEMS[@]}"; do
  subsystem_path="$SYSTEM_PATH/SUBSYSTEMS/$subsystem"
  
  echo ""
  info "Checking subsystem: $subsystem"
  
  if [[ ! -d "$subsystem_path" ]]; then
    error "Missing subsystem directory: $subsystem"
    continue
  fi
  
  # Check mandatory files
  if [[ ! -f "$subsystem_path/README.md" ]]; then
    error "Missing README.md in $subsystem"
  else
    success "README.md exists"
  fi
  
  if [[ ! -f "$subsystem_path/META.json" ]]; then
    error "Missing META.json in $subsystem"
  else
    # Validate META.json format
    if command -v jq &> /dev/null; then
      if ! jq -e '.scope == "instance"' "$subsystem_path/META.json" &> /dev/null; then
        error "META.json in $subsystem must have scope=\"instance\""
      else
        success "META.json valid with scope=instance"
      fi
    else
      warning "jq not available, skipping META.json validation"
    fi
  fi
  
  if [[ ! -f "$subsystem_path/inherit.json" ]]; then
    warning "Missing inherit.json in $subsystem"
  else
    success "inherit.json exists"
  fi
  
  # Check PLM structure
  if [[ ! -d "$subsystem_path/PLM" ]]; then
    error "Missing PLM/ directory in $subsystem"
  else
    if [[ ! -f "$subsystem_path/PLM/EBOM_LINKS.md" ]]; then
      warning "Missing PLM/EBOM_LINKS.md in $subsystem"
    else
      success "PLM/EBOM_LINKS.md exists"
    fi
    
    if [[ ! -d "$subsystem_path/PLM/CAx" ]]; then
      error "Missing PLM/CAx/ directory in $subsystem"
    else
      # Check all required CAx subdirectories
      cax_dirs=("CAD" "CAE" "CAO" "CAM" "CAI" "CAV" "CAP" "CAS" "CMP")
      missing_cax=0
      
      for cax_dir in "${cax_dirs[@]}"; do
        if [[ ! -d "$subsystem_path/PLM/CAx/$cax_dir" ]]; then
          warning "Missing CAx subdirectory: $cax_dir in $subsystem"
          ((missing_cax++))
        fi
      done
      
      if [[ $missing_cax -eq 0 ]]; then
        success "All 9 CAx subdirectories present"
      else
        warning "$missing_cax CAx subdirectories missing in $subsystem"
      fi
    fi
  fi
  
  # Check recommended directories
  for dir in "DELs" "PAx" "PROCUREMENT" "QUANTUM_OA" "SUPPLIERS" "policy" "tests"; do
    if [[ ! -d "$subsystem_path/$dir" ]]; then
      warning "Missing recommended directory: $dir in $subsystem"
    fi
  done
done

# Check for PLM/CAx at system level (should NOT exist)
if [[ -d "$SYSTEM_PATH/PLM/CAx" ]]; then
  error "PROHIBITED: PLM/CAx found at system level. PLM/CAx must ONLY exist in SUBSYSTEMS"
fi

# Summary
echo ""
echo "=========================================="
echo "Validation Summary"
echo "=========================================="
echo -e "Errors:   ${RED}$ERRORS${NC}"
echo -e "Warnings: ${YELLOW}$WARNINGS${NC}"
echo ""

if [[ $ERRORS -eq 0 ]]; then
  echo -e "${GREEN}✓ Validation PASSED${NC}"
  echo "System 06-DIMENSIONS-STATIONS complies with structure requirements"
  exit 0
else
  echo -e "${RED}✗ Validation FAILED${NC}"
  echo "Please fix errors before proceeding"
  exit 1
fi
