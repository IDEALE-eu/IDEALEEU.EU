# COMM_LINKS

Communication links and RF standards for spacecraft.

## Overview

This directory contains ECSS standards for spacecraft communication systems, including RF links, antennas, and communication protocols.

## Applicable Standards

### ECSS-E-ST-50C - Communications
- **Scope**: Space-to-ground and space-to-space communications
- **Coverage**: RF links, antennas, modulation, coding, protocols
- **Key Topics**:
  - Link budget analysis
  - Antenna design and pointing
  - Modulation and coding
  - Communication protocols (CCSDS)
  - Frequency allocation and coordination

### CCSDS (Consultative Committee for Space Data Systems)
- **Scope**: Standardized protocols for space data systems
- **Key Standards**:
  - **CCSDS 131.0**: TM Synchronization and Channel Coding
  - **CCSDS 132.0**: TM Space Data Link Protocol
  - **CCSDS 133.0**: Space Packet Protocol
  - **CCSDS 232.0**: TC Synchronization and Channel Coding
  - **CCSDS 232.1**: TC Space Data Link Protocol

## Communication System Architecture

### Typical Components
- **Transponder**: Receive uplink, transmit downlink (coherent or non-coherent)
- **Antennas**: High-gain (dishes), medium-gain (helical), low-gain (omnidirectional)
- **RF Switches and Diplexers**: Route signals to/from antennas
- **Solid-State Power Amplifier (SSPA)** or **Traveling Wave Tube Amplifier (TWTA)**: Transmit power
- **Low-Noise Amplifier (LNA)**: Receive amplification

### Frequency Bands
- **S-band**: 2-4 GHz (common for LEO, heritage)
- **X-band**: 8-12 GHz (higher data rates)
- **Ka-band**: 26-40 GHz (very high data rates, weather-sensitive)
- **Ku-band**: 12-18 GHz (some missions)
- **UHF**: 300-3000 MHz (cubesats, low data rate)

### Polarization
- **Linear**: Horizontal or vertical
- **Circular**: Right-hand or left-hand (RHCP, LHCP)
- **Elliptical**: Mix of linear and circular

## Link Budget Analysis

### Link Equation
\[
C/N_0 = EIRP + G/T - L_{path} - k - L_{other}
\]
Where:
- **EIRP**: Effective Isotropic Radiated Power (dBW)
- **G/T**: Receive figure of merit (dB/K)
- **L_path**: Free-space path loss (dB)
- **k**: Boltzmann constant (-228.6 dBW/K/Hz)
- **L_other**: Other losses (atmospheric, pointing, polarization, etc.)

### Link Budget Components

#### Transmit Side
- **Transmit Power (P_t)**: SSPA or TWTA output power
- **Transmit Antenna Gain (G_t)**: Gain towards receiver
- **Transmit Line Loss (L_t)**: Cables, waveguides, switches
- **EIRP**: P_t + G_t - L_t

#### Propagation
- **Free-Space Path Loss**: 20 log(4πd/λ)
- **Atmospheric Loss**: Rain, clouds, ionosphere
- **Pointing Loss**: Antenna mispointing

#### Receive Side
- **Receive Antenna Gain (G_r)**: Gain towards transmitter
- **System Noise Temperature (T_sys)**: Antenna + LNA + receiver noise
- **G/T**: G_r - 10 log(T_sys)
- **Receive Line Loss (L_r)**: Cables, waveguides, switches

### Margin
- **Link Margin**: Excess C/N_0 beyond required for desired Eb/N0 and data rate
- **Typical Margins**: 3-6 dB for normal operations, 0 dB worst-case

## Antennas

### Antenna Types
- **Parabolic Dish**: High gain, narrow beam (HGA)
- **Helical**: Medium gain, circular polarization (MGA)
- **Patch**: Low to medium gain, planar, lightweight
- **Horn**: Medium gain, feeds for reflectors
- **Dipole/Monopole**: Low gain, omnidirectional (LGA)

### Antenna Pointing
- **Fixed**: No pointing mechanism (body-fixed)
- **Gimbaled**: Steerable antenna (azimuth/elevation or pitch/roll)
- **Phased Array**: Electronically steered beam (no moving parts)

