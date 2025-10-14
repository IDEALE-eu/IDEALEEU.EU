#!/usr/bin/env bash
set -euo pipefail

# Validation script for aircraft subsystems structure
# Validates compliance with AMPEL360-AIR-T subsystem rules

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
  error "Aircraft root not found: $ROOT"
  exit 1
fi

info "Validating aircraft subsystems structure in $ROOT"
echo ""

# Find and validate all subsystems
info "Validating subsystem structure..."

for domain_path in "$ROOT"/*; do
  if [[ ! -d "$domain_path" || ! -d "$domain_path/SYSTEMS" ]]; then
    continue
  fi
  
  domain=$(basename "$domain_path")
  
  for system_path in "$domain_path/SYSTEMS"/*; do
    if [[ ! -d "$system_path" || ! -d "$system_path/SUBSYSTEMS" ]]; then
      continue
    fi
    
    system=$(basename "$system_path")
    
    for subsystem_path in "$system_path/SUBSYSTEMS"/*; do
      if [[ ! -d "$subsystem_path" ]]; then
        continue
      fi
      
      subsystem=$(basename "$subsystem_path")
      
      # Skip README.md files
      if [[ "$subsystem" == "README.md" ]]; then
        continue
      fi
      
      info "Validating subsystem: $domain/$system/$subsystem"
      
      # Check mandatory subsystem files
      if [[ ! -f "$subsystem_path/META.json" ]]; then
        error "Missing META.json in subsystem $domain/$system/$subsystem"
      else
        # Validate META.json format if jq is available
        if command -v jq &> /dev/null; then
          if ! jq -e '.' "$subsystem_path/META.json" &> /dev/null; then
            error "Invalid JSON in META.json for subsystem $domain/$system/$subsystem"
          else
            success "Valid META.json in $domain/$system/$subsystem"
          fi
        fi
      fi
      
      if [[ ! -f "$subsystem_path/inherit.json" ]]; then
        warning "Missing inherit.json in subsystem $domain/$system/$subsystem"
      fi
      
      if [[ ! -d "$subsystem_path/PLM" ]]; then
        error "Missing PLM/ directory in subsystem $domain/$system/$subsystem"
      else
        # Check for PLM/CAx directory
        if [[ ! -d "$subsystem_path/PLM/CAx" ]]; then
          warning "Missing PLM/CAx/ directory in subsystem $domain/$system/$subsystem"
        fi
        
        # Check for EBOM_LINKS.md
        if [[ ! -f "$subsystem_path/PLM/EBOM_LINKS.md" ]]; then
          warning "Missing PLM/EBOM_LINKS.md in subsystem $domain/$system/$subsystem"
        fi
      fi
      
      if [[ ! -d "$subsystem_path/TRACE" ]]; then
        warning "Missing TRACE/ directory in subsystem $domain/$system/$subsystem"
      fi
    done
  done
done

# Count total subsystems
info ""
info "Counting subsystems..."
total_subsystems=$(find "$ROOT" -type d -path "*/SYSTEMS/*/SUBSYSTEMS/*" -not -path "*/PLM*" -not -path "*/TRACE*" | wc -l)
total_plm=$(find "$ROOT" -type d -path "*/SYSTEMS/*/SUBSYSTEMS/*/PLM" | wc -l)
total_meta=$(find "$ROOT" -type f -path "*/SYSTEMS/*/SUBSYSTEMS/*/META.json" | wc -l)

success "Total subsystems: $total_subsystems"
success "Total PLM directories: $total_plm"
success "Total META.json files: $total_meta"

echo ""
echo "=========================================="
echo "Subsystems Validation Summary"
echo "=========================================="
echo "Errors:   $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

if [[ $ERRORS -gt 0 ]]; then
  error "Subsystems validation failed with $ERRORS errors"
  exit 1
elif [[ $WARNINGS -gt 0 ]]; then
  warning "Subsystems validation completed with $WARNINGS warnings"
  exit 0
else
  success "Subsystems validation passed successfully!"
  exit 0
fi
