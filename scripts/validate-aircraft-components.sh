#!/usr/bin/env bash
set -euo pipefail

# Validation script for aircraft components structure
# Validates compliance with TFA (Threading Functional Architecture) rules at component level
# Checks CAx subdirectories and component-level artifacts

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

info "Validating aircraft components structure in $ROOT"
echo ""

# CAx subdirectories to validate
CAX_DIRS=("CAD" "CAE" "CAO" "CAM" "CAI" "CAV" "CAP" "CAS" "CMP")

# Component counters
total_cax_directories=0
complete_cax_structures=0
cax_with_readme=0

# Individual CAx type counters
declare -A cax_type_counts

for cax_type in "${CAX_DIRS[@]}"; do
  cax_type_counts[$cax_type]=0
done

info "Scanning CAx component directories across all subsystems..."
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
      
      if [[ ! -d "$subsystem_path/PLM/CAx" ]]; then
        continue
      fi
      
      total_cax_directories=$((total_cax_directories + 1))
      
      # Check if README.md exists in CAx
      if [[ -f "$subsystem_path/PLM/CAx/README.md" ]]; then
        cax_with_readme=$((cax_with_readme + 1))
      fi
      
      # Check all CAx subdirectories
      missing_count=0
      for cax_dir in "${CAX_DIRS[@]}"; do
        if [[ -d "$subsystem_path/PLM/CAx/$cax_dir" ]]; then
          cax_type_counts[$cax_dir]=$((${cax_type_counts[$cax_dir]} + 1))
        else
          missing_count=$((missing_count + 1))
        fi
      done
      
      # If all 9 CAx subdirectories exist, it's complete
      if [[ $missing_count -eq 0 ]]; then
        complete_cax_structures=$((complete_cax_structures + 1))
        info "✓ Complete CAx structure: $domain/$system/$subsystem"
      else
        warning "Incomplete CAx structure in $domain/$system/$subsystem (missing $missing_count subdirectories)"
      fi
    done
  done
done

echo ""
info "=========================================="
info "Component Structure Summary"
info "=========================================="
echo ""

success "Total PLM/CAx directories found: $total_cax_directories"
success "Complete CAx structures (all 9 subdirs): $complete_cax_structures"
success "CAx directories with README.md: $cax_with_readme"

echo ""
info "CAx subdirectory breakdown:"
for cax_type in "${CAX_DIRS[@]}"; do
  count=${cax_type_counts[$cax_type]}
  info "  $cax_type: $count directories"
done

echo ""

# Calculate completion percentage
if [[ $total_cax_directories -gt 0 ]]; then
  completion_percentage=$(awk "BEGIN {printf \"%.1f\", ($complete_cax_structures / $total_cax_directories) * 100}")
  info "CAx Structure Completion: $completion_percentage%"
fi

# Identify pilot systems (those with complete CAx structures)
echo ""
info "=========================================="
info "Pilot Systems (Complete CAx Structures)"
info "=========================================="
echo ""

pilot_count=0
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
    
    # Count complete subsystems in this system
    complete_subsystems_in_system=0
    total_subsystems_in_system=0
    
    for subsystem_path in "$system_path/SUBSYSTEMS"/*; do
      if [[ ! -d "$subsystem_path" ]]; then
        continue
      fi
      
      total_subsystems_in_system=$((total_subsystems_in_system + 1))
      
      if [[ ! -d "$subsystem_path/PLM/CAx" ]]; then
        continue
      fi
      
      # Check if all CAx subdirectories exist
      missing_count=0
      for cax_dir in "${CAX_DIRS[@]}"; do
        if [[ ! -d "$subsystem_path/PLM/CAx/$cax_dir" ]]; then
          missing_count=$((missing_count + 1))
        fi
      done
      
      if [[ $missing_count -eq 0 ]]; then
        complete_subsystems_in_system=$((complete_subsystems_in_system + 1))
      fi
    done
    
    # If system has at least one complete subsystem, report it
    if [[ $complete_subsystems_in_system -gt 0 ]]; then
      pilot_count=$((pilot_count + 1))
      success "System: $domain/$system"
      info "  Complete subsystems: $complete_subsystems_in_system / $total_subsystems_in_system"
    fi
  done
done

echo ""
info "Total pilot systems identified: $pilot_count"

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
