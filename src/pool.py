"""
Pool module """

from game import LotteryGame


class GamePool:
    """ Create a pool object for game objects """

    def __init__(self) -> None:
        """
        Initialize the pool object

        >>> game_pool = GamePool()
        >>> game_pool
        <__main__.GamePool object at 0x...>
        >>> game_pool.games
        []

        """

        self.games = []

    def add_games(self, games: list[dict]) -> None:
        """
        Create and append game objects to the pool object

        >>> games = [
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

        """

        pass


def test():
    """ Test function """

    import doctest

    doctest.testmod(
        verbose=True, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    )


if __name__ == "__main__":
    test()
