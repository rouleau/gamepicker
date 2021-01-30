"""
PROJECT: GAMEPICKER

An advanced toolkit for selecting Loto-Québec games """

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2021 Alain Rouleau. All rights reserved."

from game import LotteryBet, LotteryGame
from gamepicker import picks

picks()
print()

lottery_bet = {
    "theoretical_payoff_rate": 0.4372,
    "cost": [1, 2, 4, 5, 10, 20],
    "daily_draw": False,
    "draw_days": ["Monday", "Thursday"],
}

my_bet = LotteryBet(lottery_bet)
print(my_bet)

lottery_game = {
    "name": "Lotto :D",
    "is_active": True,
    "bets": [
        {
            "theoretical_payoff_rate": 0.6259,
            "cost": [2],
            "daily_draw": False,
            "draw_days": ["Monday", "Thursday"],
        },
        {
            "theoretical_payoff_rate": 0.6622,
            "cost": [5],
            "daily_draw": True,
            "draw_days": [],
        },
    ],
}

lotteries = [
    {
        "name": "Astro",
        "is_active": True,
        "bets": [
            {
                "theoretical_payoff_rate": 0.4372,
                "cost": [1],
                "daily_draw": True,
                "draw_days": [],
            }
        ],
    },
    {
        "name": "Lotto Max",
        "is_active": True,
        "bets": [
            {
                "theoretical_payoff_rate": 0.48,
                "cost": [5],
                "daily_draw": False,
                "draw_days": ["Tuesday", "Friday"],
            }
        ],
    },
]


my_game = LotteryGame(lottery_game)
print(my_game)
