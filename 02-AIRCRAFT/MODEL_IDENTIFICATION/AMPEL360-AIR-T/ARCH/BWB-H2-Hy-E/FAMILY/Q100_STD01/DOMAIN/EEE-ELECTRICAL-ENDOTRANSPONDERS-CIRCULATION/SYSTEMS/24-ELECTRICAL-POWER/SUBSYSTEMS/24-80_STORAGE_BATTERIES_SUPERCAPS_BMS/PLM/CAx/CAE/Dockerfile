# Dockerfile for CO₂ Endocircular Battery System Simulations
# Provides reproducible environment with all dependencies

FROM python:3.11-slim

LABEL maintainer="IDEALE-EU Energy Systems Team"
LABEL description="CO₂ Endocircular Battery System - CAE Simulation Environment"

# Set working directory
WORKDIR /workspace

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements file
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy simulation files
COPY co2_battery_endocircular.py .
COPY test_co2_battery.py .

# Set Python path
ENV PYTHONPATH=/workspace:$PYTHONPATH

# Default command: run tests
CMD ["pytest", "test_co2_battery.py", "-v", "--cov=co2_battery_endocircular"]
