# app/session_control.py

import os
import json
import datetime

SESSION_FILE = os.path.join(os.path.dirname(__file__), "last_submission.json")
LOCK_HOURS = 20

def check_last_submission_time() -> bool:
    """Check if the user has submitted within the last 20 hours."""
    if not os.path.exists(SESSION_FILE):
        return True  # No prior submission, allow input

    with open(SESSION_FILE, "r") as f:
        data = json.load(f)
    
    last_time_str = data.get("last_submission")
    if not last_time_str:
        return True

    last_time = datetime.datetime.fromisoformat(last_time_str)
    now = datetime.datetime.now()
    elapsed = now - last_time

    return elapsed.total_seconds() >= LOCK_HOURS * 3600

def update_last_submission_time():
    """Update the submission time to now."""
    data = {
        "last_submission": datetime.datetime.now().isoformat()
    }
    with open(SESSION_FILE, "w") as f:
        json.dump(data, f)
