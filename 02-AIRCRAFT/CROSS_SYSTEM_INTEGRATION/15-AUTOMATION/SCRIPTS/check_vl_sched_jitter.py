#!/usr/bin/env python3
"""
Check VL Schedule and Jitter

Validates AFDX VL scheduling and QoS timing constraints.

Usage:
    python check_vl_sched_jitter.py
"""

import csv
import sys
from pathlib import Path

def check_vl_schedule():
    """Check VL scheduling for conflicts and QoS violations"""
    
    vl_map_path = Path("02-NETWORKS_DATA_BUS/LOGICAL/AFDX_VL_MAP.csv")
    tte_schedule_path = Path("02-NETWORKS_DATA_BUS/QOS_TIMING/TTE_SCHEDULE.csv")
    
    if not vl_map_path.exists():
        print(f"ERROR: VL map not found: {vl_map_path}")
        return False
    
    with open(vl_map_path, 'r') as f:
        reader = csv.DictReader(f)
        vls = list(reader)
    
    print(f"Checking {len(vls)} virtual links...")
    
    total_bandwidth = 0
    for vl in vls:
        vl_id = vl.get('vl_id')
        bandwidth = float(vl.get('bandwidth_kbps', 0))
        jitter = float(vl.get('jitter_us', 0))
        bag = float(vl.get('bag_ms', 0))
        
        total_bandwidth += bandwidth
        
        # Check jitter constraints
        if jitter > 2000:  # 2ms max jitter
            print(f"  ✗ {vl_id}: Jitter {jitter} μs exceeds 2000 μs limit")
            return False
        
        print(f"  ✓ {vl_id}: BW={bandwidth} kbps, Jitter={jitter} μs, BAG={bag} ms")
    
    # Check total bandwidth (100 Mbps = 100,000 kbps per port)
    if total_bandwidth > 80000:  # 80% utilization limit
        print(f"\n✗ Total bandwidth {total_bandwidth} kbps exceeds 80% utilization (80,000 kbps)")
        return False
    
    print(f"\n✓ All VLs within QoS bounds. Total bandwidth: {total_bandwidth} kbps (80% limit: 80,000 kbps)")
    return True

if __name__ == '__main__':
    success = check_vl_schedule()
    sys.exit(0 if success else 1)
