"""
Date creation module

"""

from datetime import date, timedelta
from random import sample


def create_dates(start_date="2021-01-01", end_date="2021-03-31"):
    """
    Create a list of date objects
    """
    # Create date objects for first and last day
    first_day = date.fromisoformat(start_date)
    last_day = date.fromisoformat(end_date)

    # Calculate number of days from first to last day (inclusive)
    delta = last_day - first_day
    num_days = delta.days + 1

    # Create list of dates
    dates = []
    for num in range(num_days):
        dates.append(first_day + timedelta(days=num))

    return dates


def pick_dates(dates: list, num_dates: int):
    """
    Create a random list of date objects from first to last day (inclusive)
    """
    # Remove first & last day from list
    first_day = dates.pop(0)
    last_day = dates.pop()

    # Pick random dates from list with first & last day removed
    picked_dates = sample(dates, k=num_dates - 2)
    
    # Add first and last day to final list
    picked_dates.append(first_day)
    picked_dates.append(last_day)

    return picked_dates
