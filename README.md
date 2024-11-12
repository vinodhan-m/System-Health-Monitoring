# System-Health-Monitoring\
This project consists of two Python scripts that monitor system health and application uptime. These scripts provide real-time alerts and log critical issues, helping to ensure optimal system performance and application availability.

### Table of Contents
-Project Structure
-Features
-Setup
-Usage
-Log Files
-Troubleshooting

### Project Structure
system_health_monitor/
├── monitor_system.py     # System health monitoring script
├── check_app_health.py   # Application health checker script
└── logs/
    └── health_log.txt    # Log file for alerts and health check messages

### Features
1. System Health Monitoring (monitor_system.py):
-Monitors CPU, memory, and disk usage.
-Logs alerts if any metrics exceed predefined thresholds.
2. Application Health Checking (check_app_health.py):
-Monitors the uptime of a specified application by checking its HTTP status.
-Logs alerts if the application is down or unreachable.

### Setup
1. Install Python:
-Ensure that Python is installed on your system. You can download it from python.org.
2. Install Required Libraries:
-Open a terminal in the project directory and run the following command:
   ````pip install psutil requests````
3. Set Up Directory:
-Create a logs directory within system_health_monitor to store log files.
-Inside logs, create an empty file named health_log.txt.

### Usage
1. System Health Monitoring:
-Run the following command in the terminal to start monitoring system health:
   ````python monitor_system.py````
-This script will log alerts if CPU, memory, or disk usage exceeds specified thresholds.
2. Application Health Checker:
-Open check_app_health.py and set the URL variable to the application's URL you want to monitor.
   ````python check_app_health.py````
-This script will log an alert if the application is down or unreachable.

### Log Files
-All alerts are stored in logs/health_log.txt with timestamps. Here is an example of log entries:
[2024-11-10 10:05:21] High CPU usage detected: 85%
[2024-11-10 10:10:42] Application is DOWN. Status code: 503
[2024-11-10 10:15:01] High Memory usage detected: 82%
[2024-11-10 10:20:12] Application check failed: Connection timeout

### Troubleshooting
1. Error: ModuleNotFoundError:
- Ensure psutil and requests libraries are installed.
   ````pip install psutil requests````
2. Application URL Not Responding:
-Check the URL in check_app_health.py and verify the application is running at that URL.
3. Stopping the Script:
-To stop either script, press Ctrl + C in the terminal where the script is running.



