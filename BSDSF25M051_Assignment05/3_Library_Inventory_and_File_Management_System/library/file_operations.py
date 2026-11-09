
import os

# Directory and file names
folder = "LibraryRecords"
file_path = os.path.join(folder, "books.txt")


# Create directory
def create_directory():
    os.makedirs(folder, exist_ok=True)
    print("LibraryRecords directory created!")


# Write all book records into a text file
def write_books(books):
    try:
        with open(file_path, "w") as file:
            for book in books.values():
                file.write(str(book) + "\n")

        print("Books saved successfully!")

    except PermissionError:
        print("Permission denied!")

    except OSError:
        print("File access error!")


# Append a new book without deleting existing records
def append_book(book):
    try:
        with open(file_path, "a") as file:
            file.write(str(book) + "\n")

        print("New book appended successfully!")

    except PermissionError:
        print("Permission denied!")

    except OSError:
        print("File access error!")


# Read file using read(), readline(), readlines() and seek()
def read_books():
    try:
        with open(file_path, "r") as file:

            print("\nUsing read():")
            print(file.read())

            file.seek(0)

            print("\nUsing readline():")
            print(file.readline())

            file.seek(0)

            print("\nUsing readlines():")
            print(file.readlines())

    except FileNotFoundError:
        print("File not found!")

    except PermissionError:
        print("Permission denied!")

    except OSError:
        print("File access error!")


# Check file existence and display file attributes
def file_information():
    if os.path.exists(file_path):
        print("\nFile exists!")

        print("File attributes:")
        print(os.stat(file_path))

    else:
        print("File does not exist!")


# Rename the file
def rename_file():
    new_path = os.path.join(folder, "books_backup.txt")

    try:
        if os.path.exists(file_path):

            # Remove old backup if it already exists
            if os.path.exists(new_path):
                os.remove(new_path)

            os.rename(file_path, new_path)

            print("File renamed successfully!")

        else:
            print("File not found!")

    except PermissionError:
        print("Permission denied!")

    except OSError:
        print("File access error!")


# Save updated inventory report
def save_report(books):
    report_path = os.path.join(folder, "inventory_report.txt")

    try:
        with open(report_path, "w") as file:

            file.write("LIBRARY INVENTORY REPORT\n\n")

            for book in books.values():
                file.write(str(book) + "\n")

        print("Inventory report saved successfully!")

    except PermissionError:
        print("Permission denied!")

    except OSError:
        print("File access error!")
