
# Scenario 1: University Admission Eligibility Checker

name = input("Enter applicant name: ")


total_marks = float(input("Enter total possible intermediate marks: "))

while total_marks <= 0:
    print("Total marks must be greater than zero.")
    total_marks = float(input("Enter total possible intermediate marks: "))


intermediate_marks = float(input("Enter intermediate marks obtained: "))

while intermediate_marks < 0 or intermediate_marks > total_marks:
    print("Invalid marks! Marks must be between 0 and", total_marks)
    intermediate_marks = float(input("Enter intermediate marks obtained: "))

entry_total = float(input("Enter total possible entry-test marks: "))

while entry_total <= 0:
    print("Total entry-test marks must be greater than zero.")
    entry_total = float(input("Enter total possible entry-test marks: "))

entry_marks = float(input("Enter entry-test marks obtained: "))

while entry_marks < 0 or entry_marks > entry_total:
    print("Invalid marks! Marks must be between 0 and", entry_total)
    entry_marks = float(input("Enter entry-test marks obtained: "))


intermediate_percentage = (intermediate_marks / total_marks) * 100
entry_percentage = (entry_marks / entry_total) * 100


print("\n----- Admission Eligibility Report -----")
print("Applicant Name:", name)
print("Intermediate Percentage:", round(intermediate_percentage, 2), "%")
print("Entry-Test Percentage:", round(entry_percentage, 2), "%")


if intermediate_percentage >= 60 and entry_percentage >= 50:
    print("Result: Eligible for preliminary admission.")
else:
    print("Result: Not eligible for preliminary admission.")

    if intermediate_percentage < 60:
        print("Reason: Intermediate percentage is below 60%.")

    if entry_percentage < 50:
        print("Reason: Entry-test percentage is below 50%.")

print("----------------------------------------")

