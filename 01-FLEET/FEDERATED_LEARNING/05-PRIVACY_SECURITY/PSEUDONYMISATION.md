# PSEUDONYMISATION

GDPR-compliant pseudonymisation for client identifiers.

## Aircraft ID Pseudonymisation

```
aircraft_id_hash = SHA256(tail_number + salt)

Example:
  Tail number: N12345
  Salt: secret_salt_2024
  Hash: a3f5b8c1d2e4f6a7b8c9d0e1f2a3b4c5...
```

## Flight ID Pseudonymisation

```
flight_id_hash = SHA256(flight_number + date + salt)
```

## GDPR Compliance

- **Art. 4(5)**: Pseudonymisation definition
- **Art. 32**: Security of processing
- **Recital 26**: Pseudonymised data still personal data

## Key Management

- **Salt rotation**: Annual or upon compromise
- **Storage**: Hardware Security Module (HSM)
- **Access control**: DPO only

## Related Documents

- [**../11-COMPLIANCE/PRIVACY.md**](../11-COMPLIANCE/PRIVACY.md) - GDPR compliance framework
