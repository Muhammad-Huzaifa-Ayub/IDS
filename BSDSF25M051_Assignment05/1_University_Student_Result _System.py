
# University Student Result and Exception Management System

# F: User-defined exception
class InvalidMarksError(Exception):
    pass


# B: Function using *args
def calculate_total_marks_average(name, *args):

    if len(args) == 0:
        raise ZeroDivisionError("No subject marks provided!")

    total = sum(args)
    average = total / len(args)

    return total, average


# D: Function to classify student performance
def classify_performance(average):

    if average >= 80:
        return "Excellent"

    elif average >= 60:
        return "Good"

    elif average >= 50:
        return "Satisfactory"

    else:
        return "Needs Improvement"


# A: Dictionary to store student records
students_dict = {}

no_of_students = int(input("Enter number of students: "))

for i in range(no_of_students):

    print("\nEnter details of Student", i + 1)

    try:
        # Accept student information
        name = input("Enter student name: ").strip()

        if not name:
            raise ValueError("Student name cannot be empty!")

        roll_number = int(input("Enter roll number: "))

        if roll_number in students_dict:
            raise ValueError("Roll number already exists!")

        no_of_subjects = int(input("Enter number of subjects: "))

        if no_of_subjects <= 0:
            raise ZeroDivisionError("At least one subject is required!")

        subjects_dict = {}

        # Accept subject names and marks
        for j in range(no_of_subjects):

            subject_name = input(f"Enter subject {j + 1} name: ").strip()

            if not subject_name:
                raise ValueError("Subject name cannot be empty!")

            if subject_name in subjects_dict:
                raise ValueError("Duplicate subject name!")

            try:
                marks = float(input(f"Enter marks for {subject_name}: "))

            except ValueError:
                raise ValueError("Marks must be numeric!")

            # E and F: Validate marks
            if marks < 0 or marks > 100:
                raise InvalidMarksError(
                    "Marks must be between 0 and 100!"
                )

            subjects_dict[subject_name] = marks

        # Store student information
        students_dict[roll_number] = {
            "name": name,
            "subjects": subjects_dict
            }

    except InvalidMarksError as e:
        print("Invalid Marks Error:", e)

    except ZeroDivisionError as e:
        print("Division Error:", e)

    except ValueError as e:
        print("Input Error:", e)

    except Exception as e:
        print("Unexpected Error:", e)


# H: Generate and display student reports
# G: Save reports using file handling

try:
    with open("student_result_report.txt", "w") as file:

        for roll_number, student in students_dict.items():

            name = student["name"]
            subjects = student["subjects"]

            # Check missing student information
            if not name or not subjects:
                raise ValueError("Missing student information!")

            # Calculate total and average
            total, average = calculate_total_marks_average(name, *subjects.values())

            # Calculate performance category
            category = classify_performance(average)

            # C: Calculate percentages using map() and lambda
            percentages = map(lambda marks: marks / 100 * 100,subjects.values())

            # C: Find subjects with marks >= 80
            high_scorers = filter(lambda item: item[1] >= 80,subjects.items())

            # Prepare student report
            report = "\n========== STUDENT RESULT REPORT ==========\n"

            report += f"Student Name: {name}\n"
            report += f"Roll Number: {roll_number}\n"

            report += "\nSubject-wise Results:\n"

            for subject, percentage in zip(subjects.keys(), percentages):
                marks = subjects[subject]

                report += (f"{subject}: {marks} marks ({percentage:.2f}%)\n")

            report += f"\nTotal Marks: {total}\n"
            report += f"Average Marks: {average:.2f}\n"

            report += "\nHigh Scoring Subjects (80 or above):\n"

            high_scorers = list(high_scorers)

            if high_scorers:
                for subject, marks in high_scorers:
                    report += f"{subject}: {marks}\n"
            else:
                report += "No high-scoring subjects.\n"

            report += f"\nPerformance Category: {category}\n"

            report += "===========================================\n"

            # Display report on screen
            print(report)

            # Save report in text file
            file.write(report)

    print("\nReport successfully saved in student_result_report.txt")

except ZeroDivisionError as e:
    print("Division Error:", e)

except ValueError as e:
    print("Missing Information Error:", e)

except OSError as e:
    print("File Handling Error:", e)

