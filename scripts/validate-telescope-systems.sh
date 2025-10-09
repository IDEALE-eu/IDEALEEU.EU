#!/usr/bin/env bash
set -euo pipefail

# Validation script for telescope systems structure
# Validates compliance with SPACE-T architecture rules

ROOT="05-TELESCOPES/DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001"
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

# Check if telescope structure exists
if [[ ! -d "$ROOT" ]]; then
  error "Telescope systems root not found: $ROOT"
  exit 1
fi

info "Validating telescope systems structure in $ROOT"
echo ""

# Check mandatory SYSTEMS directory
if [[ ! -d "$ROOT/SYSTEMS" ]]; then
  error "Missing mandatory SYSTEMS/ directory"
  exit 1
else
  success "SYSTEMS/ directory exists"
fi

# Expected systems (STA chapters for telescopes)
EXPECTED_SYSTEMS=(
  "01-INTRO"
  "06-DIMENSIONS_ALIGNMENTS"
  "15-ENVIRONMENT_VIBRATION"
  "21-THERMAL_CONTROL"
  "24-ELECTRICAL_POWER"
  "26-FIRE_SAFETY"
  "30-ICE_DEW_PREVENTION"
  "31-DATA_HANDLING"
  "32-POINTING_STABILIZATION"
  "33-LIGHTS"
  "34-NAVIGATION_ATTITUDE"
  "42-AVIONICS_CONTROL"
  "45-HEALTH_MONITORING"
  "51-PRIMARY_STRUCTURE"
  "52-ACCESS_HATCHES"
  "53-OPTICAL_TUBE_ASSEMBLY"
  "55-SECONDARY_SUPPORT"
  "56-WINDOWS_DOMES"
  "57-INSTRUMENT_BAYS"
  "66-DEPLOYABLE_OPTICS"
  "70-OPTICAL_SUBSYSTEMS"
  "71-INSTRUMENTS_PAYLOADS"
  "72-CRYOGENIC_COOLING"
  "73-FOCUS_ACTUATION"
  "75-THERMAL_RADIATORS"
  "76-MIRROR_CONTROL"
  "77-ALIGNMENT_SENSING"
  "78-BACKPLANE_ELECTRONICS"
  "79-LUBRICATION"
  "80-STARTUP_SEQUENCING"
  "84-PROPULSION"
  "92-EWIS_HARNESS"
  "94-ELECTRONIC_COMPARTMENTS"
  "99-SCIENCE_OPERATIONS"
)

