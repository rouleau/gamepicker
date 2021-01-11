"""
PROJECT: GAMEPICKER

An advanced toolkit for selecting Loto-Québec games """

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2021 Alain Rouleau. All rights reserved."

from utilities.rate import unique_rates
from utilities.reader import read_json

# open and read JSON files
instants = read_json("data/instants.json")
lotteries = read_json("data/lotteries.json")

# create lists of unique payoff rates from ALL bets
instant_payoff_rates = unique_rates(instants)
lottery_payoff_rates = unique_rates(lotteries)

# merge and sort lists of unique payoff rates
payoff_rates = instant_payoff_rates + lottery_payoff_rates
payoff_rates = set(payoff_rates)
payoff_rates = sorted(payoff_rates)

print(payoff_rates)

# TODO calculate budget

# TODO pick bets

# TODO display picked bets
