"""Main program for the Smart Business Utility and Reporting System."""

import importlib
import sys
import time
from functools import reduce

# C and H: Import the user-defined modules and handle import errors.
try:
    import business_utils
    import report_utils
except ImportError as error:
    print("Module import error:", error)
    print("Make sure business_utils.py and report_utils.py are in this folder.")
    raise SystemExit(1)

# I: Demonstrate reloading modules after they have been imported.
# This is useful during development after editing a module.
business_utils = importlib.reload(business_utils)
report_utils = importlib.reload(report_utils)


def read_integer(prompt, minimum):
    """Read an integer and keep asking until it meets the minimum."""
    while True:
        try:
            value = int(input(prompt))
            if value < minimum:
                raise ValueError(f"Enter a number greater than or equal to {minimum}.")
            return value
        except ValueError as error:
            print("Invalid input:", error)


def read_sales_amount(prompt):
    """Read a non-negative numeric sales amount."""
    while True:
        try:
            amount = float(input(prompt))
            if amount < 0:
                raise ValueError("Sales cannot be negative.")
            return amount
        except ValueError as error:
            print("Invalid sales amount:", error)


def main():
    # I: Show where Python searches for imported modules and where it found ours.
    print("\nPython module search locations (sys.path):")
    for location in sys.path:
        print(location if location else "(current working directory)")

    print("\nbusiness_utils loaded from:", business_utils.__file__)
    print("report_utils loaded from:", report_utils.__file__)

    print("\n===== SMART BUSINESS UTILITY AND REPORTING SYSTEM =====")

    transaction_count = read_integer("Enter number of daily sales transactions: ", 1)

    sales = []
    for index in range(transaction_count):
        amount = read_sales_amount(f"Enter sales amount for transaction {index + 1} (Rs.): ")
        sales.append(amount)

    # Start measuring the report preparation time (not the time spent entering data).
    report_start = time.perf_counter()

    # A: Use the function from business_utils.py to calculate total and average.
    function_total, average_sales = business_utils.calculate_total_and_average(sales)

    # D: Use map() and lambda to calculate 5% sales tax for every transaction.
    sales_tax = list(map(lambda amount: round(amount * 0.05, 2), sales))

    # E: Use filter() to select transactions strictly greater than Rs. 10,000.
    high_value_sales = list(filter(lambda amount: amount > 10000, sales))

    # E: Use reduce() to calculate the total sales amount.
    total_sales = reduce(lambda running_total, amount: running_total + amount, sales, 0.0)

    # A: Calculate the square root of the total sales using math (inside business_utils).
    square_root_of_sales = business_utils.calculate_square_root(total_sales)

    # A: Display current date and time using datetime (inside business_utils).
    current_datetime = business_utils.get_current_datetime()

    # B: Generate the calendar for the current month using report_utils.py.
    monthly_calendar = report_utils.generate_monthly_calendar(
        current_datetime.year, current_datetime.month
    )

    # A and F: Generate unique random transaction IDs and combine them with sales.
    transaction_ids = []
    used_ids = set()
    for _ in sales:
        transaction_id = business_utils.generate_transaction_id()
        while transaction_id in used_ids:
            transaction_id = business_utils.generate_transaction_id()
        transaction_ids.append(transaction_id)
        used_ids.add(transaction_id)

    transaction_dictionary = dict(zip(transaction_ids, sales))

    # Calculate report preparation time.
    elapsed_seconds = time.perf_counter() - report_start

    # Build the monthly report as a string.
    report_lines = [
        "=" * 58,
        "             SMART BUSINESS MONTHLY REPORT",
        "=" * 58,
        f"Report generated: {current_datetime.strftime('%Y-%m-%d %H:%M:%S')}",
        "",
        "MONTHLY CALENDAR",
        monthly_calendar,
        "TRANSACTION DETAILS",
        "-" * 58,
        f"{'Transaction ID':<18}{'Sales (Rs.)':>18}{'5% Tax (Rs.)':>18}",
        "-" * 58,
    ]

    for transaction_id, amount, tax in zip(transaction_ids, sales, sales_tax):
        report_lines.append(f"{transaction_id:<18}{amount:>18,.2f}{tax:>18,.2f}")

    report_lines.extend([
        "-" * 58,
        "TRANSACTION ID DICTIONARY (ID: SALES AMOUNT)",
    ])

    for transaction_id, amount in transaction_dictionary.items():
        report_lines.append(f"{transaction_id}: Rs. {amount:,.2f}")

    report_lines.extend([
        "",
        "SALES SUMMARY",
        f"Total sales (using reduce): Rs. {total_sales:,.2f}",
        f"Total sales (using business_utils function): Rs. {function_total:,.2f}",
        f"Average sales per transaction: Rs. {average_sales:,.2f}",
        f"Square root of total sales: {square_root_of_sales:,.2f}",
        f"Total 5% sales tax: Rs. {sum(sales_tax):,.2f}",
        "",
        "TRANSACTIONS GREATER THAN RS. 10,000",
    ])

    if high_value_sales:
        for amount in high_value_sales:
            report_lines.append(f"Rs. {amount:,.2f}")
    else:
        report_lines.append("No transactions greater than Rs. 10,000.")

    report_lines.extend([
        "",
        f"Report preparation time: {elapsed_seconds:.6f} seconds",
        "=" * 58,
    ])

    report = "\n".join(report_lines)

    # H: Display the report.
    print("\n" + report)

    # H: Save the report; the with statement closes the file automatically.
    try:
        with open("monthly_business_report.txt", "w", encoding="utf-8") as report_file:
            report_file.write(report)
    except OSError as error:
        print("File operation error:", error)
    else:
        print("\nReport successfully saved to monthly_business_report.txt")

    # G: Display elapsed report preparation time using the time module.
    print(f"Time taken to generate the report: {elapsed_seconds:.6f} seconds")


if __name__ == "__main__":
    main()
