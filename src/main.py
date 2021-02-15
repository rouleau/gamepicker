"""
Main module for application """


def app():
    from event import Schedule
    from pool import GamePool
    from utilities.data import read_json

    # Read games from JSON files
    instants = read_json("../data/games/instants.json")["games"]
    lotteries = read_json("../data/games/lotteries.json")["games"]

    # Create and add game objects to a game pool object
    game_pool = GamePool()
    game_pool.add_games(instants, "Instant")
    game_pool.add_games(lotteries, "Lottery")

    # Print all games and bets in the game pool
    print(game_pool)

    # Print all theoretical payoff rates
    theoretical_payoff_rates = game_pool.payoff_rates()
    print(theoretical_payoff_rates)

    # Print a payoff rate based on randomness and weight from the set of
    # theoretical payoff rates from all bets
    payoff_rate = game_pool.payoff_rate()
    print(f"Payoff Rate: {payoff_rate}")

    # Create a schedule
    schedule = Schedule("2021-02-15", "2021-04-30")
    print()
    print(schedule.dates)

    # Create and print a list of 30 random date objects
    random_dates = schedule.random_dates(30)
    print()
    print(random_dates)

    # Create and print a list of 30 random date objects as strings
    random_dates = schedule.random_dates_to_str(30)
    print()
    for random_date in random_dates:
        print(random_date)

    # Start Game Picker
    print("\nWelcome to the Espacejeux Game Picker!\n")


if __name__ == "__main__":
    app()
