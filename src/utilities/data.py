"""
Data utilities for various formats """

import json


def read_json(filename: str) -> dict:
    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    return data
