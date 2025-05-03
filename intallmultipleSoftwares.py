import subprocess
import sys
# python3 install_packages.py git mysql-server curl

def install_packages(packages):
    for package in packages:
        print(f"\nInstalling package: {package}")
        try:
            subprocess.run(["sudo", "apt", "install", "-y", package], check=True)
            print(f"✅ {package} installed successfully.")
        except subprocess.CalledProcessError:
            print(f"❌ Failed to install {package}.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 install_packages.py <package1> <package2> ...")
        sys.exit(1)
    
    packages = sys.argv[1:]
    install_packages(packages)
