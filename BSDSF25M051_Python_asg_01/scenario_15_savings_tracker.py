
# Scenario 15: Digital Savings Goal Tracker

name = input("Enter student name: ")

goal = float(input("Enter savings goal (Rs.): "))

while goal < 0:
    print("Savings goal cannot be negative.")
    goal = float(input("Enter savings goal (Rs.): "))

savings = float(input("Enter initial savings (Rs.): "))

while savings < 0:
    print("Savings cannot be negative.")
    savings = float(input("Enter initial savings (Rs.): "))

weeks = 0

while savings < goal:
    choice = input("Do you want to record savings for another week? (yes/no): ")

    if choice.lower() != "yes":
        break

    weekly_savings = float(input("Enter amount saved this week (Rs.): "))

    while weekly_savings < 0:
        print("Weekly savings cannot be negative.")
        weekly_savings = float(input("Enter amount saved this week (Rs.): "))

    savings = savings + weekly_savings
    weeks = weeks + 1

    remaining = goal - savings

    if remaining < 0:
        remaining = 0

    print("Total Savings: Rs.", format(savings, ".2f"))
    print("Amount Remaining: Rs.", format(remaining, ".2f"))

print("\n----- Savings Goal Report -----")
print("Student Name:", name)
print("Savings Goal: Rs.", format(goal, ".2f"))
print("Total Savings: Rs.", format(savings, ".2f"))
print("Weeks Recorded:", weeks)

if savings >= goal:
    print("Result: Savings goal achieved!")
else:
    print("Result: Savings goal not yet achieved.")

print("--------------------------------")


