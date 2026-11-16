#!/bin/bash

# Linux infrasturcture health monitoring

DISK_THRESHOLD=80
MEMORY_THRESHOLD=80

LOG_FILE='logs/system-health.log'

mkdir -p logs

log_message(){
    echo"[$(date'+%Y-%m-%d%H:%M:%S')]$1" | tee -a"$LOG_FILE"
}

log_message "starting infrasturcture health check"

HOST=$(hostname)

log_message "server:$HOST"

UPTIME=$(uptime-p)

log_message "Uptime : $UPTIME"

DISK_USAGE=$(df-p / | awk 'NR==2{gsub("%","",$5); print$5}')

log_message "Disk usage : ${DISK_USAGE}%"

if [ "$DISK_USAGE" -ge "$DISK_THRESHOLD" ]; then
    log_message "WARNING: Disk usage is above threshold!"
else
    log_message "HEALTHY: Disk usage is normal."
fi

# Memory utilization
MEMORY_USAGE=$(awk '
/MemTotal/ {total=$2}
/MemAvailable/ {available=$2}
END {
    if (total > 0)
        printf "%.0f", ((total-available)/total)*100
}' /proc/meminfo)

log_message "Memory Usage: ${MEMORY_USAGE}%"

if [ "$MEMORY_USAGE" -ge "$MEMORY_THRESHOLD" ]; then
    log_message "WARNING: Memory usage is above threshold!"
else
    log_message "HEALTHY: Memory usage is normal."
fi

log_message "Infrastructure Health Check Completed." 




