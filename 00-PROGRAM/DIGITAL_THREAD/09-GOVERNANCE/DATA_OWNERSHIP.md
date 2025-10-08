# Data Ownership

## RACI Matrix by Domain

### Avionics
| Data Element | Responsible | Accountable | Consulted | Informed |
|--------------|-------------|-------------|-----------|----------|
| Avionics Requirements | Avionics Engineer | Avionics Chief Engineer | Systems Engineer | Program Manager |
| Avionics Models (SysML) | Avionics Engineer | Avionics Chief Engineer | Digital Thread Team | Configuration Mgmt |
| Avionics Test Data | Test Engineer | Avionics Chief Engineer | Quality Engineer | Fleet Operations |
| Avionics BOM | Design Engineer | Avionics Chief Engineer | Manufacturing Eng | Supply Chain |

### Propulsion
| Data Element | Responsible | Accountable | Consulted | Informed |
|--------------|-------------|-------------|-----------|----------|
| Propulsion Requirements | Propulsion Engineer | Propulsion Chief Engineer | Systems Engineer | Program Manager |
| Propulsion Models | Propulsion Engineer | Propulsion Chief Engineer | Digital Thread Team | Configuration Mgmt |
| H2 System Data | H2 Systems Engineer | Propulsion Chief Engineer | Safety Engineer | Regulatory Affairs |
| Propulsion Test Data | Test Engineer | Propulsion Chief Engineer | Quality Engineer | Fleet Operations |

### Structures
| Data Element | Responsible | Accountable | Consulted | Informed |
|--------------|-------------|-------------|-----------|----------|
| Structural Requirements | Structures Engineer | Structures Chief Engineer | Systems Engineer | Program Manager |
| FEA Models | Structures Analyst | Structures Chief Engineer | Digital Thread Team | Certification |
| Structural Test Data | Test Engineer | Structures Chief Engineer | Quality Engineer | Safety Engineer |
| Materials Data | Materials Engineer | Structures Chief Engineer | Supply Chain | Quality |

### GNC (Guidance, Navigation, Control)
| Data Element | Responsible | Accountable | Consulted | Informed |
|--------------|-------------|-------------|-----------|----------|
| GNC Requirements | GNC Engineer | GNC Chief Engineer | Systems Engineer | Program Manager |
| GNC Algorithms | GNC Engineer | GNC Chief Engineer | Flight Software Lead | Safety Engineer |
| GNC Test Data | Test Engineer | GNC Chief Engineer | Quality Engineer | Flight Operations |
| Sensor Calibration | GNC Engineer | GNC Chief Engineer | Metrology | Quality |

### Cross-Cutting Data

#### Configuration Management
| Data Element | Responsible | Accountable | Consulted | Informed |
|--------------|-------------|-------------|-----------|----------|
| Baselines | Config Mgmt Team | Config Manager | Chief Engineers | All Stakeholders |
| Change Requests | Originator | CCB Chair | Affected Domains | All Stakeholders |
| UID Assignment | PLM System | Config Manager | Digital Thread Team | All Users |
| Version Control | Config Mgmt Team | Config Manager | Engineering | All Users |

#### Digital Twin
| Data Element | Responsible | Accountable | Consulted | Informed |
|--------------|-------------|-------------|-----------|----------|
| Twin Models | Digital Thread Team | Head of Digital Eng | Domain Engineers | Operations |
| Validation Data | Test Engineers | Domain Chief Engineers | Digital Thread Team | Fleet Operations |
| Twin API | Digital Thread Team | Head of Digital Eng | IT/Security | Operations |

#### Fleet Data
| Data Element | Responsible | Accountable | Consulted | Informed |
|--------------|-------------|-------------|-----------|----------|
| Telemetry | Fleet Ops Team | Head of Fleet Ops | Engineering | Program Mgmt |
| Maintenance Records | Maintenance Crew | Maintenance Manager | Engineering | Quality |
| Anomalies | Fleet Engineer | Head of Fleet Ops | Domain Engineers | Safety |

