import logging
import os 

# Create logs directory if it doesn't exist
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/system-health.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.info("Infrastructure monitoring started")
logging.warning("High CPU utilization detected")

# Record application events
logging.info("Infrastructure monitoring started")

cpu_usage = 90
CPU_THRESHOLD = 80

if cpu_usage >= CPU_THRESHOLD:
    logging.warning(
        f"High CPU utilization detected: {cpu_usage}%"
    )
else:
    logging.info(
        f"CPU utilization is normal: {cpu_usage}%"
    )

logging.info("Infrastructure monitoring completed")
