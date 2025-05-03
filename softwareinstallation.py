import subprocess

def install_package(package_name):
    try:
        subprocess.run(["sudo", "yum", "install", "-y", package_name], check=True)
        print(f"Package {package_name} installed successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to install package {package_name}.")

def check_package(package_name):
    try:
        result = subprocess.run(["yum", "list", "installed", package_name], check=True, text=True, capture_output=True)
        print(result.stdout)
    except subprocess.CalledProcessError:
        print(f"Package {package_name} is not installed.")

# Example usage
install_package("git")
check_package("git")