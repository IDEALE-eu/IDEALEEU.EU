# EDGE RUNTIME PROFILE

**📍 [IDEALE-EU](../../../../) > [02-AIRCRAFT](../../../) > [DIGITAL_TWIN_MODEL](../../) > 07-RUNTIME_DEPLOYMENT/RUNTIME_PROFILES > EDGE**

On-aircraft edge runtime: CPU% <15%, no remote updates in flight.

## Purpose

Runtime profile for digital twin models deployed on aircraft IMA (Integrated Modular Avionics).

## Constraints

- **CPU Usage**: <15% sustained (safety-of-flight constraint)
- **Memory**: <256 MB for twin runtime + models
- **Storage**: <1 GB for models + cache
- **Network**: Intermittent connectivity, no internet dependency for safety-critical functions
- **Updates**: No remote updates during flight, only on ground with parking brake set

## Deployed Models

### Real-Time Models (Level 5)
- Anomaly detection (H₂ leak, engine health)
- Health monitoring (system status, alerts)
- Predictive alerts (threshold monitoring)

### Model Types
- **ONNX**: Neural network models (optimized for CPU inference)
- **Lookup Tables**: Aerodynamics polars, engine maps
- **State Machines**: Behavioral models (compiled C/C++)

## Compute Environment

- **Hardware**: Aircraft IMA, x86 or ARM-based
- **OS**: Real-time OS (e.g., VxWorks, QNX)
- **Runtime**: ONNX Runtime (CPU-only), custom model loaders
- **Isolation**: Containerized (Docker) or partitioned (ARINC 653)

## Data Flow

```
[Aircraft Sensors] → [ACMS] → [Edge Twin Runtime]
                                     ↓
                        [Anomaly Detection] → [Alerts to Crew]
                                     ↓
                        [Data Buffering] → [Datalink to Ground]
```

## Deployment Process

1. **Model Validation**: V&V on ground (see `../../06-VALIDATION_VERIFICATION/`)
2. **Signing**: GPG sign models (see `../../07-RUNTIME_DEPLOYMENT/CYBERSECURITY.md`)
3. **Transfer**: Secure file transfer to aircraft (USB or datalink, on ground only)
4. **Verification**: Signature verification before loading
5. **Activation**: Load models, execute smoke tests
6. **Monitoring**: Continuous CPU/memory monitoring

## Related Documents

- **../SAFETY_GUARDS.md** - Safety constraints
- **../CYBERSECURITY.md** - Secure boot, model signing

---

**Status**: Configuration-controlled per `00-PROGRAM/CONFIG_MGMT/`
