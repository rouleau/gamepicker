"""
PROJECT: GAMEPICKER

An advanced toolkit for selecting Loto-Québec games

"""

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2021 Alain Rouleau. All rights reserved."

import random

from datetime import datetime
from utilities.data import read_json

# Open and read games file
games = "..\data\games\games.json"
games = read_json(games)["games"]

print(games)
