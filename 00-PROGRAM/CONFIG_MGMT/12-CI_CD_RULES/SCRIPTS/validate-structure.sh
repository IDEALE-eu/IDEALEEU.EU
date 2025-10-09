#!/bin/bash
# validate-structure.sh
# Validates directory structure for both aircraft (02-AIRCRAFT) and spacecraft (03-SPACECRAFT) domains
# Checks for required directories, files, and compliance with integration patterns

set -e

REPO_ROOT="/home/runner/work/IDEALEEU.EU/IDEALEEU.EU"
ERRORS=0
WARNINGS=0

# Colors for output
RED='\033[0;31m'
YELLOW='\033[1;33m'
GREEN='\033[0;32m'
NC='\033[0m' # No Color

# Function to log errors
log_error() {
    echo -e "${RED}ERROR: $1${NC}"
    ERRORS=$((ERRORS + 1))
}

# Function to log warnings
log_warning() {
    echo -e "${YELLOW}WARNING: $1${NC}"
    WARNINGS=$((WARNINGS + 1))
}

# Function to log success
log_success() {
    echo -e "${GREEN}✓ $1${NC}"
}

# Function to validate aircraft DOMAIN_INTEGRATION structure
validate_aircraft_domain_integration() {
    echo ""
    echo "Validating 02-AIRCRAFT/DOMAIN_INTEGRATION structure..."
    
    local aircraft_dir="$REPO_ROOT/02-AIRCRAFT/DOMAIN_INTEGRATION"
    
    if [ ! -d "$aircraft_dir" ]; then
        log_warning "02-AIRCRAFT/DOMAIN_INTEGRATION directory not found (optional)"
        return
    fi
    
    log_success "Aircraft DOMAIN_INTEGRATION directory exists"
}

