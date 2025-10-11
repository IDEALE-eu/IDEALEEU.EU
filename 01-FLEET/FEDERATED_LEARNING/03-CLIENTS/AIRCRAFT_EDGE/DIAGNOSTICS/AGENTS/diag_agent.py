#!/usr/bin/env python3
"""
Aircraft Edge FL Client Diagnostic Agent

This agent performs automated health monitoring of the FL client:
1. Reads check configurations from CHECKS/ directory
2. Executes health checks (hardware, network, storage, security, training)
3. Compiles results into a diagnostic report
4. Validates report against JSON schema
5. Publishes report to telemetry topic

Author: Federated Learning Team
Created: 2025-10-11
Version: 1.0.0
"""

import os
import sys
import json
import yaml
import psutil
import socket
import time
import logging
from pathlib import Path
from datetime import datetime
from typing import Dict, Any, List

# Setup paths
SCRIPT_DIR = Path(__file__).parent
DIAGNOSTICS_ROOT = SCRIPT_DIR.parent
CHECKS_DIR = DIAGNOSTICS_ROOT / "CHECKS"
SCHEMAS_DIR = DIAGNOSTICS_ROOT / "SCHEMAS"
TEMPLATES_DIR = DIAGNOSTICS_ROOT / "TEMPLATES"
LOG_DIR = Path("/var/fl-client")

# Setup logging
LOG_DIR.mkdir(parents=True, exist_ok=True)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s',
    handlers=[
        logging.FileHandler(LOG_DIR / "diagnostics.log"),
        logging.StreamHandler(sys.stdout)
    ]
)
logger = logging.getLogger(__name__)


