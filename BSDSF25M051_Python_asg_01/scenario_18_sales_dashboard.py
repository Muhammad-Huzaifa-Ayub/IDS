
# Scenario 18: Simple Sales Performance Dashboard

employees = int(input("Enter number of employees: "))

while employees < 0:
    print("Number of employees cannot be negative.")
    employees = int(input("Enter number of employees: "))

total_sales = 0
target_count = 0
highest_sales = 0
highest_employee = ""
highest_tied = False

if employees == 0:
    print("No employees to include in the report.")
else:
    for i in range(1, employees + 1):
        name = input("Enter employee " + str(i) + " name: ")
        sales = float(input("Enter sales amount for " + name + " (Rs.): "))

        while sales < 0:
            print("Sales cannot be negative.")
            sales = float(input("Enter sales amount for " + name + " (Rs.): "))

        total_sales = total_sales + sales

        print("Employee:", name, "| Sales: Rs.", format(sales, ".2f"))

        if sales >= 10000:
            target_count = target_count + 1

        if i == 1:
            highest_sales = sales
            highest_employee = name
            highest_tied = False
        elif sales > highest_sales:
            highest_sales = sales
            highest_employee = name
            highest_tied = False
        elif sales == highest_sales:
            highest_tied = True

    average_sales = total_sales / employees

    print("\n----- Sales Performance Report -----")
    print("Total Shop Sales: Rs.", format(total_sales, ".2f"))
    print("Average Sales per Employee: Rs.", format(average_sales, ".2f"))
    print("Employees Meeting Rs. 10,000 Target:", target_count)

    if highest_tied:
        print("Highest Sales: Rs.", format(highest_sales, ".2f"))
        print("Result: Highest sales are tied between two or more employees.")
    else:
        print("Highest-Performing Employee:", highest_employee)
        print("Highest Sales: Rs.", format(highest_sales, ".2f"))

    print("------------------------------------")


