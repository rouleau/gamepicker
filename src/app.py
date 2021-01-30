"""
PROJECT: GAMEPICKER

An advanced toolkit for selecting Loto-Québec games """

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2021 Alain Rouleau. All rights reserved."

from gamepicker import picks
from pool import GamePool

picks()
print()

instants = [
    {
        "name": "Holiday Towers",
        "is_active": True,
        "bets": [
            {
                "theoretical_payoff_rate": 0.93,
                "cost": [0.5, 1, 2.5, 5, 10, 15, 20, 25, 50],
            }
        ],
    },
    {
        "name": "Home for the Holly-Days",
        "is_active": True,
        "bets": [
            {
                "theoretical_payoff_rate": 0.8705,
                "cost": [0.5, 1, 2, 5, 10],
            }
        ],
    },
]

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

my_game_pool = GamePool()
my_game_pool.add_games(instants, "Instant")
my_game_pool.add_games(lotteries, "Lottery")

for game in my_game_pool.games:
    print(game)
