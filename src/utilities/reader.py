"""
File readers for various data formats """

import json


def read_json(filename: str) -> dict:
    with open(filename, "r", encoding="utf-8") as read_file:
        data = json.load(read_file)
    return data
