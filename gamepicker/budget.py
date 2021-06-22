""" Budget module """


class Budget:
    """ Create a budget for placing bets """

    def __init__(self, balance: float = 0.0, period: str = "Day") -> None:
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

    def decrease(self, amount: float) -> None:
        """
        Decrease budget balance

        >>> budget = Budget(10.25)
        >>> budget.balance
        10.25
        >>> budget.decrease(5.75)
        >>> budget.balance
        4.5
        >>> budget.decrease(5.75)
        >>> budget.balance
        -1.25

        """
        self.balance = self.balance - amount

    def increase(self, amount: float) -> None:
        """
        Increase budget balance

        >>> budget = Budget()
        >>> budget.balance
        0.0
        >>> budget.increase(5.75)
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
