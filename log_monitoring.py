import time
import os

def monitor_logs(log_file):
    with open(log_file, "r") as file:
        file.seek(0, os.SEEK_END)  # Move to the end of the file
        while True:
            line = file.readline()
            if not line:
                time.sleep(1)  # Wait for new lines
                continue
            print(line.strip())

# Example usage
monitor_logs("/var/log/messages")