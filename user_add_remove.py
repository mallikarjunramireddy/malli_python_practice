import os
import subprocess

def create_user(username):
    try:
        subprocess.run(["sudo", "useradd", username], check=True)
        print(f"User {username} created successfully.")
    except subprocess.CalledProcessError:
        print(f"Failed to create user {username}.")

# def delete_user(username):
#     try:
#         subprocess.run(["sudo", "userdel", username], check=True)
#         print(f"User {username} deleted successfully.")
#     except subprocess.CalledProcessError:
#         print(f"Failed to delete user {username}.")

# Example usage
create_user("testuser")
# delete_user("testuser")