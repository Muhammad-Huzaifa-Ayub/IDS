
# Scenario 2: Smart Electricity Bill Calculator

name = input("Enter consumer name: ")

units = float(input("Enter monthly electricity units consumed: "))

while units < 0:
    print("Invalid input! Units consumed cannot be negative.")
    units = float(input("Enter monthly electricity units consumed: "))

if units <= 100:
    bill = units * 10
elif units <= 200:
    bill = (100 * 10) + ((units - 100) * 15)
else:
    bill = (100 * 10) + (100 * 15) + ((units - 200) * 20)

print("\n----- Electricity Bill -----")
print("Consumer Name:", name)
print("Units Consumed:", units)
print("Total Bill: Rs.", format(bill, ".2f"))
print("----------------------------")

