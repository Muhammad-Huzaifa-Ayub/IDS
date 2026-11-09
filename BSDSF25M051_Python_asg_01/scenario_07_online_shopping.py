
# Scenario 7: Online Shopping Checkout

customer_name = input("Enter customer name: ")

subtotal = 0
total_items = 0

while True:
    product_name = input("\nEnter product name (or 'done' to finish): ")

    if product_name.lower() == "done":
        break

    price = float(input("Enter product price (Rs.): "))

    while price <= 0:
        print("Price must be greater than zero.")
        price = float(input("Enter product price (Rs.): "))

    quantity = int(input("Enter quantity: "))

    while quantity <= 0:
        print("Quantity must be greater than zero.")
        quantity = int(input("Enter quantity: "))

    item_cost = price * quantity
    subtotal = subtotal + item_cost
    total_items = total_items + quantity

    print("Product:", product_name)
    print("Item Cost: Rs.", format(item_cost, ".2f"))
    print("Running Subtotal: Rs.", format(subtotal, ".2f"))

if subtotal >= 5000:
    discount_rate = 10
elif subtotal >= 2000:
    discount_rate = 5
else:
    discount_rate = 0

discount = subtotal * discount_rate / 100
final_bill = subtotal - discount

print("\n===== Shopping Bill =====")
print("Customer Name:", customer_name)
print("Total Items Purchased:", total_items)
print("Subtotal: Rs.", format(subtotal, ".2f"))
print("Discount Rate:", discount_rate, "%")
print("Discount Amount: Rs.", format(discount, ".2f"))
print("Final Bill: Rs.", format(final_bill, ".2f"))
print("=========================")

