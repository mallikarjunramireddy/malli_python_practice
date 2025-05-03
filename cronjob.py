import os

def add_cron_job(job_command, schedule):
    cron_job = f"{schedule} {job_command}\n"
    with open("/tmp/cron_job", "w") as file:
        file.write(cron_job)
    os.system("crontab /tmp/cron_job")
    print(f"Cron job added: {cron_job}")

# Example usage
add_cron_job("python3 /home/ec2-user/malli_python_practice/cronjob.py", "* * * * *")  # Run daily at 3 AM
