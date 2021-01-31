"""
Pick module """

class Picker():
    """ Create a picker object for picking bets """

    def __init__(self) -> None:
        """
        Initialize the picker object
        
        >>> picker = Picker()
        >>> picker
        <__main__.Picker object at 0x...>
        
        """

def test():
    """ Doctest function """

    import doctest

    doctest.testmod(
        verbose=True, optionflags=doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    )


if __name__ == "__main__":
    test()
