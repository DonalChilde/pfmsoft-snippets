####################################################
#                                                  #
#    src/pfmsoft/snippets/datetime/date_range.py
#                                                  #
####################################################
# Created by: Chad Lowe                            #
# Created on: 2025-07-04T04:20:56-07:00            #
# Last Modified: 2025-07-04T04:22:03-07:00         #
# Source: https://github.com/DonalChilde/pfmsoft_snippets  #
####################################################

from datetime import date, timedelta
from typing import Iterator

# TODO tests


def date_range(start_date: date, end_date: date, period: int = 1) -> Iterator[date]:
    """
    Generate a range of dates from start_date to end_date, inclusive.

    Args:
        start_date (date): The starting date.
        end_date (date): The ending date.
        period (int): The number of days between each date in the range. Default 1.


    Yields:
        date: Each date in the range from start_date to end_date.
    """
    if period <= 0:
        raise ValueError(
            f"period arg was passed {period}. Period cannot be less than or equal to zero."
        )
    if end_date >= start_date:
        current_date = start_date
        while current_date <= end_date:
            yield current_date
            current_date += timedelta(days=period)
    else:
        current_date = start_date
        while current_date >= end_date:
            yield current_date
            current_date -= timedelta(days=period)


def date_range_days(start_date: date, days: int) -> Iterator[date]:
    """
    Generate a range of dates starting from start_date for a specified number of days, inclusive.

    Args:
        start_date (date): The starting date.
        days (int): The number of days to generate. Use a negative value to generate dates in reverse order.

    Yields:
        date: Each date in the range starting from start_date for the specified number of days.
    """
    if days < 0:
        days = days + 1
        day_range = range(0, days, -1)
    elif days > 0:
        days = days - 1
        day_range = range(0, days)
    else:
        return start_date
    for i in day_range:
        yield start_date + timedelta(days=i)
