#!/usr/bin/env bash
set -euo pipefail

# Create probe systems structure following SPACE-T (STA) architecture for 06-PROBES
# Usage: ./create-probe-systems.sh <PRODUCT-ID> <MODEL-ID> <TAG>

PROD="${1:?PRODUCT-ID}"; MODEL="${2:?MODEL-ID}"; TAG="${3:?TAG}"
ROOT="06-PROBES/DOMAIN_INTEGRATION/PRODUCTS/$PROD/MODELS/$MODEL/VERSION/$TAG/SYSTEMS"

# Define STA systems
STAS=(
  "STA-06_STRUCTURES"
  "STA-21_THERMAL"
  "STA-24_POWER"
  "STA-23_COMM"
  "STA-31_NAV_TDH"
  "STA-40_AVIONICS"
  "STA-22_CONTROL_FDIR"
  "STA-28_PROPULSION"
  "STA-58_ROBOTICS"
  "STA-86_ENV_SAFETY"
  "STA-07_GROUND_OPS"
  "STA-01_PROGRAM"
)

for S in "${STAS[@]}"; do
  mkdir -p "$ROOT/$S/INTERFACE_MATRIX" "$ROOT/$S/SUBSYSTEMS"
  if [[ "$S" == "STA-06_STRUCTURES" ]]; then
    mkdir -p "$ROOT/$S/SUBSYSTEMS/06-01_PRIMARY_STRUCT"/{DELs,PAx/ONB,PAx/OUT,SUPPLIERS,policy,tests,PLM/CAx/{CAD,CAE,CAM,CAI,CAO,CAP,CAS,CAV,CMP}}
    echo "# $S · Integration View" > "$ROOT/$S/INTEGRATION_VIEW.md"
    echo "# 06-01 PRIMARY_STRUCT" > "$ROOT/$S/SUBSYSTEMS/06-01_PRIMARY_STRUCT/README.md"
    echo '{}' > "$ROOT/$S/SUBSYSTEMS/06-01_PRIMARY_STRUCT/META.json"
    echo "FromSTA,ToSTA,Interface,Type,ICD,Owner,Notes" > "$ROOT/$S/INTERFACE_MATRIX/06↔OTHERS.csv"
  else
    echo "# $S · Integration View" > "$ROOT/$S/INTEGRATION_VIEW.md"
    STA_NUM=$(echo "$S" | cut -d'-' -f2 | cut -d'_' -f1)
    echo "FromSTA,ToSTA,Interface,Type,ICD,Owner,Notes" > "$ROOT/$S/INTERFACE_MATRIX/${STA_NUM}↔OTHERS.csv"
  fi
done

echo "OK -> 06-PROBES scaffold for $PROD/$MODEL/$TAG"
