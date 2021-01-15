"""
PROJECT: GAMEPICKER

An advanced toolkit for selecting Loto-Québec games """

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2021 Alain Rouleau. All rights reserved."

import game
import gamepicker

gamepicker.picks()

lottery_bet = {
    "theoretical_payoff_rate": 0.4372,
    "cost": [1, 2, 4, 5, 10, 20],
    "daily_draw": False,
    "draw_days": ["Monday", "Thursday"],
}

bet = game.Bet(lottery_bet)
print(bet)

