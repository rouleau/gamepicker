"""
Event module """

from datetime import date, timedelta


class Schedule:
    """ Create a schedule for buying tickets """

    def __init__(self) -> None:
        """
        Initialize the schedule object

        >>> schedule = Schedule()
        >>> schedule
        <__main__.Schedule object at 0x...>

        """


def test():
    """ Test docstrings using doctest """

    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
