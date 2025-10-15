#!/usr/bin/env bash
set -uo pipefail  # Removed -e to continue on errors

ROOT="${1:-.}"
FORCE="${FORCE:-0}"
DRY="${DRY:-0}"
YEAR="$(date +%Y)"

hr() { printf '%*s\n' "${COLUMNS:-80}" '' | tr ' ' '-'; }

write_file() {
  local path="$1" content="$2"
  if [[ "$DRY" == "1" ]]; then
    echo "[DRY] Would write $path"
    return
  fi
  mkdir -p "$(dirname "$path")"
  printf "%s" "$content" > "$path"
}

slug_last() { awk -F'/' '{print $NF}'; }
arch_from_path() {
  local p="$1"
  if [[ "$p" == *"/02-AIRCRAFT/"* ]]; then echo "AIR-T (ATA)"
  elif [[ "$p" == *"/03-SPACECRAFT/"* ]]; then echo "SPACE-T (STA)"
  else echo "Program"; fi
}
domain_from_path() {
  local p="$1"
  if [[ "$p" == *"/DOMAIN_INTEGRATION/"* ]]; then
    echo "$p" | sed -E 's#.*DOMAIN_INTEGRATION/([^/]+).*#\1#'
  else
    echo "N/A"
  fi
}
system_id_from_path() {
  local p="$1"
  echo "$p" | sed -nE 's#.*SYSTEMS/([^/]+)/?.*#\1#p'
}
subsystem_id_from_path() {
  local p="$1"
  echo "$p" | sed -nE 's#.*SUBSYSTEMS/([^/]+)/?.*#\1#p'
}

tpl_generic() {
  local dir="$1" arch="$2" domain="$3"
  cat <<EOF
# README — $(echo "$dir" | slug_last)

**Scope:** Placeholder / directory holder for ${arch} • Domain: ${domain}

## What lives here?

- See sibling folders / instantiated artifacts.
- Contribute following CM: ECR → ECO → baselines + ICDs → *.
- Add docs & tests before models or code.

> Owner: Domain Lead • Status: scaffold • Year: $YEAR
EOF
}

