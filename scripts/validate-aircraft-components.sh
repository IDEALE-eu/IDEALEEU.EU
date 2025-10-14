#!/usr/bin/env bash
set -Eeuo pipefail

# Validation script for aircraft components structure
# Validates compliance with AMPEL360-AIR-T component and CAx structure rules

: "${TERM:=xterm-256color}"   # color-safe on CI
ROOT="${ROOT:-02-AIRCRAFT/MODEL_IDENTIFICATION/AMPEL360-AIR-T/ARCH/BWB-H2-Hy-E/FAMILY/Q100_STD01/DOMAIN}"
ERRORS=0
WARNINGS=0

# Color codes for output
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

error() {
  echo -e "${RED}✗ ERROR:${NC} $1"
  : $((ERRORS++))
}

warning() {
  echo -e "${YELLOW}⚠ WARNING:${NC} $1"
  : $((WARNINGS++))
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

info "Validating aircraft components and CAx structure in $ROOT"
echo ""

# Expected CAx subdirectories
CAX_DIRS=(
  "CAD"
  "CAE"
  "CAM"
  "CAO"
  "CAP"
  "CAS"
  "CAV"
  "CAI"
  "CMP"
)

# Find and validate all PLM/CAx structures
info "Validating PLM/CAx component structure..."

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
      if [[ ! -d "$subsystem_path" || ! -d "$subsystem_path/PLM" ]]; then
        continue
      fi
      
      subsystem=$(basename "$subsystem_path")
      
      # Skip README.md files
      if [[ "$subsystem" == "README.md" ]]; then
        continue
      fi
      
      plm_path="$subsystem_path/PLM"
      
      # Check if CAx directory exists
      if [[ ! -d "$plm_path/CAx" ]]; then
        warning "Missing CAx directory in $domain/$system/$subsystem/PLM"
        continue
      fi
      
      info "Validating CAx in: $domain/$system/$subsystem"
      
      cax_path="$plm_path/CAx"
      cax_found=0
      
      # Check for CAx subdirectories
      for cax_dir in "${CAX_DIRS[@]}"; do
        if [[ -d "$cax_path/$cax_dir" ]]; then
          ((cax_found++))
          success "Found $cax_dir in $domain/$system/$subsystem"
          
          # Check for README.md in CAx subdirectory
          if [[ ! -f "$cax_path/$cax_dir/README.md" ]]; then
            warning "Missing README.md in $domain/$system/$subsystem/PLM/CAx/$cax_dir"
          fi
        fi
      done
      
      if [[ $cax_found -eq 0 ]]; then
        warning "No CAx subdirectories found in $domain/$system/$subsystem/PLM/CAx"
      fi
      
      # Check for EBOM_LINKS.md
      if [[ ! -f "$plm_path/EBOM_LINKS.md" ]]; then
        warning "Missing EBOM_LINKS.md in $domain/$system/$subsystem/PLM"
      fi
    done
  done
done

# Count component artifacts
info ""
info "Counting component artifacts..."
total_cax=$(find "$ROOT" -type d -path "*/PLM/CAx" | wc -l)
total_cad=$(find "$ROOT" -type d -path "*/PLM/CAx/CAD" | wc -l)
total_cae=$(find "$ROOT" -type d -path "*/PLM/CAx/CAE" | wc -l)
total_cam=$(find "$ROOT" -type d -path "*/PLM/CAx/CAM" | wc -l)
total_readme=$(find "$ROOT" -type f -path "*/PLM/CAx/*/README.md" | wc -l)

success "Total CAx directories: $total_cax"
success "Total CAD directories: $total_cad"
success "Total CAE directories: $total_cae"
success "Total CAM directories: $total_cam"
success "Total CAx README files: $total_readme"

echo ""
echo "=========================================="
echo "Components Validation Summary"
echo "=========================================="
echo "Errors:   $ERRORS"
echo "Warnings: $WARNINGS"
echo ""

# Emit machine-readable JSON summary
mkdir -p out
cat > out/components-validation.json <<EOF
{
  "timestamp": "$(date -u +%Y-%m-%dT%H:%M:%SZ)",
  "validation_type": "components",
  "errors": $ERRORS,
  "warnings": $WARNINGS,
  "total_cax": $total_cax,
  "total_cad": $total_cad,
  "total_cae": $total_cae,
  "total_cam": $total_cam,
  "total_readme": $total_readme,
  "status": "$(if [[ $ERRORS -gt 0 ]]; then echo "failed"; elif [[ $WARNINGS -gt 0 ]]; then echo "warning"; else echo "passed"; fi)"
}
EOF

# Non-blocking: always exit 0 (warnings allowed)
if [[ $ERRORS -gt 0 ]]; then
  error "Components validation found $ERRORS errors (non-blocking)"
elif [[ $WARNINGS -gt 0 ]]; then
  warning "Components validation completed with $WARNINGS warnings"
else
  success "Components validation passed successfully!"
fi
exit 0
