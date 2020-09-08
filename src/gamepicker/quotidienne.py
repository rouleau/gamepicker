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
