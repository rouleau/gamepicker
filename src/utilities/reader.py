"""
Data readers for various data formats """

import json


def read_json(json_file: str) -> dict:
    with open(json_file, "r", encoding="utf-8") as read_file:
        data = json.load(read_file, encoding="UTF-8")
    return data
