# COMPRESSION

Gradient and model compression techniques for bandwidth reduction.

## Quantization

### FP32 → FP16 (16-bit floating point)

- **Size reduction**: 50%
- **Accuracy loss**: < 1%
- **Use case**: Default compression for all clients

### FP16 → INT8 (8-bit integer)

- **Size reduction**: 75% (vs. FP32)
- **Accuracy loss**: 1-3%
- **Use case**: GEO satellite (low bandwidth)

## Sparsification

### Top-k Sparsification

- Keep only top-k% of gradients by magnitude
- **k = 10%**: 90% size reduction, 2-5% accuracy loss
- **k = 1%**: 99% size reduction, 5-10% accuracy loss

### Random Sparsification

- Randomly mask (1-p)% of gradients
- Error correction: Scale remaining gradients by 1/p

## Delta Compression

- Send only parameter changes from previous round
- **Size reduction**: 40-60% (depends on convergence)
- **Use case**: Later training rounds (model stable)

## Implementation

- **Library**: TensorFlow Model Optimization Toolkit, PyTorch quantization
- **Client-side**: Compress before upload
- **Server-side**: Decompress, aggregate, compress for download

## Related Documents

- [**../02-ORCHESTRATION/CONNECTIVITY_PROFILES.md**](../02-ORCHESTRATION/CONNECTIVITY_PROFILES.md) - Bandwidth constraints
- [**FEDAVG.md**](FEDAVG.md) - Base algorithm
