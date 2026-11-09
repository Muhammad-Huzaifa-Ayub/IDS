
# Scenario 10: ATM Withdrawal Simulator

name = input("Enter account holder name: ")

balance = float(input("Enter current account balance (Rs.): "))

while balance < 0:
    print("Balance cannot be negative.")
    balance = float(input("Enter current account balance (Rs.): "))

successful_withdrawals = 0
total_withdrawn = 0

while True:
    amount = float(input("\nEnter withdrawal amount (Rs.): "))

    if amount <= 0:
        print("Transaction failed: Amount must be positive.")

    elif amount % 500 != 0:
        print("Transaction failed: Amount must be a multiple of Rs. 500.")

    elif amount > balance:
        print("Transaction failed: Insufficient balance.")

    else:
        balance = balance - amount
        successful_withdrawals = successful_withdrawals + 1
        total_withdrawn = total_withdrawn + amount

        print("Withdrawal successful.")
        print("Withdrawn Amount: Rs.", format(amount, ".2f"))
        print("Updated Balance: Rs.", format(balance, ".2f"))

    choice = input("Do you want another transaction? (yes/no): ")

    if choice.lower() != "yes":
        break

print("\n===== ATM Transaction Report =====")
print("Account Holder:", name)
print("Successful Withdrawals:", successful_withdrawals)
print("Total Amount Withdrawn: Rs.", format(total_withdrawn, ".2f"))
print("Final Account Balance: Rs.", format(balance, ".2f"))
print("==================================")


