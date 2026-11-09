
import os
import datetime
import calendar
import threading
from functools import reduce


# A. Store employee information in a dictionary

employees = {
    "E101": {
        "name": "Ali",
        "department": "IT",
        "attendance": {}
    },

    "E102": {
        "name": "Ahmed",
        "department": "HR",
        "attendance": {}
    },

    "E103": {
        "name": "Usman",
        "department": "Finance",
        "attendance": {}
    }
}


# B. Get current month and working days

current_date = datetime.datetime.now()

current_year = current_date.year
current_month = current_date.month

month_name = calendar.month_name[current_month]

number_of_days = calendar.monthrange(
    current_year, current_month
)[1]

working_days = []

for day in range(1, number_of_days + 1):

    date = datetime.date(current_year, current_month, day)

    # Monday to Friday are working days

    if date.weekday() < 5:
        working_days.append(date)


print("\nCurrent Month:", month_name)
print("Number of Days:", number_of_days)

print("\nWorking Days:")

for date in working_days:
    print(date)


# Add sample attendance records

sample_attendance = {
    "E101": [8, 8, 7, 8, 8],
    "E102": [6, 5, 6, 5, 6],
    "E103": [4, 5, 5, 4, 5]
}

for employee_id in employees:

    for date, hours in zip(working_days[:5],
                           sample_attendance[employee_id]):

        employees[employee_id]["attendance"][str(date)] = hours


# H. Save attendance records in a text file

file_name = "attendance_payroll.txt"

try:

    with open(file_name, "w") as file:

        file.write("MONTHLY EMPLOYEE ATTENDANCE RECORDS\n\n")

        for employee_id, employee in employees.items():

            for date, hours in employee["attendance"].items():

                file.write(
                    f"{employee_id}, {employee['name']}, "
                    f"{date}, {hours} hours\n"
                )

except OSError as e:
    print("File error:", e)


# Add new attendance records

while True:

    answer = input("\nDo you want to add attendance? (y/n): ").lower()

    if answer == "n":
        break

    elif answer == "y":

        try:
            employee_id = input("Enter Employee ID: ")

            # J. Check missing employee ID

            if employee_id not in employees:
                raise KeyError("Employee ID not found!")

            date = input("Enter date (YYYY-MM-DD): ")

            attendance_date = datetime.datetime.strptime(
                date, "%Y-%m-%d"
            ).date()

            # Check current month and working day

            if (attendance_date.year != current_year or
                attendance_date.month != current_month):
                raise ValueError("Date must be in the current month!")

            if attendance_date.weekday() >= 5:
                raise ValueError("Date is not a working day!")

            if date in employees[employee_id]["attendance"]:
                raise ValueError("Attendance already exists for this date!")

            hours = float(input("Enter working hours: "))

            if hours < 0 or hours > 24:
                raise ValueError("Invalid working hours!")

            # Append new attendance record to file

            with open(file_name, "a") as file:

                file.write(
                    f"{employee_id}, "
                    f"{employees[employee_id]['name']}, "
                    f"{date}, {hours} hours\n"
                )

            employees[employee_id]["attendance"][date] = hours

            print("Attendance record added successfully!")

        except KeyError as e:
            print("Error:", e)

        except ValueError as e:
            print("Error:", e)

        except OSError as e:
            print("File error:", e)

    else:
        print("Please enter y or n!")


# C. Function to calculate total and average working hours

def calculate_working_hours(employee_id, *daily_hours):

    if employee_id not in employees:
        raise KeyError("Employee ID not found!")

    for hours in daily_hours:

        if hours < 0 or hours > 24:
            raise ValueError("Invalid attendance record!")

    total_hours = sum(daily_hours)

    if len(daily_hours) > 0:
        average_hours = total_hours / len(daily_hours)
    else:
        average_hours = 0

    return total_hours, average_hours


# Thread 1: Calculate employee working hours

working_hour_results = {}


def calculate_all_hours():

    print("\n===== THREAD 1: WORKING HOURS =====")

    for employee_id, employee in employees.items():

        try:
            daily_hours = list(employee["attendance"].values())

            total, average = calculate_working_hours(
                employee_id, *daily_hours
            )

            working_hour_results[employee_id] = {
                "total": total,
                "average": average
            }

            print("\nEmployee:", employee["name"])
            print("Total Working Hours:", total)
            print("Average Working Hours:", round(average, 2))

        except (KeyError, ValueError) as e:
            print("Error:", e)


# Thread 2: Generate employee payroll report

def generate_payroll_report():

    print("\n===== THREAD 2: PAYROLL REPORT =====")

    hourly_rate = 500

    employee_names = []
    total_hours_list = []

    employee_salaries = {}

    for employee_id, employee in employees.items():

        daily_hours = list(employee["attendance"].values())

        # D. Calculate daily salary using map() and lambda

        daily_salaries = list(
            map(lambda hours: hours * hourly_rate, daily_hours)
        )

        total_salary = sum(daily_salaries)

        employee_salaries[employee_id] = total_salary

        employee_names.append(employee["name"])

        total_hours_list.append(
            working_hour_results[employee_id]["total"]
        )

        print("\nEmployee ID:", employee_id)
        print("Employee Name:", employee["name"])
        print("Department:", employee["department"])
        print("Daily Salaries:", daily_salaries)
        print("Monthly Salary: Rs.", total_salary)

    # E. Find employees with average working hours below 6

    low_attendance = list(
        filter(
            lambda employee_id:
            working_hour_results[employee_id]["average"] < 6,
            employees
        )
    )

    print("\nEmployees with average working hours below 6:")

    for employee_id in low_attendance:
        print(
            employee_id,
            employees[employee_id]["name"]
        )

    # F. Combine employee names and total working hours using zip()

    employee_hours = dict(
        zip(employee_names, total_hours_list)
    )

    print("\nEmployee Total Working Hours:")

    for name, hours in employee_hours.items():
        print(name, ":", hours)

    # G. Calculate total salary expenditure using reduce()

    total_expenditure = reduce(
        lambda total, salary: total + salary,
        employee_salaries.values(),
        0
    )

    print("\nTotal Company Salary Expenditure: Rs.", total_expenditure)

    # H. Append payroll report to text file

    try:

        with open(file_name, "a") as file:

            file.write("\n\nMONTHLY PAYROLL REPORT\n")

            for employee_id, employee in employees.items():

                file.write(
                    f"{employee_id}, "
                    f"{employee['name']}, "
                    f"{employee['department']}, "
                    f"Total Hours: "
                    f"{working_hour_results[employee_id]['total']}, "
                    f"Salary: Rs. {employee_salaries[employee_id]}\n"
                )

            file.write(
                f"\nTotal Salary Expenditure: Rs. {total_expenditure}\n"
            )

        print("\nPayroll report saved successfully!")

    except OSError as e:
        print("File error:", e)


# I. Create two separate threads

thread1 = threading.Thread(target=calculate_all_hours)

thread2 = threading.Thread(target=generate_payroll_report)

thread1.start()
thread1.join()

thread2.start()
thread2.join()


# H. Read existing attendance and payroll records

print("\n===== MONTHLY ATTENDANCE AND PAYROLL FILE =====")

try:

    with open(file_name, "r") as file:

        records = file.read()

        print(records)

except FileNotFoundError:
    print("Attendance file not found!")

except OSError as e:
    print("File reading error:", e)


print("\nMonthly attendance and payroll report completed!")
