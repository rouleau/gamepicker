"""
Loto-Québec Game Picker

"""

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2021 Alain Rouleau. All rights reserved."

from utilities.reader import read_json


def main():
    # Open and read the Loto-Quebec games file
    data = read_json("data/Quotidienne.json")
    print(data)


if __name__ == "__main__":
    main()
