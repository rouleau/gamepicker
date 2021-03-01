""" Budget planner """

from random import choice, choices

budget = 100
bet_amounts = [2, 3, 4, 5]

bets = []

while budget > 2:
    bet = choice(bet_amounts)
    if bet <= budget:
        bets.append(bet)
        budget = budget - bet

print("Bets:", bets)
print("Number of Bets:", len(bets))
