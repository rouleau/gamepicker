"""
Menu module

"""


class Menu:
    """ Create a menu object """

    def __init__(self, menu: dict) -> None:
        """
        Initialize the menu object

        >>> MAIN = {
        ...     "header": "Welcome to Game Picker!",
        ...     1: "Games",
        ...     2: "Budget",
        ...     3: "Schedule",
        ... }
        >>> main_menu = Menu(MAIN)
        >>> main_menu
        <__main__.Menu object at 0x...>
        >>> main_menu.header
        'Welcome to Game Picker!'
        >>> main_menu.selections
        {1: 'Games', 2: 'Budget', 3: 'Schedule', 0: 'Exit'}
        >>> main_menu.messages
        {'exit': 'Goodbye!', 'invalid': 'Selection is invalid... Goodbye!'}

        """
        # Add exit to end of menu
        menu[0] = "Exit"

        self.header: str = menu.pop("header")
        self.selections: dict = menu
        self.messages: dict = {
            "exit": "Goodbye!",
            "invalid": "Selection is invalid... Goodbye!",
        }

    def __str__(self) -> str:
        """
        Return a string representation of the menu object which includes the
        header and selections by overriding the __str__ method.

        >>> MAIN = {
        ...     "header": "Welcome to Game Picker!",
        ...     1: "Games",
        ...     2: "Budget",
        ...     3: "Schedule",
        ... }
        >>> main_menu = Menu(MAIN)
        >>> print(main_menu)
        Welcome to Game Picker!
        <BLANKLINE>
        [1] Games
        [2] Budget
        [3] Schedule
        [0] Exit
        <BLANKLINE>

        """
        # Create string for header
        header = self.header + "\n\n"

        # Create string for selections
        selections = ""
        for key, value in self.selections.items():
            selections = selections + f"[{key}] {value}\n"

        return header + selections

    def get_selection(self) -> int:
        """
        Print menu and return selection

        >>> MAIN = {
        ...     "header": "Welcome to Game Picker!",
        ...     1: "Games",
        ...     2: "Budget",
        ...     3: "Schedule",
        ... }
        >>> main_menu = Menu(MAIN)
        >>> selection = main_menu.get_selection()  # doctest: +SKIP
        Welcome to Game Picker!

        [1] Games
        [2] Budget
        [3] Schedule
        [0] Exit

        > 3

        >>> selection  # doctest: +SKIP
        3

        """
        print(self)
        selection = input("> ")
        print()

        return int(selection)


def test():
    """ Test docstrings using doctest """

    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
