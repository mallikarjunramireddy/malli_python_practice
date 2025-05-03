import psutil

def monitor_system():
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()

    print(f"CPU Usage: {cpu_usage}%")
    print(f"Total Memory: {memory_info.total // (1024**3)} GB")
    print(f"Available Memory: {memory_info.available // (1024**3)} GB")
    print(f"Memory Usage: {memory_info.percent}%")

# Example usage
monitor_system()