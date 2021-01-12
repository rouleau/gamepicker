"""
Payoff rates """


def unique_payoff_rates(category_games: dict) -> list:
    """ Return a sorted list of unique payoff rates """

    rates = []

    for game in category_games["games"]:

        game_bets = game["bets"]

        for game_bet in game_bets:

            rate = game_bet["theoretical_payoff_rate"]
            rates.append(rate)

    payoff_rates = set(rates)

    return sorted(payoff_rates)
