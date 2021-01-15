"""
Game Picker module """


def picks():
    """
    Display a list of bets to purchase

    >>> picks()
    These are your picks:
    * Buy ... for $...
    <BLANKLINE>
    Good Luck!
    """
    bets = [("Astro", "$1.00"), ("Lotto Max", "$5.00")]

    print("These are your picks:")

    for bet in bets:
        print(f"* Buy a {bet[0]} for {bet[1]}")

    print()
    print("Good Luck!")


def main():
    """
    Main function
    """
    import doctest

    doctest.testmod(verbose=True, optionflags=doctest.ELLIPSIS)


if __name__ == "__main__":
    main()
