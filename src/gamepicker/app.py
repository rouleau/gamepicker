"""
Entry point for the Game Picker application
"""
from json_reader import read_data

# Open and read the Loto-Quebec games file
data = read_data("src/gamepicker/data/Quotidienne.json")
print(data)
