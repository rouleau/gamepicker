"""
Pool module """

from game import LotteryGame

class GamePool:
    """ Create a game pool composed of lottery games """

    def __init__(self) -> None:
        """Initialize a game pool object composed of game objects

        >>> game_pool = GamePool()
        >>> game_pool
        <__main__.GamePool object at 0x...>

        """


def test():
    """ Test function """

    import doctest

    doctest.testmod(
        verbose=True, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    )


if __name__ == "__main__":
    test()
