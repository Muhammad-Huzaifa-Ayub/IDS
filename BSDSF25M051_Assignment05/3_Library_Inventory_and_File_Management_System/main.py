
# Import functions from book_operations module

from library.book_operations import (
    books,
    add_book,
    search_books,
    search_by_id,
    update_quantity,
    display_available_books,
    search_by_category
)


# Import functions from file_operations module

from library.file_operations import (
    create_directory,
    write_books,
    append_book,
    read_books,
    file_information,
    rename_file,
    save_report
)


print("===== LIBRARY INVENTORY SYSTEM =====")


# Create LibraryRecords directory
create_directory()


# Display available books
display_available_books()


# Add a new book using **kwargs
add_book(
    id=104,
    title="Computer Science",
    author="Ahmed Ali",
    category="Programming",
    quantity=4
)


# Search multiple books using *args
print("\n===== SEARCH BOOKS =====")

search_books("Python Basics", "Data Science")


# Search book by ID
print("\n===== SEARCH BY ID =====")

search_by_id(101)


# Demonstrate invalid book ID
search_by_id(999)


# Update book quantity
print("\n===== UPDATE BOOK QUANTITY =====")

update_quantity(103, 5)


# Search books by category
print("\n===== SEARCH BY CATEGORY =====")

search_by_category("Programming")


# Save current inventory into text file
print("\n===== WRITE FILE =====")

write_books(books)


# Add another book
add_book(
    id=105,
    title="Computer Networks",
    author="Usman Khan",
    category="Technology",
    quantity=6
)


# Append the newly added book to the existing text file
print("\n===== APPEND FILE =====")

append_book(books[105])


# Read file using different methods
print("\n===== READ FILE =====")

read_books()


# Check file existence and attributes
print("\n===== FILE INFORMATION =====")

file_information()


# Display complete library inventory
print("\n===== COMPLETE LIBRARY INVENTORY =====")

for book in books.values():
    print(book)


# Save updated inventory report
print("\n===== SAVE INVENTORY REPORT =====")

save_report(books)


# Rename the books file
print("\n===== RENAME FILE =====")

rename_file()


print("\n===== PROGRAM COMPLETED =====")
