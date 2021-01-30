"""
PROJECT: GAMEPICKER

An advanced toolkit for selecting Loto-Québec games """

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2021 Alain Rouleau. All rights reserved."

from pool import GamePool
from utilities.reader import read_json

# Read games from JSON files
instants = read_json("../data/instants.json")["games"]
lotteries = read_json("../data/lotteries.json")["games"]

# Create and add game objects to a game pool object
my_game_pool = GamePool()
my_game_pool.add_games(instants, "Instant")
my_game_pool.add_games(lotteries, "Lottery")

# Display all games and bets in the game pool
print(my_game_pool)

# theoretical_payoff_rates = my_game_pool.payoff_rates()
# print(theoretical_payoff_rates)
