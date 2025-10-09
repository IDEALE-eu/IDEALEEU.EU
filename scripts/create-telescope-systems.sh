#!/usr/bin/env bash
set -euo pipefail

# Create telescope systems structure following SPACE-T (STA) architecture
# Based on the unified structure with SYSTEMS/, SUBSYSTEMS/, and PLM/CAx only in subsystems

ROOT="05-TELESCOPES/DOMAIN_INTEGRATION/PRODUCTS/SPACE-TELESCOPE/MODELS/BASELINE/VERSION/V001"

# Ensure base directory exists
mkdir -p "$ROOT/SYSTEMS"

# CSV header template for interface matrices
CSV_HEADER="from_system,to_system,interface_type,icd_ref,signals/measures,thermal,mechanical,electrical,data_bus,harness,sw_api,safety_class,owner,status,notes"

# Integration view template
INTEGRATION_VIEW_TEMPLATE='# Integration View — %s
**Scope:** Roles, boundaries, modes  
**Key Interfaces:** Link to `INTERFACE_MATRIX/*.csv` and ICDs in `../../../../../00-PROGRAM/CONFIG_MGMT/09-INTERFACES/`  
**Budgets:** Power/thermal/mass (refs to 24/21/51/…)  
**Controls & States:** Commands, telemetry, safing, startup/shutdown  
**Verification:** HIL/SIL, alignment/thermal tests, acceptance criteria
'

# Helper function to create a system with interface matrix
mk_system() {
  local sys_num="$1"
  local sys_name="$2"
  local interface_partners="$3"
  
  local sys_dir="$ROOT/SYSTEMS/${sys_num}-${sys_name}"
  
  mkdir -p "$sys_dir/INTERFACE_MATRIX"
  
  # Create INTEGRATION_VIEW.md
  if [[ ! -f "$sys_dir/INTEGRATION_VIEW.md" ]]; then
    printf "$INTEGRATION_VIEW_TEMPLATE" "${sys_num}-${sys_name}" > "$sys_dir/INTEGRATION_VIEW.md"
  fi
  
  # Create interface matrix CSV
  local csv_file="$sys_dir/INTERFACE_MATRIX/${sys_num}↔${interface_partners}.csv"
  if [[ ! -f "$csv_file" ]]; then
    echo "$CSV_HEADER" > "$csv_file"
  fi
}

# Helper function to create a subsystem with full PLM/CAx structure
mk_subsystem() {
  local sys_num="$1"
  local sys_name="$2"
  local sub_num="$3"
  local sub_name="$4"
  
  local sys_dir="$ROOT/SYSTEMS/${sys_num}-${sys_name}"
  local sub_dir="$sys_dir/SUBSYSTEMS/${sys_num}-${sub_num}_${sub_name}"
  
  # Create SUBSYSTEMS directory if it doesn't exist
  mkdir -p "$sys_dir/SUBSYSTEMS"
  
  # Create full subsystem structure with PLM/CAx
  mkdir -p "$sub_dir/PLM/CAx"/{CAD,CAE,CAM,CAI,CAV,CAP,CAS,CMP}
  mkdir -p "$sub_dir/DELs"
  mkdir -p "$sub_dir/PAx"
  mkdir -p "$sub_dir/SUPPLIERS"
  mkdir -p "$sub_dir/policy"
  mkdir -p "$sub_dir/tests"
  
  # Create README.md
  if [[ ! -f "$sub_dir/README.md" ]]; then
    cat > "$sub_dir/README.md" <<EOF
# ${sys_num}-${sub_num}_${sub_name}

## Description
Subsystem component of ${sys_num}-${sys_name}

## PLM/CAx
Engineering artifacts and models are maintained in PLM/CAx subdirectories.

## References
- EBOM links: see PLM/EBOM_LINKS.md
- Parent system: ../ 
EOF
  fi
  
  # Create PLM/EBOM_LINKS.md
  if [[ ! -f "$sub_dir/PLM/EBOM_LINKS.md" ]]; then
    cat > "$sub_dir/PLM/EBOM_LINKS.md" <<EOF
# EBOM Links

## Part Numbers
- Main assembly: TBD
- Configuration: TBD

## Traceability
- Requirements: TBD
- Verification: TBD
EOF
  fi
  
  # Create META.json
  if [[ ! -f "$sub_dir/META.json" ]]; then
    cat > "$sub_dir/META.json" <<EOF
{
  "scope": "instance",
  "product": "SPACE-TELESCOPE",
  "model": "BASELINE",
  "version": "V001",
  "subsystem": "${sys_num}-${sub_num}_${sub_name}"
}
EOF
  fi
}

echo "Creating telescope systems structure..."

# Create all systems according to the problem statement

# 01-INTRO
mk_system "01" "INTRO" "ALL"

# 06-DIMENSIONS_ALIGNMENTS
mk_system "06" "DIMENSIONS_ALIGNMENTS" "51_53_55_57_70_32"

# 15-ENVIRONMENT_VIBRATION
mk_system "15" "ENVIRONMENT_VIBRATION" "21_51_53_70_72_75"

# 21-THERMAL_CONTROL
mk_system "21" "THERMAL_CONTROL" "30_72_75_70_71_24_53_55_57"

# 24-ELECTRICAL_POWER
mk_system "24" "ELECTRICAL_POWER" "71_72_73_76_78_42_31_33_92"

