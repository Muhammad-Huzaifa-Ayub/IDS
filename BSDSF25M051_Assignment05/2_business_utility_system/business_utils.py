"""Utility functions for the Smart Business Utility and Reporting System."""

import math
import random
from datetime import datetime


def calculate_total_and_average(sales):
    """Return the total and average of a list of sales figures."""
    if not sales:
        raise ValueError("At least one sales transaction is required.")

    total = sum(sales)
    average = total / len(sales)
    return total, average


def calculate_square_root(sales_value):
    """Return the square root of a non-negative sales value."""
    if sales_value < 0:
        raise ValueError("The square root requires a non-negative value.")

    return math.sqrt(sales_value)


def generate_transaction_id():
    """Generate a random transaction ID."""
    return f"TXN{random.randint(100000, 999999)}"


def get_current_datetime():
    """Return the current local date and time as a datetime object."""
    return datetime.now()
