# Digital Twin Runtime Container

FROM python:3.9-slim

LABEL maintainer="dt-team@ideale-eu.eu"
LABEL version="1.0"
LABEL description="Aircraft Digital Twin Runtime"

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    libssl-dev \
    && rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY src/ ./src/
COPY models/ ./models/
COPY config/ ./config/

# Expose ports
EXPOSE 8080 50051

# Set environment variables
ENV TWIN_ENV=production
ENV LOG_LEVEL=INFO

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD python -c "import requests; requests.get('http://localhost:8080/health')"

# Run the twin runtime
CMD ["python", "src/main.py"]
