#!/bin/bash
# Run diagnostic checks and generate report
# This script is called by the systemd service

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIAGNOSTICS_ROOT="$(dirname "$SCRIPT_DIR")"
AGENT_SCRIPT="${DIAGNOSTICS_ROOT}/AGENTS/diag_agent.py"
LOG_DIR="${FL_CLIENT_HOME:-/var/fl-client}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

# Ensure log directory exists
mkdir -p "${LOG_DIR}/logs"

# Logging function
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*" | tee -a "${LOG_DIR}/logs/run_checks.log"
}

# Error handler
error_exit() {
    log "ERROR: $1"
    exit "${2:-1}"
}

# Main execution
main() {
    log "=== Starting diagnostic checks ==="
    
    # Check if Python is available
    if ! command -v python3 &> /dev/null; then
        error_exit "Python 3 not found" 1
    fi
    
    # Check if agent script exists
    if [ ! -f "${AGENT_SCRIPT}" ]; then
        error_exit "Agent script not found: ${AGENT_SCRIPT}" 1
    fi
    
    # Run diagnostic agent
    log "Running diagnostic agent..."
    if python3 "${AGENT_SCRIPT}" >> "${LOG_DIR}/logs/run_checks.log" 2>&1; then
        EXIT_CODE=$?
        log "Diagnostic checks completed successfully (exit code: ${EXIT_CODE})"
        exit ${EXIT_CODE}
    else
        EXIT_CODE=$?
        log "Diagnostic checks failed (exit code: ${EXIT_CODE})"
        exit ${EXIT_CODE}
    fi
}

# Trap errors
trap 'error_exit "Script failed at line $LINENO"' ERR

# Execute main
main "$@"
