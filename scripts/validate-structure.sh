#!/usr/bin/env bash
set -euo pipefail

# Validation script for domain integration structure
# Validates compliance with domain integration rules defined in Q100/README.md

ROOT="02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB-H2-Hy-E/CONF/VERSION/Q100/DOMAINS"
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

# Check if domain structure exists
if [[ ! -d "$ROOT" ]]; then
  error "Domain integration root not found: $ROOT"
  exit 1
fi

info "Validating domain integration structure in $ROOT"
echo ""

# Expected domains
DOMAINS=(
  "AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS"
  "PPP-PROPULSION-FUEL-SYSTEMS"
  "MEC-MECHANICAL-SYSTEMS-MODULES"
  "LCC-LINKAGES-CONTROL-COMMUNICATIONS"
  "EDI-ELECTRONICS-DIGITAL-INSTRUMENTS"
  "EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION"
  "EER-ENVIRONMENTAL-EMISSIONS-REMEDIATION"
  "DDD-DRAINAGE-DEHUMIDIFICATION-DRYING"
  "CCC-COCKPIT-CABIN-CARGO"
  "IIS-INFORMATION-INTELLIGENCE-SYSTEMS"
  "LIB-LOGISTICS-INVENTORY-BLOCKCHAIN"
  "AAP-AIRPORT-ADAPTABLE-PLATFORMS"
  "CQH-CRYOGENICS-QUANTUM-H2"
  "IIF-INDUSTRIAL-INFRASTRUCTURE-FACILITIES"
  "OOO-OS-ONTOLOGIES-OFFICE"
)

# Validate domain structure
info "Checking domain structure..."
for domain in "${DOMAINS[@]}"; do
  domain_path="$ROOT/$domain"
  
  if [[ ! -d "$domain_path" ]]; then
    warning "Domain not found: $domain"
    continue
  fi
  
  # Check mandatory SYSTEMS directory
  if [[ ! -d "$domain_path/SYSTEMS" ]]; then
    error "Missing mandatory SYSTEMS/ directory in $domain"
  else
    success "Domain $domain has SYSTEMS/ directory"
  fi
  
  # Check mandatory files
  if [[ ! -f "$domain_path/README.md" ]]; then
    error "Missing README.md in $domain"
  fi
  
  if [[ ! -f "$domain_path/META.json" ]]; then
    error "Missing META.json in $domain"
  else
    # Validate META.json format
    if command -v jq &> /dev/null; then
      if ! jq -e '.scope == "domain"' "$domain_path/META.json" &> /dev/null; then
        error "META.json in $domain must have scope=\"domain\""
      fi
    fi
  fi
  
  if [[ ! -f "$domain_path/domain-config.yaml" ]]; then
    error "Missing domain-config.yaml in $domain"
  else
    # Validate domain-config.yaml has required rules
    if command -v grep &> /dev/null; then
      if ! grep -q "plm_at_domain_level: false" "$domain_path/domain-config.yaml"; then
        error "domain-config.yaml in $domain must specify plm_at_domain_level: false"
      fi
      if ! grep -q "systems_required: true" "$domain_path/domain-config.yaml"; then
        error "domain-config.yaml in $domain must specify systems_required: true"
      fi
    fi
  fi
  
  # Check for mandatory domain-level directories
  for dir in "DELs/TEMPLATES" "DELs/SCHEMAS" "PAx/STANDARDS" "QUANTUM_OA/PATTERNS" "SUPPLIERS/CRITERIA" "policy" "tests"; do
    if [[ ! -d "$domain_path/$dir" ]]; then
      warning "Missing recommended directory: $domain/$dir"
    fi
  done
  
  # Check that PLM/CAx does NOT exist at domain level (prohibited)
  if [[ -d "$domain_path/PLM/CAx" ]]; then
    error "PROHIBITED: PLM/CAx found at domain level in $domain. PLM/CAx must ONLY exist in SUBSYSTEMS"
  fi
  
  # Validate SYSTEMS structure
  if [[ -d "$domain_path/SYSTEMS" ]]; then
    for system_path in "$domain_path/SYSTEMS"/*; do
      if [[ -d "$system_path" ]]; then
        system=$(basename "$system_path")
        
        # Check mandatory system files
        if [[ ! -f "$system_path/INTEGRATION_VIEW.md" ]]; then
          error "Missing INTEGRATION_VIEW.md in $domain/SYSTEMS/$system"
        fi
        
        if [[ ! -d "$system_path/INTERFACE_MATRIX" ]]; then
          error "Missing INTERFACE_MATRIX/ directory in $domain/SYSTEMS/$system"
        else
          # Check for at least one CSV file
          if ! ls "$system_path/INTERFACE_MATRIX"/*.csv &> /dev/null; then
            warning "No CSV files found in $domain/SYSTEMS/$system/INTERFACE_MATRIX/"
          fi
        fi
        
        if [[ ! -d "$system_path/SUBSYSTEMS" ]]; then
          error "Missing SUBSYSTEMS/ directory in $domain/SYSTEMS/$system"
        else
          # Validate SUBSYSTEMS structure
          for subsystem_path in "$system_path/SUBSYSTEMS"/*; do
            if [[ -d "$subsystem_path" ]]; then
              subsystem=$(basename "$subsystem_path")
              
              # Check mandatory subsystem directories
              if [[ ! -d "$subsystem_path/PLM/CAx" ]]; then
                error "Missing PLM/CAx/ directory in $domain/SYSTEMS/$system/SUBSYSTEMS/$subsystem"
              else
                # Check all CAx subdirectories
                cax_dirs=("CAD" "CAE" "CAO" "CAM" "CAI" "CAV" "CAP" "CAS" "CMP")
                for cax_dir in "${cax_dirs[@]}"; do
                  if [[ ! -d "$subsystem_path/PLM/CAx/$cax_dir" ]]; then
                    warning "Missing CAx subdirectory: $domain/SYSTEMS/$system/SUBSYSTEMS/$subsystem/PLM/CAx/$cax_dir"
                  fi
                done
                
                success "Subsystem $subsystem has PLM/CAx structure"
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
              
              if [[ ! -f "$subsystem_path/inherit.json" ]]; then
                warning "Missing inherit.json in subsystem $subsystem"
              fi
              
              if [[ ! -f "$subsystem_path/PLM/EBOM_LINKS.md" ]]; then
                warning "Missing PLM/EBOM_LINKS.md in subsystem $subsystem"
              fi
            fi
          done
        fi
      fi
    done
  fi
done

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
