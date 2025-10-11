# Error Codes

Diagnostic error codes and their meanings.

## Health Check Errors (H-xxx)

### H-001: CPU Usage Exceeds Threshold
**Severity**: Critical  
**Condition**: CPU usage > 75%  
**Action**: Suspend training, yield CPU to flight-critical systems  
**Recovery**: Automatic when CPU usage drops below threshold  

### H-002: CPU Temperature Critical
**Severity**: Critical  
**Condition**: CPU temperature > 75°C  
**Action**: Suspend training immediately, throttle CPU  
**Recovery**: Manual verification required after cooling  

### H-003: Memory Usage High
**Severity**: Warning  
**Condition**: Memory usage > 70%  
**Action**: Clear caches, log warning  
**Recovery**: Automatic cache cleanup  

### H-004: Memory Usage Critical
**Severity**: Critical  
**Condition**: Memory usage > 80%  
**Action**: Suspend training, clear all caches  
**Recovery**: Automatic when memory usage drops  

### H-005: GPU Temperature Critical
**Severity**: Critical  
**Condition**: GPU temperature > 85°C  
**Action**: Suspend training immediately  
**Recovery**: Automatic when GPU temperature drops below 80°C  

### H-006: Disk Space Low
**Severity**: Warning  
**Condition**: Disk usage > 75%  
**Action**: Trigger cleanup of old gradients/logs  
**Recovery**: Automatic after cleanup  

### H-007: Disk Space Critical
**Severity**: Critical  
**Condition**: Disk usage > 85%  
**Action**: Suspend training, emergency cleanup  
**Recovery**: Manual verification required  

## Network Errors (N-xxx)

### N-001: Central Server Unreachable
**Severity**: Critical  
**Condition**: Cannot connect to FL server for > 5 minutes  
**Action**: Defer training, retry with exponential backoff  
**Recovery**: Automatic when connectivity restored  

### N-002: High Latency
**Severity**: Warning  
**Condition**: Network latency > 500ms for > 5 minutes  
**Action**: Log warning, continue with reduced priority  
**Recovery**: Automatic when latency drops  

### N-003: Packet Loss
**Severity**: Warning  
**Condition**: Packet loss > 5%  
**Action**: Log warning, reduce upload rate  
**Recovery**: Automatic when packet loss drops  

### N-004: Bandwidth Insufficient
**Severity**: Warning  
**Condition**: Available bandwidth < 5 Mbps  
**Action**: Skip large model downloads  
**Recovery**: Automatic when bandwidth improves  

## Storage Errors (S-xxx)

### S-001: Data Directory Missing
**Severity**: Critical  
**Condition**: /var/fl-client directory does not exist  
**Action**: Suspend all operations, alert operator  
**Recovery**: Manual creation of directory required  

### S-002: Data Directory Size Exceeded
**Severity**: Critical  
**Condition**: FL data directory > 10GB  
**Action**: Emergency cleanup, suspend training  
**Recovery**: Manual verification after cleanup  

### S-003: Model File Integrity Failed
**Severity**: Critical  
**Condition**: Model checksum verification failed  
**Action**: Delete corrupted model, re-download  
**Recovery**: Automatic after successful re-download  

### S-004: Log Rotation Failed
**Severity**: Warning  
**Condition**: Log files not rotated properly  
**Action**: Manual log rotation  
**Recovery**: Manual intervention required  

## Security Errors (SEC-xxx)

### SEC-001: Certificate Expired
**Severity**: Critical  
**Condition**: Client certificate expired  
**Action**: Suspend all operations immediately  
**Recovery**: Manual certificate renewal required  

### SEC-002: Certificate Expiring Soon
**Severity**: Warning  
**Condition**: Certificate expires in < 30 days  
**Action**: Alert security team  
**Recovery**: Manual certificate renewal recommended  

### SEC-003: Insecure File Permissions
**Severity**: Warning  
**Condition**: Private key has permissions other than 600/400  
**Action**: Log warning, alert security team  
**Recovery**: Manual permission correction  

### SEC-004: TLS Version Insecure
**Severity**: Critical  
**Condition**: TLS version < 1.2  
**Action**: Upgrade TLS version  
**Recovery**: Manual configuration required  

### SEC-005: Weak Cipher Suite
**Severity**: Warning  
**Condition**: Weak cipher suite in use  
**Action**: Configure stronger cipher suite  
**Recovery**: Manual configuration recommended  

## Training Environment Errors (T-xxx)

### T-001: Docker Not Available
**Severity**: Critical  
**Condition**: Docker daemon not running  
**Action**: Skip training round  
**Recovery**: Automatic when Docker starts  

### T-002: Docker Image Missing
**Severity**: Critical  
**Condition**: Required Docker image not present  
**Action**: Skip training round, attempt pull  
**Recovery**: Automatic after successful pull  

### T-003: Docker Image Version Mismatch
**Severity**: Warning  
**Condition**: Docker image version too old  
**Action**: Log warning, continue with old version  
**Recovery**: Manual update recommended  

### T-004: FL Client Process Not Running
**Severity**: Warning  
**Condition**: FL client process not found  
**Action**: Attempt to start process  
**Recovery**: Automatic process restart  

### T-005: Python Environment Invalid
**Severity**: Critical  
**Condition**: Required Python packages missing  
**Action**: Skip training round  
**Recovery**: Manual package installation required  

### T-006: Model Inference Test Failed
**Severity**: Warning  
**Condition**: Test inference exceeds latency threshold  
**Action**: Log warning, continue  
**Recovery**: Automatic monitoring  

### T-007: Training Phase Invalid
**Severity**: Info  
**Condition**: Aircraft not in cruise phase  
**Action**: Defer training until cruise phase  
**Recovery**: Automatic when entering cruise phase  

## System Errors (SYS-xxx)

### SYS-001: Diagnostic Agent Crash
**Severity**: Critical  
**Condition**: Agent process crashed unexpectedly  
**Action**: Restart agent via systemd  
**Recovery**: Automatic via systemd restart policy  

### SYS-002: Schema Validation Failed
**Severity**: Warning  
**Condition**: Report does not match schema  
**Action**: Log error, skip publishing  
**Recovery**: Automatic in next cycle  

### SYS-003: Telemetry Publish Failed
**Severity**: Warning  
**Condition**: Cannot publish to MQTT broker  
**Action**: Queue report for later, retry  
**Recovery**: Automatic when connectivity restored  

## Error Response Priority

1. **Critical** (Immediate Action)
   - Suspend operations
   - Alert operator
   - Log to local and remote
   
2. **Warning** (Degraded Operation)
   - Log warning
   - Attempt remediation
   - Continue with reduced capability
   
3. **Info** (Normal Operation)
   - Log for monitoring
   - No immediate action
   - Informational only

## Related Documents

- [**checklist.md**](checklist.md) - Pre-deployment checklist
- [**../00-README.md**](../00-README.md) - Diagnostics overview
- [**../TEMPLATES/alert_rules.yaml**](../TEMPLATES/alert_rules.yaml) - Alert rule configuration
