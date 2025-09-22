import hashlib
import json
import os
from logs import log_event

USER_DB_FILE = "users.json"
# load_users() reads (loads) the JSON in users.json and converts it into a Python dict
def load_users():
    if not os.path.exists(USER_DB_FILE):
        return {}
    with open(USER_DB_FILE, "r") as f:
        return json.load(f) #loads json file as a dictionary

#save_users(users) takes a Python dict (users) and writes it back out to users.json in JSON format (overwriting whatever was there).
def save_users(users):
    with open(USER_DB_FILE, "w") as f:
        json.dump(users, f, indent=4)  #writes to the json file in a formatted json format

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest() #hashes the json file passwords

def register_user(username, password, role):
    users = load_users()

    if username in users:
        return False, "Username already exists."

    if role not in ['admin', 'user']:
        return False, "Invalid role."

    users[username] = {
        "password": hash_password(password),
        "role": role
    }
    save_users(users)
    log_event(username, "registered")  # filename removed
    return True, "Registration successful."

def login_user(username, password):
    users = load_users()

    if username not in users:
        return None, "User does not exist."

    hashed = hash_password(password)
    if users[username]["password"] != hashed:
        return None, "Incorrect password."

    log_event(username, "logged in")  # filename removed
    return {"username": username, "role": users[username]["role"]}, "Login successful."

def delete_user(current_user, username_to_delete):
    if current_user["role"] != "admin":
        return False, "Only admins can delete user accounts."

    users = load_users()
    if username_to_delete not in users:
        return False, "User does not exist."

    if username_to_delete == current_user["username"]:
        return False, "You cannot delete your own account while logged in."

    admin_count = sum(1 for u in users.values() if u["role"] == "admin")
    if users[username_to_delete]["role"] == "admin" and admin_count == 1:
        return False, "Cannot delete the last remaining admin."

    del users[username_to_delete]
    save_users(users)
    log_event(current_user["username"], f"deleted user '{username_to_delete}'")  # filename removed
    return True, f"User '{username_to_delete}' deleted successfully."

def get_all_users():
    return load_users()
