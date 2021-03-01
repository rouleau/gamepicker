""" Picker module """


class Picker:
    """ Create a picker object for picking bets """

    def __init__(self) -> None:
        """
        Initialize the picker object

        >>> picker = Picker()
        >>> picker
        <__main__.Picker object at 0x...>

        """


def test():
    """ Test docstrings using doctest """

    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
