
# Scenario 13: Restaurant Table Reservation and Seating Plan

rows = int(input("Enter number of rows: "))

while rows < 0:
    print("Rows cannot be negative.")
    rows = int(input("Enter number of rows: "))

seats_per_row = int(input("Enter seats per row: "))

while seats_per_row < 0:
    print("Seats per row cannot be negative.")
    seats_per_row = int(input("Enter seats per row: "))

capacity = rows * seats_per_row

print("\n----- Restaurant Seating Plan -----")

seat_number = 1

for r in range(rows):
    for s in range(seats_per_row):
        print(seat_number, end=" ")
        seat_number = seat_number + 1
    print()

print("Total Seating Capacity:", capacity)

customers = int(input("Enter number of customers who arrived: "))

while customers < 0 or customers > capacity:
    print("Customer count must be between 0 and", capacity)
    customers = int(input("Enter number of customers who arrived: "))

unoccupied = capacity - customers

print("Customers Arrived:", customers)
print("Unoccupied Seats:", unoccupied)
print("------------------------------------")

