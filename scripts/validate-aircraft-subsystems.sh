#!/usr/bin/env bash
set -euo pipefail

# Validation script for aircraft subsystems structure
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

info "Validating aircraft subsystems structure in $ROOT"
echo ""

# Count total subsystems
total_subsystems=$(find "$ROOT" -type d -path "*/SUBSYSTEMS/*" ! -path "*/SUBSYSTEMS/*/PLM*" ! -path "*/SUBSYSTEMS/*/TRACE*" ! -name "SUBSYSTEMS" ! -name "README.md" | wc -l)

if [[ $total_subsystems -eq 0 ]]; then
  error "No subsystems found in aircraft structure"
  exit 1
else
  success "Found $total_subsystems subsystems to validate"
fi

# Sample a few subsystems from each domain to validate structure
info ""
info "Validating subsystem structure (sampling)..."

# Get all domains
domains=$(find "$ROOT" -mindepth 1 -maxdepth 1 -type d | sort)

checked_subsystems=0
for domain_path in $domains; do
  domain=$(basename "$domain_path")
  
  # Skip non-domain directories
  if [[ "$domain" == "README.md" || "$domain" == "ATA_DOMAIN_MAPPING.csv" ]]; then
    continue
  fi
  
  # Find all subsystems in this domain (sample first 2 per system)
  systems_in_domain=$(find "$domain_path/SYSTEMS" -mindepth 1 -maxdepth 1 -type d 2>/dev/null)
  
  for system_path in $systems_in_domain; do
    system=$(basename "$system_path")
    
    # Skip non-system directories
    if [[ "$system" == "INTERFACE_MATRIX" || "$system" == "README.md" ]]; then
      continue
    fi
    
    if [[ ! -d "$system_path/SUBSYSTEMS" ]]; then
      continue
    fi
    
    # Sample first 2 subsystems from this system
    subsystems=$(find "$system_path/SUBSYSTEMS" -mindepth 1 -maxdepth 1 -type d | head -2)
    
    for subsystem_path in $subsystems; do
      subsystem=$(basename "$subsystem_path")
      
      # Skip non-subsystem directories
      if [[ "$subsystem" == "README.md" ]]; then
        continue
      fi
      
      checked_subsystems=$((checked_subsystems + 1))
      info "Checking subsystem: $domain/$system/$subsystem"
      
      # Check mandatory subsystem directories
      if [[ ! -d "$subsystem_path/PLM" ]]; then
        error "  Missing PLM/ directory in $domain/$system/SUBSYSTEMS/$subsystem"
      else
        success "  PLM/ directory exists"
        
        # Check PLM/CAx structure
        if [[ ! -d "$subsystem_path/PLM/CAx" ]]; then
          error "  Missing PLM/CAx/ directory in $domain/$system/SUBSYSTEMS/$subsystem"
        else
          # Check all CAx subdirectories
          cax_dirs=("CAD" "CAE" "CAO" "CAM" "CAI" "CAV" "CAS" "CMP")
          missing_cax=0
          for cax_dir in "${cax_dirs[@]}"; do
            if [[ ! -d "$subsystem_path/PLM/CAx/$cax_dir" ]]; then
              warning "  Missing CAx subdirectory: $cax_dir"
              missing_cax=$((missing_cax + 1))
            fi
          done
          
          if [[ $missing_cax -eq 0 ]]; then
            success "  Complete PLM/CAx structure (all 8 CAx subdirectories present)"
          elif [[ $missing_cax -lt 8 ]]; then
            warning "  Incomplete PLM/CAx structure ($missing_cax CAx subdirectories missing)"
          else
            error "  No CAx subdirectories found"
          fi
        fi
        
        # Check for EBOM_LINKS.md
        if [[ ! -f "$subsystem_path/PLM/EBOM_LINKS.md" ]]; then
          warning "  Missing PLM/EBOM_LINKS.md in subsystem $subsystem"
        else
          success "  PLM/EBOM_LINKS.md exists"
        fi
      fi
      
      # Check for TRACE directory
      if [[ ! -d "$subsystem_path/TRACE" ]]; then
        warning "  Missing TRACE/ directory in $domain/$system/SUBSYSTEMS/$subsystem"
      fi
      
      echo ""
    done
  done
done

# Validate PLM structure counts across all subsystems
info ""
info "Validating PLM structure completeness..."

total_plm=$(find "$ROOT" -type d -path "*/SUBSYSTEMS/*/PLM" | wc -l)
total_cax=$(find "$ROOT" -type d -path "*/SUBSYSTEMS/*/PLM/CAx" | wc -l)
total_ebom=$(find "$ROOT" -type f -path "*/SUBSYSTEMS/*/PLM/EBOM_LINKS.md" | wc -l)

success "Total PLM directories: $total_plm"
success "Total CAx directories: $total_cax"
success "Total EBOM_LINKS.md files: $total_ebom"

# Calculate coverage percentage
if [[ $total_subsystems -gt 0 ]]; then
  plm_coverage=$(( (total_plm * 100) / total_subsystems ))
  cax_coverage=$(( (total_cax * 100) / total_subsystems ))
  ebom_coverage=$(( (total_ebom * 100) / total_subsystems ))
  
  info "PLM coverage: $plm_coverage%"
  info "CAx coverage: $cax_coverage%"
  info "EBOM coverage: $ebom_coverage%"
  
  if [[ $plm_coverage -lt 90 ]]; then
    warning "PLM coverage is below 90%"
  fi
  if [[ $cax_coverage -lt 90 ]]; then
    warning "CAx coverage is below 90%"
  fi
  if [[ $ebom_coverage -lt 90 ]]; then
    warning "EBOM coverage is below 90%"
  fi
fi

echo ""
echo "=========================================="
echo "Validation Summary"
echo "=========================================="
echo "Total subsystems: $total_subsystems"
echo "Checked subsystems (sample): $checked_subsystems"
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
