# CONNECTIVITY_PROFILES

Network connectivity profiles for federated learning clients.

## Overview

This document defines the network connectivity characteristics, bandwidth caps, latency requirements, and recovery strategies for FL clients operating over heterogeneous communication links.

## Connectivity Matrix

| Client Type     | Primary Link      | Latency (ms) | Bandwidth (Mbps) | Availability | Fallback          |
|-----------------|-------------------|--------------|------------------|--------------|-------------------|
| Aircraft (LEO)  | Starlink/OneWeb   | 20-40        | 50-200 ↓ / 10-40 ↑ | 95%+         | GEO SATCOM        |
| Aircraft (GEO)  | Traditional SATCOM| 500-700      | 1-10 ↓ / 0.5-2 ↑   | 80-90%       | Ground station    |
| Ground Stations | Fiber / Ethernet  | 5-20         | 1000+ ↓↑         | 99.9%        | 4G/5G backup      |
| Sim Rigs        | Data center LAN   | < 1          | 10,000+ ↓↑       | 99.99%       | None (local only) |

## LEO Satellite Connectivity (Primary for Aircraft)

### Characteristics

**Providers:**
- Starlink (SpaceX)
- OneWeb (Eutelsat)

**Coverage:**
- **Global**: 95%+ coverage including polar regions
- **Altitude**: Service available from ground to FL450 (45,000 ft)
- **No blackout zones**: Continuous coverage (no orbital gaps)

**Performance:**
- **Latency**: 20-40 ms (comparable to terrestrial fiber)
- **Bandwidth**: 50-200 Mbps downlink, 10-40 Mbps uplink
- **Jitter**: < 10 ms (suitable for real-time applications)
- **Packet loss**: < 1% (under normal conditions)

### FL-Specific Configuration

**Upload Profiles:**
- **Compressed gradients**: 5-20 MB per upload (FP16, INT8 quantization)
- **Full model weights**: 50-200 MB per download (initial model distribution)
- **Heartbeat messages**: 1 KB every 60 seconds (client health check)

**Bandwidth Allocation:**
- **Training phase**: Low priority (best-effort, < 1 Mbps background)
- **Upload phase**: Medium priority (burst to 10 Mbps for gradient upload)
- **Download phase**: High priority (full bandwidth for model distribution)

**QoS Settings:**
- DSCP marking: AF21 (Assured Forwarding, medium priority)
- Rate limiting: 20 Mbps max burst (to avoid congestion)

### Blackout Recovery

**Causes:**
- Satellite handoff (switching between satellites)
- Extreme weather (heavy rain, lightning)
- Interference (rare)

**Detection:**
- Heartbeat timeout: > 5 minutes without response
- Upload failure: 3 consecutive failed attempts

**Recovery Strategy:**
1. **Retry with exponential backoff**: 1 min, 5 min, 15 min
2. **Fallback to GEO SATCOM**: If LEO unavailable for > 30 minutes
3. **Store-and-forward**: Queue gradients, upload during next flight
4. **Ground station uplink**: Upload when aircraft lands (last resort)

## GEO Satellite Connectivity (Fallback for Aircraft)

### Characteristics

**Providers:**
- Inmarsat
- Iridium
- Thuraya

**Coverage:**
- **Global**: 80-90% coverage (gaps over polar regions)
- **Altitude**: Service available from ground to FL500 (50,000 ft)
- **Blackout zones**: Polar latitudes > 70°N/S

**Performance:**
- **Latency**: 500-700 ms (round-trip to geostationary orbit)
- **Bandwidth**: 1-10 Mbps downlink, 0.5-2 Mbps uplink (shared)
- **Jitter**: 50-100 ms (high variability)
- **Packet loss**: 2-5% (under normal conditions)

### FL-Specific Configuration

**Upload Profiles:**
- **Compressed gradients only**: 2-5 MB per upload (INT8, top-k sparsification)
- **No full model downloads**: Too slow; use LEO or ground station
- **Heartbeat messages**: 1 KB every 120 seconds (less frequent)

**Bandwidth Allocation:**
- **Upload phase**: Low priority (avoid congestion on shared link)
- **Rate limiting**: 1 Mbps max burst

**QoS Settings:**
- DSCP marking: AF11 (Assured Forwarding, low priority)
- Avoid large uploads during high-traffic periods

### Usage Policy

**When to Use GEO:**
- LEO unavailable or degraded
- Aircraft in polar region (> 70°N/S latitude)
- Emergency model update (critical safety fix)

**When NOT to Use GEO:**
- Routine training rounds (too slow)
- Large model distribution (use ground station instead)
- Non-critical updates (wait for LEO recovery)

## Ground Station Connectivity (Ground-Based Clients)

### Characteristics

**Primary Link:**
- Fiber optic or 1 Gbps+ Ethernet
- Latency: 5-20 ms (within continent)
- Availability: 99.9% (SLA guaranteed)

