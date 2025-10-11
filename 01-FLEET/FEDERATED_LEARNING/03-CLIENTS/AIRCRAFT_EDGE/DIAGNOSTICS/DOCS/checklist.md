# Diagnostics Deployment Checklist

Pre-deployment checklist for aircraft edge FL client diagnostics system.

## Pre-Deployment

### System Requirements
- [ ] Linux OS with systemd (Ubuntu 20.04+ or RHEL 8+)
- [ ] Python 3.8 or higher installed
- [ ] Minimum 1GB RAM available for FL client
- [ ] Minimum 10GB disk space for FL data
- [ ] Network connectivity to FL server

### Python Dependencies
- [ ] `psutil` installed (`pip install psutil`)
- [ ] `PyYAML` installed (`pip install PyYAML`)
- [ ] `jsonschema` installed (`pip install jsonschema`)
- [ ] `pynvml` installed if using GPU (`pip install pynvml`)
- [ ] `docker` Python SDK installed if using Docker (`pip install docker`)

### Directory Structure
- [ ] `/var/fl-client` created with correct permissions
- [ ] `/var/fl-client/logs` created
- [ ] `/var/fl-client/reports` created
- [ ] `/var/fl-client/models` created
- [ ] `/var/fl-client/gradients` created
- [ ] `/etc/fl-client/certs` created with secure permissions (700)

### Configuration Files
- [ ] `CHECKS/*.yaml` files present and valid
- [ ] `TEMPLATES/config.yaml` customized for aircraft
- [ ] `TEMPLATES/alert_rules.yaml` reviewed and approved
- [ ] `SCHEMAS/*.schema.json` files present

### Security
- [ ] Client certificate installed in `/etc/fl-client/certs/client.crt`
- [ ] Private key installed in `/etc/fl-client/certs/client.key` (permissions 600)
- [ ] CA certificate installed in `/etc/fl-client/certs/ca.crt`
- [ ] Certificate expiry date verified (> 30 days)
- [ ] File permissions verified on all certificate files
- [ ] TLS 1.2+ enforced

### Systemd Configuration
- [ ] `aircraft-diag.service` copied to `/etc/systemd/system/`
- [ ] `aircraft-diag.timer` copied to `/etc/systemd/system/`
- [ ] Service file permissions set to 644
- [ ] User `fl-client` exists on system
- [ ] Group `fl-client` exists on system
- [ ] Service unit paths updated if necessary

### Resource Limits
- [ ] CPU quota set to 30% in service file
- [ ] Memory limit set to 1GB in service file
- [ ] cgroups configured and working
- [ ] Resource limits tested under load

## Deployment

### Installation
- [ ] Diagnostic agent script deployed to `/opt/fl-client/diagnostics/AGENTS/`
- [ ] Check files deployed to `/opt/fl-client/diagnostics/CHECKS/`
- [ ] Scripts deployed to `/opt/fl-client/diagnostics/SCRIPTS/`
- [ ] Scripts made executable (`chmod +x *.sh`)
- [ ] All files owned by `fl-client:fl-client`

### Logrotate Configuration
- [ ] `logrotate.conf` copied to `/etc/logrotate.d/fl-client`
- [ ] Logrotate configuration tested (`logrotate -d /etc/logrotate.d/fl-client`)

### Service Activation
- [ ] Systemd daemon reloaded (`systemctl daemon-reload`)
- [ ] Service enabled (`systemctl enable aircraft-diag.service`)
- [ ] Timer enabled (`systemctl enable aircraft-diag.timer`)
- [ ] Service started (`systemctl start aircraft-diag.service`)
- [ ] Timer started (`systemctl start aircraft-diag.timer`)
- [ ] Service status verified (`systemctl status aircraft-diag.service`)
- [ ] Timer status verified (`systemctl status aircraft-diag.timer`)

## Post-Deployment

### Functional Testing
- [ ] Diagnostic agent runs successfully (`./SCRIPTS/run_checks.sh`)
- [ ] Diagnostic report generated in `/var/fl-client/reports/`
- [ ] Report validates against schema (`./TESTS/validate_reports.py`)
- [ ] All check categories execute (health, network, storage, security, training)
- [ ] Logs written to `/var/fl-client/diagnostics.log`
- [ ] Bundle collection works (`./SCRIPTS/collect_bundle.sh`)

### Health Checks
- [ ] CPU check passes
- [ ] Memory check passes
- [ ] Disk check passes
- [ ] GPU check passes (if applicable)
- [ ] Network connectivity check passes
- [ ] Storage check passes
- [ ] Security check passes
- [ ] Training environment check passes

### Alert Testing
- [ ] Critical alert triggered successfully (test condition)
- [ ] Warning alert triggered successfully (test condition)
- [ ] Alert notifications sent to correct channels
- [ ] Alert cooldown working correctly

### Telemetry
- [ ] Reports published to MQTT topic
- [ ] FL orchestrator receiving reports
- [ ] System health monitor receiving alerts
- [ ] Report retention working (24 hours for reports)

### Performance Verification
- [ ] Diagnostic agent completes in < 10 seconds
- [ ] CPU usage during check < 10%
- [ ] Memory usage during check < 100MB
- [ ] No impact on flight-critical systems verified
- [ ] Timer interval verified (60 seconds)

### Integration Testing
- [ ] FL orchestrator uses diagnostic data for client selection
- [ ] Unhealthy clients automatically excluded from training
- [ ] Training deferred when network down
- [ ] Training suspended when storage critical

## Operational Readiness

### Documentation
- [ ] Error codes documented and understood
- [ ] Alert response procedures documented
- [ ] Escalation procedures defined
- [ ] Operator training completed

### Monitoring
- [ ] Dashboard configured to show fleet health
- [ ] Alerts configured in monitoring system
- [ ] On-call rotation established
- [ ] Incident response procedures tested

### Backup and Recovery
- [ ] Configuration files backed up
- [ ] Certificate backup procedure in place
- [ ] Recovery procedure documented and tested
- [ ] Rollback plan prepared

### Compliance
- [ ] Security review completed
- [ ] Privacy requirements met
- [ ] Regulatory requirements verified
- [ ] Audit logging enabled

## Pre-Flight Checklist

Run before each flight with FL training enabled:

- [ ] Diagnostic agent running (`systemctl status aircraft-diag.timer`)
- [ ] Recent diagnostic report generated (< 5 minutes old)
- [ ] Overall status: `healthy`
- [ ] All certificates valid
- [ ] Network connectivity to FL server verified
- [ ] Sufficient disk space (< 75% used)
- [ ] Training environment ready

## Troubleshooting

If diagnostics fail:
1. Check logs: `/var/fl-client/diagnostics.log`
2. Check systemd journal: `journalctl -u aircraft-diag.service`
3. Run manually: `python3 /opt/fl-client/diagnostics/AGENTS/diag_agent.py`
4. Collect diagnostic bundle: `./SCRIPTS/collect_bundle.sh`
5. Contact support with bundle file

## Sign-Off

- [ ] Development team sign-off
- [ ] QA team sign-off
- [ ] Security team sign-off
- [ ] Operations team sign-off
- [ ] Flight operations team sign-off

---

**Date**: _______________  
**Deployed By**: _______________  
**Verified By**: _______________  
**Aircraft ID**: _______________  

## Related Documents

- [**error_codes.md**](error_codes.md) - Error code reference
- [**../00-README.md**](../00-README.md) - Diagnostics overview
- [**../../RUNTIME_CONSTRAINTS.md**](../../RUNTIME_CONSTRAINTS.md) - Resource constraints
- [**../../SANDBOXING.md**](../../SANDBOXING.md) - Security isolation
