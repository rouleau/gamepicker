"""
Quotidienne 2, Quotidienne 3, Quotidienne 4
"""

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2020 Alain Rouleau. All rights reserved."


class Quotidienne:
    """
    Create a Quotidienne lottery ticket.
    """

    def __init__(self, numbers: int) -> None:
        """
        Initialize a new lottery ticket.

        >>> lottery_ticket = Quotidienne(2)
        >>> lottery_ticket.name            
        'Quotidienne 2'
        """
        self.name = "Quotidienne " + str(numbers)
        self.payoff_rate = {"Quotidienne 2": "50%", "Quotidienne 3": "45%", "Quotidienne 4": "45%"}
        self.first_draw = "September 10, 1979"
        self.draw_frequency = "Daily"
        self.deadline_wagers = "10:30 p.m. every evening"
        self.any_order = [0.50, 1, 2, 5, 10]
        self.exact_order = [0.50, 1, 2, 5, 10]

def main():
    import doctest

    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
