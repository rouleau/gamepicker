"""
Event module """

import csv

from datetime import date, timedelta
from random import sample


class Schedule:
    """ Create a schedule object """

    def __init__(self, start_date: str, end_date: str) -> None:
        """
        Initialize the schedule object

        >>> schedule = Schedule("2021-01-01", "2021-03-31")
        >>> schedule
        <__main__.Schedule object at 0x...>
        >>> schedule.dates
        [datetime.date(2021, 1, 1), ..., datetime.date(2021, 3, 31)]

        """

        # Create date objects for first and last day
        first_day = date.fromisoformat(start_date)
        last_day = date.fromisoformat(end_date)

        # Calculate number of days from first to last day (inclusive)
        delta = last_day - first_day
        num_days = delta.days + 1

        # Create a list of dates
        dates = [first_day + timedelta(days=num) for num in range(num_days)]

        self.dates = dates

    def random_dates(self, num_dates: int = 2) -> list[date]:
        """
        Return a sorted list of randomly selected date objects from the dates
        in the schedule which includes the start and end date

        >>> schedule = Schedule("2021-01-01", "2021-03-31")
        >>> random_dates = schedule.random_dates(5)
        >>> random_dates
        [datetime.date(2021, 1, 1), ..., ..., ..., datetime.date(2021, 3, 31)]

        """

        dates = self.dates.copy()

        # Remove first & last day from list
        first_day = dates.pop(0)
        last_day = dates.pop()

        # Pick random dates from list with first & last day removed
        random_dates = sample(dates, k=num_dates - 2)

        # Add first & last day to list of random dates
        random_dates.append(first_day)
        random_dates.append(last_day)

        return sorted(random_dates)

    def random_dates_to_str(self, num_dates: int = 2) -> list[str]:
        """
        Return a sorted list of strings from randomly selected date objects
        from the dates in the schedule which includes the start and end date

        >>> schedule = Schedule("2021-02-15", "2021-04-30")
        >>> random_dates = schedule.random_dates_to_str(5)
        >>> random_dates
        ['2021-02-15 Monday, February 15, 2021', ..., ..., ...,
         '2021-04-30 Friday, April 30, 2021']

        """

        # Create a list of random date objects
        dates = self.random_dates(num_dates)

        # Create a list of strings from list of random date objects
        random_dates = []

        for date in dates:
            date = date.isoformat() + " " + date.strftime("%A, %B %d, %Y")
            random_dates.append(date)

        return random_dates

    def random_dates_to_csv(self, num_dates: int = 2):
        """
        Write a CSV file of sorted dates to the datetime sub-folder of the
        data folder from randomly selected date objects from the dates in the
        schedule which includes the start and end date

        >>> schedule = Schedule("2021-02-15", "2021-04-30")
        >>> schedule.random_dates_to_csv(30)  # doctest: +SKIP

        """

        # Create a list of random date objects
        dates = self.random_dates(num_dates)

        # Create a string for each date object, split the string, append the
        # returned list of strings to another list resulting in a list of lists
        random_dates = []

        for date in dates:
            date = date.isoformat() + ", " + date.strftime("%A, %B, %d, %Y")
            date = date.split(",")
            random_dates.append(date)

        # Create a CSV file, write a header, write the random dates
        filename = "../data/datetime/random_dates.csv"

        with open(filename, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["ISO 8601 Format", " Weekday", " Month", " Day", " Year"])

            for date in random_dates:
                writer.writerow(date)


def test():
    """ Test docstrings using doctest """

    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
