
# Dictionary to store book records

books = {
    101: {
        "id": 101,
        "title": "Python Basics",
        "author": "John Smith",
        "category": "Programming",
        "quantity": 5
    },

    102: {
        "id": 102,
        "title": "Data Science",
        "author": "David Brown",
        "category": "Technology",
        "quantity": 3
    },

    103: {
        "id": 103,
        "title": "English Grammar",
        "author": "Ali Khan",
        "category": "English",
        "quantity": 2
    }
}


# Add a new book using **kwargs
def add_book(**book_info):
    book_id = book_info["id"]
    books[book_id] = book_info
    print("Book added successfully!")


# Search books by multiple titles using *args
def search_books(*titles):
    for title in titles:
        found = False

        for book in books.values():
            if book["title"].lower() == title.lower():
                print(book)
                found = True

        if found == False:
            print(title, "not found!")


# Search book by ID
def search_by_id(book_id):
    try:
        print(books[book_id])

    except KeyError:
        print("Invalid book ID!")


# Update available book quantity
def update_quantity(book_id, quantity):
    try:
        books[book_id]["quantity"] = quantity
        print("Book quantity updated successfully!")

    except KeyError:
        print("Invalid book ID!")


# Display all available books using filter and lambda
def display_available_books():
    available_books = filter(
        lambda book: book["quantity"] > 0,
        books.values()
    )

    print("\nAvailable Books:")

    for book in available_books:
        print(book)


# Search books by category using filter and lambda
def search_by_category(category):
    category_books = filter(
        lambda book: book["category"].lower() == category.lower(),
        books.values()
    )

    print("\nBooks in", category, "category:")

    for book in category_books:
        print(book)
