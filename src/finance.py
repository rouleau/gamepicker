"""
Finance module """


class Budget:
    """ Create a budget for picking bets and buying tickets """

    def __init__(self) -> None:
        """
        Initialize the budget object

        >>> budget = Budget()
        >>> budget
        <__main__.Budget object at 0x...>

        """


def test():
    """ Test docstrings using doctest """

    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
