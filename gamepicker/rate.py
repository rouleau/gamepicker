""" Rate module """


def payoff_rates(games_available: list[dict]) -> list[float]:
    "Return a list of unique payoff rates from games available"
    rates = []

    for game in games_available:
        for bet in game["bets"]:
            rate = bet["theoretical_payoff_rate"]
            rates.append(rate)

    # ALL the unique payoff rates as a set
    rates = set(rates)

    # ALL the unique payoff rates sorted into a list
    rates = sorted(rates)

    return rates
