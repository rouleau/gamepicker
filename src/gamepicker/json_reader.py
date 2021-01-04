"""
Read data from JSON file

"""

import json

def read_data(json_file: str) -> dict:
    with open(json_file, "r", encoding="utf-8") as read_file:
        data = json.load(read_file, encoding="UTF-8")
    return data
