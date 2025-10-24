#!/usr/bin/env bash
set -euo pipefail

# ci_smoke.sh - Run smoke tests for CAE cases
# This script runs fast, coarse cases suitable for CI environments

echo "=========================================="
echo "CAE Smoke Test Suite"
echo "=========================================="

# Store script directory
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
CAE_ROOT="$(dirname "$SCRIPT_DIR")"

echo "CAE Root: $CAE_ROOT"
echo ""

# Step 1: Check metadata
echo "Step 1: Checking metadata..."
python3 "$SCRIPT_DIR/check_metadata.py" --dir "$CAE_ROOT" || {
    echo "ERROR: Metadata validation failed"
    exit 1
}
echo "✓ Metadata check passed"
echo ""

# Step 2: Run CFD smoke case (if exists)
CFD_SMOKE="$CAE_ROOT/CFD/cases/tank_solidification/smoke"
if [ -d "$CFD_SMOKE" ]; then
    echo "Step 2: Running CFD smoke case..."
    python3 "$SCRIPT_DIR/cfd_runner.py" --case "$CFD_SMOKE" --timeout 600 || {
        echo "ERROR: CFD smoke case failed"
        exit 1
    }
    echo "✓ CFD smoke case passed"
    echo ""
    
    # Step 3: Export CFD metrics
    echo "Step 3: Exporting CFD metrics..."
    python3 "$SCRIPT_DIR/export_metrics.py" --case "$CFD_SMOKE" || {
        echo "ERROR: CFD metrics export failed"
        exit 1
    }
    echo "✓ CFD metrics exported"
    echo ""
else
    echo "Step 2: Skipping CFD smoke case (not found)"
    echo ""
fi

# Step 4: Run FEA smoke case (if exists)
FEA_SMOKE="$CAE_ROOT/FEA/cases/static_stress/smoke"
if [ -d "$FEA_SMOKE" ]; then
    echo "Step 4: Running FEA smoke case..."
    python3 "$SCRIPT_DIR/fea_runner.py" --case "$FEA_SMOKE" --timeout 600 || {
        echo "ERROR: FEA smoke case failed"
        exit 1
    }
    echo "✓ FEA smoke case passed"
    echo ""
    
    # Step 5: Export FEA metrics
    echo "Step 5: Exporting FEA metrics..."
    python3 "$SCRIPT_DIR/export_metrics.py" --case "$FEA_SMOKE" || {
        echo "ERROR: FEA metrics export failed"
        exit 1
    }
    echo "✓ FEA metrics exported"
    echo ""
else
    echo "Step 4: Skipping FEA smoke case (not found)"
    echo ""
fi

echo "=========================================="
echo "All smoke tests passed!"
echo "=========================================="
exit 0
