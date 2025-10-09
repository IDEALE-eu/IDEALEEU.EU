#!/usr/bin/env bash
set -euo pipefail

# Script to create STA-aligned satellite domain integration structure
# Usage: ./scripts/create-satellite-domains.sh [MISSION] [CONF] [TAG]
# Example: ./scripts/create-satellite-domains.sh EXAMPLE-SAT-1 BASELINE V1.0

MISSION="${1:-EXAMPLE-SAT-1}"
CONF="${2:-BASELINE}"
TAG="${3:-V1.0}"

ROOT="04-SATELLITES/DOMAIN_INTEGRATION/PRODUCTS/${MISSION}/MODELS/${CONF}/VERSION/${TAG}"

echo "Creating satellite domain structure for:"
echo "  Mission: $MISSION"
echo "  Configuration: $CONF"
echo "  Version: $TAG"
echo "  Path: $ROOT"
echo ""

# Helper functions
mk_system() {
  local sys="$1"
  local desc="$2"
  
  mkdir -p "$ROOT/SYSTEMS/$sys/INTERFACE_MATRIX" \
           "$ROOT/SYSTEMS/$sys/SUBSYSTEMS"
  
  # Create INTEGRATION_VIEW.md
  [[ -f "$ROOT/SYSTEMS/$sys/INTEGRATION_VIEW.md" ]] || cat > "$ROOT/SYSTEMS/$sys/INTEGRATION_VIEW.md" <<EOF
# $sys — Integration View

## Overview
$desc

## Functional Description
Brief description of how this system integrates with the overall satellite architecture.

## Operating Modes
- Mode 1: Description
- Mode 2: Description

## Key Interfaces
See INTERFACE_MATRIX/ for detailed interface definitions.

## Dependencies
- Power requirements
- Thermal requirements
- Data bus connections
- Command & control links

## Integration Points
- Structural mounting
- Electrical connections
- Thermal interfaces
- Data interfaces
EOF

  # Create interface matrix template
  local sys_num="${sys%%-*}"
  [[ -f "$ROOT/SYSTEMS/$sys/INTERFACE_MATRIX/${sys_num}↔OTHERS.csv" ]] || cat > "$ROOT/SYSTEMS/$sys/INTERFACE_MATRIX/${sys_num}↔OTHERS.csv" <<'EOF'
from_sta,to_sta,interface_type,signal_medium,protocol_spec,power_W,data_rate,notes
EOF
}

