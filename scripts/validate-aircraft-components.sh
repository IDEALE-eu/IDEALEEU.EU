#!/usr/bin/env bash
set -euo pipefail

# Validation script for aircraft components structure
# Validates compliance with AMPEL360-AIR-T TFA (Technical Functional Architecture) rules

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

info "Validating aircraft components structure (TFA) in $ROOT"
echo ""

# Get all domains
domains=$(find "$ROOT" -mindepth 1 -maxdepth 1 -type d | sort)

# Track systems with and without component structure
systems_with_conf=0
systems_without_conf=0
systems_with_components=0
total_components=0

info "Checking for component configuration structure (CONF/BASELINE/COMPONENTS)..."
echo ""

for domain_path in $domains; do
  domain=$(basename "$domain_path")
  
  # Skip non-domain directories
  if [[ "$domain" == "README.md" || "$domain" == "ATA_DOMAIN_MAPPING.csv" ]]; then
    continue
  fi
  
  if [[ ! -d "$domain_path/SYSTEMS" ]]; then
    continue
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
    
    # Check for CONF directory
    if [[ -d "$system_path/CONF" ]]; then
      systems_with_conf=$((systems_with_conf + 1))
      
      # Check for BASELINE/COMPONENTS structure
      if [[ -d "$system_path/CONF/BASELINE/COMPONENTS" ]]; then
        systems_with_components=$((systems_with_components + 1))
        
        # Count components in this system
        component_count=$(find "$system_path/CONF/BASELINE/COMPONENTS" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l)
        if [[ $component_count -gt 0 ]]; then
          total_components=$((total_components + component_count))
          info "✓ $domain/$system has $component_count components"
          
          # Sample first component to validate structure
          first_component=$(find "$system_path/CONF/BASELINE/COMPONENTS" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | head -1)
          if [[ -n "$first_component" ]]; then
            component=$(basename "$first_component")
            
            # Check for SUBPRODUCT structure
            if [[ ! -d "$first_component/SUBPRODUCT" ]]; then
              warning "  Component $component missing SUBPRODUCT/ directory"
            else
              # Check for subproduct directories
              subproduct_count=$(find "$first_component/SUBPRODUCT" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | wc -l)
              if [[ $subproduct_count -gt 0 ]]; then
                success "  Component $component has $subproduct_count subproducts"
                
                # Sample first subproduct
                first_subproduct=$(find "$first_component/SUBPRODUCT" -mindepth 1 -maxdepth 1 -type d 2>/dev/null | head -1)
                if [[ -n "$first_subproduct" ]]; then
                  # Check for required files
                  if [[ ! -f "$first_component/SUBPRODUCT_INDEX.csv" ]]; then
                    warning "  Missing SUBPRODUCT_INDEX.csv"
                  fi
                  
                  # Check for SUBJECT structure
                  if [[ ! -d "$first_subproduct/SUBJECT" ]]; then
                    warning "  Missing SUBJECT/ directory in subproduct"
                  fi
                fi
              else
                warning "  Component $component has no subproducts"
              fi
            fi
          fi
        else
          warning "  $domain/$system CONF/BASELINE/COMPONENTS exists but is empty"
        fi
      else
        warning "  $domain/$system has CONF/ but missing BASELINE/COMPONENTS structure"
      fi
    else
      systems_without_conf=$((systems_without_conf + 1))
    fi
  done
done

# Count ATA chapters (these should have component definitions)
info ""
info "Analyzing ATA chapter coverage..."

total_ata_systems=$(find "$ROOT" -type d -path "*/SYSTEMS/*" | grep -E "/[0-9]{2}-" | wc -l)
ata_with_conf=$(find "$ROOT" -type d -path "*/SYSTEMS/[0-9][0-9]-*/CONF" 2>/dev/null | wc -l)

info "Total ATA systems: $total_ata_systems"
info "ATA systems with CONF: $ata_with_conf"

if [[ $ata_with_conf -eq 0 ]]; then
  error "No ATA systems have component configuration (CONF) structure"
elif [[ $ata_with_conf -lt $((total_ata_systems / 2)) ]]; then
  warning "Less than 50% of ATA systems have component configuration"
fi

echo ""
echo "=========================================="
echo "Validation Summary"
echo "=========================================="
echo "Systems with CONF: $systems_with_conf"
echo "Systems without CONF: $systems_without_conf"
echo "Systems with components: $systems_with_components"
echo "Total components defined: $total_components"
echo "Errors:   $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

# Provide recommendation
if [[ $total_components -eq 0 ]]; then
  echo "=========================================="
  echo "RECOMMENDATION"
  echo "=========================================="
  error "No component structure found in aircraft systems"
  echo ""
  echo "The aircraft systems lack component configuration structure."
  echo "Expected structure: DOMAIN/{ATA_CHAPTER}/SYSTEMS/{ATA_MID}/CONF/BASELINE/COMPONENTS/{COMP}/SUBPRODUCT/{SUBPROD_ID}"
  echo ""
  echo "To create component structure, use:"
  echo "  cd 02-AIRCRAFT/MODEL_IDENTIFICATION"
  echo "  make add-item DOMAIN=<domain> ATA_CHAPTER=<chapter> ATA_MID=<system> COMP=<component> ..."
  echo ""
  echo "See CORRECTIVE_ACTION_PLAN.md for detailed guidance."
  echo ""
fi

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
