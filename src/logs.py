import os
from datetime import datetime

LOG_FILE = "logs.txt"

def log_event(username, action, filename=None):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if filename and filename != "N/A":
        entry = f"[{timestamp}] {username} {action} '{filename}'\n"
    else:
        entry = f"[{timestamp}] {username} {action}\n"

    with open(LOG_FILE, "a") as log:
        log.write(entry)

def view_logs():
    if not os.path.exists(LOG_FILE):
        return False, "No logs available."

    with open(LOG_FILE, "r") as log:
        logs = log.read()
    return True, logs

def clear_logs():
    with open(LOG_FILE, "w") as log:
        log.write("")  # overwrite with empty string
