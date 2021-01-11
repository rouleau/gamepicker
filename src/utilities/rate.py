"""
Helper functions for payoff rates """


def unique_rates(punts: dict) -> list:
    """ Return a sorted list of unique payoff rates """

    payoff_rates = []

    for game in punts["games"]:

        game_bets = game["bets"]

        for game_bet in game_bets:

            payoff_rate = game_bet["theoretical_payoff_rate"]
            payoff_rates.append(payoff_rate)

    unique_payoff_rates = set(payoff_rates)

    return sorted(unique_payoff_rates)
