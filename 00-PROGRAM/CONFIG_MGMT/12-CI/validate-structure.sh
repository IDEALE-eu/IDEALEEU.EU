#!/usr/bin/env bash
set -euo pipefail
fail=0
# 1) Every domain must have SYSTEMS/
for d in 02-AIRCRAFT/DOMAIN_INTEGRATION 03-SPACECRAFT/DOMAIN_INTEGRATION 04-SATELLITES/DOMAIN_INTEGRATION 05-TELESCOPES/DOMAIN_INTEGRATION 06-PROBES/DOMAIN_INTEGRATION 07-DRONES/DOMAIN_INTEGRATION 08-LAUNCHERS/DOMAIN_INTEGRATION 09-STM-SPACE-STATION-MODULES/DOMAIN_INTEGRATION; do
  [ -d "$d" ] || continue
  while IFS= read -r prod; do
    systems=$(find "$prod" -type d -path "*/SYSTEMS" | wc -l)
    if [ "$systems" -eq 0 ]; then echo "[STRUCT] Missing SYSTEMS under $prod"; fail=1; fi
  done < <(find "$d/PRODUCTS" -maxdepth 2 -mindepth 2 -type d || true)
done
# 2) PLM/CAx only under SUBSYSTEMS
while IFS= read -r plm; do
  case "$plm" in
    */SUBSYSTEMS/*/PLM) : ;;
    *) echo "[STRUCT] Illegal PLM at $plm (must be under SUBSYSTEMS)"; fail=1;;
  esac
done < <(find . -type d -name PLM || true)
# 3) EWIS rule (ATA-92 only)
if find 02-AIRCRAFT/DOMAIN_INTEGRATION -type d -name "*92*" | grep -q .; then :; fi
if grep -R --include="*.csv" -n "EWIS" 02-AIRCRAFT/DOMAIN_INTEGRATION/*/SYSTEMS | grep -v "92" >/dev/null 2>&1; then
  echo "[STRUCT] EWIS references outside ATA-92 detected"; fail=1
fi
exit $fail
