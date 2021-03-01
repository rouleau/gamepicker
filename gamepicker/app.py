""" Application module """


def main():
    """ Main function for the gamepicker application """

    import interface

    from constants.menus import MAIN
    from menu import Menu

    # Create MAIN menu
    main_menu = Menu(MAIN)

    # Print MAIN menu and get selection
    print()
    selection = main_menu.get_selection()

    # Menu functions
    if selection == 1:
        interface.show_game()

    elif selection == 2:
        interface.show_budget()

    elif selection == 3:
        interface.show_schedule()

    elif selection == 0:
        main_menu.print_message("exit")

    else:
        main_menu.print_message("invalid")


if __name__ == "__main__":
    main()
