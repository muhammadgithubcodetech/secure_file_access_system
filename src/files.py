import os
from encryption import xor_encrypt_decrypt
from logs import log_event

DATA_FOLDER = "data"
XOR_KEY = "mysecretkey"

# Ensure data folder exists
if not os.path.exists(DATA_FOLDER):
    os.makedirs(DATA_FOLDER)

def get_user_file_path(username, filename):
    safe_name = filename.strip().replace(" ", "_")
    return os.path.join(DATA_FOLDER, f"{username}_{safe_name}.txt")

def create_file(username, filename, content):
    if not filename.strip():
        return False, "Filename cannot be empty."

    if not content.strip():
        return False, "File content cannot be empty."

    filepath = get_user_file_path(username, filename)

    if os.path.exists(filepath):
        return False, "File already exists."

    try:
        # Convert content to bytes, encrypt, write in binary mode
        encrypted_content = xor_encrypt_decrypt(content.encode("utf-8"), XOR_KEY)

        with open(filepath, "wb") as f:
            f.write(encrypted_content)
        log_event(username, "created", filename)
        return True, f"File '{filename}' created and owned by {username}."
    except Exception as e:
        return False, f"Error creating file: {e}"

def view_file(username, role, filename):
    try:
        all_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".txt")]

        accessible_files = [
            f for f in all_files if role == "admin" or f.startswith(f"{username}_")
        ]

        matched_file = next(
            (f for f in accessible_files if f.endswith(f"{filename}.txt")), None
        )

        if not matched_file:
            return False, "File not found or access denied."

        """ 
        matched_file = None
        for f in accessible_files:
            if f.endswith(f"{filename}.txt"):
            matched_file = f
            break
        """

        filepath = os.path.join(DATA_FOLDER, matched_file)

        # Read in binary, decrypt as bytes, decode to string
        with open(filepath, "rb") as f:
            encrypted_content = f.read()

        decrypted_content = xor_encrypt_decrypt(encrypted_content, XOR_KEY).decode("utf-8")
        log_event(username, "viewed", filename)
        return True, decrypted_content
    except Exception as e:
        return False, f"Error viewing file: {e}"

def delete_file(username, role, filename):
    try:
        all_files = [f for f in os.listdir(DATA_FOLDER) if f.endswith(".txt")]

        accessible_files = [
            f for f in all_files if role == "admin" or f.startswith(f"{username}_")
        ]

        matched_file = next(
            (f for f in accessible_files if f.endswith(f"{filename}.txt")), None
        )

        if not matched_file:
            return False, "File not found or access denied."


        filepath = os.path.join(DATA_FOLDER, matched_file)
        os.remove(filepath)

        log_event(username, "deleted", filename)
        return True, f"Deleted file: {matched_file}"
    except Exception as e:
        return False, f"Error deleting file: {e}"
