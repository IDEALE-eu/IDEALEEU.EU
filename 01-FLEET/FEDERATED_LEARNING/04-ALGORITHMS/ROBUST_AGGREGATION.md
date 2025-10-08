# ROBUST_AGGREGATION

Byzantine-resilient aggregation methods for adversarial settings.

## Overview

Protect against malicious or compromised clients sending corrupted model updates.

## Methods

### Krum

- Select client update closest to others (geometric median)
- **Byzantine tolerance**: Tolerate f < n/2 - 1 malicious clients
- **Trade-off**: Slower convergence (less averaging)

### TrimmedMean

- Sort updates, remove top/bottom 10%, average remainder
- **Byzantine tolerance**: Tolerate f < n/4 malicious clients
- **Trade-off**: Reduced noise robustness

### Median

- Coordinate-wise median of updates
- **Byzantine tolerance**: Tolerate f < n/2 malicious clients
- **Trade-off**: Slow, not always convergent

## When to Use

- **Krum**: High-risk environment (known adversaries)
- **TrimmedMean**: Moderate risk, faster than Krum
- **FedAvg**: Low risk, trusted clients (default)

## Related Documents

- [**../05-PRIVACY_SECURITY/THREAT_MODEL.md**](../05-PRIVACY_SECURITY/THREAT_MODEL.md) - Threat analysis
- [**../02-ORCHESTRATION/CLIENT_SELECTION.md**](../02-ORCHESTRATION/CLIENT_SELECTION.md) - Blacklist policy
