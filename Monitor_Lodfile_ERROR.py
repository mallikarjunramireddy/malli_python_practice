import re
def monitor_log(logfile, error_keyword="ERROR"):
    with open(logfile, 'r') as file:
        for line in file:
            if error_keyword in line:
                print(f"Error found: {line.strip()}")
if __name__ == "__main__":
    logfile = input("Enter the log file path: ")
    keyword = input("Enter the keyword to search for (default: ERROR): ") or "ERROR"
    monitor_log(logfile, keyword)
