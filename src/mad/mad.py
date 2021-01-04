"""
PROJECT: MAD

A program to spend $100 on Espacejeux from January 01, 2021 to March 31, 2021

"""

__version__ = "0.0.0"
__author__ = "Alain Rouleau"
__copyright__ = "Copyright © 2021 Alain Rouleau. All rights reserved."

from datetime import date
from schedule import create_dates, pick_dates

# Create a list of dates
start_date = "2021-01-04"
end_date = "2021-03-31"
list_of_dates = create_dates(start_date, end_date)

# Randomly pick 20-dates from the list of dates
random_dates = pick_dates(list_of_dates, 20)
random_dates.sort()

# Print list of dates
for num, item in enumerate(random_dates, start=1):
    print(num, item.isoformat(), item.strftime("%A, %B %d, %Y"))

# STEP 03: Generate .txt file of days and games
