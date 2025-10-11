# Encryption Requirements

## Data in Transit

### Protocol
- **TLS 1.3** for all network communications
- Minimum cipher suite: `TLS_AES_256_GCM_SHA384`
- Perfect Forward Secrecy (PFS) required
- Certificate validation mandatory

### Implementation
```python
import ssl

context = ssl.create_default_context(ssl.Purpose.CLIENT_AUTH)
context.minimum_version = ssl.TLSVersion.TLSv1_3
context.set_ciphers('TLS_AES_256_GCM_SHA384')
```

## Data at Rest

### Encryption
- **AES-256-GCM** for database encryption
- **AES-256-CBC** for file system encryption
- Key rotation: Every 90 days

### Key Management
- AWS KMS or equivalent for key storage
- Separate keys for production/development
- Multi-party authorization for key access

## Cryptographic Hashing

### Integrity Verification
- **SHA-256** for data integrity checks
- **HMAC-SHA256** for message authentication

### Example
```python
import hashlib
import hmac

# Integrity check
hash_obj = hashlib.sha256(data)
digest = hash_obj.hexdigest()

# Message authentication
mac = hmac.new(key, data, hashlib.sha256).hexdigest()
```

## Compliance

- FIPS 140-2 validated cryptographic modules
- No deprecated algorithms (MD5, SHA-1, DES)
- Regular security audits
