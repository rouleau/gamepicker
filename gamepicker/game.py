""" Game module """

from datetime import datetime


class InstantBet:
    """ Create an Instant bet object from a dict """

    def __init__(self, instant_bet: dict) -> None:
        """
        Initialize an Instant bet object from a dict

        >>> instant_bet = {
        ...     "theoretical_payoff_rate": 0.8705,
        ...     "cost": [0.5, 1, 2, 5, 10]
        ... }
        >>> bet = InstantBet(instant_bet)
        >>> bet
        <__main__.InstantBet object at 0x...>
        >>> bet.is_available
        >>> bet.theoretical_payoff_rate
        0.8705
        >>> bet.cost
        [0.5, 1, 2, 5, 10]

        """
        self.is_available = None
        self.theoretical_payoff_rate = instant_bet["theoretical_payoff_rate"]
        self.cost = instant_bet["cost"]

    def __str__(self) -> str:
        """
        Return a string representation of the Instant bet object which includes
        if available, the theoretical payoff rate and cost by overriding the
        __str__ method.

        >>> instant_bet = {
        ...     "theoretical_payoff_rate": 0.8705,
        ...     "cost": [0.5, 1, 2, 5, 10]
        ... }
        >>> bet = InstantBet(instant_bet)
        >>> print(bet)
        Available: None
        Theoretical Payoff Rate: 0.8705
        Cost: [0.5, 1, 2, 5, 10]

        """
        line_1 = f"Available: {self.is_available}\n"
        line_2 = f"Theoretical Payoff Rate: {self.theoretical_payoff_rate}\n"
        line_3 = f"Cost: {self.cost}\n"

        return line_1 + line_2 + line_3


class InstantGame:
    """ Create an Instant game object from a dict """

    def __init__(self, instant_game: dict) -> None:
        """
        Initialize an Instant game object from a dict

        >>> instant_game = {
        ...     "name": "Merry Multiplier",
        ...     "is_active": True,
        ...     "bets": [
        ...         {
        ...             "theoretical_payoff_rate": 0.8479,
        ...             "cost": [3]
        ...         },
        ...         {
        ...             "theoretical_payoff_rate": 0.85,
        ...             "cost": [1, 2, 4, 5]
        ...         },
        ...     ],
        ... }
        >>> game = InstantGame(instant_game)
        >>> game
        <__main__.InstantGame object at 0x...>
        >>> game.name
        'Merry Multiplier'
        >>> game.is_active
        True
        >>> game.bets
        [<__main__.InstantBet object at 0x...>,
         <__main__.InstantBet object at 0x...>]

        """
        self.name = instant_game["name"]
        self.is_active = instant_game["is_active"]
        self.bets = []

        for bet in instant_game["bets"]:
            bet = InstantBet(bet)
            bet.is_available = self.is_active
            self.bets.append(bet)

    def __str__(self) -> str:
        """
        Return a string representation of the Instant game object which
        includes the name, if active, and the bets by overriding the
        __str__ method.

        >>> instant_game = {
        ...     "name": "Merry Multiplier",
        ...     "is_active": True,
        ...     "bets": [
        ...         {
        ...             "theoretical_payoff_rate": 0.8479,
        ...             "cost": [3]
        ...         },
        ...         {
        ...             "theoretical_payoff_rate": 0.85,
        ...             "cost": [1, 2, 4, 5]
        ...         },
        ...     ],
        ... }
        >>> game = InstantGame(instant_game)
        >>> print(game)
        Name: Merry Multiplier
        Active: True
        Bet 1
        Available: True
        Theoretical Payoff Rate: 0.8479
        Cost: [3]
        Bet 2
        Available: True
        Theoretical Payoff Rate: 0.85
        Cost: [1, 2, 4, 5]

        """
        line_1 = f"Name: {self.name}\n"
        line_2 = f"Active: {self.is_active}\n"
        line_3 = ""

        # Create a string from all bets
        for idx, bet in enumerate(self.bets, start=1):
            line_3 = line_3 + f"Bet {idx}\n{str(bet)}"

        return line_1 + line_2 + line_3 + "\n"


