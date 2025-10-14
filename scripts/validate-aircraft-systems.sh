#!/usr/bin/env bash
set -euo pipefail

# Validation script for aircraft systems structure
# Validates compliance with AMPEL360-AIR-T architecture rules

ROOT="02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN"
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

# Check if aircraft structure exists
if [[ ! -d "$ROOT" ]]; then
  error "Aircraft systems root not found: $ROOT"
  exit 1
fi

info "Validating aircraft systems structure in $ROOT"
echo ""

# Expected domains
DOMAINS=(
  "AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS"
  "AAP-AIRPORT-ADAPTABLE-PLATFORMS"
  "CCC-COCKPIT-CABIN-CARGO"
  "CQH-CRYOGENICS-QUANTUM-H2"
  "DDD-DRAINAGE-DEHUMIDIFICATION-DRYING"
  "EDI-ELECTRONICS-DIGITAL-INSTRUMENTS"
  "EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION"
  "EER-ENVIRONMENTAL-EMISSIONS-REMEDIATION"
  "IIF-INDUSTRIAL-INFRASTRUCTURE-FACILITIES"
  "IIS-INFORMATION-INTELLIGENCE-SYSTEMS"
  "LCC-LINKAGES-CONTROL-COMMUNICATIONS"
  "LIB-LOGISTICS-INVENTORY-BLOCKCHAIN"
  "MEC-MECHANICAL-SYSTEMS-MODULES"
  "OOO-OS-ONTOLOGIES-OFFICE"
  "PPP-PROPULSION-FUEL-SYSTEMS"
)

info "Checking domain structure..."
for domain in "${DOMAINS[@]}"; do
  domain_path="$ROOT/$domain"
  if [[ ! -d "$domain_path" ]]; then
    error "Missing domain: $domain"
  else
    success "Domain exists: $domain"
    
    # Check if domain has SYSTEMS directory
    if [[ ! -d "$domain_path/SYSTEMS" ]]; then
      warning "Domain $domain has no SYSTEMS directory"
    else
      # Count systems in domain
      system_count=$(find "$domain_path/SYSTEMS" -mindepth 1 -maxdepth 1 -type d | wc -l)
      if [[ $system_count -eq 0 ]]; then
        warning "No systems found in $domain/SYSTEMS/"
      else
        success "$domain has $system_count systems"
        
        # Validate each system has mandatory files
        for system_path in "$domain_path/SYSTEMS"/*; do
          if [[ -d "$system_path" ]]; then
            system=$(basename "$system_path")
            
            # Check mandatory system files/directories
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
            fi
          fi
        done
      fi
    fi
  fi
done

echo ""
echo "=========================================="
echo "Systems Validation Summary"
echo "=========================================="
echo "Errors:   $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

if [[ $ERRORS -gt 0 ]]; then
  error "Systems validation failed with $ERRORS errors"
  exit 1
elif [[ $WARNINGS -gt 0 ]]; then
  warning "Systems validation completed with $WARNINGS warnings"
  exit 0
else
  success "Systems validation passed successfully!"
  exit 0
fi
