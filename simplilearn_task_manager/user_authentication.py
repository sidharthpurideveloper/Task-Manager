import hashlib
import os

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

class UserAuthentication:
    def __init__(self, credentials_file='users.txt'):
        self.credentials_file = credentials_file
        if not os.path.exists(self.credentials_file):
            open(self.credentials_file, 'w').close()

    def register(self, username, password):
        if self.user_exists(username):
            print("Username already exists. Please choose another username.")
            return False
        with open(self.credentials_file, 'a') as f:
            f.write(f"{username},{hash_password(password)}\n")
        print("Registration successful!")
        return True

    def login(self, username, password):
        if self.user_exists(username):
            with open(self.credentials_file, 'r') as f:
                for line in f:
                    stored_username, stored_password = line.strip().split(',')
                    if username == stored_username and hash_password(password) == stored_password:
                        print("Login successful!")
                        return True
        print("Invalid username or password.")
        return False

    def user_exists(self, username):
        with open(self.credentials_file, 'r') as f:
            for line in f:
                stored_username, _ = line.strip().split(',')
                if username == stored_username:
                    return True
        return False
