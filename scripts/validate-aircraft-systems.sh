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
  echo "ℹ $1"
}

# Check if aircraft structure exists
if [[ ! -d "$ROOT" ]]; then
  error "Aircraft domain root not found: $ROOT"
  exit 1
fi

info "Validating aircraft systems structure in $ROOT"
echo ""

# Get all domains
domains=$(find "$ROOT" -mindepth 1 -maxdepth 1 -type d | sort)
domain_count=$(echo "$domains" | wc -l)

if [[ $domain_count -eq 0 ]]; then
  error "No domains found in $ROOT"
  exit 1
else
  success "Found $domain_count domains"
fi

# Check each domain for SYSTEMS directory
info ""
info "Checking domain structures..."

for domain_path in $domains; do
  domain=$(basename "$domain_path")
  
  # Skip non-domain directories
  if [[ "$domain" == "README.md" || "$domain" == "ATA_DOMAIN_MAPPING.csv" ]]; then
    continue
  fi
  
  info "Checking domain: $domain"
  
  # Check for SYSTEMS directory
  if [[ ! -d "$domain_path/SYSTEMS" ]]; then
    error "Missing SYSTEMS/ directory in domain $domain"
    continue
  fi
  
  success "  SYSTEMS/ directory exists in $domain"
  
  # Count systems in this domain
  system_count=$(find "$domain_path/SYSTEMS" -mindepth 1 -maxdepth 1 -type d | wc -l)
  if [[ $system_count -eq 0 ]]; then
    warning "  No systems found in $domain/SYSTEMS/"
  else
    success "  $domain has $system_count systems"
  fi
  
  # Check each system
  for system_path in "$domain_path/SYSTEMS"/*; do
    if [[ ! -d "$system_path" ]]; then
      continue
    fi
    
    system=$(basename "$system_path")
    
    # Skip non-system directories
    if [[ "$system" == "INTERFACE_MATRIX" || "$system" == "README.md" ]]; then
      continue
    fi
    
    # Check mandatory system files/directories
    if [[ ! -f "$system_path/INTEGRATION_VIEW.md" ]]; then
      warning "  Missing INTEGRATION_VIEW.md in $domain/SYSTEMS/$system"
    fi
    
    if [[ ! -f "$system_path/README.md" ]]; then
      warning "  Missing README.md in $domain/SYSTEMS/$system"
    fi
    
    if [[ ! -d "$system_path/INTERFACE_MATRIX" ]]; then
      warning "  Missing INTERFACE_MATRIX/ directory in $domain/SYSTEMS/$system"
    else
      # Check for at least one CSV file
      csv_count=$(find "$system_path/INTERFACE_MATRIX" -name "*.csv" 2>/dev/null | wc -l)
      if [[ $csv_count -eq 0 ]]; then
        warning "  No CSV files found in $domain/SYSTEMS/$system/INTERFACE_MATRIX/"
      fi
    fi
    
    if [[ ! -d "$system_path/SUBSYSTEMS" ]]; then
      error "  Missing SUBSYSTEMS/ directory in $domain/SYSTEMS/$system"
    else
      # Count subsystems
      subsystem_count=$(find "$system_path/SUBSYSTEMS" -mindepth 1 -maxdepth 1 -type d | wc -l)
      if [[ $subsystem_count -eq 0 ]]; then
        warning "  No subsystems found in $domain/SYSTEMS/$system/SUBSYSTEMS/"
      fi
    fi
  done
done

# Check naming conventions (hyphens vs underscores)
info ""
info "Checking naming conventions..."

# Aircraft uses hyphens in ATA system names, which is different from spacecraft
ata_systems=$(find "$ROOT" -type d -path "*/SYSTEMS/*" | grep -E "/[0-9]{2}-" | wc -l)
if [[ $ata_systems -gt 0 ]]; then
  success "Found $ata_systems ATA-standard system directories (using hyphens as expected)"
else
  warning "No ATA-standard system directories found"
fi

# Count total systems and subsystems
info ""
info "Counting systems and subsystems..."
total_systems=$(find "$ROOT" -type d -path "*/SYSTEMS/*" ! -path "*/SUBSYSTEMS/*" ! -path "*/INTERFACE_MATRIX/*" ! -name "SYSTEMS" | wc -l)
total_subsystems=$(find "$ROOT" -type d -path "*/SUBSYSTEMS/*" -not -path "*/SUBSYSTEMS/*/PLM*" -not -path "*/SUBSYSTEMS/*/TRACE*" -not -name "SUBSYSTEMS" | wc -l)

success "Total systems: $total_systems"
success "Total subsystems: $total_subsystems"

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
