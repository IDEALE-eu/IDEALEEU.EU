# Access Control Policy

## Role-Based Access Control (RBAC)

### Engineering Roles

**Engineer**
- Read: Design data, requirements, models
- Write: Assigned work packages
- No approval authority

**Lead Engineer**
- Read: All engineering data
- Write: Domain-specific data
- Approve: Domain design changes (within authority)

**Chief Engineer**
- Read: All program data
- Write: All engineering data (with limits)
- Approve: Major design changes, baselines

### Manufacturing Roles

**Technician**
- Read: Work instructions, BOMs, drawings (assigned tasks)
- Write: As-built data, inspection results
- No approval authority

**Manufacturing Engineer**
- Read: All manufacturing data
- Write: Work instructions, process data
- Approve: Process changes (within authority)

**Production Manager**
- Read: All manufacturing and quality data
- Write: Production planning data
- Approve: Production schedule, resource allocation

### Operations Roles

**Operator**
- Read: Operations manuals, procedures
- Write: Flight/mission logs
- No approval authority

**Maintenance Crew**
- Read: Maintenance procedures, as-maintained config
- Write: Maintenance records
- Approve: Maintenance sign-off (certified items)

**Fleet Manager**
- Read: All fleet data
- Write: Fleet operations data
- Approve: Maintenance authorization, fleet modifications

### Quality Roles

**Quality Inspector**
- Read: Quality procedures, specifications
- Write: Inspection results
- Approve: First article inspection (FAI)

**Quality Engineer**
- Read: All quality data
- Write: NCRs, corrective actions
- Approve: Disposition of NCRs

**Quality Manager**
- Read: All program data (quality perspective)
- Write: Quality system documentation
- Approve: Quality system changes, major NCR dispositions

### Administrative Roles

**System Administrator**
- Full access to system configuration
- User account management
- No access to controlled technical data (unless authorized)

**Security Administrator**
- Access control configuration
- Security audit review
- Incident investigation

## Data Classification

### Public
- General program information
- Marketing materials
- Public documentation

**Access**: Unrestricted

### Internal
- Internal processes
- Business data (non-technical)
- General correspondence

**Access**: All employees

### Controlled (ITAR/EAR)
- Technical data (drawings, specs, test data)
- Export-controlled information
- Proprietary designs

**Access**: Authorized U.S. persons (ITAR) or export-authorized individuals

**Requirements**:
- Annual ITAR/EAR training
- Approved by security administrator
- Need-to-know justification
- Audit trail of all access

### Classified (if applicable)
- Government classified information
- SAP (Special Access Program) data

**Access**: Cleared individuals with appropriate level and need-to-know

## Access Request Process

1. **Request Submission**: User submits access request via system
2. **Justification**: Business need and role-based justification
3. **Approval**: Manager approval + Security approval (for controlled data)
4. **Training**: Complete required training (e.g., ITAR)
5. **Provisioning**: System admin grants access
6. **Notification**: User notified of access grant
7. **Review**: Quarterly access reviews

## ITAR/EAR Compliance

### ITAR (International Traffic in Arms Regulations)
- U.S. persons only (citizens, permanent residents, protected individuals)
- Export license required for non-U.S. persons
- Technical data marked with ITAR notice
- Audit trail of access and exports

### EAR (Export Administration Regulations)
- Export-controlled technical data
- License exceptions may apply
- ECCN (Export Control Classification Number) assigned
- Audit trail of exports

### Controlled Data Handling
- Data flagged at UID level (06-DATA_MANAGEMENT/)
- Access verified before granting
- Watermarked documents
- Secure transfer methods (encrypted)
- No cloud storage in non-approved locations

## Access Reviews

### Quarterly Reviews
- All user access reviewed
- Inactive accounts disabled
- Role changes reflected
- Controlled data access re-justified

### Annual Audits
- External audit (AS9100, ISO 27001)
- ITAR/EAR compliance verification
- Access policy effectiveness
- Security incident review

## Multi-Factor Authentication (MFA)

Required for:
- Access to controlled technical data
- Administrative accounts
- Remote access (VPN)
- Production systems

Methods:
- SMS/Email code
- Authenticator app (Google Authenticator, Microsoft Authenticator)
- Hardware token (YubiKey)

## Session Management

- Session timeout: 30 minutes (inactive)
- Re-authentication for sensitive operations
- Logout on browser close
- Concurrent session limits

## Security Monitoring

- Real-time alerting for unauthorized access attempts
- Anomaly detection (unusual access patterns)
- Failed login tracking (lockout after 5 attempts)
- Audit log review (weekly)

