#!/usr/bin/env bash
set -euo pipefail

# Validation script for aircraft systems structure
# Validates compliance with TFA (Threading Functional Architecture) rules

ROOT="02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN"
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
  ERRORS=$((ERRORS + 1))
}

warning() {
  echo -e "${YELLOW}⚠ WARNING:${NC} $1"
  WARNINGS=$((WARNINGS + 1))
}

success() {
  echo -e "${GREEN}✓${NC} $1"
}

info() {
  echo -e "${BLUE}ℹ${NC} $1"
}

# Check if aircraft structure exists
if [[ ! -d "$ROOT" ]]; then
  error "Aircraft domain root not found: $ROOT"
  exit 1
fi

info "Validating aircraft systems structure in $ROOT"
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
echo ""

for domain in "${DOMAINS[@]}"; do
  domain_path="$ROOT/$domain"
  
  if [[ ! -d "$domain_path" ]]; then
    warning "Domain not found: $domain"
    continue
  fi
  
  success "Domain exists: $domain"
  
  # Check mandatory SYSTEMS directory
  if [[ ! -d "$domain_path/SYSTEMS" ]]; then
    error "Missing mandatory SYSTEMS/ directory in $domain"
  else
    # Count systems
    system_count=$(find "$domain_path/SYSTEMS" -mindepth 1 -maxdepth 1 -type d | wc -l)
    if [[ $system_count -eq 0 ]]; then
      warning "No systems found in $domain/SYSTEMS/"
    else
      info "$domain has $system_count systems"
    fi
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
    warning "Missing domain-config.yaml in $domain"
  else
    # Validate domain-config.yaml has required rules
    if command -v grep &> /dev/null; then
      if ! grep -q "plm_at_domain_level: false" "$domain_path/domain-config.yaml" 2>/dev/null; then
        warning "domain-config.yaml in $domain should specify plm_at_domain_level: false"
      fi
      if ! grep -q "systems_required: true" "$domain_path/domain-config.yaml" 2>/dev/null; then
        warning "domain-config.yaml in $domain should specify systems_required: true"
      fi
    fi
  fi
  
  # Check that PLM/CAx does NOT exist at domain level (prohibited)
  if [[ -d "$domain_path/PLM/CAx" ]]; then
    error "PROHIBITED: PLM/CAx found at domain level in $domain. PLM/CAx must ONLY exist in SUBSYSTEMS"
  fi
done

echo ""
info "Validating system-level structure..."
echo ""

# Count total systems
total_systems=0
systems_with_interface_matrix=0
systems_with_integration_view=0
systems_with_subsystems=0

for domain in "${DOMAINS[@]}"; do
  domain_path="$ROOT/$domain"
  
  if [[ ! -d "$domain_path/SYSTEMS" ]]; then
    continue
  fi
  
  for system_path in "$domain_path/SYSTEMS"/*; do
    if [[ -d "$system_path" ]]; then
      system=$(basename "$system_path")
      total_systems=$((total_systems + 1))
      
      # Check mandatory system files
      if [[ -f "$system_path/INTEGRATION_VIEW.md" ]]; then
        systems_with_integration_view=$((systems_with_integration_view + 1))
      else
        warning "Missing INTEGRATION_VIEW.md in $domain/SYSTEMS/$system"
      fi
      
      if [[ -d "$system_path/INTERFACE_MATRIX" ]]; then
        systems_with_interface_matrix=$((systems_with_interface_matrix + 1))
        # Check for at least one CSV file
        if ! ls "$system_path/INTERFACE_MATRIX"/*.csv &> /dev/null; then
          warning "No CSV files found in $domain/SYSTEMS/$system/INTERFACE_MATRIX/"
        fi
      else
        warning "Missing INTERFACE_MATRIX/ directory in $domain/SYSTEMS/$system"
      fi
      
      if [[ -d "$system_path/SUBSYSTEMS" ]]; then
        systems_with_subsystems=$((systems_with_subsystems + 1))
      else
        error "Missing SUBSYSTEMS/ directory in $domain/SYSTEMS/$system"
      fi
    fi
  done
done

success "Total systems found: $total_systems"
success "Systems with INTEGRATION_VIEW.md: $systems_with_integration_view"
success "Systems with INTERFACE_MATRIX/: $systems_with_interface_matrix"
success "Systems with SUBSYSTEMS/: $systems_with_subsystems"

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