# Function to validate spacecraft DOMAIN_INTEGRATION structure
validate_spacecraft_domain_integration() {
    echo ""
    echo "Validating 03-SPACECRAFT/DOMAIN_INTEGRATION structure..."
    
    local spacecraft_dir="$REPO_ROOT/03-SPACECRAFT/DOMAIN_INTEGRATION"
    
    if [ ! -d "$spacecraft_dir" ]; then
        log_error "03-SPACECRAFT/DOMAIN_INTEGRATION directory not found"
        return
    fi
    
    log_success "Spacecraft DOMAIN_INTEGRATION directory exists"
    
    # Check for README
    if [ ! -f "$spacecraft_dir/README.md" ]; then
        log_error "Missing README.md in 03-SPACECRAFT/DOMAIN_INTEGRATION"
    else
        log_success "DOMAIN_INTEGRATION README.md present"
    fi
    
    # Check for PRODUCTS directory
    if [ ! -d "$spacecraft_dir/PRODUCTS" ]; then
        log_error "Missing PRODUCTS directory in DOMAIN_INTEGRATION"
        return
    fi
    
    log_success "PRODUCTS directory exists"
    
    # Validate each mission/product
    for mission_dir in "$spacecraft_dir/PRODUCTS"/*; do
        if [ -d "$mission_dir" ]; then
            validate_mission_structure "$mission_dir"
        fi
    done
}

# Function to validate mission/product structure
validate_mission_structure() {
    local mission_dir="$1"
    local mission_name=$(basename "$mission_dir")
    
    echo ""
    echo "  Validating mission: $mission_name"
    
    # Skip README files
    if [ "$mission_name" == "README.md" ]; then
        return
    fi
    
    # Check for MODELS directory
    if [ ! -d "$mission_dir/MODELS" ]; then
        log_error "Missing MODELS directory in $mission_name"
        return
    fi
    
    # Validate each configuration model
    for config_dir in "$mission_dir/MODELS"/*; do
        if [ -d "$config_dir" ]; then
            validate_config_structure "$config_dir" "$mission_name"
        fi
    done
}

# Function to validate configuration structure
validate_config_structure() {
    local config_dir="$1"
    local mission_name="$2"
    local config_name=$(basename "$config_dir")
    
    echo "    Validating configuration: $config_name"
    
    # Check for VERSION directory
    if [ ! -d "$config_dir/VERSION" ]; then
        log_error "Missing VERSION directory in $mission_name/$config_name"
        return
    fi
    
    # Validate each version
    for version_dir in "$config_dir/VERSION"/*; do
        if [ -d "$version_dir" ]; then
            validate_version_structure "$version_dir" "$mission_name" "$config_name"
        fi
    done
}

# Function to validate version structure
validate_version_structure() {
    local version_dir="$1"
    local mission_name="$2"
    local config_name="$3"
    local version_name=$(basename "$version_dir")
    
    echo "      Validating version: $version_name"
    
    # Check for SYSTEMS directory
    if [ ! -d "$version_dir/SYSTEMS" ]; then
        log_error "Missing SYSTEMS directory in $mission_name/$config_name/$version_name"
        return
    fi
    
    log_success "SYSTEMS directory exists for $version_name"
    
    # Validate each system
    local systems_count=0
    for system_dir in "$version_dir/SYSTEMS"/*; do
        if [ -d "$system_dir" ]; then
            validate_system_structure "$system_dir" "$version_name"
            systems_count=$((systems_count + 1))
        fi
    done
    
    if [ $systems_count -eq 0 ]; then
        log_warning "No systems found in $version_name"
    else
        log_success "Found $systems_count systems in $version_name"
    fi
}

# Function to validate individual system structure
validate_system_structure() {
    local system_dir="$1"
    local version_name="$2"
    local system_name=$(basename "$system_dir")
    
    # Check if system name follows ATA-XX_NAME pattern
    if [[ ! "$system_name" =~ ^[0-9]{2}-[A-Z_]+$ ]]; then
        log_warning "System $system_name does not follow ATA-XX_NAME pattern"
    fi
    
    # Check for INTEGRATION_VIEW.md
    if [ ! -f "$system_dir/INTEGRATION_VIEW.md" ]; then
        log_error "Missing INTEGRATION_VIEW.md in system $system_name"
    fi
    
    # Check for INTERFACE_MATRIX directory
    if [ ! -d "$system_dir/INTERFACE_MATRIX" ]; then
        log_error "Missing INTERFACE_MATRIX directory in system $system_name"
    else
        # Check for at least one CSV file
        local csv_count=$(find "$system_dir/INTERFACE_MATRIX" -maxdepth 1 -name "*.csv" 2>/dev/null | wc -l)
        if [ $csv_count -eq 0 ]; then
            log_warning "No CSV files found in $system_name/INTERFACE_MATRIX"
        fi
    fi
    
    # Check for SUBSYSTEMS directory
    if [ ! -d "$system_dir/SUBSYSTEMS" ]; then
        log_warning "No SUBSYSTEMS directory in system $system_name (may be intentional)"
    else
        validate_subsystems "$system_dir/SUBSYSTEMS" "$system_name"
    fi
}

# Function to validate subsystems structure
validate_subsystems() {
    local subsystems_dir="$1"
    local system_name="$2"
    
    for subsystem_dir in "$subsystems_dir"/*; do
        if [ -d "$subsystem_dir" ]; then
            validate_subsystem_structure "$subsystem_dir" "$system_name"
        fi
    done
}

# Function to validate individual subsystem structure
validate_subsystem_structure() {
    local subsystem_dir="$1"
    local system_name="$2"
    local subsystem_name=$(basename "$subsystem_dir")
    
    # Check for PLM directory
    if [ ! -d "$subsystem_dir/PLM" ]; then
        log_error "Missing PLM directory in subsystem $subsystem_name of system $system_name"
        return
    fi
    
    # Check for CAx directory under PLM
    if [ ! -d "$subsystem_dir/PLM/CAx" ]; then
        log_error "Missing PLM/CAx directory in subsystem $subsystem_name"
    else
        # Check for CAx subdirectories
        local cax_dirs=("CAD" "CAE" "CAM" "ANALYSIS")
        for cax_dir in "${cax_dirs[@]}"; do
            if [ ! -d "$subsystem_dir/PLM/CAx/$cax_dir" ]; then
                log_warning "Missing PLM/CAx/$cax_dir in subsystem $subsystem_name"
            fi
        done
    fi
    
    # Check for PLM documentation
    if [ ! -f "$subsystem_dir/PLM/README.md" ] && [ ! -f "$subsystem_dir/PLM/EBOM_LINKS.md" ]; then
        log_warning "Missing PLM documentation (README.md or EBOM_LINKS.md) in subsystem $subsystem_name"
    fi
}

# Function to check for PLM artifacts outside of SUBSYSTEMS/*/PLM/CAx/
validate_plm_placement() {
    echo ""
    echo "Validating PLM artifact placement rules..."
    
    local spacecraft_dir="$REPO_ROOT/03-SPACECRAFT/DOMAIN_INTEGRATION"
    
    if [ ! -d "$spacecraft_dir" ]; then
        return
    fi
    
    # Find any directories named CAD, CAE, CAM that are NOT under SUBSYSTEMS/*/PLM/CAx/
    local invalid_plm_paths=$(find "$spacecraft_dir" -type d \( -name "CAD" -o -name "CAE" -o -name "CAM" \) ! -path "*/SUBSYSTEMS/*/PLM/CAx/*" 2>/dev/null)
    
    if [ -n "$invalid_plm_paths" ]; then
        log_error "Found PLM artifacts outside of SUBSYSTEMS/*/PLM/CAx/ structure:"
        echo "$invalid_plm_paths"
    else
        log_success "All PLM artifacts are correctly placed under SUBSYSTEMS/*/PLM/CAx/"
    fi
}

# Function to validate software placement rules
validate_software_placement() {
    echo ""
    echo "Validating software placement rules..."
    
    # Check that software is with host LRU (documented in functional chapters)
    # This is a manual review item - just check for documentation
    
    local spacecraft_dir="$REPO_ROOT/03-SPACECRAFT/DOMAIN_INTEGRATION"
    
    if [ ! -d "$spacecraft_dir" ]; then
        return
    fi
    
    log_success "Software placement rule: SW must be with host LRU in functional chapter"
    echo "  Note: Manual review required to verify SW is documented with host hardware"
}

# Function to validate EWIS placement rules
validate_ewis_placement() {
    echo ""
    echo "Validating EWIS placement rules..."
    
    local spacecraft_dir="$REPO_ROOT/03-SPACECRAFT/DOMAIN_INTEGRATION"
    
    if [ ! -d "$spacecraft_dir" ]; then
        return
    fi
    
    # Check if ATA-92 exists for physical EWIS
    local ewis_system=$(find "$spacecraft_dir" -type d -name "92-*" 2>/dev/null | head -1)
    
    if [ -z "$ewis_system" ]; then
        log_warning "ATA-92 (EWIS/Geometry) system not found - physical EWIS should be in ATA-92"
    else
        log_success "ATA-92 system found for physical EWIS/harness"
    fi
    
    echo "  Note: Other systems should reference ATA-92 for wiring/harness"
}

# Main validation execution
echo "=========================================="
echo "Structure Validation Script"
echo "=========================================="
echo "Repository: $REPO_ROOT"
echo ""

# Validate aircraft domain integration
validate_aircraft_domain_integration

# Validate spacecraft domain integration
validate_spacecraft_domain_integration

# Validate PLM artifact placement
validate_plm_placement

# Validate software placement
validate_software_placement

# Validate EWIS placement
validate_ewis_placement

# Summary
echo ""
echo "=========================================="
echo "Validation Summary"
echo "=========================================="
if [ $ERRORS -eq 0 ] && [ $WARNINGS -eq 0 ]; then
    echo -e "${GREEN}✓ All checks passed!${NC}"
    exit 0
elif [ $ERRORS -eq 0 ]; then
    echo -e "${YELLOW}⚠ Validation completed with $WARNINGS warning(s)${NC}"
    exit 0
else
    echo -e "${RED}✗ Validation failed with $ERRORS error(s) and $WARNINGS warning(s)${NC}"
    exit 1
fi
