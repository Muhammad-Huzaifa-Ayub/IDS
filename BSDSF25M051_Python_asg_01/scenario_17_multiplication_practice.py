
# Scenario 17: Multiplication Practice and Performance Report

name = input("Enter student name: ")

table_number = int(input("Enter multiplication table number: "))

while table_number <= 0:
    print("Table number must be greater than zero.")
    table_number = int(input("Enter multiplication table number: "))

questions = int(input("Enter number of questions: "))

while questions <= 0:
    print("Number of questions must be greater than zero.")
    questions = int(input("Enter number of questions: "))

correct = 0
incorrect = 0

for i in range(1, questions + 1):
    answer = int(input(str(table_number) + " x " + str(i) + " = "))

    correct_answer = table_number * i

    if answer == correct_answer:
        print("Correct answer!")
        correct = correct + 1
    else:
        print("Incorrect answer. The correct answer is", correct_answer)
        incorrect = incorrect + 1

percentage = (correct / questions) * 100

print("\n----- Performance Report -----")
print("Student Name:", name)
print("Multiplication Table:", table_number)
print("Total Questions:", questions)
print("Correct Answers:", correct)
print("Incorrect Answers:", incorrect)
print("Percentage Score:", format(percentage, ".2f"), "%")

if percentage >= 80:
    print("Performance: Excellent!")
elif percentage >= 60:
    print("Performance: Good!")
elif percentage >= 40:
    print("Performance: Keep practicing.")
else:
    print("Performance: More practice is needed.")

print("------------------------------")



