"""
Menu module

"""


class Menu:
    """ Create a menu object """

    def __init__(self, menu: dict) -> None:
        """
        Initialize the menu object

        >>> MAIN = {
        ...     "header": "Welcome to the Espacejeux Game Picker!",
        ...     1: "Games",
        ...     2: "Budget",
        ...     3: "Schedule",
        ...     4: "Exit",
        ... }
        >>> main_menu = Menu(MAIN)
        >>> main_menu
        <__main__.Menu object at 0x...>
        >>> main_menu.header
        'Welcome to the Espacejeux Game Picker!'
        >>> main_menu.selections
        {1: 'Games', 2: 'Budget', 3: 'Schedule', 4: 'Exit'}

        """
        self.header: str = menu.pop("header")
        self.selections: dict = menu

    def __str__(self) -> str:
        """
        Return a string representation of the menu object which includes the
        header and selections by overriding the __str__ method.

        >>> MAIN = {
        ...     "header": "Welcome to the Espacejeux Game Picker!",
        ...     1: "Games",
        ...     2: "Budget",
        ...     3: "Schedule",
        ...     4: "Exit",
        ... }
        >>> main_menu = Menu(MAIN)
        >>> print(main_menu)
        Welcome to the Espacejeux Game Picker!
        <BLANKLINE>
        [1] Games
        [2] Budget
        [3] Schedule
        [4] Exit
        <BLANKLINE>

        """
        # Create a header string
        header = self.header + "\n\n"

        # Create a selections string
        selections = ""

        for key, value in self.selections.items():
            selections = selections + f"[{key}] {value}\n"

        return header + selections


def test():
    """ Test docstrings using doctest """

    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
