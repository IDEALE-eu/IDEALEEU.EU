#!/usr/bin/env bash
set -euo pipefail

# Validation script for spacecraft systems structure
# Validates compliance with AMPEL360-SPACE-T architecture rules

ROOT="03-SPACECRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-SPACE-T/MODELS/PLUS/VERSION/Q10"
ERRORS=0
WARNINGS=0

# Color codes for output
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
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
  echo "ℹ $1"
}

# Check if spacecraft structure exists
if [[ ! -d "$ROOT" ]]; then
  error "Spacecraft systems root not found: $ROOT"
  exit 1
fi

info "Validating spacecraft systems structure in $ROOT"
echo ""

# Check mandatory SYSTEMS directory
if [[ ! -d "$ROOT/SYSTEMS" ]]; then
  error "Missing mandatory SYSTEMS/ directory"
  exit 1
else
  success "SYSTEMS/ directory exists"
fi

# Expected systems
EXPECTED_SYSTEMS=(
  "06_DIMENSIONS_ALIGNMENTS"
  "50_PAYLOAD_STRUCTURES"
  "51_PRIMARY_STRUCTURE"
  "52_DOORS_HATCHES"
  "53_STRUCTURAL_BODY"
  "55_ADCS_STRUCTURES"
  "56_WINDOWS"
  "57_SOLAR_ARRAYS"
  "66_MECHANISMS"
  "94_QUALIFICATION_ACCEPTANCE"
)

info ""
info "Checking systems structure..."

for system in "${EXPECTED_SYSTEMS[@]}"; do
  system_path="$ROOT/SYSTEMS/$system"
  
  if [[ ! -d "$system_path" ]]; then
    error "System not found: $system"
    continue
  fi
  
  success "System exists: $system"
  
  # Check mandatory system files/directories
  if [[ ! -f "$system_path/INTEGRATION_VIEW.md" ]]; then
    error "Missing INTEGRATION_VIEW.md in $system"
  fi
  
  if [[ ! -d "$system_path/INTERFACE_MATRIX" ]]; then
    error "Missing INTERFACE_MATRIX/ directory in $system"
  else
    # Check for at least one CSV file
    if ! ls "$system_path/INTERFACE_MATRIX"/*.csv &> /dev/null; then
      warning "No CSV files found in $system/INTERFACE_MATRIX/"
    fi
  fi
  
  if [[ ! -d "$system_path/SUBSYSTEMS" ]]; then
    error "Missing SUBSYSTEMS/ directory in $system"
  else
    # Count subsystems
    subsystem_count=$(find "$system_path/SUBSYSTEMS" -mindepth 1 -maxdepth 1 -type d | wc -l)
    if [[ $subsystem_count -eq 0 ]]; then
      warning "No subsystems found in $system/SUBSYSTEMS/"
    else
      success "$system has $subsystem_count subsystems"
    fi
  fi
done

# Validate subsystem structure (check a few examples)
info ""
info "Validating subsystem structure..."

# Define subsystems to check for each system
declare -A SUBSYSTEMS_TO_CHECK
SUBSYSTEMS_TO_CHECK["06_DIMENSIONS_ALIGNMENTS"]="06_00_DIMENSIONS_STATIONS_GENERAL 06_10_REFERENCE_FRAMES"
SUBSYSTEMS_TO_CHECK["50_PAYLOAD_STRUCTURES"]="50_00_PAYLOAD_STRUCTURES_GENERAL 50_10_PAYLOAD_ADAPTERS_RINGS"
SUBSYSTEMS_TO_CHECK["51_PRIMARY_STRUCTURE"]="51_00_STRUCTURES_GENERAL_GENERAL 51_10_BUS_PRIMARY_STRUCTURE"
SUBSYSTEMS_TO_CHECK["66_MECHANISMS"]="66_00_MECHANISMS_GENERAL 66_10_RELEASE_DEVICES_HDRM"

for system in "${!SUBSYSTEMS_TO_CHECK[@]}"; do
  for subsystem in ${SUBSYSTEMS_TO_CHECK[$system]}; do
    subsystem_path="$ROOT/SYSTEMS/$system/SUBSYSTEMS/$subsystem"
    
    if [[ ! -d "$subsystem_path" ]]; then
      error "Subsystem not found: $system/SUBSYSTEMS/$subsystem"
      continue
    fi
    
    # Check mandatory subsystem directories
    if [[ ! -d "$subsystem_path/PLM/CAx" ]]; then
      error "Missing PLM/CAx/ directory in $system/SUBSYSTEMS/$subsystem"
    else
      # Check all CAx subdirectories
      cax_dirs=("CAD" "CAE" "CAO" "CAM" "CAI" "CAV" "CAS" "CMP")
      missing_cax=0
      for cax_dir in "${cax_dirs[@]}"; do
        if [[ ! -d "$subsystem_path/PLM/CAx/$cax_dir" ]]; then
          warning "Missing CAx subdirectory: $system/SUBSYSTEMS/$subsystem/PLM/CAx/$cax_dir"
          ((missing_cax++))
        fi
      done
      
      if [[ $missing_cax -eq 0 ]]; then
        success "Subsystem $subsystem has complete PLM/CAx structure"
      fi
    fi
    
    if [[ ! -f "$subsystem_path/PLM/EBOM_LINKS.md" ]]; then
      warning "Missing PLM/EBOM_LINKS.md in subsystem $subsystem"
    fi
  done
done

# Check that underscores are used (not hyphens) in naming
info ""
info "Checking naming conventions (underscores only)..."

hyphen_count=$(find "$ROOT/SYSTEMS" -name "*-*" -type d | grep -v "INTERFACE_MATRIX" | wc -l || true)
if [[ $hyphen_count -gt 0 ]]; then
  warning "Found $hyphen_count directories with hyphens (should use underscores)"
  find "$ROOT/SYSTEMS" -name "*-*" -type d | grep -v "INTERFACE_MATRIX" | head -5 || true
else
  success "All directories use underscores (no hyphens found)"
fi

# Count total subsystems
info ""
info "Counting subsystems..."
total_subsystems=$(find "$ROOT/SYSTEMS" -type d -path "*/SUBSYSTEMS/*" -not -path "*/SUBSYSTEMS/*/PLM*" | wc -l)
total_plm=$(find "$ROOT/SYSTEMS" -type d -path "*/SUBSYSTEMS/*/PLM" | wc -l)
total_cax=$(find "$ROOT/SYSTEMS" -type d -path "*/SUBSYSTEMS/*/PLM/CAx" | wc -l)
total_ebom=$(find "$ROOT/SYSTEMS" -type f -path "*/SUBSYSTEMS/*/PLM/EBOM_LINKS.md" | wc -l)

success "Total subsystems: $total_subsystems"
success "Total PLM directories: $total_plm"
success "Total CAx directories: $total_cax"
success "Total EBOM_LINKS.md files: $total_ebom"

# Validate that counts match
if [[ $total_subsystems -eq $total_plm && $total_plm -eq $total_cax && $total_cax -eq $total_ebom ]]; then
  success "All subsystems have complete PLM structure"
else
  error "Mismatch in subsystem counts (expected all equal)"
fi

echo ""
echo "=========================================="
echo "Validation Summary"
echo "=========================================="
echo "Errors:   $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

if [[ $ERRORS -gt 0 ]]; then
  error "Validation failed with $ERRORS errors"
  exit 1
elif [[ $WARNINGS -gt 0 ]]; then
  warning "Validation completed with $WARNINGS warnings"
  exit 0
else
  success "Validation passed successfully!"
  exit 0
fi
