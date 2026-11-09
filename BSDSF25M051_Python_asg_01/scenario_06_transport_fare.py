
# Scenario 6: Public Transport Fare Estimator

name = input("Enter passenger name: ")

age = int(input("Enter passenger age: "))

while age < 0:
    print("Age cannot be negative.")
    age = int(input("Enter passenger age: "))

distance = float(input("Enter travel distance in km: "))

while distance <= 0:
    print("Travel distance must be greater than zero.")
    distance = float(input("Enter travel distance in km: "))

if distance <= 5:
    base_fare = 50
elif distance <= 15:
    base_fare = 100
elif distance <= 30:
    base_fare = 180
else:
    base_fare = 250

if age >= 60:
    discount = base_fare * 0.20
else:
    discount = 0

final_fare = base_fare - discount

print("\n----- Transport Fare Report -----")
print("Passenger Name:", name)
print("Passenger Age:", age)
print("Travel Distance:", distance, "km")
print("Base Fare: Rs.", format(base_fare, ".2f"))
print("Discount: Rs.", format(discount, ".2f"))
print("Final Fare: Rs.", format(final_fare, ".2f"))
print("---------------------------------")



