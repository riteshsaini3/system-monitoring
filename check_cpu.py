import psutil
import time
from datetime import datetime

# Thresholds
cpu_threshold = 75   # in percent
mem_threshold = 80   # in percent
check_interval = 1   # second

def check_system_health():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory()
    mem_usage = memory.percent

    print(f"\n Time: {datetime.now()}")
    print(f"Cpu usage: {cpu_usage}")
    print(f"Memory usage: {mem_usage}")

    if  cpu_usage > cpu_threshold:
      print("ALERT: cpu usage exceeded threshold!")

    if mem_usage > mem_threshold:
       print("ALERT: memory usage exceeded threshold!")

def main():
    print("System Monitoring Started...")
while True:
    check_system_health()
    time.sleep(check_interval) 

if __name__ == "_main_":
    main()