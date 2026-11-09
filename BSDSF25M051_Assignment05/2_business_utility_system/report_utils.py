"""Calendar and report helper functions."""

import calendar


def generate_monthly_calendar(year, month):
    """Return a text calendar for the supplied year and month."""
    if month < 1 or month > 12:
        raise ValueError("Month must be between 1 and 12.")

    return calendar.month(year, month)