**Fallback Link:**
- 4G/5G cellular (backup)
- Latency: 30-50 ms
- Bandwidth: 50-100 Mbps

### FL-Specific Configuration

**Upload Profiles:**
- **Full gradients**: 50-200 MB (no compression needed)
- **Full model weights**: 50-200 MB download
- **Continuous heartbeat**: 1 KB every 30 seconds

**Bandwidth Allocation:**
- No restrictions (dedicated FL traffic)
- QoS: High priority (DSCP EF - Expedited Forwarding)

### Redundancy

- Active-active fiber links (load balanced)
- Automatic failover to 4G/5G (< 10 seconds)
- UPS power backup (4-hour runtime)

## Simulation Rig Connectivity (Data Center)

### Characteristics

**Link:**
- Data center LAN (10 Gbps+)
- Latency: < 1 ms (same rack) to 5 ms (cross-DC)
- Availability: 99.99%

**FL-Specific Configuration:**
- No bandwidth restrictions
- Local aggregation server (no internet transit)

## Bandwidth Optimization Strategies

### Gradient Compression

**Quantization:**
- FP32 → FP16: 50% size reduction, <1% accuracy loss
- FP16 → INT8: 75% size reduction, 1-3% accuracy loss
- See 04-ALGORITHMS/COMPRESSION.md for details

**Sparsification:**
- Top-k gradients: Keep only top 10% of gradients by magnitude
- Random sparsification: 90% sparsity with error correction
- 90% size reduction, 2-5% accuracy loss

**Delta Compression:**
- Send only parameter differences from previous round
- 40-60% size reduction (depends on model convergence)

### Scheduled Uploads

**Off-Peak Hours:**
- Aircraft: During cruise phase (minimal cockpit activity)
- Ground stations: 2:00-6:00 AM local time (low network usage)

**Upload Batching:**
- Aggregate multiple clients' gradients before upload (ground stations only)
- Reduces overhead, increases throughput

## Latency Requirements

### Training Round Latency Budget

| Phase                  | Duration | Latency Impact  |
|------------------------|----------|-----------------|
| Model distribution     | 1-4 hours| High (depends on bandwidth) |
| Local training         | 24-72 hours | Low (async) |
| Gradient upload        | 1-4 hours| High (depends on bandwidth) |
| Aggregation            | 30 min   | Medium (server-side) |
| Validation             | 1-2 hours| Low (server-side) |
| **Total round time**   | **3-5 days** | - |

### Acceptable Delays

- **Model distribution**: < 24 hours (to all clients)
- **Gradient upload**: < 4 hours (per client)
- **Aggregation**: < 1 hour (server-side)
- **End-to-end round**: < 7 days (weekly cadence)

## Network Security

### Encryption

- **TLS 1.3**: All client-server communication
- **Cipher suites**: AES-256-GCM (preferred), ChaCha20-Poly1305 (fallback)
- **Certificate validation**: X.509 with OCSP stapling

### Authentication

- **Client certificates**: Unique per aircraft, ground station, sim rig
- **Mutual TLS**: Server authenticates client, client authenticates server
- **Certificate rotation**: Annual or upon compromise

### Firewall Rules

- **Inbound**: Port 443 (HTTPS) only, from known client IPs
- **Outbound**: Aggregation server IPs whitelisted
- **Monitoring**: IDS/IPS for anomalous traffic patterns

## Monitoring and Alerts

### Metrics

- **Connectivity uptime**: % of time client has active link
- **Latency**: p50, p95, p99 percentiles
- **Bandwidth usage**: Upload/download volume per training round
- **Packet loss**: % of packets lost during uploads
- **Failover events**: Count of LEO → GEO or fiber → 4G/5G failovers

### Alerting Thresholds

| Metric                | Warning      | Critical     |
|-----------------------|--------------|--------------|
| Connectivity uptime   | < 90%        | < 80%        |
| Latency (p95)         | > 1000 ms    | > 2000 ms    |
| Packet loss           | > 5%         | > 10%        |
| Bandwidth cap exceeded| 80% of limit | 100% of limit|

**Alert Routing:**
- Slack: #fl-network-alerts
- PagerDuty: Network Operations Team
- Email: AI/ML Team, Fleet Operations

## Related Documents

- **SCHEDULER.md** - Training round schedules aligned with connectivity
- **CLIENT_SELECTION.md** - Eligibility based on network health
- **04-ALGORITHMS/COMPRESSION.md** - Bandwidth reduction techniques
- **12-METRICS/KPI_DEFINITIONS.md** - Connectivity metrics tracking

## Change History

| Version | Date    | Changes                        | Author         |
|---------|---------|--------------------------------|----------------|
| 1.0     | 2024-Q4 | Initial connectivity profiles  | AI/ML Network Team |
