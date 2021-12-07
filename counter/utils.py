"""
Util functions to work with a date
"""
import datetime


def calculate_weeks(
    current_datetime: datetime.datetime, start_datetime=datetime.datetime(2018, 12, 23)
) -> int:
    """
    The main business logical function. Calculates a number of week from a given
    date. Takes second additional arg "start_datetime", is not required, sets
    the start point to calculate (one week before the first week)
    """
    # Convert to the seconds from Unix epoch
    start_point = start_datetime.timestamp()
    x_point = current_datetime.timestamp()
    # Find the difference in seconds between given date and start date
    delta = x_point - start_point
    # Find the number of weeks. Delta in sec divided by 60*60*24 and divide
    # floorly a result by 7 days in a week
    week = (delta / 86400) // 7
    # To reduce '.00' convert decimal to integer
    return int(week)


def convert_date_string(date_string):
    """
    Converts date string into datetime.datetime.
    Format of the string: four_chars_year, two_or_one_chars_month and
    two_or_one_chars_day dash separated
    """
    return datetime.datetime.strptime(date_string, "%Y-%m-%d")
