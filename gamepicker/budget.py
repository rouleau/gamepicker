""" Budget module """


class Budget:
    """ Create a budget for placing bets """

    def __init__(self, balance: float = 0.00, period: str = "Day") -> None:
        """
        Initialize the budget object

        >>> budget = Budget()
        >>> budget
        <__main__.Budget object at 0x...>
        >>> budget.balance
        0.0
        >>> budget.period
        'Day'

        """
        self.balance = balance
        self.period = period

    def add_funds(self, amount: float) -> None:
        """
        Add funds to budget balance

        >>> budget = Budget()
        >>> budget.balance
        0.0
        >>> budget.add_funds(5.75)
        >>> budget.balance
        5.75

        """
        self.balance = self.balance + amount


def test():
    """ Test docstrings using doctest """

    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
