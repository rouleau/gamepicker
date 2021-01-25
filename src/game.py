"""
Game module """


class LotteryBet:
    """ Create a lottery bet object from a dict """

    def __init__(self, lottery_bet: dict) -> None:
        """
        Initialize a lottery bet object from a dict

        >>> lottery_bet = {
        ...     "theoretical_payoff_rate": 0.4372,
        ...     "cost": [1, 2, 4, 5, 10, 20],
        ...     "daily_draw": False,
        ...     "draw_days": ["Monday", "Thursday"],
        ... }
        >>> bet = LotteryBet(lottery_bet)
        >>> bet.theoretical_payoff_rate
        0.4372
        >>> bet.cost
        [1, 2, 4, 5, 10, 20]
        >>> bet.daily_draw
        False
        >>> bet.draw_days
        ['Monday', 'Thursday']

        """

        self.theoretical_payoff_rate = lottery_bet["theoretical_payoff_rate"]
        self.cost = lottery_bet["cost"]
        self.daily_draw = lottery_bet["daily_draw"]
        self.draw_days = lottery_bet["draw_days"]

    def __str__(self) -> str:
        """
        Return a string representation of the lottery bet object which
        includes the theoretical payoff rate, cost, daily draw, and draw days
        by overriding the __str__ method.

        >>> lottery_bet = {
        ...     "theoretical_payoff_rate": 0.4372,
        ...     "cost": [1, 2, 4, 5, 10, 20],
        ...     "daily_draw": False,
        ...     "draw_days": ["Monday", "Thursday"],
        ... }
        >>> bet = LotteryBet(lottery_bet)
        >>> print(bet)
        Theoretical Payoff Rate: 0.4372
        Cost: [1, 2, 4, 5, 10, 20]
        Daily Draw: False
        Draw Days: ['Monday', 'Thursday']
        <BLANKLINE>

        """

        line_1 = f"Theoretical Payoff Rate: {self.theoretical_payoff_rate}\n"
        line_2 = f"Cost: {self.cost}\n"
        line_3 = f"Daily Draw: {self.daily_draw}\n"
        line_4 = f"Draw Days: {self.draw_days}\n"

        return line_1 + line_2 + line_3 + line_4


class LotteryGame:
    """ Create a lottery game object from a dict """

    def __init__(self, lottery_game: dict) -> None:
        """
        Initialize a lottery game object from a dict

        >>> lottery_game = {
        ...     "name": "Lotto :D",
        ...     "is_active": True,
        ...     "bets": [
        ...         {
        ...             "theoretical_payoff_rate": 0.6259,
        ...             "cost": [2],
        ...             "daily_draw": False,
        ...             "draw_days": ["Monday", "Thursday"],
        ...         },
        ...         {
        ...             "theoretical_payoff_rate": 0.6622,
        ...             "cost": [5],
        ...             "daily_draw": True,
        ...             "draw_days": [],
        ...         },
        ...     ],
        ... }
        >>> game = LotteryGame(lottery_game)
        >>> game.name
        'Lotto :D'
        >>> game.is_active
        True
        >>> game.bets # doctest: +ELLIPSIS +NORMALIZE_WHITESPACE
        [<__main__.LotteryBet object at 0x...>,
         <__main__.LotteryBet object at 0x...>]

        """

        self.name = lottery_game["name"]
        self.is_active = lottery_game["is_active"]
        self.bets = [LotteryBet(bet) for bet in lottery_game["bets"]]

    def __str__(self) -> str:
        """
        Return a string representation of the lottery game object which
        includes the name, if active, and the bets by overriding the
        __str__ method.

        >>> lottery_game = {
        ...     "name": "Lotto :D",
        ...     "is_active": True,
        ...     "bets": [
        ...         {
        ...             "theoretical_payoff_rate": 0.6259,
        ...             "cost": [2],
        ...             "daily_draw": False,
        ...             "draw_days": ["Monday", "Thursday"],
        ...         },
        ...         {
        ...             "theoretical_payoff_rate": 0.6622,
        ...             "cost": [5],
        ...             "daily_draw": True,
        ...             "draw_days": [],
        ...         },
        ...     ],
        ... }
        >>> game = LotteryGame(lottery_game)
        >>> print(game)
        Name: Lotto :D
        Active: True
        Bet 1
        Theoretical Payoff Rate: 0.6259
        Cost: [2]
        Daily Draw: False
        Draw Days: ['Monday', 'Thursday']
        Bet 2
        Theoretical Payoff Rate: 0.6622
        Cost: [5]
        Daily Draw: True
        Draw Days: []
        <BLANKLINE>

        """

        line_1 = f"Name: {self.name}\n"
        line_2 = f"Active: {self.is_active}\n"
        line_3 = ""

        # Create a string from all bets
        for idx, bet in enumerate(self.bets, start=1):
            line_3 = line_3 + f"Bet {idx}\n{str(bet)}"

        return line_1 + line_2 + line_3


# TODO
class InstantBet:
    """ Create an instant bet object from a dict """

    pass


# TODO
class InstantGame:
    """ Create an instant game object from a dict """

    pass


def main():
    """ Main function """

    import doctest

    doctest.testmod(verbose=True)


if __name__ == "__main__":
    main()
