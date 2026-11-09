
# Scenario 4: Student Cafeteria Order and Billing System

grand_total = 0

name = input("Enter customer name: ")

while True:
    print("\n----- Cafeteria Menu -----")
    print("1. Sandwich - Rs. 250")
    print("2. Burger - Rs. 400")
    print("3. Pizza slice - Rs. 300")
    print("4. Juice - Rs. 120")

    choice = input("Select an item (1-4): ")

    if choice == "1":
        item = "Sandwich"
        price = 250
    elif choice == "2":
        item = "Burger"
        price = 400
    elif choice == "3":
        item = "Pizza slice"
        price = 300
    elif choice == "4":
        item = "Juice"
        price = 120
    else:
        print("Invalid menu selection.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

    subtotal = price * quantity

    if subtotal >= 1000:
        discount = subtotal * 0.10
    else:
        discount = 0

    final_bill = subtotal - discount
    grand_total = grand_total + final_bill

    print("\n----- Order Receipt -----")
    print("Customer Name:", name)
    print("Item:", item)
    print("Price per item: Rs.", price)
    print("Quantity:", quantity)
    print("Subtotal: Rs.", format(subtotal, ".2f"))
    print("Discount: Rs.", format(discount, ".2f"))
    print("Final Bill: Rs.", format(final_bill, ".2f"))
    print("-------------------------")

    again = input("Would you like to place another order? (yes/no): ")

    if again.lower() != "yes":
        break

print("\n===== Final Billing Summary =====")
print("Customer Name:", name)
print("Total of all orders: Rs.", format(grand_total, ".2f"))
print("Thank you for visiting our cafeteria!")

