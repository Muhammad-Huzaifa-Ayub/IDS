
# Scenario 12: Employee Attendance and Salary Assessment

name = input("Enter employee name: ")

daily_wage = float(input("Enter daily wage (Rs.): "))

while daily_wage < 0:
    print("Daily wage cannot be negative.")
    daily_wage = float(input("Enter daily wage (Rs.): "))

present_days = 0
absent_days = 0

for day in range(1, 27):
    attendance = input("Enter attendance for day " + str(day) + " (P/A): ")
    attendance = attendance.upper()

    while attendance != "P" and attendance != "A":
        print("Invalid entry. Enter P for present or A for absent.")
        attendance = input("Enter attendance for day " + str(day) + " (P/A): ")
        attendance = attendance.upper()

    if attendance == "P":
        present_days = present_days + 1
    else:
        absent_days = absent_days + 1

attendance_percentage = (present_days / 26) * 100
salary = present_days * daily_wage

print("\n===== Employee Attendance Report =====")
print("Employee Name:", name)
print("Working Days:", 26)
print("Present Days:", present_days)
print("Absent Days:", absent_days)
print("Attendance Percentage:", format(attendance_percentage, ".2f"), "%")
print("Calculated Salary: Rs.", format(salary, ".2f"))

if attendance_percentage < 80:
    print("Warning: Attendance is below 80%.")
else:
    print("Attendance requirement satisfied.")

print("=======================================")