class DiagnosticAgent:
    """Main diagnostic agent for FL client health monitoring."""
    
    def __init__(self):
        """Initialize the diagnostic agent."""
        self.checks = {}
        self.results = {}
        self.config = self._load_config()
        logger.info("Diagnostic Agent initialized")
    
    def _load_config(self) -> Dict[str, Any]:
        """Load agent configuration."""
        config_file = TEMPLATES_DIR / "config.yaml"
        if config_file.exists():
            with open(config_file, 'r') as f:
                config = yaml.safe_load(f)
                logger.info(f"Configuration loaded from {config_file}")
                return config
        else:
            logger.warning(f"Config file not found: {config_file}, using defaults")
            return {
                "agent_id": "aircraft-edge-001",
                "check_interval": 60,
                "report_format": "json"
            }
    
    def load_checks(self):
        """Load all check configurations from CHECKS/ directory."""
        check_files = [
            "health.yaml",
            "network.yaml",
            "storage.yaml",
            "security.yaml",
            "training.yaml"
        ]
        
        for check_file in check_files:
            check_path = CHECKS_DIR / check_file
            if check_path.exists():
                with open(check_path, 'r') as f:
                    check_name = check_file.replace('.yaml', '')
                    self.checks[check_name] = yaml.safe_load(f)
                    logger.info(f"Loaded check: {check_name}")
            else:
                logger.warning(f"Check file not found: {check_path}")
    
    def run_health_checks(self) -> Dict[str, Any]:
        """Execute health checks (CPU, Memory, GPU, Disk)."""
        logger.info("Running health checks...")
        results = {
            "status": "healthy",
            "checks": []
        }
        
        if "health" not in self.checks:
            logger.warning("Health check configuration not loaded")
            results["status"] = "unknown"
            return results
        
        health_config = self.checks["health"]
        
        # CPU check
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_temp = self._get_cpu_temperature()
        cpu_check = {
            "name": "cpu",
            "status": "pass",
            "metrics": {
                "usage_percent": cpu_percent,
                "temperature_celsius": cpu_temp
            }
        }
        
        # Check against thresholds
        cpu_thresholds = health_config.get("thresholds", {}).get("cpu", {})
        if cpu_percent > cpu_thresholds.get("max_usage_percent", 75):
            cpu_check["status"] = "fail"
            cpu_check["message"] = f"CPU usage {cpu_percent}% exceeds threshold"
            results["status"] = "unhealthy"
        
        if cpu_temp and cpu_temp > cpu_thresholds.get("max_temperature_celsius", 75):
            cpu_check["status"] = "fail"
            cpu_check["message"] = f"CPU temperature {cpu_temp}°C exceeds threshold"
            results["status"] = "unhealthy"
        
        results["checks"].append(cpu_check)
        
        # Memory check
        memory = psutil.virtual_memory()
        memory_check = {
            "name": "memory",
            "status": "pass",
            "metrics": {
                "usage_percent": memory.percent,
                "available_mb": memory.available / (1024 * 1024),
                "total_mb": memory.total / (1024 * 1024)
            }
        }
        
        memory_thresholds = health_config.get("thresholds", {}).get("memory", {})
        if memory.percent > memory_thresholds.get("max_usage_percent", 80):
            memory_check["status"] = "fail"
            memory_check["message"] = f"Memory usage {memory.percent}% exceeds threshold"
            results["status"] = "unhealthy"
        
        results["checks"].append(memory_check)
        
        # GPU check (if configured)
        gpu_check = self._check_gpu()
        if gpu_check:
            results["checks"].append(gpu_check)
            if gpu_check["status"] == "fail":
                results["status"] = "unhealthy"
        
        # Disk check
        disk = psutil.disk_usage('/')
        disk_check = {
            "name": "disk",
            "status": "pass",
            "metrics": {
                "usage_percent": disk.percent,
                "available_gb": disk.free / (1024 ** 3),
                "total_gb": disk.total / (1024 ** 3)
            }
        }
        
        disk_thresholds = health_config.get("thresholds", {}).get("disk", {})
        if disk.percent > disk_thresholds.get("max_usage_percent", 85):
            disk_check["status"] = "fail"
            disk_check["message"] = f"Disk usage {disk.percent}% exceeds threshold"
            results["status"] = "unhealthy"
        
        results["checks"].append(disk_check)
        
        logger.info(f"Health checks completed: {results['status']}")
        return results
    
    def run_network_checks(self) -> Dict[str, Any]:
        """Execute network connectivity and latency checks."""
        logger.info("Running network checks...")
        results = {
            "status": "healthy",
            "checks": []
        }
        
        if "network" not in self.checks:
            logger.warning("Network check configuration not loaded")
            results["status"] = "unknown"
            return results
        
        network_config = self.checks["network"]
        
        # Check connectivity to central server
        server_host = network_config.get("central_server", {}).get("host", "fl-server.ideale-eu.eu")
        server_port = network_config.get("central_server", {}).get("port", 443)
        
        connectivity_check = {
            "name": "central_server_connectivity",
            "status": "pass",
            "metrics": {}
        }
        
        try:
            # Test connectivity
            start_time = time.time()
            sock = socket.create_connection((server_host, server_port), timeout=5)
            latency_ms = (time.time() - start_time) * 1000
            sock.close()
            
            connectivity_check["metrics"]["latency_ms"] = latency_ms
            connectivity_check["metrics"]["host"] = server_host
            
            # Check latency threshold
            max_latency = network_config.get("thresholds", {}).get("max_latency_ms", 500)
            if latency_ms > max_latency:
                connectivity_check["status"] = "warn"
                connectivity_check["message"] = f"High latency: {latency_ms:.2f}ms"
        
        except (socket.timeout, socket.error) as e:
            connectivity_check["status"] = "fail"
            connectivity_check["message"] = f"Cannot reach server: {str(e)}"
            results["status"] = "unhealthy"
        
        results["checks"].append(connectivity_check)
        
        logger.info(f"Network checks completed: {results['status']}")
        return results
    
    def run_storage_checks(self) -> Dict[str, Any]:
        """Execute storage checks (FL data directory, model storage)."""
        logger.info("Running storage checks...")
        results = {
            "status": "healthy",
            "checks": []
        }
        
        if "storage" not in self.checks:
            logger.warning("Storage check configuration not loaded")
            results["status"] = "unknown"
            return results
        
        storage_config = self.checks["storage"]
        
        # Check FL client data directory
        fl_data_dir = Path(storage_config.get("fl_data_directory", "/var/fl-client"))
        
        if fl_data_dir.exists():
            dir_check = {
                "name": "fl_data_directory",
                "status": "pass",
                "metrics": {
                    "path": str(fl_data_dir),
                    "exists": True
                }
            }
            
            # Calculate directory size
            try:
                total_size = sum(f.stat().st_size for f in fl_data_dir.rglob('*') if f.is_file())
                dir_check["metrics"]["size_mb"] = total_size / (1024 * 1024)
                
                # Check against storage limit
                max_size_gb = storage_config.get("thresholds", {}).get("max_directory_size_gb", 10)
                if total_size > max_size_gb * 1024 ** 3:
                    dir_check["status"] = "warn"
                    dir_check["message"] = f"Directory size exceeds {max_size_gb}GB"
            
            except Exception as e:
                logger.warning(f"Error calculating directory size: {e}")
        
        else:
            dir_check = {
                "name": "fl_data_directory",
                "status": "fail",
                "metrics": {
                    "path": str(fl_data_dir),
                    "exists": False
                },
                "message": "FL data directory does not exist"
            }
            results["status"] = "unhealthy"
        
        results["checks"].append(dir_check)
        
        logger.info(f"Storage checks completed: {results['status']}")
        return results
    
    def run_security_checks(self) -> Dict[str, Any]:
        """Execute security checks (certificates, permissions)."""
        logger.info("Running security checks...")
        results = {
            "status": "healthy",
            "checks": []
        }
        
        if "security" not in self.checks:
            logger.warning("Security check configuration not loaded")
            results["status"] = "unknown"
            return results
        
        security_config = self.checks["security"]
        
        # Check certificates
        cert_paths = security_config.get("certificates", [])
        for cert_config in cert_paths:
            cert_path = Path(cert_config.get("path", ""))
            cert_check = {
                "name": f"certificate_{cert_config.get('name', 'unknown')}",
                "status": "pass",
                "metrics": {
                    "path": str(cert_path)
                }
            }
            
            if cert_path.exists():
                # Check file permissions
                stat_info = cert_path.stat()
                permissions = oct(stat_info.st_mode)[-3:]
                cert_check["metrics"]["permissions"] = permissions
                
                # Warn if permissions are too open
                if permissions not in ['600', '400', '644']:
                    cert_check["status"] = "warn"
                    cert_check["message"] = f"Insecure permissions: {permissions}"
            else:
                cert_check["status"] = "fail"
                cert_check["message"] = "Certificate file not found"
                results["status"] = "unhealthy"
            
            results["checks"].append(cert_check)
        
        logger.info(f"Security checks completed: {results['status']}")
        return results
    
    def run_training_checks(self) -> Dict[str, Any]:
        """Execute training environment checks (Docker, dependencies)."""
        logger.info("Running training checks...")
        results = {
            "status": "healthy",
            "checks": []
        }
        
        if "training" not in self.checks:
            logger.warning("Training check configuration not loaded")
            results["status"] = "unknown"
            return results
        
        training_config = self.checks["training"]
        
        # Check if training environment is present
        env_check = {
            "name": "training_environment",
            "status": "pass",
            "metrics": {}
        }
        
        # Check for Docker (if required)
        if training_config.get("requires_docker", False):
            try:
                import docker
                client = docker.from_env()
                env_check["metrics"]["docker_available"] = True
                
                # Check for required container
                required_image = training_config.get("docker_image", "")
                if required_image:
                    try:
                        client.images.get(required_image)
                        env_check["metrics"]["required_image_present"] = True
                    except docker.errors.ImageNotFound:
                        env_check["status"] = "fail"
                        env_check["message"] = f"Required Docker image not found: {required_image}"
                        results["status"] = "unhealthy"
            
            except ImportError:
                env_check["status"] = "warn"
                env_check["message"] = "Docker Python SDK not installed"
            except Exception as e:
                env_check["status"] = "fail"
                env_check["message"] = f"Docker not available: {str(e)}"
                results["status"] = "unhealthy"
        
        results["checks"].append(env_check)
        
        logger.info(f"Training checks completed: {results['status']}")
        return results
    
    def _get_cpu_temperature(self):
        """Get CPU temperature if available."""
        try:
            temps = psutil.sensors_temperatures()
            if 'coretemp' in temps:
                return temps['coretemp'][0].current
            elif 'cpu_thermal' in temps:
                return temps['cpu_thermal'][0].current
        except:
            pass
        return None
    
    def _check_gpu(self) -> Dict[str, Any]:
        """Check GPU availability and health."""
        gpu_check = {
            "name": "gpu",
            "status": "pass",
            "metrics": {}
        }
        
        try:
            # Try to import pynvml for NVIDIA GPU monitoring
            import pynvml
            pynvml.nvmlInit()
            
            device_count = pynvml.nvmlDeviceGetCount()
            gpu_check["metrics"]["gpu_count"] = device_count
            
            if device_count > 0:
                handle = pynvml.nvmlDeviceGetHandleByIndex(0)
                gpu_temp = pynvml.nvmlDeviceGetTemperature(handle, pynvml.NVML_TEMPERATURE_GPU)
                memory_info = pynvml.nvmlDeviceGetMemoryInfo(handle)
                
                gpu_check["metrics"]["temperature_celsius"] = gpu_temp
                gpu_check["metrics"]["memory_used_mb"] = memory_info.used / (1024 * 1024)
                gpu_check["metrics"]["memory_total_mb"] = memory_info.total / (1024 * 1024)
                
                # Check GPU temperature threshold
                if "health" in self.checks:
                    gpu_thresholds = self.checks["health"].get("thresholds", {}).get("gpu", {})
                    max_temp = gpu_thresholds.get("max_temperature_celsius", 85)
                    if gpu_temp > max_temp:
                        gpu_check["status"] = "fail"
                        gpu_check["message"] = f"GPU temperature {gpu_temp}°C exceeds threshold"
            
            pynvml.nvmlShutdown()
        
        except ImportError:
            gpu_check["status"] = "unknown"
            gpu_check["message"] = "GPU monitoring library not available"
        except Exception as e:
            gpu_check["status"] = "unknown"
            gpu_check["message"] = f"GPU check failed: {str(e)}"
        
        return gpu_check
    
    def generate_report(self) -> Dict[str, Any]:
        """Generate comprehensive diagnostic report."""
        logger.info("Generating diagnostic report...")
        
        report = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "agent_id": self.config.get("agent_id", "unknown"),
            "aircraft_id": self.config.get("aircraft_id", "AC-H2-001"),
            "diagnostics": {
                "health": self.run_health_checks(),
                "network": self.run_network_checks(),
                "storage": self.run_storage_checks(),
                "security": self.run_security_checks(),
                "training": self.run_training_checks()
            }
        }
        
        # Determine overall status
        statuses = [v["status"] for v in report["diagnostics"].values()]
        if "unhealthy" in statuses:
            report["overall_status"] = "unhealthy"
        elif "unknown" in statuses:
            report["overall_status"] = "unknown"
        else:
            report["overall_status"] = "healthy"
        
        logger.info(f"Diagnostic report generated: {report['overall_status']}")
        return report
    
    def validate_report(self, report: Dict[str, Any]) -> bool:
        """Validate report against JSON schema."""
        schema_file = SCHEMAS_DIR / "diag_report.schema.json"
        
        if not schema_file.exists():
            logger.warning(f"Schema file not found: {schema_file}, skipping validation")
            return True
        
        try:
            import jsonschema
            with open(schema_file, 'r') as f:
                schema = json.load(f)
            
            jsonschema.validate(instance=report, schema=schema)
            logger.info("Report validated successfully against schema")
            return True
        
        except ImportError:
            logger.warning("jsonschema library not available, skipping validation")
            return True
        except jsonschema.ValidationError as e:
            logger.error(f"Report validation failed: {e.message}")
            return False
        except Exception as e:
            logger.error(f"Unexpected error during validation: {e}")
            return False
    
    def publish_report(self, report: Dict[str, Any]):
        """Publish report to telemetry topic."""
        # In production, this would publish to a message queue or telemetry system
        # For now, we'll write to a file
        
        output_dir = LOG_DIR / "reports"
        output_dir.mkdir(parents=True, exist_ok=True)
        
        timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
        report_file = output_dir / f"diag_report_{timestamp}.json"
        
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
        
        logger.info(f"Report published to: {report_file}")
    
    def run(self):
        """Main execution loop."""
        logger.info("=== Starting Diagnostic Agent ===")
        
        # Load check configurations
        self.load_checks()
        
        # Generate report
        report = self.generate_report()
        
        # Validate report
        if self.validate_report(report):
            # Publish report
            self.publish_report(report)
            
            # Log summary
            logger.info(f"Overall Status: {report['overall_status']}")
            logger.info("=== Diagnostic Agent Complete ===")
            
            # Exit with appropriate code
            return 0 if report['overall_status'] in ['healthy', 'unknown'] else 1
        else:
            logger.error("Report validation failed, not publishing")
            return 2


def main():
    """Main entry point."""
    try:
        agent = DiagnosticAgent()
        return agent.run()
    except Exception as e:
        logger.error(f"Fatal error: {e}", exc_info=True)
        return 3


if __name__ == "__main__":
    sys.exit(main())
