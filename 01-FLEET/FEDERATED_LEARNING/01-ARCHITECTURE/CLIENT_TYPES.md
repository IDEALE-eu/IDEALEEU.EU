# CLIENT_TYPES

Federated learning client types, capabilities, and certification status.

## Overview

The IDEALE FL system supports three client types, each with distinct computational capabilities, data access, connectivity patterns, and certification requirements.

## Client Type Matrix

| Client Type       | Compute     | Connectivity        | Data Access           | Cert Status      | Count Target |
|-------------------|-------------|---------------------|-----------------------|------------------|--------------|
| Aircraft Edge     | Limited     | Intermittent        | Local telemetry only  | DO-178C Level C  | 200          |
| Ground Stations   | High        | Continuous          | Full fleet dataset    | Non-certified    | 10           |
| Simulation Rigs   | Very High   | Continuous          | Synthetic + test data | Non-certified    | 20           |

## 1. Aircraft Edge Clients

### Hardware Profile

**Compute Platform:**
- **Processor**: ARM Cortex-A53 (quad-core, 1.5 GHz) or equivalent
- **Memory**: 4 GB RAM, 32 GB storage (SSD)
- **GPU/TPU**: Optional edge AI accelerator (e.g., Coral TPU, NVIDIA Jetson Nano)
- **Power Budget**: ≤ 50W continuous, ≤ 100W peak
- **Thermal**: Operating range -40°C to +85°C (DO-160 Category A)

**Connectivity:**
- **Primary**: LEO satellite (Starlink, OneWeb) - 50-200 Mbps downlink
- **Secondary**: GEO satellite (traditional SATCOM) - 1-10 Mbps
- **Tertiary**: Ground station uplink when landed

**Sensor Interfaces:**
- ARINC 429, ARINC 664 (AFDX), MIL-STD-1553
- CAN bus, Ethernet (avionics and sensors)
- Time-series telemetry: 100-1000 Hz sample rates

### Software Stack

**Operating System:**
- Real-time OS (e.g., VxWorks, QNX) or Linux with RT_PREEMPT patch
- ARINC 653 partitioning for safety-critical isolation

**FL Client Software:**
- **Runtime**: TensorFlow Lite, ONNX Runtime, PyTorch Mobile
- **Framework**: Flower (federated learning framework) or custom client
- **Sandboxing**: Docker/containerd with resource limits (cgroups)

**Resource Constraints:**
- CPU usage: ≤ 30% during training (non-flight-critical partition)
- Memory: ≤ 1 GB for FL client
- Disk I/O: ≤ 10 MB/s (avoid SSD wear)
- Network: Upload ≤ 100 MB per training round

### Certification Status

**DO-178C Classification:**
- **Level C (Major)** - Failure could significantly reduce safety margins
- **Rationale**: FL models are advisory; no direct actuation on flight controls
- **Evidence Required**: Software verification plan, test cases, traceability matrix

**DO-326A (Cybersecurity):**
- Security risk assessment
- Threat modeling (see [05-PRIVACY_SECURITY/THREAT_MODEL.md](05-PRIVACY_SECURITY/THREAT_MODEL.md))
- Penetration testing (quarterly)

**Safety Boundaries:**
- FL training only during cruise phase (altitude > 10,000 ft)
- Automatic suspension if CPU temp > 75°C or power > 100W
- No training during critical flight phases (takeoff, landing, emergency)

### Data Access

**Local Data Only:**
- Flight telemetry (airspeed, altitude, fuel, engine parameters)
- Environmental sensors (temperature, pressure, turbulence)
- System health (CPU, memory, disk, network)
- Maintenance logs (from onboard HUMS)

**Privacy Controls:**
- No PII (Personally Identifiable Information)
- Pseudonymised aircraft ID (cryptographic hash of tail number)
- Differential privacy (ε=1.0, δ=1e-5) applied to gradients

### Typical Use Cases

- Predictive maintenance models (bearing wear, component fatigue)
- Flight envelope optimization (fuel efficiency, trajectory)
- Anomaly detection (sensor drift, system faults)

## 2. Ground Station Clients

### Hardware Profile

**Compute Platform:**
- **Processor**: Intel Xeon or AMD EPYC (16-64 cores)
- **Memory**: 128 GB - 512 GB RAM
- **GPU**: NVIDIA A100 or H100 (for large-scale training)
- **Storage**: 10 TB - 100 TB (RAID array)
- **Power**: Data center UPS and cooling

