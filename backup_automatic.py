import os
import tarfile
from datetime import datetime

def create_backup(source_dir, backup_dir):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = os.path.join(backup_dir, f"backup_{timestamp}.tar.gz")
    
    with tarfile.open(backup_file, "w:gz") as tar:
        tar.add(source_dir, arcname=os.path.basename(source_dir))
    
    print(f"Backup created at {backup_file}")

# Example usage
create_backup("/home/ec2-user/malli_python_practice", "/var/backups")