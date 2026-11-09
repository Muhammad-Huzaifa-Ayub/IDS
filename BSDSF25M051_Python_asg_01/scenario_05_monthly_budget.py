
# Scenario 5: Personal Monthly Budget Assistant

name = input("Enter student name: ")

allowance = float(input("Enter monthly allowance (Rs.): "))

while allowance < 0:
    print("Allowance cannot be negative.")
    allowance = float(input("Enter monthly allowance (Rs.): "))

food = float(input("Enter food expenses (Rs.): "))
transport = float(input("Enter transport expenses (Rs.): "))
internet = float(input("Enter internet expenses (Rs.): "))
books = float(input("Enter books expenses (Rs.): "))
other = float(input("Enter other personal expenses (Rs.): "))

while food < 0 or transport < 0 or internet < 0 or books < 0 or other < 0:
    print("Expenses cannot be negative. Please enter all expenses again.")
    food = float(input("Enter food expenses (Rs.): "))
    transport = float(input("Enter transport expenses (Rs.): "))
    internet = float(input("Enter internet expenses (Rs.): "))
    books = float(input("Enter books expenses (Rs.): "))
    other = float(input("Enter other personal expenses (Rs.): "))

total_expenses = food + transport + internet + books + other
balance = allowance - total_expenses

print("\n----- Monthly Budget Report -----")
print("Student Name:", name)
print("Monthly Allowance: Rs.", format(allowance, ".2f"))
print("Total Expenditure: Rs.", format(total_expenses, ".2f"))
print("Remaining Balance: Rs.", format(balance, ".2f"))

if total_expenses < allowance:
    print("Financial Position: Within Budget")
elif total_expenses == allowance:
    print("Financial Position: Budget Exhausted")
else:
    print("Financial Position: Overspending")

if allowance > 0:
    percentage = (total_expenses / allowance) * 100
    print("Percentage Spent:", format(percentage, ".2f"), "%")

    if percentage > 80:
        print("Warning: More than 80% of your allowance has been spent.")
else:
    print("Percentage Spent: Cannot be calculated because allowance is zero.")

print("---------------------------------")


