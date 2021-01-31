"""
Game Pool module """

from game import InstantGame, LotteryGame


class GamePool:
    """ Create a game pool object for game objects """

    def __init__(self) -> None:
        """
        Initialize the game pool object

        >>> game_pool = GamePool()
        >>> game_pool
        <__main__.GamePool object at 0x...>
        >>> game_pool.games
        []

        """

        self.games = []

    def __str__(self) -> str:
        """
        Return a string representation of the game pool object which
        includes all games and bets by overriding the __str__ method.

        >>> lotteries = [
        ...     {
        ...         "name": "Astro",
        ...         "is_active": True,
        ...         "bets": [
        ...             {
        ...                 "theoretical_payoff_rate": 0.4372,
        ...                 "cost": [1, 2, 5],
        ...                 "daily_draw": True,
        ...                 "draw_days": []
        ...             }
        ...         ]
        ...     },
        ...     {
        ...         "name": "Lotto Max",
        ...         "is_active": True,
        ...         "bets": [
        ...             {
        ...                 "theoretical_payoff_rate": 0.48,
        ...                 "cost": [5],
        ...                 "daily_draw": False,
        ...                 "draw_days": ["Tuesday", "Friday"]
        ...             },
        ...             {
        ...                 "theoretical_payoff_rate": 0.495,
        ...                 "cost": [10],
        ...                 "daily_draw": False,
        ...                 "draw_days": ["Tuesday", "Friday"]
        ...             }
        ...         ]
        ...     }
        ... ]
        >>> game_pool = GamePool()
        >>> game_pool.add_games(lotteries, "Lottery")
        >>> print(game_pool)
        Game 1
        Name: Astro
        Active: True
        Bet 1
        Theoretical Payoff Rate: 0.4372
        Cost: [1, 2, 5]
        Daily Draw: True
        Draw Days: []
        <BLANKLINE>
        Game 2
        Name: Lotto Max
        Active: True
        Bet 1
        Theoretical Payoff Rate: 0.48
        Cost: [5]
        Daily Draw: False
        Draw Days: ['Tuesday', 'Friday']
        Bet 2
        Theoretical Payoff Rate: 0.495
        Cost: [10]
        Daily Draw: False
        Draw Days: ['Tuesday', 'Friday']

        """

        str_repr = ""

        # Create a string from all games
        for idx, game in enumerate(self.games, start=1):
            str_repr = str_repr + f"Game {idx}\n{str(game)}"

        return str_repr

    def add_games(self, games: list[dict], category: str) -> None:
        """
        Create and add game objects to the game pool object

        >>> lotteries = [
        ...     {
        ...         "name": "Astro",
        ...         "is_active": True,
        ...         "bets": [
        ...             {
        ...                 "theoretical_payoff_rate": 0.4372,
        ...                 "cost": [1],
        ...                 "daily_draw": True,
        ...                 "draw_days": []
        ...             }
        ...         ]
        ...     },
        ...     {
        ...         "name": "Lotto Max",
        ...         "is_active": True,
        ...         "bets": [
        ...             {
        ...                 "theoretical_payoff_rate": 0.48,
        ...                 "cost": [5],
        ...                 "daily_draw": False,
        ...                 "draw_days": ["Tuesday", "Friday"]
        ...             }
        ...         ]
        ...     }
        ... ]
        >>> game_pool = GamePool()
        >>> game_pool.add_games(lotteries, "Lottery")
        >>> game_pool.games
        [<game.LotteryGame object at 0x...>,
         <game.LotteryGame object at 0x...>]

        """

        if category == "Instant":
            self.games = self.games + [InstantGame(game) for game in games]
        elif category == "Lottery":
            self.games = self.games + [LotteryGame(game) for game in games]

    def payoff_rates(self) -> list[float]:
        """
        Return a sorted list from a set of theoretical payoff rates from all bets

        >>> instants = [
        ...     {
        ...         "name": "Holiday Towers",
        ...         "is_active": True,
        ...         "bets": [
        ...             {
        ...                 "theoretical_payoff_rate": 0.93,
        ...                 "cost": [0.5, 1, 2.5, 5],
        ...             },
        ...             {
        ...                 "theoretical_payoff_rate": 0.8705,
        ...                 "cost": [10, 15, 20, 25, 50],
        ...             }
        ...         ],
        ...     },
        ...     {
        ...         "name": "Home for the Holly-Days",
        ...         "is_active": True,
        ...         "bets": [
        ...             {
        ...                 "theoretical_payoff_rate": 0.8705,
        ...                 "cost": [0.5, 1, 2, 5, 10],
        ...             }
        ...         ],
        ...     },
        ... ]
        >>> game_pool = GamePool()
        >>> game_pool.add_games(instants, "Instant")
        >>> game_pool.payoff_rates()
        [0.8705, 0.93]

        """

        theoretical_payoff_rates = {
            bet.theoretical_payoff_rate for game in self.games for bet in game.bets
        }

        return sorted(theoretical_payoff_rates)


def test():
    """ Test docstrings using doctest """
    
    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
