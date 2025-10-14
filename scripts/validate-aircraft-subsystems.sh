#!/usr/bin/env bash
set -euo pipefail

# Validation script for aircraft subsystems structure
# Validates compliance with TFA (Threading Functional Architecture) rules at subsystem level

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

info "Validating aircraft subsystems structure in $ROOT"
echo ""

# Count subsystems
total_subsystems=0
subsystems_with_plm=0
subsystems_with_cax=0
subsystems_with_ebom=0
subsystems_with_meta=0
subsystems_with_readme=0
subsystems_with_inherit=0

info "Scanning all subsystems across all domains..."
echo ""

for domain_path in "$ROOT"/*; do
  if [[ ! -d "$domain_path" ]]; then
    continue
  fi
  
  domain=$(basename "$domain_path")
  
  if [[ ! -d "$domain_path/SYSTEMS" ]]; then
    continue
  fi
  
  for system_path in "$domain_path/SYSTEMS"/*; do
    if [[ ! -d "$system_path" ]]; then
      continue
    fi
    
    system=$(basename "$system_path")
    
    if [[ ! -d "$system_path/SUBSYSTEMS" ]]; then
      continue
    fi
    
    for subsystem_path in "$system_path/SUBSYSTEMS"/*; do
      if [[ ! -d "$subsystem_path" ]]; then
        continue
      fi
      
      subsystem=$(basename "$subsystem_path")
      total_subsystems=$((total_subsystems + 1))
      
      # Check mandatory subsystem files
      if [[ -f "$subsystem_path/README.md" ]]; then
        subsystems_with_readme=$((subsystems_with_readme + 1))
      else
        warning "Missing README.md in $domain/$system/$subsystem"
      fi
      
      if [[ -f "$subsystem_path/META.json" ]]; then
        subsystems_with_meta=$((subsystems_with_meta + 1))
        # Validate META.json format
        if command -v jq &> /dev/null; then
          if ! jq -e '.scope == "instance"' "$subsystem_path/META.json" &> /dev/null; then
            error "META.json in $domain/$system/$subsystem must have scope=\"instance\""
          fi
        fi
      else
        error "Missing META.json in $domain/$system/$subsystem"
      fi
      
      if [[ -f "$subsystem_path/inherit.json" ]]; then
        subsystems_with_inherit=$((subsystems_with_inherit + 1))
      else
        warning "Missing inherit.json in $domain/$system/$subsystem"
      fi
      
      # Check mandatory PLM directory
      if [[ -d "$subsystem_path/PLM" ]]; then
        subsystems_with_plm=$((subsystems_with_plm + 1))
      else
        error "Missing PLM/ directory in $domain/$system/$subsystem"
      fi
      
      # Check PLM/CAx directory
      if [[ -d "$subsystem_path/PLM/CAx" ]]; then
        subsystems_with_cax=$((subsystems_with_cax + 1))
        
        # Check all CAx subdirectories
        cax_dirs=("CAD" "CAE" "CAO" "CAM" "CAI" "CAV" "CAP" "CAS" "CMP")
        missing_cax=0
        for cax_dir in "${cax_dirs[@]}"; do
          if [[ ! -d "$subsystem_path/PLM/CAx/$cax_dir" ]]; then
            missing_cax=$((missing_cax + 1))
          fi
        done
        
        if [[ $missing_cax -eq 0 ]]; then
          # Only show success for complete CAx structures
          info "✓ $domain/$system/$subsystem has complete PLM/CAx structure"
        else
          warning "PLM/CAx in $domain/$system/$subsystem is missing $missing_cax subdirectories"
        fi
      else
        warning "Missing PLM/CAx/ directory in $domain/$system/$subsystem"
      fi
      
      # Check EBOM_LINKS.md
      if [[ -f "$subsystem_path/PLM/EBOM_LINKS.md" ]]; then
        subsystems_with_ebom=$((subsystems_with_ebom + 1))
      else
        warning "Missing PLM/EBOM_LINKS.md in $domain/$system/$subsystem"
      fi
    done
  done
done

echo ""
info "=========================================="
info "Subsystem Structure Summary"
info "=========================================="
echo ""

success "Total subsystems: $total_subsystems"
success "Subsystems with README.md: $subsystems_with_readme"
success "Subsystems with META.json: $subsystems_with_meta"
success "Subsystems with inherit.json: $subsystems_with_inherit"
success "Subsystems with PLM/: $subsystems_with_plm"
success "Subsystems with PLM/CAx/: $subsystems_with_cax"
success "Subsystems with PLM/EBOM_LINKS.md: $subsystems_with_ebom"

echo ""

# Check if all subsystems have complete PLM structure
if [[ $total_subsystems -eq $subsystems_with_plm ]] && \
   [[ $subsystems_with_plm -eq $subsystems_with_cax ]] && \
   [[ $subsystems_with_cax -eq $subsystems_with_ebom ]]; then
  success "All subsystems have complete PLM structure (PLM/CAx/EBOM)"
else
  warning "Not all subsystems have complete PLM structure"
  info "Expected: $total_subsystems subsystems with PLM, CAx, and EBOM"
  info "Found: PLM=$subsystems_with_plm, CAx=$subsystems_with_cax, EBOM=$subsystems_with_ebom"
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
