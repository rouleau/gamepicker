"""
Event module """

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
        Return a sorted list of a specified number of random dates
        from start date to end date (inclusive)

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


def test():
    """ Test docstrings using doctest """

    import doctest

    flags = doctest.ELLIPSIS | doctest.NORMALIZE_WHITESPACE
    doctest.testmod(verbose=True, optionflags=flags)


if __name__ == "__main__":
    test()
