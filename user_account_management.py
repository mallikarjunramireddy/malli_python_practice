import os
import subprocess
def create_user(username):
    try:
        # Check if the user already exists
        result = subprocess.run(['id', username], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if result.returncode == 0:
            print(f"User '{username}' already exists.")
        else:
            # Create the user
            subprocess.run(['sudo', 'useradd', '-m', username])
            print(f"User '{username}' created successfully.")
    except Exception as e:
        print(f"Error: {e}")
if __name__ == "__main__":
    username = input("Enter the username to create: ")
    create_user(username)
    