class LotteryBet:
    """ Create a lottery bet object from a dict """

    def __init__(self, lottery_bet: dict) -> None:
        """
        Initialize a lottery bet object from a dict

        >>> lottery_bet = {
        ...     "theoretical_payoff_rate": 0.4372,
        ...     "cost": [1, 2, 4, 5, 10, 20],
        ...     "daily_draw": False,
        ...     "draw_days": ["Monday", "Thursday"]
        ... }
        >>> bet = LotteryBet(lottery_bet)
        >>> bet
        <__main__.LotteryBet object at 0x...>
        >>> bet.is_available
        >>> bet.theoretical_payoff_rate
        0.4372
        >>> bet.cost
        [1, 2, 4, 5, 10, 20]
        >>> bet.daily_draw
        False
        >>> bet.draw_days
        ['Monday', 'Thursday']

        """
        self.is_available = None
        self.theoretical_payoff_rate = lottery_bet["theoretical_payoff_rate"]
        self.cost = lottery_bet["cost"]
        self.daily_draw = lottery_bet["daily_draw"]
        self.draw_days = lottery_bet["draw_days"]

    def __str__(self) -> str:
        """
        Return a string representation of the lottery bet object which includes
        if available, the theoretical payoff rate, cost, daily draw, and
        draw days by overriding the __str__ method.

        >>> lottery_bet = {
        ...     "theoretical_payoff_rate": 0.4372,
        ...     "cost": [1, 2, 4, 5, 10, 20],
        ...     "daily_draw": False,
        ...     "draw_days": ["Monday", "Thursday"]
        ... }
        >>> bet = LotteryBet(lottery_bet)
        >>> print(bet)
        Available: None
        Theoretical Payoff Rate: 0.4372
        Cost: [1, 2, 4, 5, 10, 20]
        Daily Draw: False
        Draw Days: ['Monday', 'Thursday']

        """
        line_1 = f"Available: {self.is_available}\n"
        line_2 = f"Theoretical Payoff Rate: {self.theoretical_payoff_rate}\n"
        line_3 = f"Cost: {self.cost}\n"
        line_4 = f"Daily Draw: {self.daily_draw}\n"
        line_5 = f"Draw Days: {self.draw_days}\n"

        return line_1 + line_2 + line_3 + line_4 + line_5


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
        ...             "draw_days": ["Monday", "Thursday"]
        ...         },
        ...         {
        ...             "theoretical_payoff_rate": 0.6622,
        ...             "cost": [5],
        ...             "daily_draw": True,
        ...             "draw_days": []
        ...         },
        ...     ],
        ... }
        >>> game = LotteryGame(lottery_game)
        >>> game
        <__main__.LotteryGame object at 0x...>
        >>> game.name
        'Lotto :D'
        >>> game.is_active
        True
        >>> game.bets
        [<__main__.LotteryBet object at 0x...>,
         <__main__.LotteryBet object at 0x...>]

        """
        self.name = lottery_game["name"]
        self.is_active = lottery_game["is_active"]
        self.bets = []

        today = datetime.now().strftime("%A")

        for bet in lottery_game["bets"]:
            bet = LotteryBet(bet)

            # Determine if lottery bet is available today
            if not self.is_active:
                bet.is_available = False
            elif bet.daily_draw:
                bet.is_available = True
            elif today in bet.draw_days:
                bet.is_available = True
            else:
                bet.is_available = False

            self.bets.append(bet)

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
        ...             "draw_days": ["Monday", "Thursday"]
        ...         },
        ...         {
        ...             "theoretical_payoff_rate": 0.6622,
        ...             "cost": [5],
        ...             "daily_draw": True,
        ...             "draw_days": []
        ...         },
        ...     ],
        ... }
        >>> game = LotteryGame(lottery_game)
        >>> print(game)
        Name: Lotto :D
        Active: True
        Bet 1
        Available: ...
        Theoretical Payoff Rate: 0.6259
        Cost: [2]
        Daily Draw: False
        Draw Days: ['Monday', 'Thursday']
        Bet 2
        Available: True
        Theoretical Payoff Rate: 0.6622
        Cost: [5]
        Daily Draw: True
        Draw Days: []

        """
        line_1 = f"Name: {self.name}\n"
        line_2 = f"Active: {self.is_active}\n"
        line_3 = ""

        # Create a string from all bets
        for idx, bet in enumerate(self.bets, start=1):
            line_3 = line_3 + f"Bet {idx}\n{str(bet)}"

        return line_1 + line_2 + line_3 + "\n"


def test():
    """ Test docstrings using doctest """

    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
