
import psutil
import platform
import time
import logging
import sys
from pathlib import Path
from datetime import datetime
from alert_manager import send_alert

# Step 1: Create logs directory if it does not exist
Path("logs").mkdir(parents=True, exist_ok=True)

# Step 2: Configure logging
logging.basicConfig(
    filename="logs/system-health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Step 3: Monitoring thresholds
CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

overall_status = "HEALTHY"

hostname = platform.node()

print("=" * 45)
print("    CLOUD INFRASTRUCTURE HEALTH MONITOR")
print("=" * 45)

print(f"Server Name: {hostname}")
print(f"Date and Time: {datetime.now()}")

logging.info("Infrastructure monitoring started")

# CPU Monitoring
cpu_usage = psutil.cpu_percent(interval=1)
print(f"\nCPU Usage: {cpu_usage}%")

if cpu_usage >= CPU_THRESHOLD:
    print("WARNING: High CPU utilization")
    logging.warning(f"High CPU utilization: {cpu_usage}%")
    overall_status = "CRITICAL"
    send_alert("CPU", cpu_usage, CPU_THRESHOLD)
else:
    print("HEALTHY: CPU utilization is normal")
    logging.info(f"CPU utilization is normal: {cpu_usage}%")

# Memory Monitoring
memory = psutil.virtual_memory()
memory_usage = memory.percent

print(f"\nMemory Usage: {memory_usage}%")

if memory_usage >= MEMORY_THRESHOLD:
    print("WARNING: High memory utilization")
    logging.warning(f"High memory utilization: {memory_usage}%")
    send_alert("Memory", memory_usage, MEMORY_THRESHOLD)
else:
    print("HEALTHY: Memory utilization is normal")
    logging.info(f"Memory utilization is normal: {memory_usage}%")

# Disk Monitoring
disk = psutil.disk_usage("/")
disk_usage = disk.percent

print(f"\nDisk Usage: {disk_usage}%")

if disk_usage >= DISK_THRESHOLD:
    print("WARNING: High disk utilization")
    logging.warning(f"High disk utilization: {disk_usage}%")
    send_alert("Disk", disk_usage, DISK_THRESHOLD)
else:
    print("HEALTHY: Disk utilization is normal")
    logging.info(f"Disk utilization is normal: {disk_usage}%")

# System uptime
uptime_seconds = time.time() - psutil.boot_time()
uptime_hours = uptime_seconds / 3600

print(f"\nSystem Uptime: {uptime_hours:.2f} hours")
logging.info(f"System uptime: {uptime_hours:.2f} hours")

print("\nInfrastructure Health Check Completed")
logging.info("Infrastructure monitoring completed")


print(f"\nOVERALL SERVER STATUS: {overall_status}")
logging.info(f"Overall server status: {overall_status}")

if overall_status == "CRITICAL":
    sys.exit(1)
else:
    sys.exit(0)

print("=" * 45)

