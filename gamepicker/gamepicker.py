"""
PROJECT: GAMEPICKER

An advanced toolkit for selecting Loto-Québec games

"""

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2021 Alain Rouleau. All rights reserved."

import random

from datetime import datetime

from budget import Budget
from datareader import read_json
from rate import payoff_rates

# Start program
print()
print("Welcome to the Espacejeux Game Picker!")
print()

# Create budget
amount = float(input("Enter today's budget: "))
budget = Budget(amount)

print()

# Open and read games file
games = "..\data\games\games.json"
games = read_json(games)["games"]

print("Number of games:", len(games))
print(games)
print()

# Determine active and non-active games
games_active = []
games_not_active = []

for game in games:
    if game["is_active"]:
        games_active.append(game)
    else:
        games_not_active.append(game)

print("Active games:", len(games_active))
print("Non-active games:", len(games_not_active))
print()

# Determine available and non-available games
games_available = []
games_not_available = []

for game in games_active:
    if game["type"] == "instant":
        games_available.append(game)
    elif game["type"] == "lottery":
        if game["daily_draw"]:
            games_available.append(game)
        elif datetime.now().strftime("%A") in game["draw_days"]:
            games_available.append(game)
        else:
            games_not_available.append(game)

print("Available games:", games_available)
print()
print("Non-available games:", games_not_available)
print()

# Determine payoff rates for available games
rates = payoff_rates(games_available)

print("Payoff Rates:", rates)
print()

# Choose a payoff rate
payoff_pick = random.choices(rates, rates, k=1)
payoff_pick = payoff_pick[0]

print("Payoff pick:", payoff_pick)
print()

# Determine available games with payoff pick
picks = []

for game in games_available:
    for bet in game["bets"]:
        if bet["theoretical_payoff_rate"] == payoff_pick:
            picks.append([game["name"], bet])

print("Game Picks:", picks)
print()

# Choose pick for today if more than one game
pick_for_today = random.choice(picks)

print("Pick for Today:", pick_for_today)
print()

# Pick message
pick_name = pick_for_today[0]
pick_cost = pick_for_today[1]
pick_message = f"Buy a {pick_name} for $ {pick_cost['cost']}"

print("Today's Pick:", pick_message)
