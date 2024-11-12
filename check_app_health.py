import requests
import time
from datetime import datetime

# Configuration
URL = "http://example.com"  # Replace with the application URL
CHECK_INTERVAL = 60  # Time interval to check (in seconds)
LOG_FILE = 'logs/health_log.txt'

def log_message(message):
    """Log message with timestamp."""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(LOG_FILE, 'a') as log_file:
        log_file.write(f"[{timestamp}] {message}\n")

def check_application_health():
    """Check if the application is up by verifying the HTTP status code."""
    try:
        response = requests.get(URL, timeout=5)
        if response.status_code == 200:
            print(f"Application is UP. Status code: {response.status_code}")
        else:
            log_message(f"Application is DOWN. Status code: {response.status_code}")
    except requests.exceptions.RequestException as e:
        log_message(f"Application check failed: {e}")

def monitor_application():
    """Continuously check application health at regular intervals."""
    while True:
        check_application_health()
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    log_message("Starting Application Health Checker...")
    monitor_application()
