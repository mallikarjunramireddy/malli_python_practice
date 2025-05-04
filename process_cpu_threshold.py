import psutil

def terminate_high_cpu_process(threshold):
    for proc in psutil.process_iter(['pid', 'name', 'cpu_percent']):
        try:
            if proc.info['cpu_percent'] > threshold:
                print(f"Terminating {proc.info['name']} (PID: {proc.info['pid']})")
                proc.terminate()
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue

# Example usage
terminate_high_cpu_process(threshold=10)