tpl_system() {
  local sys="$1" arch="$2" domain="$3"
  cat <<EOF
# SYSTEM: ${sys}

**Architecture:** ${arch} • **Domain:** ${domain}

## Purpose

Integration anchor for **${sys}** with interface map and views.

## Quick Links

- **Interface Matrix:** \`INTERFACE_MATRIX/*.csv\`
- **Integration View:** \`INTEGRATION_VIEW.md\`
- **Sub-Systems:** \`SUBSYSTEMS/*/\`

## UiX Workflow

1. Define scope & boundaries in \`INTEGRATION_VIEW.md\`
2. Add / extend \`INTERFACE_MATRIX/*.csv\` header below
3. Implement sub-systems in \`SUBSYSTEMS/*/\`

> PLM & CAx **inside each subsystem** only

### CSV Use Everywhere :

\`\`\`csv
from_ata,to_ata,interface,signal_or_medium,protocol/spec,notes
\`\`\`

## Compliance

- **ICDs:** see \`00-PROGRAM/CONFIG_MGMT/09-INTERFACES/\`
- **Baselines & Changes:** \`00-PROGRAM/CONFIG_MGMT/04-BASELINES/\`

EOF
}

tpl_subsystem() {
  local sys="$1" sub="$2" arch="$3" domain="$4"
  cat <<EOF
# SUBSYSTEM: ${sub}

**Under System:** ${sys} • **Architecture:** ${arch} • **Domain:** ${domain}

## Purpose

Implements the sub-assembly with full PLM artifacts.

## Folder Contract

- \`PLM/CAx/*\` → design / reports / MOCs
- \`PLM/EBOM_LINKS.md\` → packaging / on & off-board bundles
- \`META.json\` + \`inherit.json\` → CAD/CAE/CAM only here

## Rules

- **Verification:** see \`README.md\` + template provenance
- **ICDs:** see traceability in \`INTERFACE_MATRIX\`
- **Sourcing:** see \`PLM/EBOM_LINKS.md\`

## How to Contribute

- Keep SW in its host LRU chapter
- EWIS lives in ATA-92; reference via interfaces *.
- Update \`META.json\` with owner & status

EOF
}

tpl_plm() {
  cat <<'EOF'
# PLM — Engineering BOM & CAx

**Authoritative ERP items** see EBOM_LINKS.md.

## Engineering Files

See layout under **CAx/**:

- **CAD**: Mechanical design
- **CAE**: Engineering analysis
- **CAO**: Optimization studies
- **CAM**: Manufacturing data
- **CAI**: Installation drawings
- **CAV**: Validation models
- **CAP**: Procurement specs
- **CAS**: Service (operational) models
- **CMP**: Compliance and Certification post Operation caused Modifications (CoMPost)

## Rules

- No PLM outside SUBSYSTEMS/
- Use neutral formats (STEP / JT / glTF) alongside native where possible.
- Include SBOM / BOM exports in EBOM_LINKS.md

EOF
}

tpl_cax_leaf() {
  local leaf="$1"
  cat <<EOF
# ${leaf}

## What to store

- **Design:** CAD models / drawings
- **Analysis:** FEA decks, scripts, results
- **Mfg / Test:** NC paths, tooling, fixtures, inspection

Commit big binaries via LFS. Provide a short README.md per model with inputs / outputs / solver / tool version.

EOF
}

tpl_ifx_matrix() {
  cat <<'EOF'
# Interface Matrix

Place one CSV per set of interfaces (e.g. \`21↔24_28_30_36_92.csv\`).

## Header:

\`\`\`csv
from_ata,to_ata,interface,signal_or_medium,protocol/spec,notes
\`\`\`

Link from INTEGRATION_VIEW.md. References for physical wiring in ATA-92.

EOF
}

tpl_bez_leaf() {
  local name="$1"
  cat <<EOF
# ${name}

This directory provides templates / policies. Instances do not live here. Schemas / checklists guide contributors.

EOF
}

# Main
mapfile -d '' -t FILES < <(find "$ROOT" -type f -name .gitkeep -print0 | sort -z)
if [[ ${#FILES[@]} -eq 0 ]]; then
  echo "No .gitkeep found in $ROOT"
  exit 0
fi

echo "Found ${#FILES[@]} .gitkeep files"
hr

CREATED=0; SKIPPED=0; ERRORS=0
for keep in "${FILES[@]}"; do
  dir="$(dirname "$keep")"
  readme="$dir/README.md"
  base="$(basename "$dir")"

  # Decide which template
  if [[ "$dir" == *"/PLM/CAx/"* ]]; then
    leaf=$(echo "$dir" | slug_last)
    content=$(tpl_cax_leaf "$leaf")
  elif [[ "$dir" == *"/INTERFACE_MATRIX" ]]; then
    content=$(tpl_ifx_matrix)
  elif [[ "$dir" == *"/PLM" ]] && [[ "$dir" != *"/PLM/CAx/"* ]]; then
    content=$(tpl_plm)
  elif [[ "$dir" == *"/SUBSYSTEMS/"* ]] && [[ "$dir" != *"/PLM"* ]]; then
    sys=$(system_id_from_path "$dir")
    sub=$(subsystem_id_from_path "$dir")
    arch=$(arch_from_path "$dir")
    domain=$(domain_from_path "$dir")
    content=$(tpl_subsystem "${sys:-SYSTEM}" "${sub:-SUBSYSTEM}" "$arch" "$domain")
  elif [[ "$dir" == *"/SYSTEMS/"* ]]; then
    sys=$(system_id_from_path "$dir")
    arch=$(arch_from_path "$dir")
    domain=$(domain_from_path "$dir")
    content=$(tpl_system "${sys:-SYSTEM}" "$arch" "$domain")
  elif [[ "$base" == "DELs" ]] || [[ "$base" == "PAx" ]] || \
       [[ "$base" == "QUANTUM_OA" ]] || [[ "$base" == "SUPPLIERS" ]] || \
       [[ "$base" == "policy" ]] || [[ "$base" == "tests" ]]; then
    content=$(tpl_bez_leaf "$base")
  else
    arch=$(arch_from_path "$dir")
    domain=$(domain_from_path "$dir")
    content=$(tpl_generic "$dir" "$arch" "$domain")
  fi

  # Write or skip
  if [[ -f "$readme" ]] && [[ "$FORCE" != "1" ]]; then
    echo "SKIP: $readme exists"
    ((SKIPPED++))
  else
    if write_file "$readme" "$content"; then
      if [[ "$DRY" != "1" ]]; then
        rm -f "$keep" || echo "WARNING: Could not remove $keep"
        echo "✓ Wrote: $readme | Removed: $keep"
      fi
      ((CREATED++))
    else
      echo "ERROR: Failed to write $readme"
      ((ERRORS++))
    fi
  fi
done

hr
echo "Done. Updated: $CREATED | Skipped: $SKIPPED | Errors: $ERRORS"
echo "Hints: DRY=1 to preview | FORCE=1 to overwrite existing README.md"
