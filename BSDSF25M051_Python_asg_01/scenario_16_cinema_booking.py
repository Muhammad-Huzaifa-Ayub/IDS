
# Scenario 16: Cinema Ticket Booking and Revenue Report

children = 0
adults = 0
seniors = 0
total_revenue = 0

while True:
    choice = input("Enter customer age or type 'done' to finish: ")

    if choice.lower() == "done":
        break

    age = int(choice)

    while age < 0:
        print("Age cannot be negative.")
        age = int(input("Enter customer age: "))

    if age < 12:
        category = "Child"
        price = 300
        children = children + 1
    elif age < 60:
        category = "Adult"
        price = 600
        adults = adults + 1
    else:
        category = "Senior"
        price = 400
        seniors = seniors + 1

    total_revenue = total_revenue + price

    print("Category:", category)
    print("Ticket Price: Rs.", price)

total_tickets = children + adults + seniors

print("\n----- Cinema Sales Report -----")
print("Child Tickets:", children)
print("Adult Tickets:", adults)
print("Senior Tickets:", seniors)
print("Total Tickets Sold:", total_tickets)
print("Total Revenue: Rs.", total_revenue)

if total_tickets > 0:
    average_price = total_revenue / total_tickets
    print("Average Ticket Price: Rs.", format(average_price, ".2f"))
else:
    print("Average Ticket Price: No tickets sold.")

print("--------------------------------")

