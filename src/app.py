"""
Application module

"""


def main():
    """
    Main function for the gamepicker application

    """
    from constants.menus import BUDGET, GAMES, SCHEDULE, SCHEDULE_SUB_MENU
    from interface import menu, menu_exit, menu_invalid
    from pool import GamePool
    from schedule import Schedule
    from utilities.data import read_json

    # START GAME PICKER
    print()

    # Print MAIN menu and return selection
    selection = menu()

    if selection == 1:  # GAMES

        # TODO selections\games.py

        # Read games from JSON files
        instants = read_json("../data/games/instants.json")["games"]
        lotteries = read_json("../data/games/lotteries.json")["games"]

        # Create and add game objects to a game pool object
        game_pool = GamePool()
        game_pool.add_games(instants, "Instant")
        game_pool.add_games(lotteries, "Lottery")

        # Print GAMES menu and return selection
        selection = menu(GAMES)

        if selection == 1:  # Print Games

            # Print all games and bets in the game pool
            print(game_pool)

            # Print all theoretical payoff rates
            theoretical_payoff_rates = game_pool.payoff_rates()
            print("PAYOFF RATES")
            print("------------")
            print()
            print(theoretical_payoff_rates)

            # Print a payoff rate based on randomness and weight from the set of
            # theoretical payoff rates from all bets
            payoff_rate = game_pool.payoff_rate()
            print()
            print(f"Payoff Rate: {payoff_rate} (randomly selected based on weight)")

        elif selection == 2:  # Print exit message
            menu_exit()

        else:  # Print invalid option message
            menu_invalid(selection)

    elif selection == 2:  # BUDGET

        # TODO selections\budget.py

        # Print BUDGET menu and return selection
        selection = menu(BUDGET)

        if selection == 1:  # Create budget

            # TODO Create budget
            print("Creating budget...")

        elif selection == 2:  # Print exit message
            menu_exit()

        else:  # Print invalid option message
            menu_invalid(selection)

    elif selection == 3:  # SCHEDULE

        # TODO selections\schedule.py

        # Print SCHEDULE menu and return selection
        selection = menu(SCHEDULE)

        if selection == 1:  # Create Schedule

            # Input start and end dates for schedule
            start_date = input("Start Date [2021-01-01]: ") or "2021-01-01"
            end_date = input("End Date   [2021-03-31]: ") or "2021-03-31"

            # Create a schedule
            schedule = Schedule(start_date, end_date)
            total_days = len(schedule.dates)

            print()
            print(f"Schedule created from {start_date} to {end_date}")
            print(f"Total Days: {total_days}")
            print()

            # Print SCHEDULE sub-menu and return selection
            sub_selection = menu(SCHEDULE_SUB_MENU)

            if sub_selection == 1:  # Print random dates as objects

                # Create and print a list of 30 random date objects
                random_dates = schedule.random_dates(30)
                print(random_dates)

            elif sub_selection == 2:  # Print random dates as strings

                # Create and print a list of 30 random date objects as strings
                random_dates = schedule.random_dates_to_str(30)
                for random_date in random_dates:
                    print(random_date)

            elif sub_selection == 3:  # Write random dates as strings to CSV file

                # Create and write a list of 30 random dates to a CSV file in the
                # datetime sub-folder of the data folder
                print("Writing random dates as strings to CSV file...")
                schedule.random_dates_to_csv(30)
                print("Done!")

            elif sub_selection == 4:  # Print exit message
                menu_exit()

            else:  # Print invalid option message
                menu_invalid(sub_selection)

        elif selection == 2:  # Print exit message
            menu_exit()

        else:  # Print invalid option message
            menu_invalid(selection)

    elif selection == 4:  # Print exit message
        menu_exit()

    else:  # Print invalid option message
        menu_invalid(selection)


if __name__ == "__main__":
    main()
