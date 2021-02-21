""" Interface module """

from constants.menus import BUDGET, GAME, SCHEDULE, SCHEDULE_SUB_MENU
from gamepool import GamePool
from menu import Menu
from schedule import Schedule
from utilities.data import read_json

# Create menus
budget_menu = Menu(BUDGET)
game_menu = Menu(GAME)
schedule_menu = Menu(SCHEDULE)
schedule_sub_menu = Menu(SCHEDULE_SUB_MENU)


def show_game() -> None:
    """
    Game function

    """
    # Read games from JSON files
    instants = read_json("../data/games/instants.json")["games"]
    lotteries = read_json("../data/games/lotteries.json")["games"]

    # Create and add game objects to a game pool object
    game_pool = GamePool()
    game_pool.add_games(instants, "Instant")
    game_pool.add_games(lotteries, "Lottery")

    # Print GAME menu and get selection
    selection = game_menu.get_selection()

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

    elif selection == 0:  # Print exit message
        game_menu.print_message("exit")

    else:  # Print invalid selection message
        game_menu.print_message("invalid")


def show_budget() -> None:
    """
    Budget function

    """
    # Print BUDGET menu and get selection
    selection = budget_menu.get_selection()

    if selection == 1:  # Create budget

        # TODO Create budget
        print("Creating budget...")

    elif selection == 0:  # Print exit message
        budget_menu.print_message("exit")

    else:  # Print invalid selection message
        budget_menu.print_message("invalid")


def show_schedule() -> None:
    """
    Schedule function

    """
    # Print SCHEDULE menu and get selection
    selection = schedule_menu.get_selection()

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

        # Print SCHEDULE sub-menu and get selection
        selection = schedule_sub_menu.get_selection()

        if selection == 1:  # Print random dates as objects

            # Create and print a list of 30 random date objects
            random_dates = schedule.random_dates(30)
            print(random_dates)

        elif selection == 2:  # Print random dates as strings

            # Create and print a list of 30 random date objects as strings
            random_dates = schedule.random_dates_to_str(30)
            for random_date in random_dates:
                print(random_date)

        elif selection == 3:  # Write random dates as strings to CSV file

            # Create and write a list of 30 random dates to a CSV file in the
            # datetime sub-folder of the data folder
            print("Writing random dates as strings to CSV file...")
            schedule.random_dates_to_csv(30)
            print("Done!")

        elif selection == 0:  # Print exit message
            schedule_sub_menu.print_message("exit")

        else:  # Print invalid selection message
            schedule_sub_menu.print_message("invalid")

    elif selection == 0:  # Print exit message
        schedule_menu.print_message("exit")

    else:  # Print invalid selection message
        schedule_menu.print_message("invalid")
