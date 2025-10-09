#!/usr/bin/env bash
set -euo pipefail

ROOT="02-AIRCRAFT/DOMAIN_INTEGRATION/PRODUCTS/AMPEL360-AIR-T/MODELS/BWB/VERSION/Q100"
DOMAINS=(
  "AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS"
  "PPP-PROPULSION-FUEL-SYSTEMS"
  "MEC-MECHANICAL-SYSTEMS-MODULES"
  "LCC-LINKAGES-CONTROL-COMMUNICATIONS"
  "EDI-ELECTRONICS-DIGITAL-INSTRUMENTS"
  "EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION"
  "EER-ENVIRONMENTAL-EMISSIONS-REMEDIATION"
  "DDD-DRAINAGE-DEHUMIDIFICATION-DRYING"
  "CCC-COCKPIT-CABIN-CARGO"
  "IIS-INFORMATION-INTELLIGENCE-SYSTEMS"
  "LIB-LOGISTICS-INVENTORY-BLOCKCHAIN"
  "AAP-AIRPORT-ADAPTABLE-PLATFORMS"
  "CQH-CRYOGENICS-QUANTUM-H2"
  "IIF-INDUSTRIAL-INFRASTRUCTURE-FACILITIES"
  "OOO-OS-ONTOLOGIES-OFFICE"
)

# --- helpers ---
mk_domain() {
  local d="$1"
  mkdir -p "$ROOT/$d/SYSTEMS" \
           "$ROOT/$d/DELs/TEMPLATES" "$ROOT/$d/DELs/SCHEMAS" \
           "$ROOT/$d/PAx/STANDARDS" \
           "$ROOT/$d/QUANTUM_OA/PATTERNS" \
           "$ROOT/$d/SUPPLIERS/CRITERIA" \
           "$ROOT/$d/policy" "$ROOT/$d/tests"

  [[ -f "$ROOT/$d/README.md" ]] || cat > "$ROOT/$d/README.md" <<EOF
# $d
Ámbito, RASCI y reglas del dominio. Convención unificada: /SYSTEMS/…; PLM/CAx **solo** en SUBSYSTEMS.
EOF

  [[ -f "$ROOT/$d/META.json" ]] || cat > "$ROOT/$d/META.json" <<EOF
{ "scope": "domain", "product": "AMPEL360-AIR-T", "model": "BWB", "version": "Q100" }
EOF

  [[ -f "$ROOT/$d/domain-config.yaml" ]] || cat > "$ROOT/$d/domain-config.yaml" <<'EOF'
rules:
  plm_at_domain_level: false
  systems_required: true
  ewis_only_ata_92: true
  sw_with_host_lru: true
EOF
}

mk_system() {
  # $1 domain, $2 path "ATA-XX_NAME"
  local d="$1"; local sys="$2"
  mkdir -p "$ROOT/$d/SYSTEMS/$sys/INTERFACE_MATRIX" \
           "$ROOT/$d/SYSTEMS/$sys/SUBSYSTEMS"
  [[ -f "$ROOT/$d/SYSTEMS/$sys/INTEGRATION_VIEW.md" ]] || cat > "$ROOT/$d/SYSTEMS/$sys/INTEGRATION_VIEW.md" <<EOF
# $sys — Integration View
Descripción breve del encaje funcional, dependencias y modos.
EOF
  [[ -f "$ROOT/$d/SYSTEMS/$sys/INTERFACE_MATRIX/${sys%%_*}↔OTROS.csv" ]] || cat > "$ROOT/$d/SYSTEMS/$sys/INTERFACE_MATRIX/${sys%%_*}↔OTROS.csv" <<'EOF'
from_ata,to_ata,interface,signal_or_medium,protocol/spec,notes
XX,YY,ejemplo_bus,ARINC/Ethernet/fluido,ref-ICD,observaciones
EOF
}

mk_subsystem_with_plm() {
  # $1 domain, $2 system path, $3 sub "XX-YY_SUBSYS"
  local d="$1"; local sys="$2"; local sub="$3"
  local base="$ROOT/$d/SYSTEMS/$sys/SUBSYSTEMS/$sub"
  mkdir -p "$base/DELs" "$base/PAx/ONB" "$base/PAx/OUT" \
           "$base/PLM/CAx"/{CAD,CAE,CAO,CAM,CAI,CAV,CAP,CAS,CMP} \
           "$base/PROCUREMENT/VENDORSCOMPONENTS" "$base/QUANTUM_OA" \
           "$base/SUPPLIERS"/{BIDS,SERVICES} "$base/policy" "$base/tests"

  [[ -f "$base/README.md" ]] || echo "# $sub — descripción" > "$base/README.md"
  [[ -f "$base/PLM/EBOM_LINKS.md" ]] || cat > "$base/PLM/EBOM_LINKS.md" <<'EOF'
# EBOM Links
- P/N → PLM item
- Config rules / effectivity
EOF
  [[ -f "$base/META.json" ]] || cat > "$base/META.json" <<'EOF'
{ "scope": "instance" }
EOF
  [[ -f "$base/inherit.json" ]] || cat > "$base/inherit.json" <<'EOF'
{ "inherit_from": ["../../../../DELs/TEMPLATES", "../../../../PAx/STANDARDS"] }
EOF
}

# --- create domains ---
for d in "${DOMAINS[@]}"; do mk_domain "$d"; done

# --- sample systems + subsystems with PLM/CAx (mínimos) ---

# AAA — 53 Fuselage Structures / 53-10 Center Body
mk_system "AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS" "53-FUSELAGE-STRUCTURES"
mk_subsystem_with_plm "AAA-AIRFRAMES-AERODYNAMICS-AIRWORTHINESS" "53-FUSELAGE-STRUCTURES" "53-10_CENTER-BODY"

# MEC — 32 Landing Gear / 32-10 Main Gear
mk_system "MEC-MECHANICAL-SYSTEMS-MODULES" "32-LANDING-GEAR-SYSTEMS"
mk_subsystem_with_plm "MEC-MECHANICAL-SYSTEMS-MODULES" "32-LANDING-GEAR-SYSTEMS" "32-10_MAIN-GEAR"

# EEE — 24 Electrical Power / 24-40 Distribution
mk_system "EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION" "24-ELECTRICAL-POWER"
mk_subsystem_with_plm "EEE-ELECTRICAL-ENDOTRANSPONDERS-CIRCULATION" "24-ELECTRICAL-POWER" "24-40_DISTRIBUTION"

# PPP — 71 Power Plant / 71-00 General
mk_system "PPP-PROPULSION-FUEL-SYSTEMS" "71-POWER-PLANT"
mk_subsystem_with_plm "PPP-PROPULSION-FUEL-SYSTEMS" "71-POWER-PLANT" "71-00_GENERAL"

# EDI — 34 Navigation Avionics / 34-20 AHRS_IRS_GNSS
mk_system "EDI-ELECTRONICS-DIGITAL-INSTRUMENTS" "34-NAVIGATION-AVIONICS"
mk_subsystem_with_plm "EDI-ELECTRONICS-DIGITAL-INSTRUMENTS" "34-NAVIGATION-AVIONICS" "34-20_AHRS_IRS_GNSS"

# CCC — 25 Equipment & Furnishings / 25-50 Cabin Interiors
mk_system "CCC-COCKPIT-CABIN-CARGO" "25-EQUIPMENT-FURNISHINGS"
mk_subsystem_with_plm "CCC-COCKPIT-CABIN-CARGO" "25-EQUIPMENT-FURNISHINGS" "25-50_CABIN_INTERIORS"

echo "✓ Estructura creada en $ROOT"
