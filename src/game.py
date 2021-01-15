"""
Game module """


class Bet:
    """ Create a bet """

    def __init__(self, game_bet: dict) -> None:
        """
        Initialize a new bet from a dict

        >>> lottery_bet = {
        ... "theoretical_payoff_rate": 0.4372,
        ... "cost": [1, 2, 4, 5, 10, 20],
        ... "daily_draw": False,
        ... "draw_days": ["Monday", "Thursday"]
        ... }
        >>> bet = Bet(lottery_bet)
        >>> bet.theoretical_payoff_rate
        0.4372
        >>> bet.cost
        [1, 2, 4, 5, 10, 20]
        >>> bet.daily_draw
        False
        >>> bet.draw_days
        ['Monday', 'Thursday']

        """
        self.theoretical_payoff_rate = game_bet["theoretical_payoff_rate"]
        self.cost = game_bet["cost"]
        self.daily_draw = game_bet["daily_draw"]
        self.draw_days = game_bet["draw_days"]

    def __str__(self) -> None:
        """
        Return a string representation of the Bet object which includes
        the theoretical payoff rate, cost, daily draw, and draw days by
        overriding the __str__ method.

        >>> lottery_bet = {
        ... "theoretical_payoff_rate": 0.4372,
        ... "cost": [1, 2, 4, 5, 10, 20],
        ... "daily_draw": False,
        ... "draw_days": ["Monday", "Thursday"]
        ... }
        >>> bet = Bet(lottery_bet)
        >>> print(bet)
        Theoretical Payoff Rate: 0.4372
        Cost: [1, 2, 4, 5, 10, 20]
        Daily Draw: False
        Draw Days: ['Monday', 'Thursday']

        """
        line_1 = f"Theoretical Payoff Rate: {self.theoretical_payoff_rate}\n"
        line_2 = f"Cost: {self.cost}\n"
        line_3 = f"Daily Draw: {self.daily_draw}\n"
        line_4 = f"Draw Days: {self.draw_days}"

        return line_1 + line_2 + line_3 + line_4


class Lottery:
    """ Create a Lottery game """

    pass


class Instant:
    """ Create an Instant game """

    pass


def main():
    """ Main function """

    import doctest

    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