### Antenna Patterns
- **Beam width**: 3 dB beam width, half-power beam width
- **Gain**: Peak gain on boresight
- **Sidelobes**: Off-axis radiation (interference concern)
- **Polarization**: Linear or circular, purity

## Modulation and Coding

### Modulation Schemes
- **BPSK**: Binary Phase Shift Keying (simple, robust)
- **QPSK**: Quadrature PSK (2 bits/symbol)
- **8PSK**: 3 bits/symbol (higher spectral efficiency)
- **OQPSK**: Offset QPSK (constant envelope)
- **GMSK**: Gaussian Minimum Shift Keying (narrow bandwidth)

### Channel Coding
- **Convolutional Coding**: Rate 1/2, constraint length 7 (NASA standard)
- **Reed-Solomon**: Block code for error correction
- **Turbo Codes**: Near Shannon limit performance
- **LDPC**: Low-Density Parity-Check codes (modern, efficient)
- **Concatenation**: Outer RS + inner convolutional

### Data Rate vs. Eb/N0
- **BER (Bit Error Rate)**: Typically 10⁻⁵ or 10⁻⁶ required
- **Eb/N0**: Energy per bit to noise density (dB)
- **Required Eb/N0**: Depends on modulation, coding, BER target
- **Example**: BPSK, rate 1/2 convolutional, BER 10⁻⁵ requires ~4.5 dB Eb/N0

## Communication Protocols

### CCSDS Protocol Stack
- **Space Packet**: Fixed header, variable data (CCSDS 133.0)
- **Data Link Layer**: Frame formatting, error detection (CCSDS 132.0, 232.1)
- **Synchronization and Coding**: Frame sync, channel coding (CCSDS 131.0, 232.0)

### Telemetry (TM)
- **Downlink**: Spacecraft to ground
- **Data Types**: Science data, housekeeping, payload data
- **Packetization**: CCSDS packets (APIDs, sequence count, timestamps)

### Telecommand (TC)
- **Uplink**: Ground to spacecraft
- **Command Types**: Immediate, time-tagged, stored
- **Authentication**: Command encryption, CRC

## Frequency Coordination

### Regulatory Bodies
- **ITU**: International Telecommunication Union (frequency allocation)
- **National Authorities**: FCC (USA), ANFR (France), etc.
- **Space Agencies**: ESA, NASA frequency management

### Coordination Process
1. Identify required frequencies and orbits
2. Submit frequency filing to ITU via national authority
3. Coordinate with other users (satellite operators, radio astronomy)
4. Obtain frequency authorization
5. Notify pre-launch and post-launch

## Key Deliverables

1. **Communication System Design** - Architecture, components, interfaces
2. **Link Budget Analysis** - Uplink and downlink budgets with margins
3. **Antenna Design and Patterns** - Antenna specifications, gain patterns
4. **Modulation and Coding Plan** - Modulation, coding, data rates
5. **Frequency Plan** - Allocated frequencies, coordination status
6. **Communication Protocol Specification** - CCSDS compliance, packet formats
7. **RF Test Plan and Report** - Radiated power, antenna patterns, link testing
8. **Frequency Coordination Documentation** - ITU filing, authorizations

## Compliance Requirements

- Communication system per ECSS-E-ST-50C
- CCSDS protocols for interoperability
- Frequency coordination per ITU regulations
- Link budgets verified with margins
- RF testing demonstrates compliance

## Integration with Other Standards

- **ECSS-E-ST-10C** - Systems engineering defines communication requirements
- **ECSS-E-ST-20C** - Electrical design for RF systems
- **ECSS-E-ST-20-07C** - EMC for RF emissions and susceptibility

## Common Issues

- Insufficient link margin (underestimated losses)
- Antenna pattern not meeting requirements
- Frequency coordination delays
- Interference from other spacecraft or ground sources
- Modulation/coding incompatibility with ground stations

## Tools and Templates

- Link budget calculators (Excel, STK)
- Antenna pattern analysis (GRASP, CST)
- RF simulation tools (Keysight ADS, ANSYS HFSS)
- Frequency coordination databases

## References

- 01-REGISTER/STANDARDS_REGISTER.csv - ECSS standards
- ECSS Portal: https://ecss.nl
- CCSDS: https://public.ccsds.org (CCSDS standards, free)
- ITU Radio Regulations

---

**Status**: Configuration-controlled per 00-PROGRAM/CONFIG_MGMT/
