
# Scenario 3: Password Strength and Validity Checker

while True:
    password = input("Enter your password: ")

    has_upper = False
    has_lower = False
    has_digit = False

    if len(password) >= 8:
        print("Length requirement: Satisfied")
    else:
        print("Length requirement: Not satisfied (minimum 8 characters)")

    for ch in password:
        if ch >= 'A' and ch <= 'Z':
            has_upper = True
        elif ch >= 'a' and ch <= 'z':
            has_lower = True
        elif ch >= '0' and ch <= '9':
            has_digit = True

    if has_upper:
        print("Uppercase letter requirement: Satisfied")
    else:
        print("Uppercase letter requirement: Missing")

    if has_lower:
        print("Lowercase letter requirement: Satisfied")
    else:
        print("Lowercase letter requirement: Missing")

    if has_digit:
        print("Digit requirement: Satisfied")
    else:
        print("Digit requirement: Missing")

    if len(password) >= 8 and has_upper and has_lower and has_digit:
        print("Result: Password is acceptable.")
        break
    else:
        print("Result: Password is not acceptable.")

        choice = input("Would you like to try again? (yes/no): ")

        if choice.lower() != "yes":
            print("Password checking stopped.")
            break

        