#!/bin/bash
# Collect diagnostic bundle for troubleshooting
# Gathers logs, reports, and system information

set -euo pipefail

# Configuration
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DIAGNOSTICS_ROOT="$(dirname "$SCRIPT_DIR")"
FL_CLIENT_HOME="${FL_CLIENT_HOME:-/var/fl-client}"
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
BUNDLE_NAME="diag_bundle_${TIMESTAMP}.tar.gz"
BUNDLE_DIR="/tmp/diag_bundle_${TIMESTAMP}"

# Logging function
log() {
    echo "[$(date +'%Y-%m-%d %H:%M:%S')] $*"
}

# Error handler
error_exit() {
    log "ERROR: $1"
    exit "${2:-1}"
}

# Create bundle directory
create_bundle_dir() {
    log "Creating bundle directory: ${BUNDLE_DIR}"
    mkdir -p "${BUNDLE_DIR}"
}

# Collect system information
collect_system_info() {
    log "Collecting system information..."
    
    {
        echo "=== System Information ==="
        echo "Hostname: $(hostname)"
        echo "Date: $(date)"
        echo "Uptime: $(uptime)"
        echo ""
        
        echo "=== CPU Info ==="
        lscpu || echo "lscpu not available"
        echo ""
        
        echo "=== Memory Info ==="
        free -h || echo "free not available"
        echo ""
        
        echo "=== Disk Usage ==="
        df -h || echo "df not available"
        echo ""
        
        echo "=== Network Interfaces ==="
        ip addr show || ifconfig || echo "Network info not available"
        echo ""
        
    } > "${BUNDLE_DIR}/system_info.txt" 2>&1
}

# Collect FL client data
collect_fl_data() {
    log "Collecting FL client data..."
    
    if [ -d "${FL_CLIENT_HOME}" ]; then
        # Copy logs
        if [ -d "${FL_CLIENT_HOME}/logs" ]; then
            cp -r "${FL_CLIENT_HOME}/logs" "${BUNDLE_DIR}/" || log "Warning: Failed to copy logs"
        fi
        
        # Copy recent reports
        if [ -d "${FL_CLIENT_HOME}/reports" ]; then
            mkdir -p "${BUNDLE_DIR}/reports"
            find "${FL_CLIENT_HOME}/reports" -name "*.json" -mtime -7 -exec cp {} "${BUNDLE_DIR}/reports/" \; || log "Warning: Failed to copy reports"
        fi
        
        # Collect directory structure
        tree -L 3 "${FL_CLIENT_HOME}" > "${BUNDLE_DIR}/fl_client_structure.txt" 2>&1 || \
            find "${FL_CLIENT_HOME}" -type d > "${BUNDLE_DIR}/fl_client_structure.txt" 2>&1 || \
            log "Warning: Failed to collect directory structure"
    else
        log "Warning: FL client home not found: ${FL_CLIENT_HOME}"
    fi
}

# Collect diagnostic check configurations
collect_check_configs() {
    log "Collecting check configurations..."
    
    if [ -d "${DIAGNOSTICS_ROOT}/CHECKS" ]; then
        cp -r "${DIAGNOSTICS_ROOT}/CHECKS" "${BUNDLE_DIR}/" || log "Warning: Failed to copy check configs"
    fi
    
    if [ -f "${DIAGNOSTICS_ROOT}/TEMPLATES/config.yaml" ]; then
        cp "${DIAGNOSTICS_ROOT}/TEMPLATES/config.yaml" "${BUNDLE_DIR}/" || log "Warning: Failed to copy agent config"
    fi
}

# Collect systemd service status
collect_service_status() {
    log "Collecting service status..."
    
    {
        echo "=== Systemd Service Status ==="
        systemctl status aircraft-diag.service --no-pager 2>&1 || echo "Service status not available"
        echo ""
        
        echo "=== Systemd Timer Status ==="
        systemctl status aircraft-diag.timer --no-pager 2>&1 || echo "Timer status not available"
        echo ""
        
        echo "=== Systemd Journal (last 1000 lines) ==="
        journalctl -u aircraft-diag.service -n 1000 --no-pager 2>&1 || echo "Journal not available"
        
    } > "${BUNDLE_DIR}/service_status.txt" 2>&1
}

# Run diagnostic checks
run_diagnostics() {
    log "Running diagnostic checks..."
    
    AGENT_SCRIPT="${DIAGNOSTICS_ROOT}/AGENTS/diag_agent.py"
    if [ -f "${AGENT_SCRIPT}" ]; then
        python3 "${AGENT_SCRIPT}" > "${BUNDLE_DIR}/diagnostic_run.txt" 2>&1 || log "Warning: Diagnostic run failed"
    else
        log "Warning: Agent script not found"
    fi
}

# Create tarball
create_tarball() {
    log "Creating tarball: ${BUNDLE_NAME}"
    
    cd "$(dirname "${BUNDLE_DIR}")"
    tar -czf "${BUNDLE_NAME}" "$(basename "${BUNDLE_DIR}")" || error_exit "Failed to create tarball" 1
    
    log "Bundle created: $(pwd)/${BUNDLE_NAME}"
    log "Bundle size: $(du -h "${BUNDLE_NAME}" | cut -f1)"
}

# Cleanup
cleanup() {
    log "Cleaning up temporary directory..."
    rm -rf "${BUNDLE_DIR}"
}

# Main execution
main() {
    log "=== Starting diagnostic bundle collection ==="
    
    create_bundle_dir
    collect_system_info
    collect_fl_data
    collect_check_configs
    collect_service_status
    run_diagnostics
    create_tarball
    cleanup
    
    log "=== Diagnostic bundle collection complete ==="
    log "Bundle location: $(pwd)/${BUNDLE_NAME}"
}

# Trap errors
trap 'error_exit "Script failed at line $LINENO"' ERR

# Execute main
main "$@"