# 26-FIRE_SAFETY
mk_system "26" "FIRE_SAFETY" "21_24_42_92"

# 30-ICE_DEW_PREVENTION
mk_system "30" "ICE_DEW_PREVENTION" "21_24_53_56"

# 31-DATA_HANDLING
mk_system "31" "DATA_HANDLING" "24_42_71_32_77_99"

# 32-POINTING_STABILIZATION
mk_system "32" "POINTING_STABILIZATION" "34_24_70_76_45_21_92"

# 33-LIGHTS
mk_system "33" "LIGHTS" "70_71_24_31"

# 34-NAVIGATION_ATTITUDE
mk_system "34" "NAVIGATION_ATTITUDE" "32_42_31_24"

# 42-AVIONICS_CONTROL
mk_system "42" "AVIONICS_CONTROL" "31_24_32_34_71_45_70_92"

# 45-HEALTH_MONITORING
mk_system "45" "HEALTH_MONITORING" "70_71_32_24_31_42"

# 51-PRIMARY_STRUCTURE
mk_system "51" "PRIMARY_STRUCTURE" "53_55_57_21_70_71_92"

# 52-ACCESS_HATCHES
mk_system "52" "ACCESS_HATCHES" "53_21_24_92"

# 53-OPTICAL_TUBE_ASSEMBLY
mk_system "53" "OPTICAL_TUBE_ASSEMBLY" "51_55_57_21_70_92"

# 55-SECONDARY_SUPPORT
mk_system "55" "SECONDARY_SUPPORT" "53_51_70_73_76"

# 56-WINDOWS_DOMES
mk_system "56" "WINDOWS_DOMES" "30_53_21_24"

# 57-INSTRUMENT_BAYS
mk_system "57" "INSTRUMENT_BAYS" "71_70_21_24_92"

# 66-DEPLOYABLE_OPTICS
mk_system "66" "DEPLOYABLE_OPTICS" "57_53_55_21_24_92"

# 70-OPTICAL_SUBSYSTEMS (custom optics block with subsystems)
mk_system "70" "OPTICAL_SUBSYSTEMS" "21_32_45_51_55_57"
mk_subsystem "70" "OPTICAL_SUBSYSTEMS" "10" "PRIMARY_MIRROR"
mk_subsystem "70" "OPTICAL_SUBSYSTEMS" "20" "SECONDARY_MIRROR"
mk_subsystem "70" "OPTICAL_SUBSYSTEMS" "30" "TERTIARY_FLAT"
mk_subsystem "70" "OPTICAL_SUBSYSTEMS" "40" "CORRECTORS_LENS"
mk_subsystem "70" "OPTICAL_SUBSYSTEMS" "50" "FILTERS_GRISMS"
mk_subsystem "70" "OPTICAL_SUBSYSTEMS" "60" "DETECTOR_CRYOSTATS"
mk_subsystem "70" "OPTICAL_SUBSYSTEMS" "70" "WAVEFRONT_SENSORS"
mk_subsystem "70" "OPTICAL_SUBSYSTEMS" "80" "CALIBRATION_SOURCES"

# 71-INSTRUMENTS_PAYLOADS (with subsystems)
mk_system "71" "INSTRUMENTS_PAYLOADS" "24_31_70_57"
mk_subsystem "71" "INSTRUMENTS_PAYLOADS" "10" "IMAGER"
mk_subsystem "71" "INSTRUMENTS_PAYLOADS" "20" "SPECTROGRAPH"
mk_subsystem "71" "INSTRUMENTS_PAYLOADS" "30" "CORONAGRAPH"

# 72-CRYOGENIC_COOLING
mk_system "72" "CRYOGENIC_COOLING" "21_24_70_71_75_92"

# 73-FOCUS_ACTUATION
mk_system "73" "FOCUS_ACTUATION" "24_70_32_42_45_92"

# 75-THERMAL_RADIATORS
mk_system "75" "THERMAL_RADIATORS" "21_72_24_53_57"

# 76-MIRROR_CONTROL
mk_system "76" "MIRROR_CONTROL" "70_32_24_42_45"

# 77-ALIGNMENT_SENSING
mk_system "77" "ALIGNMENT_SENSING" "70_32_31_24_45"

# 78-BACKPLANE_ELECTRONICS
mk_system "78" "BACKPLANE_ELECTRONICS" "71_70_24_31_42_92"

# 79-LUBRICATION
mk_system "79" "LUBRICATION" "73_66_57"

# 80-STARTUP_SEQUENCING
mk_system "80" "STARTUP_SEQUENCING" "42_21_24_66_72_70_71"

# 84-PROPULSION (optional, station-keeping)
mk_system "84" "PROPULSION" "24_21_32_34_92"

# 92-EWIS_HARNESS (ONLY physical wiring)
mk_system "92" "EWIS_HARNESS" "ALL"

# 94-ELECTRONIC_COMPARTMENTS
mk_system "94" "ELECTRONIC_COMPARTMENTS" "24_31_42_78_92_21"

# 99-SCIENCE_OPERATIONS
mk_system "99" "SCIENCE_OPERATIONS" "31_42_71_24"

echo "✓ Telescope systems structure created in $ROOT"
echo "✓ Total systems created: $(find "$ROOT/SYSTEMS" -mindepth 1 -maxdepth 1 -type d | wc -l)"
echo "✓ Subsystems with PLM/CAx created for systems 70 and 71"
