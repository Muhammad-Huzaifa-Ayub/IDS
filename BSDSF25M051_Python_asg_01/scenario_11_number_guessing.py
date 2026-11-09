
# Scenario 11: Number Guessing Game
import random
name = input("Enter player name: ")

secret_number = random.randint(1, 100)

attempts = 0
max_attempts = 7
guessed_correctly = False

print("Guess the secret number between 1 and 100.")
print("You have a maximum of 7 valid attempts.")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))

    if guess < 1 or guess > 100:
        print("Invalid guess. Enter a number between 1 and 100.")
        continue

    attempts = attempts + 1

    if guess == secret_number:
        guessed_correctly = True
        print("Congratulations,", name + "!")
        print("You guessed the correct number.")
        print("Attempts used:", attempts)
        break

    elif guess < secret_number:
        print("Too low. Try again.")

    else:
        print("Too high. Try again.")

if not guessed_correctly:
    print("\nGame over,", name + ".")
    print("You have used all 7 valid attempts.")
    print("The secret number was:", secret_number)


    