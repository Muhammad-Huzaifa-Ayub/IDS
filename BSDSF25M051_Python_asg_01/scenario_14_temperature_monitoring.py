
# Scenario 14: Daily Temperature Monitoring

days = int(input("Enter number of monitoring days: "))

while days <= 0:
    print("Number of days must be greater than zero.")
    days = int(input("Enter number of monitoring days: "))

total_temperature = 0
above_35 = 0
below_10 = 0
normal_range = 0

for day in range(1, days + 1):
    temperature = float(input("Enter temperature for day " + str(day) + ": "))

    total_temperature = total_temperature + temperature

    if day == 1:
        highest = temperature
        lowest = temperature
    else:
        if temperature > highest:
            highest = temperature
        if temperature < lowest:
            lowest = temperature

    if temperature > 35:
        above_35 = above_35 + 1
    elif temperature < 10:
        below_10 = below_10 + 1
    else:
        normal_range = normal_range + 1

average = total_temperature / days

print("\n----- Temperature Report -----")
print("Monitoring Days:", days)
print("Average Temperature:", format(average, ".2f"), "C")
print("Highest Temperature:", highest, "C")
print("Lowest Temperature:", lowest, "C")
print("Days Above 35 C:", above_35)
print("Days Below 10 C:", below_10)
print("Days Between 10 C and 35 C:", normal_range)
print("------------------------------")

