""" Quotidienne 2, Quotidienne 3, Quotidienne 4 """


class Quotidienne:
    """ Baseclass for a Quotidienne lottery ticket """

    def __init__(self) -> None:
        """
        Initialize a new base lottery ticket.

        >>> base_ticket = Quotidienne()
        >>> base_ticket.name
        'Quotidienne'

        """
        self.name = "Quotidienne"
        self.is_active = True
        self.online = True
        self.first_draw = "September 10, 1979"
        self.draw_frequency = "Daily"
        self.deadline_wagers = "10:30 p.m. every evening"
        self.wager_exact_order = [0, 0.50, 1, 2, 5, 10]
        self.wager_any_order = [0, 0.50, 1, 2, 5, 10]


def main():
    import doctest

    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
