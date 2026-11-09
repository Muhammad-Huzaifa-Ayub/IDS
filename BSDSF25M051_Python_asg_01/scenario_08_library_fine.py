
# Scenario 8: Library Late-Return Fine Calculator

student_name = input("Enter student name: ")
book_title = input("Enter book title: ")

days_late = int(input("Enter number of days late: "))

while days_late < 0:
    print("Days late cannot be negative.")
    days_late = int(input("Enter number of days late: "))

if days_late == 0:
    fine = 0
elif days_late <= 5:
    fine = days_late * 10
elif days_late <= 10:
    fine = (5 * 10) + ((days_late - 5) * 20)
else:
    fine = (5 * 10) + (5 * 20) + ((days_late - 10) * 50)

print("\n===== Library Fine Report =====")
print("Student Name:", student_name)
print("Book Title:", book_title)
print("Days Late:", days_late)

if days_late == 0:
    print("Status: Book returned on time. No fine is due.")
else:
    print("Total Fine: Rs.", format(fine, ".2f"))

print("===============================")

