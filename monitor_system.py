import psutil
import time
from datetime import datetime

# Thresholds
CPU_THRESHOLD = 80  # in percentage
MEMORY_THRESHOLD = 80  # in percentage
DISK_THRESHOLD = 80  # in percentage

# Log file path
LOG_FILE = 'logs/health_log.txt'

def log_message(message):
    """Log message with timestamp."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

def check_cpu_usage():
    """Check CPU usage."""
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_message(f"High CPU usage detected: {cpu_usage}%")

def check_memory_usage():
    """Check memory usage."""
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_message(f"High Memory usage detected: {memory_usage}%")

def check_disk_usage():
    """Check disk usage."""
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_message(f"High Disk usage detected: {disk_usage}%")

def monitor_system():
    """Monitor system health at regular intervals."""
    while True:
        check_cpu_usage()
        check_memory_usage()
        check_disk_usage()
        time.sleep(5)  # Check every 5 seconds

if __name__ == "__main__":
    log_message("Starting System Health Monitoring...")
    monitor_system()
