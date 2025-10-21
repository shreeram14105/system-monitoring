import psutil
import logging
from datetime import datetime

# Setup logging
logging.basicConfig(
    filename='system_health.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Thresholds
CPU_THRESHOLD = 80    # percent
MEM_THRESHOLD = 80    # percent
DISK_THRESHOLD = 80   # percent

def check_cpu():
    cpu = psutil.cpu_percent(interval=1)
    if cpu > CPU_THRESHOLD:
        logging.warning(f"High CPU Usage detected: {cpu}%")
    return cpu

def check_memory():
    memory = psutil.virtual_memory()
    if memory.percent > MEM_THRESHOLD:
        logging.warning(f"High Memory Usage detected: {memory.percent}%")
    return memory.percent

def check_disk():
    disk = psutil.disk_usage('/')
    if disk.percent > DISK_THRESHOLD:
        logging.warning(f"High Disk Usage detected: {disk.percent}%")
    return disk.percent

def check_processes():
    processes = [p.info for p in psutil.process_iter(['pid', 'name', 'cpu_percent'])]
    high_cpu_processes = [p for p in processes if p['cpu_percent'] > 50]
    if high_cpu_processes:
        logging.warning(f"High CPU Processes: {high_cpu_processes}")
    return processes

def main():
    cpu = check_cpu()
    mem = check_memory()
    disk = check_disk()
    processes = check_processes()

    print(f"CPU Usage: {cpu}%")
    print(f"Memory Usage: {mem}%")
    print(f"Disk Usage: {disk}%")
    print(f"Top processes by CPU usage logged in system_health.log")

if __name__ == "__main__":
    main()