mk_subsystem() {
  local sys="$1"
  local sub="$2"
  local desc="$3"
  
  local base="$ROOT/SYSTEMS/$sys/SUBSYSTEMS/$sub"
  
  mkdir -p "$base/DELs" \
           "$base/PAx/ONB" "$base/PAx/OUT" \
           "$base/PLM/CAx"/{CAD,CAE,CAO,CAM,CAI,CAV,CAP,CAS,CMP} \
           "$base/PLM/EBOM" \
           "$base/PROCUREMENT/VENDORS" \
           "$base/QUANTUM_OA" \
           "$base/SUPPLIERS"/{BIDS,SERVICES} \
           "$base/policy" \
           "$base/tests"
  
  # Create subsystem README
  [[ -f "$base/README.md" ]] || cat > "$base/README.md" <<EOF
# $sub

## Description
$desc

## Contents
- **DELs/** - Deliverables and documentation
- **PAx/** - Package assemblies (ONB: onboard, OUT: outputs)
- **PLM/** - Product lifecycle management
  - **CAx/** - Computer-aided engineering tools (CAD, CAE, CAO, CAM, etc.)
  - **EBOM/** - Engineering bill of materials
- **PROCUREMENT/** - Vendor management
- **QUANTUM_OA/** - Quantum/OA specific artifacts
- **SUPPLIERS/** - Supplier bids and services
- **policy/** - Local policies and procedures
- **tests/** - Test specifications and results

## Design Notes
Add specific design considerations, constraints, and requirements here.
EOF

  # Create PLM EBOM links
  [[ -f "$base/PLM/EBOM_LINKS.md" ]] || cat > "$base/PLM/EBOM_LINKS.md" <<'EOF'
# EBOM Links

## Part Number Mapping
- P/N → PLM item ID
- Configuration rules
- Effectivity conditions

## BOM Structure
Link to main BOM in PLM system.

## Change Control
References to ECOs/ECNs affecting this subsystem.
EOF

  # Create META.json
  [[ -f "$base/META.json" ]] || cat > "$base/META.json" <<EOF
{
  "scope": "subsystem",
  "mission": "$MISSION",
  "model": "$CONF",
  "version": "$TAG",
  "sta_system": "$sys",
  "subsystem": "$sub"
}
EOF

  # Create inherit.json
  [[ -f "$base/inherit.json" ]] || cat > "$base/inherit.json" <<'EOF'
{
  "inherit_from": [
    "../../../../DELs/TEMPLATES",
    "../../../../PAx/STANDARDS"
  ]
}
EOF
}

# Create root structure
mkdir -p "$ROOT/SYSTEMS"

# Create main README
[[ -f "$ROOT/README.md" ]] || cat > "$ROOT/README.md" <<EOF
# $MISSION - $CONF ($TAG)

STA-aligned satellite system structure following ECSS standards.

## Mission Overview
Mission: **$MISSION**
Configuration: **$CONF**
Version: **$TAG**

## Structure
This directory contains all systems for the satellite organized according to SPACE-T (STA) architecture:

\`\`\`
SYSTEMS/
├─ 01-INTRO/                     # Mission overview and CONOPS
├─ 06-DIMENSIONS_ALIGNMENTS/     # Reference frames and alignments
├─ 15-ENVIRONMENT_VIBRATION/     # Environmental specifications
├─ 21-THERMAL_CONTROL/           # Thermal management
├─ 23-COMMS_TT&C_RF_OPTICAL/     # Communications
├─ 24-ELECTRICAL_POWER_EPS/      # Power generation and distribution
├─ 28-PROPELLANT_SYSTEMS/        # Propellant storage and feed
├─ 29-PRESSURIZATION_PURGE/      # Pressurization systems
├─ 31-DATA_HANDLING_CDH/         # Command and data handling
├─ 34-NAVIGATION_ATTITUDE/       # GNC systems
├─ 40-DATABUS_NETWORKS/          # Internal data networks
├─ 42-AVIONICS_COMPUTE_FSW/      # Flight software and computers
├─ 45-HEALTH_MONITORING_FDIR/    # Health monitoring
├─ 50-MECHANISMS_DEPLOYABLES/    # Deployment mechanisms
├─ 51-PRIMARY_STRUCTURE/         # Structural elements
├─ 57-INSTRUMENT_BAYS/           # Payload accommodation
├─ 61-RCS_ATTITUDE_CONTROL/      # Reaction control system
├─ 70-OPTICAL_SUBSYSTEMS/        # Optical payloads (if applicable)
├─ 71-PAYLOADS/                  # Science/mission payloads
├─ 72-PROPULSION_MAIN/           # Main propulsion (if applicable)
├─ 84-ELECTRIC_PROPULSION/       # Electric propulsion (if applicable)
├─ 87-RADIATION/                 # Radiation analysis
├─ 90-SPACE_TRAFFIC_CONJUNCTION/ # Collision avoidance
├─ 97-ELECTRICAL_HARNESS/        # Electrical harness (STA-97)
└─ 99-MISSION_OPERATIONS/        # Operations concept
\`\`\`

## Key Principles
1. **PLM/CAx only in SUBSYSTEMS** - All engineering artifacts at subsystem level
2. **Integration focus** - Each system has INTEGRATION_VIEW.md and INTERFACE_MATRIX/
3. **STA-97 for harness** - All physical harness in dedicated chapter (not ATA-92)
4. **ECSS compliance** - Following ECSS-E/M/Q/S standards

## System Interfaces
Interface control documents are maintained in INTERFACE_MATRIX/ folders within each system.
Cross-system interfaces are documented using CSV format: \`XX↔YY.csv\`

## Configuration Management
This configuration is baselined and controlled through:
- 00-PROGRAM/CONFIG_MGMT/04-BASELINES/
- Change control via CCB process
- Version control in Git

## References
- **ECSS Standards**: [ECSS website](https://ecss.nl/)
- **STA Structure**: [04-SATELLITES/00-README.md](../../../../00-README.md)
- **Interface Definitions**: [00-PROGRAM/DIGITAL_THREAD/04-MBSE/INTERFACE_DEFINITIONS/](../../../../../../../00-PROGRAM/DIGITAL_THREAD/04-MBSE/INTERFACE_DEFINITIONS/)
EOF

# Create domain-level metadata
[[ -f "$ROOT/META.json" ]] || cat > "$ROOT/META.json" <<EOF
{
  "scope": "mission",
  "mission": "$MISSION",
  "model": "$CONF",
  "version": "$TAG",
  "standard": "STA",
  "domain": "SATELLITES"
}
EOF

[[ -f "$ROOT/domain-config.yaml" ]] || cat > "$ROOT/domain-config.yaml" <<'EOF'
rules:
  plm_at_domain_level: false
  systems_required: true
  harness_chapter: 97  # STA-97, not ATA-92
  plm_in_subsystems_only: true
  ecss_compliance: true
EOF

# ========================================
# Create representative systems
# ========================================

echo "Creating representative systems..."

# 01-INTRO
mk_system "01-INTRO" "Mission introduction, CONOPS, and operating modes"
mkdir -p "$ROOT/SYSTEMS/01-INTRO"
[[ -f "$ROOT/SYSTEMS/01-INTRO/README.md" ]] || cat > "$ROOT/SYSTEMS/01-INTRO/README.md" <<EOF
# 01-INTRO — Mission Introduction

## Mission Overview
Mission objectives, concept of operations (CONOPS), and system-level requirements.

## Contents
- Mission objectives and success criteria
- Concept of operations
- Mission phases and timelines
- Operating modes
- Top-level requirements

## References
- Mission Definition documents
- System Requirements Specification (SRS)
EOF

# 06-DIMENSIONS_ALIGNMENTS
mk_system "06-DIMENSIONS_ALIGNMENTS" "Reference frames, coordinate systems, and alignment specifications"
mkdir -p "$ROOT/SYSTEMS/06-DIMENSIONS_ALIGNMENTS"
[[ -f "$ROOT/SYSTEMS/06-DIMENSIONS_ALIGNMENTS/README.md" ]] || cat > "$ROOT/SYSTEMS/06-DIMENSIONS_ALIGNMENTS/README.md" <<EOF
# 06-DIMENSIONS_ALIGNMENTS

Reference frames, coordinate systems, focal stations, and alignment tolerances.

## Key Definitions
- Spacecraft body frame
- Orbital reference frames
- Sensor alignments
- Mounting interfaces
EOF

# 15-ENVIRONMENT_VIBRATION
mk_system "15-ENVIRONMENT_VIBRATION" "Environmental specifications including acoustic, vibration, shock, and radiation"
mkdir -p "$ROOT/SYSTEMS/15-ENVIRONMENT_VIBRATION"
[[ -f "$ROOT/SYSTEMS/15-ENVIRONMENT_VIBRATION/README.md" ]] || cat > "$ROOT/SYSTEMS/15-ENVIRONMENT_VIBRATION/README.md" <<EOF
# 15-ENVIRONMENT_VIBRATION

Environmental specifications for launch, on-orbit, and mission phases.

## Specifications
- Launch vibration profiles
- Acoustic environment
- Shock loads
- Radiation environment (links to STA-87)
- Thermal environment
EOF

# 21-THERMAL_CONTROL
mk_system "21-THERMAL_CONTROL" "Thermal management including radiators, MLI, heaters, and thermal control loops"
mk_subsystem "21-THERMAL_CONTROL" "21-10_RADIATORS_HX" "Radiators and heat exchangers for heat rejection"
mk_subsystem "21-THERMAL_CONTROL" "21-20_MLI_INSULATION" "Multi-layer insulation blankets"
mk_subsystem "21-THERMAL_CONTROL" "21-30_HEATERS_THERMOSTATS" "Survival heaters and thermostatic controls"

# Create interface matrix for thermal
[[ -f "$ROOT/SYSTEMS/21-THERMAL_CONTROL/INTERFACE_MATRIX/21↔24_31_34_70_75_97.csv" ]] || cat > "$ROOT/SYSTEMS/21-THERMAL_CONTROL/INTERFACE_MATRIX/21↔24_31_34_70_75_97.csv" <<'EOF'
from_sta,to_sta,interface_type,signal_medium,protocol_spec,power_W,data_rate,notes
21,24,power,electrical,28V_bus,150,,Heater power supply
21,31,telemetry,digital,CCSDS,0,1kbps,Temperature sensor data
21,34,thermal,conductive,thermal_strap,0,,Star tracker thermal mgmt
21,70,thermal,conductive,cold_plate,0,,Detector cooling
21,97,power,electrical,harness,0,,Heater control wiring
EOF

# 23-COMMS_TT&C_RF_OPTICAL
mk_system "23-COMMS_TT&C_RF_OPTICAL" "Communications, telemetry, tracking and command systems"
mk_subsystem "23-COMMS_TT&C_RF_OPTICAL" "23-10_RF_FRONTEND_L_S_X_KA" "RF front-end electronics for various frequency bands"
mk_subsystem "23-COMMS_TT&C_RF_OPTICAL" "23-20_TRANSCEIVERS_MODEMS" "Communication transceivers and modems"
mk_subsystem "23-COMMS_TT&C_RF_OPTICAL" "23-30_ANTENNAS_POINTING" "Antenna systems and pointing mechanisms"

# 24-ELECTRICAL_POWER_EPS
mk_system "24-ELECTRICAL_POWER_EPS" "Electrical power system: generation, storage, conversion, and distribution"
mk_subsystem "24-ELECTRICAL_POWER_EPS" "24-10_GENERATION_ARRAYS_FUELCELLS" "Solar arrays and power generation"
mk_subsystem "24-ELECTRICAL_POWER_EPS" "24-20_STORAGE_BATTERIES" "Battery storage systems"
mk_subsystem "24-ELECTRICAL_POWER_EPS" "24-30_CONVERSION_PCDU_DCDC" "Power conditioning and distribution unit"

[[ -f "$ROOT/SYSTEMS/24-ELECTRICAL_POWER_EPS/INTERFACE_MATRIX/24↔21_31_40_42_70_71_97.csv" ]] || cat > "$ROOT/SYSTEMS/24-ELECTRICAL_POWER_EPS/INTERFACE_MATRIX/24↔21_31_40_42_70_71_97.csv" <<'EOF'
from_sta,to_sta,interface_type,signal_medium,protocol_spec,power_W,data_rate,notes
24,21,power,electrical,28V_bus,150,,Thermal heater power
24,31,power,electrical,28V_bus,80,,OBC power supply
24,40,power,electrical,28V_bus,30,,Data bus power
24,42,power,electrical,28V_bus,100,,Avionics power
24,70,power,electrical,28V_bus,200,,Payload power
24,71,power,electrical,28V_bus,150,,Science payload power
24,97,power,electrical,harness,0,,Power distribution harness
EOF

# 28-PROPELLANT_SYSTEMS
mk_system "28-PROPELLANT_SYSTEMS" "Propellant storage, tanks, and propellant management devices"
mk_subsystem "28-PROPELLANT_SYSTEMS" "28-10_TANKS_PMD" "Propellant tanks and propellant management devices"

# 29-PRESSURIZATION_PURGE
mk_system "29-PRESSURIZATION_PURGE" "Pressurization and purge systems"
mk_subsystem "29-PRESSURIZATION_PURGE" "29-10_PRESSURE_REG_MANIFOLDS" "Pressure regulation and manifolds"

# 31-DATA_HANDLING_CDH
mk_system "31-DATA_HANDLING_CDH" "Command and data handling: OBC, mass memory, and TM/TC routing"
mk_subsystem "31-DATA_HANDLING_CDH" "31-10_OBC_PROCESSING" "On-board computer and processing units"
mk_subsystem "31-DATA_HANDLING_CDH" "31-20_MASS_MEMORY" "Mass memory storage devices"

[[ -f "$ROOT/SYSTEMS/31-DATA_HANDLING_CDH/INTERFACE_MATRIX/31↔23_24_34_40_42_45_70_71_97.csv" ]] || cat > "$ROOT/SYSTEMS/31-DATA_HANDLING_CDH/INTERFACE_MATRIX/31↔23_24_34_40_42_45_70_71_97.csv" <<'EOF'
from_sta,to_sta,interface_type,signal_medium,protocol_spec,power_W,data_rate,notes
31,23,data,digital,CCSDS,0,10Mbps,Telemetry downlink
31,24,telemetry,digital,CAN,0,100kbps,EPS telemetry
31,34,data,digital,RS422,0,1Mbps,GNC data exchange
31,40,data,digital,SpaceWire,0,100Mbps,Internal data bus
31,42,data,digital,Ethernet,0,1Gbps,FSW interface
31,45,telemetry,digital,CAN,0,100kbps,Health monitoring
31,70,data,digital,CameraLink,0,500Mbps,Optical payload data
31,71,data,digital,LVDS,0,200Mbps,Science data
31,97,data,electrical,harness,0,,Data harness connections
EOF

# 34-NAVIGATION_ATTITUDE
mk_system "34-NAVIGATION_ATTITUDE" "Navigation and attitude determination systems"
mk_subsystem "34-NAVIGATION_ATTITUDE" "34-10_STAR_TRACKERS_IMU" "Star trackers and inertial measurement units"
mk_subsystem "34-NAVIGATION_ATTITUDE" "34-20_GNSS_SENSORS" "GNSS receivers and navigation sensors"

# 40-DATABUS_NETWORKS
mk_system "40-DATABUS_NETWORKS" "Internal data networks: SpaceWire, MIL-STD-1553, CAN, time distribution"
mk_subsystem "40-DATABUS_NETWORKS" "40-10_SWITCHES_BRIDGES" "Data bus switches and network bridges"

# 42-AVIONICS_COMPUTE_FSW
mk_system "42-AVIONICS_COMPUTE_FSW" "Avionics computers and flight software: FDIR, mode management, and updates"
mk_subsystem "42-AVIONICS_COMPUTE_FSW" "42-10_FLIGHT_COMPUTERS" "Flight computers and processing units"

# 45-HEALTH_MONITORING_FDIR
mk_system "45-HEALTH_MONITORING_FDIR" "Health monitoring and fault detection, isolation, and recovery"
mk_subsystem "45-HEALTH_MONITORING_FDIR" "45-10_MONITORS_RULESETS" "Health monitors and FDIR rule sets"

# 50-MECHANISMS_DEPLOYABLES
mk_system "50-MECHANISMS_DEPLOYABLES" "Deployment mechanisms: solar arrays, antennas, booms, sunshields"
mk_subsystem "50-MECHANISMS_DEPLOYABLES" "50-10_DEPLOY_DRIVES_LATCHES" "Deployment drives, actuators, and latches"

# 51-PRIMARY_STRUCTURE
mk_system "51-PRIMARY_STRUCTURE" "Primary spacecraft structure and load paths"
mk_subsystem "51-PRIMARY_STRUCTURE" "51-10_BUS_PRIMARY_STRUCTURE" "Main spacecraft bus structure"

# 57-INSTRUMENT_BAYS
mk_system "57-INSTRUMENT_BAYS" "Payload accommodation and instrument bays"
mk_subsystem "57-INSTRUMENT_BAYS" "57-10_PAYLOAD_INTERFACE_PLATES" "Payload mounting interfaces and adapter plates"

# 61-RCS_ATTITUDE_CONTROL
mk_system "61-RCS_ATTITUDE_CONTROL" "Reaction control system for attitude control"
mk_subsystem "61-RCS_ATTITUDE_CONTROL" "61-10_THRUSTER_MODULES" "RCS thruster modules and assemblies"

# 70-OPTICAL_SUBSYSTEMS (optional, for optical missions)
mk_system "70-OPTICAL_SUBSYSTEMS" "Optical subsystems for imaging and remote sensing payloads"
mk_subsystem "70-OPTICAL_SUBSYSTEMS" "70-10_PRIMARY_OPTICS" "Primary mirrors and optical assemblies"
mk_subsystem "70-OPTICAL_SUBSYSTEMS" "70-60_DETECTOR_CRYOSTATS" "Detector assemblies and cryogenic cooling"

# 71-PAYLOADS
mk_system "71-PAYLOADS" "Science and mission payloads"
mk_subsystem "71-PAYLOADS" "71-10_IMAGER" "Imaging payload system"
mk_subsystem "71-PAYLOADS" "71-20_SPECTROMETER" "Spectrometer instrument"

# 72-PROPULSION_MAIN (optional, for missions with main engines)
mk_system "72-PROPULSION_MAIN" "Main propulsion system for large delta-V maneuvers"
mk_subsystem "72-PROPULSION_MAIN" "72-10_MAIN_ENGINE" "Main engine assembly"

# 84-ELECTRIC_PROPULSION (optional, for EP missions)
mk_system "84-ELECTRIC_PROPULSION" "Electric propulsion system"
mk_subsystem "84-ELECTRIC_PROPULSION" "84-10_THRUSTERS" "Electric propulsion thrusters"
mk_subsystem "84-ELECTRIC_PROPULSION" "84-20_PPU" "Power processing units for EP"

# 87-RADIATION
mk_system "87-RADIATION" "Radiation analysis and shielding"
mkdir -p "$ROOT/SYSTEMS/87-RADIATION"
[[ -f "$ROOT/SYSTEMS/87-RADIATION/README.md" ]] || cat > "$ROOT/SYSTEMS/87-RADIATION/README.md" <<EOF
# 87-RADIATION

Radiation environment analysis, total ionizing dose (TID), single-event effects (SEE), and shielding design.

## Contents
- Radiation environment definition
- TID analysis
- SEE analysis
- Shielding design
- Component derating
EOF

# 90-SPACE_TRAFFIC_CONJUNCTION
mk_system "90-SPACE_TRAFFIC_CONJUNCTION" "Space traffic management and conjunction assessment"
mkdir -p "$ROOT/SYSTEMS/90-SPACE_TRAFFIC_CONJUNCTION"
[[ -f "$ROOT/SYSTEMS/90-SPACE_TRAFFIC_CONJUNCTION/README.md" ]] || cat > "$ROOT/SYSTEMS/90-SPACE_TRAFFIC_CONJUNCTION/README.md" <<EOF
# 90-SPACE_TRAFFIC_CONJUNCTION

Space traffic management, collision avoidance, and conjunction assessment.

## Contents
- Orbital tracking and monitoring
- Conjunction analysis
- Collision avoidance maneuvers
- Space debris mitigation
EOF

# 97-ELECTRICAL_HARNESS (STA-97, not ATA-92!)
mk_system "97-ELECTRICAL_HARNESS" "All physical electrical harness, bundles, and connectors"
mk_subsystem "97-ELECTRICAL_HARNESS" "97-10_HARNESS_BUNDLES_CONNECTORS" "Harness bundles, cables, and connectors"

[[ -f "$ROOT/SYSTEMS/97-ELECTRICAL_HARNESS/INTERFACE_MATRIX/97↔ALL.csv" ]] || cat > "$ROOT/SYSTEMS/97-ELECTRICAL_HARNESS/INTERFACE_MATRIX/97↔ALL.csv" <<'EOF'
from_sta,to_sta,interface_type,signal_medium,protocol_spec,power_W,data_rate,notes
97,21,harness,electrical,power_wiring,0,,Thermal heater wiring
97,23,harness,electrical,RF_coax,0,,RF signal cables
97,24,harness,electrical,power_bus,0,,Power distribution harness
97,31,harness,electrical,data_cables,0,,Data interface cables
97,34,harness,electrical,sensor_cables,0,,Sensor interface wiring
97,40,harness,electrical,network_cables,0,,Data bus cabling
97,42,harness,electrical,avionics_cables,0,,Avionics interconnect
97,45,harness,electrical,monitor_wiring,0,,Health monitoring wiring
97,61,harness,electrical,actuator_cables,0,,Thruster valve wiring
97,70,harness,electrical,payload_cables,0,,Optical payload cabling
97,71,harness,electrical,science_cables,0,,Science payload wiring
EOF

# 99-MISSION_OPERATIONS
mk_system "99-MISSION_OPERATIONS" "Mission operations concept and ground segment interfaces"
mkdir -p "$ROOT/SYSTEMS/99-MISSION_OPERATIONS"
[[ -f "$ROOT/SYSTEMS/99-MISSION_OPERATIONS/README.md" ]] || cat > "$ROOT/SYSTEMS/99-MISSION_OPERATIONS/README.md" <<EOF
# 99-MISSION_OPERATIONS

Mission operations planning, ground segment interfaces, and operations procedures.

## Contents
- Operations concept (CONOPS)
- Ground segment architecture
- Mission control procedures
- Contingency operations
- End-of-life disposal
EOF

# Optional systems (create README stubs only)
for sys in "07-MGSE" "16-EGSE" "46-GROUND_SEGMENT_MOC" "32-EDL_LANDING_OPS" "48-OPTICAL_COMMS" "58-DOCKING" "59-ROBOTICS_SAMPLING" "86-PLANETARY_PROTECTION" "94-ELECTRONIC_COMPARTMENTS"; do
  mkdir -p "$ROOT/SYSTEMS/$sys"
  sys_name="${sys##*-}"
  [[ -f "$ROOT/SYSTEMS/$sys/README.md" ]] || cat > "$ROOT/SYSTEMS/$sys/README.md" <<EOF
# $sys

Optional system - include if applicable to mission.

## Purpose
Placeholder for $sys_name subsystem if required by mission design.
EOF
done

echo ""
echo "✓ Satellite domain structure created successfully!"
echo ""
echo "Structure created at: $ROOT"
echo ""
echo "Key systems created:"
echo "  - Thermal Control (STA-21)"
echo "  - Communications (STA-23)"
echo "  - Electrical Power (STA-24)"
echo "  - Data Handling (STA-31)"
echo "  - Navigation/Attitude (STA-34)"
echo "  - Data Bus (STA-40)"
echo "  - Avionics/FSW (STA-42)"
echo "  - Health Monitoring (STA-45)"
echo "  - Mechanisms (STA-50)"
echo "  - Primary Structure (STA-51)"
echo "  - Instrument Bays (STA-57)"
echo "  - RCS (STA-61)"
echo "  - Optical Subsystems (STA-70)"
echo "  - Payloads (STA-71)"
echo "  - Main Propulsion (STA-72)"
echo "  - Electric Propulsion (STA-84)"
echo "  - Electrical Harness (STA-97) ← Note: Uses STA-97, not ATA-92!"
echo ""
echo "All systems include:"
echo "  - INTEGRATION_VIEW.md"
echo "  - INTERFACE_MATRIX/"
echo "  - SUBSYSTEMS/ (with PLM/CAx structure)"
echo ""
