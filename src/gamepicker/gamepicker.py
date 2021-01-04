"""
Loto-Québec Game Picker

"""

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2021 Alain Rouleau. All rights reserved."

from json_reader import read_data


def main():
    # Open and read the Loto-Quebec games file
    data = read_data("src/gamepicker/data/Quotidienne.json")
    print(data)


if __name__ == "__main__":
    main()
