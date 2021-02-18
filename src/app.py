"""
Application module

"""


def main():
    """
    Main function for the gamepicker application

    """

    from constants.menus import SCHEDULE
    from schedule import Schedule
    from interface import menu
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

    # Start Game Picker
    # Print main menu and return selection
    menu_selection = menu()

    if menu_selection == 1:
        print("Create a Schedule")

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

        # Create and write a list of 30 random dates to a CSV file in the
        # datetime sub-folder of the data folder
        print()
        print("Writing to CSV file...")
        schedule.random_dates_to_csv(30)
        print("Done!")

    else:
        print(f"Option {menu_selection}")
        print("Goodbye!")


if __name__ == "__main__":
    main()