# Validate systems structure
info "Checking systems structure..."
for system in "${EXPECTED_SYSTEMS[@]}"; do
  system_path="$ROOT/SYSTEMS/$system"
  
  if [[ ! -d "$system_path" ]]; then
    error "System not found: $system"
    continue
  fi
  
  # Check mandatory system files
  if [[ ! -f "$system_path/INTEGRATION_VIEW.md" ]]; then
    error "Missing INTEGRATION_VIEW.md in SYSTEMS/$system"
  fi
  
  if [[ ! -d "$system_path/INTERFACE_MATRIX" ]]; then
    error "Missing INTERFACE_MATRIX/ directory in SYSTEMS/$system"
  else
    # Check for at least one CSV file
    if ! ls "$system_path/INTERFACE_MATRIX"/*.csv &> /dev/null; then
      warning "No CSV files found in SYSTEMS/$system/INTERFACE_MATRIX/"
    else
      # Validate CSV header
      for csv_file in "$system_path/INTERFACE_MATRIX"/*.csv; do
        if [[ -f "$csv_file" ]]; then
          first_line=$(head -n 1 "$csv_file")
          expected_header="from_system,to_system,interface_type,icd_ref,signals/measures,thermal,mechanical,electrical,data_bus,harness,sw_api,safety_class,owner,status,notes"
          if [[ "$first_line" != "$expected_header" ]]; then
            error "Invalid CSV header in $(basename "$csv_file"). Expected standard interface matrix header."
          fi
        fi
      done
    fi
  fi
  
  # Check that PLM/CAx does NOT exist at system level (prohibited)
  if [[ -d "$system_path/PLM/CAx" ]]; then
    error "PROHIBITED: PLM/CAx found at system level in $system. PLM/CAx must ONLY exist in SUBSYSTEMS"
  fi
  
  success "System $system validated"
done

# Validate special systems with subsystems
info ""
info "Checking subsystems structure..."

# Validate 70-OPTICAL_SUBSYSTEMS subsystems
OPTICAL_SUBSYSTEMS=(
  "70-10_PRIMARY_MIRROR"
  "70-20_SECONDARY_MIRROR"
  "70-30_TERTIARY_FLAT"
  "70-40_CORRECTORS_LENS"
  "70-50_FILTERS_GRISMS"
  "70-60_DETECTOR_CRYOSTATS"
  "70-70_WAVEFRONT_SENSORS"
  "70-80_CALIBRATION_SOURCES"
)

for subsystem in "${OPTICAL_SUBSYSTEMS[@]}"; do
  subsystem_path="$ROOT/SYSTEMS/70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/$subsystem"
  
  if [[ ! -d "$subsystem_path" ]]; then
    error "Optical subsystem not found: $subsystem"
    continue
  fi
  
  # Check mandatory subsystem directories
  if [[ ! -d "$subsystem_path/PLM/CAx" ]]; then
    error "Missing PLM/CAx/ directory in 70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/$subsystem"
  else
    # Check all CAx subdirectories
    cax_dirs=("CAD" "CAE" "CAM" "CAI" "CAV" "CAP" "CAS" "CMP")
    for cax_dir in "${cax_dirs[@]}"; do
      if [[ ! -d "$subsystem_path/PLM/CAx/$cax_dir" ]]; then
        warning "Missing CAx subdirectory: 70-OPTICAL_SUBSYSTEMS/SUBSYSTEMS/$subsystem/PLM/CAx/$cax_dir"
      fi
    done
    
    success "Optical subsystem $subsystem has PLM/CAx structure"
  fi
  
  # Check mandatory files
  if [[ ! -f "$subsystem_path/README.md" ]]; then
    warning "Missing README.md in subsystem $subsystem"
  fi
  
  if [[ ! -f "$subsystem_path/META.json" ]]; then
    error "Missing META.json in subsystem $subsystem"
  else
    # Validate META.json format
    if command -v jq &> /dev/null; then
      if ! jq -e '.scope == "instance"' "$subsystem_path/META.json" &> /dev/null; then
        error "META.json in subsystem $subsystem must have scope=\"instance\""
      fi
    fi
  fi
  
  if [[ ! -f "$subsystem_path/PLM/EBOM_LINKS.md" ]]; then
    warning "Missing PLM/EBOM_LINKS.md in subsystem $subsystem"
  fi
done

# Validate 71-INSTRUMENTS_PAYLOADS subsystems
INSTRUMENT_SUBSYSTEMS=(
  "71-10_IMAGER"
  "71-20_SPECTROGRAPH"
  "71-30_CORONAGRAPH"
)

for subsystem in "${INSTRUMENT_SUBSYSTEMS[@]}"; do
  subsystem_path="$ROOT/SYSTEMS/71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/$subsystem"
  
  if [[ ! -d "$subsystem_path" ]]; then
    error "Instrument subsystem not found: $subsystem"
    continue
  fi
  
  # Check mandatory subsystem directories
  if [[ ! -d "$subsystem_path/PLM/CAx" ]]; then
    error "Missing PLM/CAx/ directory in 71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/$subsystem"
  else
    # Check all CAx subdirectories
    cax_dirs=("CAD" "CAE" "CAM" "CAI" "CAV" "CAP" "CAS" "CMP")
    for cax_dir in "${cax_dirs[@]}"; do
      if [[ ! -d "$subsystem_path/PLM/CAx/$cax_dir" ]]; then
        warning "Missing CAx subdirectory: 71-INSTRUMENTS_PAYLOADS/SUBSYSTEMS/$subsystem/PLM/CAx/$cax_dir"
      fi
    done
    
    success "Instrument subsystem $subsystem has PLM/CAx structure"
  fi
  
  # Check mandatory files
  if [[ ! -f "$subsystem_path/README.md" ]]; then
    warning "Missing README.md in subsystem $subsystem"
  fi
  
  if [[ ! -f "$subsystem_path/META.json" ]]; then
    error "Missing META.json in subsystem $subsystem"
  else
    # Validate META.json format
    if command -v jq &> /dev/null; then
      if ! jq -e '.scope == "instance"' "$subsystem_path/META.json" &> /dev/null; then
        error "META.json in subsystem $subsystem must have scope=\"instance\""
      fi
    fi
  fi
  
  if [[ ! -f "$subsystem_path/PLM/EBOM_LINKS.md" ]]; then
    warning "Missing PLM/EBOM_LINKS.md in subsystem $subsystem"
  fi
done

# Validate EWIS special rules
info ""
info "Checking EWIS special rules..."
if [[ -d "$ROOT/SYSTEMS/92-EWIS_HARNESS" ]]; then
  success "92-EWIS_HARNESS system exists (centralized wiring location)"
  
  # Check that EWIS has INTERFACE_MATRIX
  if [[ ! -d "$ROOT/SYSTEMS/92-EWIS_HARNESS/INTERFACE_MATRIX" ]]; then
    error "Missing INTERFACE_MATRIX/ in 92-EWIS_HARNESS"
  fi
else
  error "Missing 92-EWIS_HARNESS system (required for centralized wiring)"
fi

echo ""
echo "=========================================="
echo "Validation Summary"
echo "=========================================="
echo "Errors:   $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

if [[ $ERRORS -eq 0 ]]; then
  success "All critical validations passed!"
  if [[ $WARNINGS -gt 0 ]]; then
    echo -e "${YELLOW}Note: There are $WARNINGS warnings that should be addressed.${NC}"
    exit 0
  fi
  exit 0
else
  error "Validation failed with $ERRORS errors"
  exit 1
fi
