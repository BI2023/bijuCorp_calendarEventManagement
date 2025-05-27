# from datetime import date

# def get_status_for_date(check_date: date) -> str:
#     # Simulated logic: even days are "success", odd are "failure"
#     return 'success' if check_date.day % 2 == 0 else 'failure'


# from datetime import date

# def get_status_for_date(check_date: date) -> str:
#     return 'success' if check_date.day % 2 == 0 else 'failure'


# =========================


# import json
# from datetime import date
# import os

# STATUS_FILE = os.path.join(os.path.dirname(__file__), "status_history.json")

# def load_status_data():
#     try:
#         with open(STATUS_FILE, "r") as f:
#             return json.load(f)
#     except (FileNotFoundError, json.JSONDecodeError):
#         return {}

# def get_stored_status(check_date: date) -> str:
#     data = load_status_data()
#     return data.get(check_date.isoformat(), "")




# ==================================


import json
import os

STATUS_FILE = os.path.join(os.path.dirname(__file__), "status_history.json")

def load_status_data():
    try:
        with open(STATUS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}