**Connectivity:**
- Fiber optic (10 Gbps+)
- Direct internet access with redundancy
- VPN to aggregation server

### Software Stack

**Operating System:**
- Ubuntu 22.04 LTS or RHEL 8/9
- Kubernetes for containerized FL clients

**FL Client Software:**
- Full PyTorch or TensorFlow (not lite versions)
- Flower FL framework or PySyft
- MLflow for experiment tracking

### Certification Status

**Non-certified:**
- Ground stations do not require DO-178C or ECSS certification
- Subject to IT security policies (ISO 27001)

### Data Access

**Full Fleet Dataset:**
- Aggregated telemetry from all aircraft (historical and real-time)
- Maintenance records (MRO database)
- Flight operations data (routes, weather, scheduling)

**Role in FL:**
- **Data augmentation**: Supplement aircraft data with ground-based analytics
- **Validation**: Test models on historical data before deployment
- **Baseline training**: Train initial models before fleet deployment

### Typical Use Cases

- Fleet-wide anomaly detection (cross-aircraft pattern recognition)
- Predictive maintenance at scale (trend analysis across tail numbers)
- Digital twin calibration (physics-informed models)

## 3. Simulation Rig Clients

### Hardware Profile

**Compute Platform:**
- High-performance workstations or cloud instances (AWS, Azure, GCP)
- **Processor**: Intel i9 or AMD Ryzen 9 (16-32 cores)
- **Memory**: 64 GB - 256 GB RAM
- **GPU**: NVIDIA RTX 4090 or A40 (for simulation rendering and ML)
- **Storage**: 1 TB - 10 TB NVMe SSD

**Connectivity:**
- Data center LAN (10 Gbps+)
- Private network (no external internet access for security)

### Software Stack

**Simulation Environments:**
- **HIL (Hardware-in-Loop)**: Real avionics hardware with simulated environment
- **SIL (Software-in-Loop)**: Fully software-based simulation
- **Digital Twin**: High-fidelity physics models (see 00-PROGRAM/DIGITAL_THREAD/05-DIGITAL_TWIN/)

**FL Client Software:**
- Full ML frameworks (PyTorch, TensorFlow, JAX)
- Custom simulation interfaces (e.g., X-Plane, FlightGear, Simulink)

### Certification Status

**Non-certified:**
- Simulation rigs are development/testing environments
- Not subject to DO-178C, but follow IEC 61508 for functional safety testing

### Data Access

**Synthetic and Test Data:**
- Simulated flight scenarios (nominal and failure modes)
- Stress testing (extreme weather, system failures)
- Edge case data (rare events unlikely to occur in fleet)

**Role in FL:**
- **Pre-deployment validation**: Test FL algorithms before aircraft rollout
- **Fault injection**: Train models on failure scenarios
- **Certification evidence**: Generate test data for DO-178C compliance

### Typical Use Cases

- Training models for rare failure modes (engine stall, sensor loss)
- Validating FL convergence under adversarial conditions
- Safety case generation for certification authorities

## Client Selection Criteria

### Eligibility Requirements

**Aircraft:**
- Must be post-maintenance (no open NCRs in FL-relevant systems)
- Minimum 50 flight hours since last FL model deployment
- Hardware health check passed (CPU, memory, disk, network)

**Ground Stations:**
- Active participation in all training rounds (unless scheduled maintenance)
- Data quality checks passed (no missing or corrupted telemetry)

**Simulation Rigs:**
- On-demand participation (used for specific experiments only)
- Validation data available for target use case

### Client Fairness

- **Minimum participation**: Each client must contribute ≥ 3 training rounds per quarter
- **Data distribution**: Balance across flight phases, weather conditions, aircraft types
- **Computational fairness**: Aggregation weights adjusted for client compute capability

## Related Documents

- [**FL_TOPOLOGY.md**](FL_TOPOLOGY.md) - Network topology and communication patterns
- [**02-ORCHESTRATION/CLIENT_SELECTION.md**](../02-ORCHESTRATION/CLIENT_SELECTION.md) - Client selection algorithms
- [**03-CLIENTS/**](../03-CLIENTS/) - Detailed client implementation specifications
- [**08-VALIDATION_VVP/TEST_PLANS.md**](../08-VALIDATION_VVP/TEST_PLANS.md) - Client validation procedures

## Change History

| Version | Date    | Changes                        | Author    |
|---------|---------|--------------------------------|-----------|
| 1.0     | 2024-Q4 | Initial client type definition | AI/ML Team|
