"""
Pick module """

import random


class Picker:
    """ Create a picker object for picking bets """

    def __init__(self) -> None:
        """
        Initialize the picker object

        >>> picker = Picker()
        >>> picker
        <__main__.Picker object at 0x...>

        """

    def payoff_rate(self, payoff_rates: list[float]) -> float:
        """
        Return a single payoff rate based on randomness and weight from a list
        of unique theoretical payoff rates from all bets

        >>> payoff_rates = [
        ...     0.4372, 0.45, 0.4555, 0.47, 0.48, 0.49, 0.499,
        ...     0.5, 0.5017, 0.5462, 0.578, 0.5818, 0.6, 0.6259,
        ...     0.6328, 0.64, 0.6622, 0.8479, 0.85, 0.8705, 0.93,
        ... ]
        >>> picker = Picker()
        >>> payoff_rate = picker.payoff_rate(payoff_rates)
        >>> payoff_rate # doctest: +SKIP
        0.8479

        """

        payoff_rate = random.choices(payoff_rates, weights=payoff_rates, k=1)

        return payoff_rate[0]


def test():
    """ Test docstrings using doctest """

    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
