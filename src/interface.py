"""
Interface module

"""
from constants.menus import MAIN


def menu(menu_to_print: dict = MAIN) -> int:
    """
    Print the menu and return the selection

    >>> MAIN = {
    ...     "header": "Welcome to Game Picker!",
    ...     1: "Create a schedule",
    ...     2: "Create a budget",
    ...     3: "Pick games",
    ... }
    >>> menu_selection = menu(MAIN)  # doctest: +SKIP
    Welcome to Game Picker!
    -----------------------

    [1] Create a schedule
    [2] Create a budget
    [3] Pick games

    > 2

    >>> menu_selection  # doctest: +SKIP
    2

    """
    header = menu_to_print.pop("header")

    print(header)

    if menu_to_print != MAIN:
        print("-" * len(header))

    print()

    for key, value in menu_to_print.items():
        print(f"[{key}] {value}")

    selection = input("\n> ")

    print()

    return int(selection)


def menu_exit() -> None:
    """
    Print exit message for menus

    >>> menu_exit()
    Goodbye!

    """
    print("Goodbye!")


def menu_invalid(selection: int) -> None:
    """
    Print invalid message for menus

    >>> selection = 3
    >>> menu_invalid(selection)
    Option 3 is Invalid... Goodbye!

    """
    print(f"Option {selection} is Invalid... Goodbye!")


def test():
    """ Test docstrings using doctest """

    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
