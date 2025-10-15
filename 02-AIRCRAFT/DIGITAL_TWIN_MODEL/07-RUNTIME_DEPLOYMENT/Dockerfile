FROM python:3.11.9-slim

LABEL maintainer="digitaltwin@idealeeu.eu"
LABEL description="Digital Twin Model Runtime"

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy model artifacts
COPY 02-MODELS/ /app/models/
COPY 12-CODE/src/ /app/src/

# Expose API port
EXPOSE 8080

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# Run runtime
CMD ["python", "src/runtime/main.py"]
